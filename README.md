🎧 WhisperAI Transcriber (macOS)

A sleek, lightweight, and easy-to-use Streamlit web application that uses OpenAI's Whisper model to transcribe English audio into accurate text.

Upload an .mp3 or .wav file and get back clean English text, with the option to download the result in .srt subtitle format.

🚀 Features

🔊 Upload clear English audio files (.mp3, .wav)

✨ Transcribe using OpenAI Whisper (Base model)

📄 Display transcription directly in the browser

🔗 Download the transcription as .srt subtitle format

🔸 Simple and interactive UI using Streamlit

🚲 Quick Demo

 

🔧 Tech Stack

Frontend/UI: Streamlit

Model: OpenAI Whisper (base model)

Audio Processing: librosa, ffmpeg, wave

🪧 Installation (macOS)

1. Clone the Repository

git clone https://github.com/Nydv01/WhisperAI_Transcriber.git
cd WhisperAI_Transcriber

2. Create and Activate Virtual Environment

python3 -m venv Whisperai
source Whisperai/bin/activate

3. Install Dependencies

brew install ffmpeg  # Required for Whisper to handle audio
pip install -r requirements.txt

4. Run the App

streamlit run app.py

Once running, your browser will open http://localhost:8501

🔹 Usage Instructions

Launch the app with streamlit run app.py

Upload your English audio file (.mp3 or .wav)

Let the model transcribe it (progress bar shows loading)

View the transcribed text

Optionally download the output as an .srt subtitle file

🔮 Sample Output

Input Audio

Transcribed Text

meeting.mp3

"Welcome to the quarterly review..."

lecture.wav

"In this chapter, we discuss machine learning."

🚨 Troubleshooting

ffmpeg not found: Make sure ffmpeg is installed via brew install ffmpeg

Model errors: Ensure you’re connected to the internet when Whisper model is first loaded

Incorrect transcription: Make sure the input is clear English audio (no background noise, good mic)

👨‍💻 Author

Nitin YadavGitHub: @Nydv01

📁 Repository

https://github.com/Nydv01/WhisperAI_Transcriber

📄 License

This project is licensed under the MIT License.

🚀 Future Plans

Add support for Hindi and other languages

Subtitle editor for fine-tuning lines

Mobile-friendly UI

Export formats: .txt, .docx, .vtt

If you find this helpful, give it a ⭐️ on GitHub!
