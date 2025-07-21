import streamlit as st
from textblob import TextBlob
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Load NLP tools
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Topic keywords (from your LDA topics)
topic_keywords = {
    "Clarity Issues": ["confusing", "unclear", "understand", "explain"],
    "Pacing": ["fast", "rushed", "slow", "pace"],
    "Engagement": ["boring", "interactive", "engage", "motivate"],
    "Tech Issues": ["audio", "video", "platform", "error", "technical"],
    "Content Quality": ["outdated", "relevant", "deep", "valuable"]
}

# Clean the review text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', '', text)
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(w) for w in tokens if w not in stop_words]
    return " ".join(tokens)

# Predict dominant topic
def detect_topic(text):
    for topic, keywords in topic_keywords.items():
        if any(word in text for word in keywords):
            return topic
    return "General Feedback"

# Streamlit UI
st.title("🎓 Instructor Review Sentiment Checker")

input_text = st.text_area(✍️ Enter a student review:")

if st.button("🔍 Analyze"):
    if input_text.strip():
        cleaned = clean_text(input_text)
        sentiment = TextBlob(input_text).sentiment.polarity

        if sentiment > 0.2:
            label = "Positive"
        elif sentiment < -0.2:
            label = "Negative"
        else:
            label = "Neutral"

        topic = detect_topic(cleaned)

        st.markdown(f"### ✅ Sentiment: `{label}`")
        st.markdown(f"📊 Sentiment Score: `{round(sentiment, 3)}`")
        st.markdown(f"🧠 Detected Topic: `{topic}`")
    else:
        st.warning("Please enter some review text.")
