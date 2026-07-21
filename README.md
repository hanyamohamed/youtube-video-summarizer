# 🎥 YouTube Video Summarizer

An AI-powered web application that summarizes YouTube videos using Hugging Face Transformers and Streamlit.

## Features

- Extract transcript from YouTube videos
- Split long transcripts into chunks
- Generate AI-powered summaries
- Display the full transcript
- Download summary as txt file
- Simple and user-friendly Streamlit interface

## Technologies

- Python
- Streamlit
- Hugging Face Transformers
- youtube-transcript-api
- PyTorch

## Project Structure

```
youtube-video-summarizer/
├── app.py                # Streamlit application
├── kaggle.ipynb          # Notebook implementation
├── README.md
├── requirements.txt

```

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
streamlit run app.py
```

## Model

This project uses the **FalconsAI Text Summarization** model from Hugging Face.

## Future Improvements

- Arabic summarization support
- Download summary as PDF
- Multiple summarization models
- Deploy on Streamlit Cloud
