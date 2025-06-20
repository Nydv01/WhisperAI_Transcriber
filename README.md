# 🎙️ WhisperAI Transcription App

A lightweight web app for transcribing `.mp3` or `.wav` files using OpenAI’s Whisper model and Streamlit.

🔗 **GitHub Repo**: [https://github.com/Nydv01/WhisperAI_Transcriber](https://github.com/Nydv01/WhisperAI_Transcriber)

---

## 🚀 Features

- 📤 Upload MP3/WAV files
- 🧠 Transcribe audio using OpenAI Whisper (base model)
- 📄 View transcript in-browser
- 💾 Download transcript as `.srt`
- ⚡ Fast and easy interface with Streamlit

---

## 🖥️ Project Structure

WhisperAI_Transcriber/
│
├── app.py # Main Streamlit app
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── Whisperai/ # Python virtual environment (ignored)

yaml
Copy
Edit

---

## 📦 Installation (macOS)

### 🧰 Prerequisites

- Python 3.10+ (recommended with pyenv)
- [Homebrew](https://brew.sh/)
- Git

---

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Nydv01/WhisperAI_Transcriber.git
cd WhisperAI_Transcriber
2️⃣ Set Up Virtual Environment
bash
Copy
Edit
python3 -m venv Whisperai
source Whisperai/bin/activate
3️⃣ Install Dependencies
bash
Copy
Edit
brew install ffmpeg
pip install streamlit openai-whisper librosa tqdm
4️⃣ Run the App
bash
Copy
Edit
streamlit run app.py
Then open your browser to http://localhost:8501

📜 Sample Code (app.py)
python
Copy
Edit
import streamlit as st
import whisper
import tempfile

# Load Whisper base model
model = whisper.load_model("base")

def transcribe(audio_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=audio_file.name.split('.')[-1]) as tmp:
        tmp.write(audio_file.read())
        tmp_path = tmp.name

    result = model.transcribe(tmp_path, language="en")
    return result["text"]

def main():
    st.title("🎙️ WhisperAI Audio Transcription")
    st.write("Upload an MP3 or WAV file to get its transcription.")

    audio_file = st.file_uploader("Upload your audio file", type=["mp3", "wav"])
    if audio_file:
        with st.spinner("Transcribing..."):
            text = transcribe(audio_file)
        if text:
            st.success("Transcription Complete ✅")
            st.write(text)
            st.download_button("📥 Download as SRT", f"1\n00:00:00,000 --> 00:00:10,000\n{text}", file_name="transcription.srt")

if __name__ == "__main__":
    main()
📹 Demo (Optional)
Add a short video or GIF showing the app in use.

🧩 Future Improvements
 Support other Whisper models (tiny, medium, large)

 Multilingual transcription

 Better timestamping in SRT

 Drag-and-drop audio UI

 Upload audio via URL

🙏 Credits
OpenAI Whisper

Streamlit

Librosa

📝 License
MIT License © Nydv01

yaml
Copy
Edit

---


