# 📺 Game YouTube Summarizer — EduAters

**🎓 Project Type:** Educational AI Tool  
**💡 Purpose:** Turn long YouTube lectures into short, fun summaries with emojis, quizzes, and reward coins!  
**🚀 Status:** Working and deployed locally (soon to be deployed online)

---

## 🔧 Features
- 🎥 **YouTube Video Input**: Just paste a YouTube link.
- ✍️ **Transcription**: Converts speech to text using OpenAI Whisper.
- 🧠 **Summarization with Emojis**: HuggingFace transformers + emoji enhancer.
- 📄 **Transcript Viewer**: View full video transcript.
- ❓ **Quiz Generator**: Answer questions based on video.
- 🪙 **Gamification**: Earn coins for correct answers!
- 🧑‍🎨 **Animated UI**: Clean and interactive frontend (HTML/CSS/JS).
- 🔐 **Login & Session Management** *(coming soon)*

---

## 💻 Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python, Flask
- **AI Models**:
  - OpenAI Whisper (for transcription)
  - T5 / BART (for summarization)
- **Other Tools**:
  - `yt_dlp` – to download audio from YouTube
  - `transformers`, `torch`, `flask`, `jinja2`, etc. 

---
 -**Future Additions**
-🔐 User authentication system

-🏆 Leaderboard and coin-based rewards

-🌐 Deploy on Render / Netlify / Vercel

 ---
 **📹 Demo Video**
 
## 🏁 Setup Instructions

```bash
# Step 1: Clone the repo
git clone https://github.com/Antara80978/Game-Youtube-summarizer-eduaters.git

# Step 2: Navigate to the folder
cd Game-Youtube-summarizer-eduaters

# Step 3: Create virtual environment
python -m venv .venv

# Step 4: Activate it
# For Windows
.venv\Scripts\activate
# For Mac/Linux
source .venv/bin/activate

# Step 5: Install dependencies
pip install -r requirements.txt

# Step 6: Run the Flask app
python app.py
