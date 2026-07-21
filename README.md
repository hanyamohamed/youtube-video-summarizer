# 🎥 YouTube Video Summarizer

An AI-powered web application that summarizes YouTube videos using Hugging Face Transformers and Streamlit.

The application extracts the transcript of a YouTube video, divides long transcripts into manageable chunks, summarizes each chunk using a transformer model, and combines the results into a final summary.

---

## ✨ Features

- Extract YouTube transcripts automatically
- Handle long videos using transcript chunking
- AI-powered text summarization
- Interactive Streamlit interface
- Public sharing using ngrok
- Supports English transcript summarization

---

## 🧠 How it Works

1. The user enters a YouTube video URL.
2. The application extracts the video ID.
3. The transcript is fetched using `youtube-transcript-api`.
4. The transcript is divided into overlapping chunks.
5. Each chunk is summarized using the **FalconsAI Text Summarization** model.
6. All summaries are combined into a final summary.
7. The generated summary is displayed through a Streamlit interface.

---

## 🏗️ Architecture

YouTube URL

↓

youtube-transcript-api

↓

Transcript

↓

Chunking

↓

FalconsAI Text Summarization

↓

Combined Summary

↓

Streamlit GUI

---

## 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| Programming Language | Python |
| User Interface | Streamlit |
| AI Model | FalconsAI Text Summarization |
| NLP Library | Hugging Face Transformers |
| Transcript Extraction | youtube-transcript-api |
| Deep Learning Framework | PyTorch |
| Sharing | ngrok |

---

## 📁 Project Structure

```
youtube-video-summarizer/
│
├── app.py
├── kaggle.ipynb
├── README.md
├── requirements.txt
```

---

## 🚀 Installation

```bash
git clone <repo-url>

cd <repo-folder>

pip install -r requirements.txt

streamlit run app.py
```

---

## 🔮 Future Improvements

- Support multilingual summarization.
- Add PDF export not just txt file.
- Deploy the application permanently using Streamlit Community Cloud.
