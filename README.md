# 🐦 Twitter Sentiment & Emotion Analysis System

<div align="center">

## AI-Powered Django Web Application for Twitter Sentiment & Emotion Detection

Analyze tweets using Machine Learning and Natural Language Processing (NLP) techniques to predict sentiment polarity and emotional state.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Django](https://img.shields.io/badge/Django-Framework-green.svg)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-orange.svg)
![NLP](https://img.shields.io/badge/NLP-Twitter%20Analysis-purple.svg)
![Docker](https://img.shields.io/badge/Docker-Supported-blue.svg)

</div>

---

# 📌 Project Overview

Twitter Sentiment & Emotion Analysis System is a Django-based Machine Learning web application designed to analyze textual content from tweets and classify them into:

- 📊 Sentiment Categories
- 😊 Emotional States
- 🗣️ Opinion Patterns

The system combines:

- Natural Language Processing (NLP)
- Machine Learning Classification
- Twitter Text Processing
- Django Web Development

to provide intelligent insights from social media text.

The application supports:

✅ Sentiment Analysis  
✅ Emotion Detection  
✅ Live Tweet Processing  
✅ Manual Tweet Analysis  
✅ Interactive Django Interface  
✅ Docker Deployment  

---

# 🚀 Key Features

# 📊 Sentiment Analysis

Classifies tweets into:

- Positive 😊
- Neutral 😐
- Negative 😞

The sentiment engine processes tweet text using NLP preprocessing and machine learning models.

---

# 😊 Emotion Analysis

Predicts emotional states from tweet text such as:

- Happy
- Sad
- Angry
- Fear
- Surprise
- Neutral

Emotion classification is performed using trained ML models and textual feature extraction.

---

# 🐦 Live Twitter Tweet Analysis

Supports importing live tweets using:

- Twitter handles
- Hashtags
- Raw tweet text

Users can analyze real-time tweet content dynamically.

---

# ✍️ Manual Tweet Input

Users can manually enter tweet text and perform:

- Sentiment Prediction
- Emotion Detection
- Opinion Classification

---

# 🌐 Interactive Django Web Interface

Frontend built using:

- Django Templates
- Bootstrap
- HTML/CSS
- JavaScript

Features include:

- Responsive UI
- Dynamic pages
- Prediction forms
- Interactive visualization sections

---

# 🤖 Machine Learning Integration

Integrated ML workflow includes:

- Text preprocessing
- Feature extraction
- Trained classification models
- Real-time prediction pipeline

Technologies used:

- Scikit-learn
- Pickle Models
- NLP Pipelines

---

# 📁 Pretrained Model Support

Pre-trained ML models are stored using:

```python
pickle.dump()
```

Serialized model file:

```text
finalized_model.sav
```

---

# 🐳 Docker Support

Project includes:

- Dockerfile
- docker-compose.yml

for containerized deployment and scalability.

---

# 🏗️ System Architecture

```text
User Tweet Input
        ↓
Text Cleaning & Preprocessing
        ↓
Feature Extraction (TF-IDF / Vectorization)
        ↓
Machine Learning Prediction
        ↓
Sentiment / Emotion Classification
        ↓
Result Display on Django Frontend
```

---

# ⚙️ Technology Stack

# Backend

- Python
- Django Framework

---

# Machine Learning & NLP

- Scikit-learn
- NLP Processing
- TF-IDF Vectorization
- Pickle Serialization

---

# Frontend

- HTML5
- CSS3
- Bootstrap
- JavaScript

---

# Database

- SQLite3

---

# Deployment & DevOps

- Docker
- Gunicorn
- Render
- Railway

---

# 📂 Project Structure

```text
Twitter-Sentiment-Emotion-Analysis/
│
├── sentiment_emotion_analysis/
│   │
│   ├── emotion/
│   │   ├── migrations/
│   │   ├── static/
│   │   ├── templates/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── emotion_analysis_code.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── tweepy_emotion.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── sentiment/
│   │   ├── migrations/
│   │   ├── static/
│   │   ├── templates/
│   │   ├── admin.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── sentiment_analysis_code.py
│   │   ├── tweepy_sentiment.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── sentiment_or_emotion/
│   │   ├── migrations/
│   │   ├── static/
│   │   ├── templates/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── sentiment_emotion_analysis/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── __init__.py
│   │
│   ├── db.sqlite3
│   ├── finalized_model.sav
│   ├── manage.py
│   ├── requirements.txt
│   └── text_emotion.csv
│
├── Dockerfile
├── docker-compose.yml
├── README.md
└── .gitignore
```

---

# 🧠 Machine Learning Workflow

# Step 1 — Data Collection

Tweet datasets are collected for:

- Sentiment labels
- Emotion labels

---

# Step 2 — Text Preprocessing

The tweet text undergoes:

- Lowercasing
- Stopword removal
- Punctuation cleaning
- Tokenization
- Text normalization

---

# Step 3 — Feature Extraction

Text is transformed into vectors using:

- CountVectorizer
- TF-IDF

---

# Step 4 — Model Training

Machine Learning models are trained for:

- Sentiment Classification
- Emotion Classification

---

# Step 5 — Model Serialization

Models are saved using:

```python
pickle.dump()
```

---

# Step 6 — Real-Time Prediction

User tweets are processed dynamically and predictions are displayed on the frontend.

---

# 🚀 Installation & Setup

# 1️⃣ Clone Repository

```bash
git clone <repository-url>
cd Twitter-Sentiment-Emotion-Analysis
```

---

# 2️⃣ Create Virtual Environment

## Windows

```bash
python -m venv venv
venv\Scripts\activate
```

## Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 4️⃣ Run Database Migrations

```bash
python manage.py migrate
```

---

# 5️⃣ Start Django Server

```bash
python manage.py runserver
```

---

# 6️⃣ Open Browser

```text
http://127.0.0.1:8000/
```

---

# 🐳 Docker Deployment

# Build Docker Image

```bash
docker build -t twitter-sentiment .
```

---

# Run Docker Container

```bash
docker run -p 8000:8000 twitter-sentiment
```

---

# Using Docker Compose

```bash
docker-compose up
```

---

# 🌐 Deployment on Render

# Build Command

```bash
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
```

---

# Start Command

```bash
gunicorn sentiment_emotion_analysis.wsgi:application
```

---

# 📊 Supported Functionalities

| Module | Description |
|---|---|
| Sentiment Analysis | Detects tweet polarity |
| Emotion Analysis | Predicts emotional state |
| Live Tweet Import | Analyze tweets using hashtags/handles |
| Manual Tweet Analysis | User-entered tweet predictions |
| Django UI | Interactive frontend interface |
| Docker Deployment | Containerized deployment support |

---

# 📸 Application Screens

The application contains:

✅ Home Dashboard  
✅ Sentiment Analysis Page  
✅ Emotion Analysis Page  
✅ Live Tweet Analysis  
✅ Manual Tweet Input Interface  

---

# 🔒 Future Enhancements

Planned future improvements include:

- 🔴 Real-time Twitter API integration
- 🧠 Deep Learning models (LSTM/BERT)
- 📈 Sentiment visualization dashboards
- 📊 Interactive analytics charts
- 👥 User authentication system
- 🌍 Multi-language support
- ⚡ Streaming tweet analysis
- 🔗 REST API integration
- ☁️ Cloud deployment scalability

---

# 📈 Potential Use Cases

This project can be used for:

- Brand Reputation Monitoring
- Social Media Analytics
- Political Sentiment Analysis
- Customer Feedback Analysis
- Opinion Mining
- Emotion-Aware Applications
- Market Trend Analysis

---

# 👨‍💻 Author

Developed as a Django + Machine Learning + NLP based project for Twitter Sentiment and Emotion Analysis.

---

# 📜 License

This project is intended for:

- Educational purposes
- Research purposes
- Learning and experimentation

---