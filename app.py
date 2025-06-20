import streamlit as st
import whisper
import librosa
import wave
import mimetypes
from tqdm import tqdm
import tempfile

# Load Whisper model
model = whisper.load_model("base")

def transcribe(audio_file):
    file_extension = audio_file.name.split('.')[-1]

    if file_extension not in ("mp3", "wav"):
        st.error("Unsupported file format. Please upload an MP3 or WAV file.")
        return None

    # Save uploaded file to a temp location
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_extension}") as tmp:
        tmp.write(audio_file.read())
        tmp_path = tmp.name

    # Let Whisper handle file directly
    result = model.transcribe(tmp_path, task="transcribe", language="en")
    text = result["text"]
    return text

def download_link(text):
    srt_content = f"1\n00:00:00,000 --> 00:00:10,000\n{text}\n"
    st.download_button("Download Transcription as .srt", srt_content, file_name="transcription.srt")

def main():
    st.title("🎙️ WhisperAI Audio Transcription App")
    st.write("Upload an MP3 or WAV file to get its transcription.")

    audio_file = st.file_uploader("Upload audio", type=["mp3", "wav"])

    if audio_file is not None:
        with st.spinner("Transcribing..."):
            text = transcribe(audio_file)

        if text:
            st.success("Transcription Complete ✅")
            st.write(text)
            download_link(text)

if __name__ == "__main__":
    main()
