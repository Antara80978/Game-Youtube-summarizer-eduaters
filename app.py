from flask import Flask, render_template, request, redirect, url_for, session
from utils.download_audio import download_audio
from utils.transcribe import transcribe_audio
from utils.summarize_real import summarize_text, add_emojis
from utils.quiz import get_two_questions, check_answers
from flask import Flask, render_template, request, redirect, url_for, session, flash


app = Flask(__name__)
app.secret_key = "super_secret_key"

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    transcript = ""

    if "points" not in session:
        session["points"] = 0

    if request.method == "POST":
        youtube_url = request.form["youtube_url"]
        action = request.form["action"]


        if action == "transcript":
            audio_path = download_audio(youtube_url)
            transcript = transcribe_audio(audio_path)
            session["transcript"] = transcript
            return render_template("index.html", transcript=transcript, points=session["points"])

        elif action == "summary":
            transcript = session.get("transcript", "")
            if transcript:
                summary = summarize_text(transcript)
                summary = add_emojis(summary)
                session["summary"] = summary
                return render_template("index.html", transcript=transcript, summary=summary, points=session["points"])
            else:
                return render_template("index.html", summary="❌ No transcript available.", points=session["points"])

    return render_template("index.html", points=session["points"])

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if "points" not in session:
        session["points"] = 0

    if request.method == "POST":
        user_answer1 = request.form.get("answer1")
        user_answer2 = request.form.get("answer2")
        correct1 = session.get("correct1")
        correct2 = session.get("correct2")

        coins_earned = 0
        if user_answer1 == correct1:
            coins_earned += 150
        if user_answer2 == correct2:
            coins_earned += 150

        session["points"] += coins_earned
        flash(f"✅ You earned {coins_earned} coins!", "success")
        return redirect(url_for("quiz"))

    q1, q2 = get_two_questions()
    session["correct1"] = q1[2]
    session["correct2"] = q2[2]
    return render_template("quiz.html", q1=q1, q2=q2, points=session["points"])

if __name__ == "__main__":
    app.run(debug=True)
