import streamlit as st
from transformers import pipeline
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi

# Page Setup
st.set_page_config(
    page_title="YouTube Video Summarizer",
    page_icon="🎥",
    layout="wide"
)

st.title("🎥 YouTube Video Summarizer")
st.write("Paste a YouTube video link and get an AI-generated summary.")

# Load Model
@st.cache_resource
def load_model():
    return pipeline(
        "summarization",
        model="Falconsai/text_summarization"
    )

summarizer = load_model()

# Functions
def extract_video_id(url):
    parsed = urlparse(url)
    qs = parse_qs(parsed.query)
    video_ids = qs.get("v")

    if not video_ids:
        raise ValueError("Invalid YouTube URL")

    return video_ids[0]


def get_transcript(video_id):
    api = YouTubeTranscriptApi()
    fetched = api.fetch(video_id, languages=["en"])
    return " ".join(snippet.text for snippet in fetched)


def chunk_text(text, chunk_size=300, overlap=20):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks


def summarize_video(text):
    chunks = chunk_text(text)
    summaries = []

    progress = st.progress(0)

    for i, chunk in enumerate(chunks):
        result = summarizer(
            chunk,
            max_new_tokens=100,
            min_length=10,
            do_sample=False
        )

        summaries.append(result[0]["summary_text"])
        progress.progress((i + 1) / len(chunks))

    return " ".join(summaries)

# GUI
url = st.text_input(
    "YouTube URL",
    placeholder="https://www.youtube.com/watch?v=..."
)

if st.button("Generate Summary"):

    if not url.strip():
        st.warning("Please enter a YouTube URL.")

    else:
        try:
            video_id = extract_video_id(url)

            with st.spinner("Extracting transcript..."):
                transcript = get_transcript(video_id)

            with st.spinner("Generating summary..."):
                summary = summarize_video(transcript)

            tab1, tab2 = st.tabs(["📄 Summary", "📝 Transcript"])

            with tab1:
                st.subheader("AI Summary")
                st.write(summary)

                st.download_button(
                    "⬇ Download Summary",
                    summary,
                    file_name="summary.txt",
                    mime="text/plain"
                )

            with tab2:
                st.subheader("Transcript")
                st.write(transcript)

        except Exception as e:
            st.error(f"Error: {e}")