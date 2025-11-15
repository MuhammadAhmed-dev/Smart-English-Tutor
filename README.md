# English Learning Assistant 📚🇬🇧

A Streamlit-based web application that helps English learners improve their writing skills by analyzing uploaded PDF documents and providing personalized feedback and practice suggestions.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-FF6F00?style=for-the-badge)

## ✨ Features

- **📄 PDF Text Extraction**: Upload any PDF document and extract text content automatically
- **📊 Writing Analysis**: Comprehensive analysis of writing including:
  - Sentence and word counts
  - Vocabulary richness and diversity
  - Parts of speech identification (verbs, nouns, adjectives)
  - Average sentence length
  - Sentiment analysis
- **💡 Personalized Feedback**: Get actionable suggestions to improve your writing style
- **🎯 Practice Exercises**: Receive random, targeted practice suggestions to enhance specific writing skills

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/english-learning-assistant.git
cd english-learning-assistant
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
streamlit run chatbot_v2_pdf_UI.py
```

4. **Open your browser** and navigate to `http://localhost:8501`

## 📦 Dependencies

The project requires the following Python packages:

```txt
streamlit>=1.28.0
nltk>=3.8.0
textblob>=0.17.1
PyPDF2>=3.0.0
```

Create a `requirements.txt` file with the above content for easy installation.

## 🛠️ Setup

1. **Install Python dependencies**:
```bash
pip install nltk textblob PyPDF2 streamlit
```

2. **Download NLTK data** (run once):
```python
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
```

## 📁 Project Structure

```
english-learning-assistant/
│
├── chatbot_v2_pdf_UI.py     # Main application file
├── requirements.txt         # Python dependencies
```

## 🎯 How to Use

1. **Launch the app** using `streamlit run chatbot_v2_pdf_UI.py`
2. **Upload a PDF** file containing your English writing
3. **View analysis results** in the dashboard:
   - Basic metrics (sentences, words, vocabulary richness)
   - Writing feedback and improvement suggestions
   - Personalized practice exercises
4. **Implement the suggestions** to improve your English writing skills

## 🔧 Technical Details

### Analysis Metrics
- **Vocabulary Richness**: Percentage of unique words in the text
- **Sentence Structure**: Average words per sentence analysis
- **Parts of Speech**: Identification of verbs, nouns, and adjectives
- **Sentiment Analysis**: Overall tone of the writing (positive/negative/neutral)

### Feedback System
The app provides targeted feedback on:
- Vocabulary diversity
- Sentence length optimization
- Use of descriptive language
- Action-oriented writing
- Tone and sentiment

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- NLP capabilities powered by [NLTK](https://www.nltk.org/) and [TextBlob](https://textblob.readthedocs.io/)
- PDF processing with [PyPDF2](https://pypi.org/project/PyPDF2/)

---

**Happy Learning!** 🌟 Practice makes perfect when it comes to mastering English writing skills.
