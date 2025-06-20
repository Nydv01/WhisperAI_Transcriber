# 🎙️ WhisperAI Transcriber

A lightweight, fast, and intuitive web app that **transcribes English audio files** (MP3/WAV) into text using **OpenAI's Whisper model** — all within a clean **Streamlit** interface.

> Built with 💡 by **Nitin Yadav**, **Krish Mittal**, **Aditya Jain**, and **Aryak**.
>HERE'S THE LINK TO THE DEMO VIDEO WHICH SHOWS THE WORKING: https://drive.google.com/file/d/1oEfZ_PT9F3oX-m8UDRqjEQEt4wiIljMJ/view?usp=sharing

---

## 📽️ Demo Preview

🚀 Live App: _Run locally_  
📂 Repository: [WhisperAI_Transcriber](https://github.com/Nydv01/WhisperAI_Transcriber)

---

## 🧠 Key Features

✅ Upload audio files (`.mp3` / `.wav`)  
✅ Transcribe using Whisper (base) model  
✅ Display transcript on the web app  
✅ Download transcript as `.srt` subtitle file  
✅ Works offline once setup  
✅ MacOS compatible

---

## 🧱 Tech Stack

| Layer        | Technology               |
|--------------|---------------------------|
| Frontend     | [Streamlit](https://streamlit.io/) |
| Backend      | [Python](https://www.python.org/), [Whisper](https://github.com/openai/whisper) |
| Audio Utils  | [Librosa](https://librosa.org/), [FFmpeg](https://ffmpeg.org/) |
| Environment  | Virtualenv + Pyenv (for Python 3.10.13) |
| Deployment   | Localhost via Streamlit |

---

## 🛠️ Setup Instructions (macOS)

```bash
# Step 1: Clone the repo
git clone https://github.com/Nydv01/WhisperAI_Transcriber.git
cd WhisperAI_Transcriber

# Step 2: Create and activate virtual environment
python3 -m venv Whisperai
source Whisperai/bin/activate

# Step 3: Install system dependencies
brew install ffmpeg

# Step 4: Install Python packages
pip install --upgrade pip
pip install -r requirements.txt

# Step 5: Run the app
streamlit run app.py
Your app will launch at: http://localhost:8501

📂 Project Structure
plaintext
Copy
Edit
WhisperAI_Transcriber/
│
├── app.py                # Streamlit app code
├── requirements.txt      # Python dependencies
├── README.md             # You're reading it!
├── Whisperai/            # Virtual environment (excluded from GitHub)
└── demo_audio.mp3        # (optional) Sample audio for testing
🎓 Team Members
Name	Role
Nitin Yadav	Project Lead, Setup & UI Design
Krish Mittal	Core Developer, Model Integration & Live Demo
Aditya Jain	Testing, Debugging & Future Scope
Aryak	Remote Contributor, Audio Pipeline Integration

🚧 Challenges Faced
🔧 Whisper model required exact language setting (language="en") for clean transcription.

🧱 FFmpeg was missing, causing runtime file errors.

📉 Wrong file formats led to poor quality until we filtered non-audio inputs.

🛠️ macOS M1 required native ARM-based Python wheels and dependencies.

📈 Future Scope
🌍 Multilingual transcription support

🎬 Subtitle generator for video (.mp4) files

☁️ Deploy on Streamlit Cloud or HuggingFace Spaces

📱 Mobile responsive UI

🧠 Add advanced punctuation & formatting post-processing

🧾 License
This project is licensed under the MIT License.

🙏 Acknowledgements
Thanks to OpenAI for releasing Whisper as open-source.

Shoutout to Streamlit for simplifying web apps with Python.

© 2025 Nitin Yadav, Krish Mittal, Aditya Jain, Aryak — All Rights Reserved.

yaml
Copy
Edit

---

Let me know if you want:

- A PDF version of this
- GitHub badges (build status, license, etc.)
- Slide deck or intro video script based on this

Ready to paste — 100% GitHub-compatible ✅
