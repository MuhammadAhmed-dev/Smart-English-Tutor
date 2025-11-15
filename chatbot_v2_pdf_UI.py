import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from textblob import TextBlob
import random
import PyPDF2
import streamlit as st

# nltk.download(['punkt', 'averaged_perceptron_tagger', 'stopwords'])

class EnglishLearningAssistant:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def extract_text_from_pdf(self, pdf_file):
        try:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
        except Exception as e:
            return f"Error reading PDF: {e}"

    def analyze_text(self, text):
        analysis = {}
        sentences = sent_tokenize(text)
        words = word_tokenize(text.lower())
        content_words = [w for w in words if w.isalpha() and w not in self.stop_words]

        analysis['sentence_count'] = len(sentences)
        analysis['word_count'] = len(words)
        analysis['unique_words'] = len(set(words))
        analysis['vocab_richness'] = round(analysis['unique_words'] / len(words) * 100, 1) if words else 0

        pos_tags = pos_tag(words)
        analysis['verbs'] = [w for w, t in pos_tags if t.startswith('V')]
        analysis['nouns'] = [w for w, t in pos_tags if t.startswith('N')]
        analysis['adjectives'] = [w for w, t in pos_tags if t.startswith('J')]

        analysis['sentiment'] = TextBlob(text).sentiment.polarity
        analysis['avg_sentence_length'] = round(len(words) / len(sentences), 1) if sentences else 0

        return analysis

    def generate_feedback(self, analysis):
        feedback = []
        if analysis['vocab_richness'] < 30:
            feedback.append("🔄 Try using more varied vocabulary. You're repeating words quite a bit.")
        elif analysis['vocab_richness'] > 60:
            feedback.append("🌟 Great vocabulary diversity! You're using a wide range of words.")

        if analysis['avg_sentence_length'] > 20:
            feedback.append("✂️ Your sentences are quite long. Try breaking them up for clarity.")
        elif analysis['avg_sentence_length'] < 8:
            feedback.append("📝 Your sentences are very short. Try combining ideas for better flow.")

        if len(analysis['adjectives']) < 2:
            feedback.append("🎨 Add more descriptive words (adjectives) to make your writing vivid.")

        if len(analysis['verbs']) < 3:
            feedback.append("⚡ Try using more action words to make your writing more dynamic.")

        if analysis['sentiment'] > 0.3:
            feedback.append("😊 Your writing has a positive tone!")
        elif analysis['sentiment'] < -0.3:
            feedback.append("😟 Your writing has a negative tone.")

        return feedback

    def practice_suggestion(self):
        practices = [
            "✍️ Write about your day using at least 5 different verbs.",
            "🌆 Describe your favorite place with plenty of adjectives.",
            "📖 Write a short story with sentences of varying lengths.",
            "🔗 Use compound sentences with 'and', 'but', and 'because'.",
            "🆕 Try using at least three new words you learned recently."
        ]
        return random.choice(practices)

# ----------------- Streamlit UI -----------------
st.set_page_config(page_title="English Learning Assistant", page_icon="🇬🇧", layout="wide")

st.title("English Learning Assistant")
st.markdown("### Upload a PDF and get instant English writing analysis, feedback, and practice suggestions.")

uploaded_file = st.file_uploader("📂 Upload a PDF", type=["pdf"])

assistant = EnglishLearningAssistant()

if uploaded_file is not None:
    text = assistant.extract_text_from_pdf(uploaded_file)

    if not text or len(text.strip()) < 10:
        st.error("Could not extract enough text from the PDF.")
    else:
        analysis = assistant.analyze_text(text)
        feedback = assistant.generate_feedback(analysis)
        practice = assistant.practice_suggestion()

        # Create columns for better layout
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📊 Analysis")
            st.metric("Sentences", analysis['sentence_count'])
            st.metric("Words", analysis['word_count'])
            st.metric("Unique Words", analysis['unique_words'])
            st.metric("Vocabulary Richness", f"{analysis['vocab_richness']}%")
            st.metric("Avg Sentence Length", f"{analysis['avg_sentence_length']} words")
            st.metric("Sentiment Score", round(analysis['sentiment'], 2))

        with col2:
            st.subheader("💡 Feedback")
            for f in feedback:
                st.write(f"- {f}")

        st.markdown("---")
        st.subheader("🎯 Practice Suggestion")
        st.success(practice)
