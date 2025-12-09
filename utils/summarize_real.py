from transformers import pipeline # type: ignore

# Load Hugging Face summarizer
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    if len(text.strip()) == 0:
        return "No content to summarize."
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def add_emojis(summary):
    # Very basic example, you can expand this
    summary = summary.replace("important", "🌟 important")
    summary = summary.replace("note", "📝 note")
    summary = summary.replace("warning", "⚠️ warning")
    return summary
