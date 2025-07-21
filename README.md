![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Last Commit](https://img.shields.io/github/last-commit/chibuogwuonyemaechi/instructor-sentiment-analysis)
![Status](https://img.shields.io/badge/status-completed-brightgreen)


# 📊 Instructor Engagement Dashboard using Sentiment Analysis

## 🧩 Project Overview
This project aims to detect instructor engagement issues by analyzing student reviews. It uses natural language processing (NLP) and sentiment analysis to extract insights from feedback, allowing instructors and administrators to improve teaching effectiveness.

---

## 🎯 Problem Statement
Student feedback is often unstructured and hard to act on. The goal is to:
- Classify sentiment (positive/neutral/negative)
- Detect themes and complaints (via topic modeling)
- Visualize trends per instructor/course
- Identify areas needing attention

---

## 🔧 Tools Used
| Role | Tools |
|------|-------|
| Data Cleaning & Modeling | Python (Pandas, NLTK, Scikit-learn, Gensim, TextBlob) |
| Dashboarding | Power BI |
| Deployment (Optional) | Streamlit |
| Version Control | Git, GitHub |

---

## 🛠️ Project Workflow
1. **Data Loading** – Instructors, Courses, Students, Reviews
2. **Text Preprocessing** – Tokenization, stopword removal, lemmatization
3. **Sentiment Labeling** – Based on `rating_score` (1–2: Negative, 3: Neutral, 4–5: Positive)
4. **Modeling** – TF-IDF + Naive Bayes for sentiment prediction
5. **Topic Modeling** – LDA to discover recurring themes
6. **Output Table** – Final CSV with sentiment, score, topics
7. **Power BI Dashboard** – Sentiment trends, course issues, regional satisfaction
8. **PDF Exports** – Instructor-specific performance snapshots

---

## 📈 Dashboard Features
- 🔍 Filter by Instructor, Course, Sentiment
- 🧑‍🏫 View each instructor’s sentiment breakdown
- 📅 Trend line of feedback sentiment over time
- 🌍 Region-wise satisfaction analysis
- 📚 Course-level comparison by category and level

---

## 📄 Deliverables
- `Sentiment_Analysis_Results_Full.csv` – Final structured data
- `Instructor_Report_[Name].pdf` – PDF reports (1 per instructor)
- `README.md` – This file
- (Optional) `app.py` – Streamlit mini app
- Power BI `.pbix` file – Interactive dashboard

---

## ✅ How to Run
If you'd like to recreate the model:
```bash
# Install Python dependencies
pip install pandas nltk spacy scikit-learn gensim textblob matplotlib seaborn wordcloud

# Run sentiment and topic analysis in Jupyter or Colab
