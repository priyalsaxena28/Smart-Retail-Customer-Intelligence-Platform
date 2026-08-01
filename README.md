# 🛍️ Smart Retail Customer Intelligence Platform

> **AI-Powered Smart Retail & Customer Intelligence Platform using Computer Vision, NLP, FastAPI, and Machine Learning.**

---

# 📖 Project Overview

The **Smart Retail Customer Intelligence Platform** is an AI-powered retail analytics system that integrates multiple Artificial Intelligence modules into a unified application. It enables retailers to:

- 👤 Recognize customers using Face Recognition
- 🛒 Classify retail products from images
- 💬 Analyze customer review sentiments
- 🤖 Provide AI-powered customer support
- 🌐 Serve AI models through FastAPI APIs

The project is built using **Python**, **TensorFlow**, **Scikit-learn**, **OpenCV**, **FastAPI**, and **Google Colab**.

---

# 🚀 Features

- 👤 Customer Face Recognition
- 🛒 Product Image Classification
- 💬 Customer Review Sentiment Analysis
- 🤖 AI Retail Chatbot
- 🌐 FastAPI Backend Integration

---

# 🛠️ Tech Stack

## Programming Language
- Python

## Machine Learning & Deep Learning
- TensorFlow
- Keras
- MobileNetV2
- Scikit-learn

## Natural Language Processing
- TF-IDF
- Logistic Regression

## Computer Vision
- OpenCV

## Backend
- FastAPI

## Development Tools
- Google Colab
- Git
- GitHub

---

# 📂 Project Structure

```text
Smart-Retail-Customer-Intelligence-Platform/
│
├── app/
├── data/
├── docs/
├── images/
├── models/
│   ├── product_classifier.h5
│   ├── sentiment_model.pkl
│   ├── vectorizer.pkl
│   ├── face_recognition_model.pkl
│   └── chatbot.pkl
│
├── notebooks/
│   ├── 01_Product_Classifier.ipynb
│   ├── 02_Sentiment_Analysis.ipynb
│   ├── 03_Face_Recognition.ipynb
│   └── 04_Retail_Chatbot.ipynb
│
├── README.md
├── LICENSE
└── .gitignore
```

---

# 📌 Module 1 – Product Image Classification

## 🎯 Objective

Classify retail product images into different product categories using Deep Learning.

## 📂 Dataset

Fashion Product Images Dataset (Kaggle)

## 🤖 Model

- MobileNetV2 (Transfer Learning)

## 🔄 Workflow

```text
Product Image
      │
      ▼
Image Preprocessing
      │
      ▼
MobileNetV2
      │
      ▼
Product Category Prediction
```

## 📤 Output

- `product_classifier.h5`

## ✅ Status

Completed

---

# 📌 Module 2 – Customer Review Sentiment Analysis

## 🎯 Objective

Classify customer reviews into **Positive**, **Neutral**, and **Negative** sentiments using Natural Language Processing.

## 📂 Dataset

Women's Clothing E-Commerce Reviews (Kaggle)

## 🤖 Model

- TF-IDF Vectorizer
- Logistic Regression

## 🔄 Workflow

```text
Customer Review
      │
      ▼
Text Cleaning
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Logistic Regression
      │
      ▼
Positive / Neutral / Negative
```

## 📈 Model Performance

| Metric | Value |
|---------|-------|
| Accuracy | **76.5%** |

## 📤 Output

- `sentiment_model.pkl`
- `vectorizer.pkl`

## ✅ Status

Completed

---

# 📌 Module 3 – Face Recognition

## 🎯 Objective

Recognize customers using facial recognition.

## 📂 Dataset

Labeled Faces in the Wild (LFW)

## 🤖 Model

- Support Vector Machine (SVM)

## 🔄 Workflow

```text
Face Image
     │
     ▼
Feature Extraction
     │
     ▼
SVM Classifier
     │
     ▼
Recognized Person
```

## 📤 Output

- `face_recognition_model.pkl`

## ✅ Status

Completed

---

# 📌 Module 4 – AI Retail Chatbot

## 🎯 Objective

Develop an AI-powered chatbot capable of answering common customer queries related to retail services.

## 🛠️ Technologies Used

- Python
- Sentence Transformers
- FAISS
- NumPy

## ✨ Features

- Answers customer questions
- Semantic search using embeddings
- Fast response generation

## 💬 Sample Questions

- What is your return policy?
- Do you provide home delivery?
- How can I track my order?
- What payment methods do you accept?

## 📤 Output

- `chatbot.pkl`

## ✅ Status

Completed

---

# 📌 Module 5 – FastAPI Integration

## 🎯 Objective

Deploy all AI models through REST APIs using FastAPI for seamless integration with frontend applications.

## 🚧 Status

In Progress

---

# 📊 Project Progress

| Module | Status |
|---------|--------|
| Product Image Classification | ✅ Completed |
| Sentiment Analysis | ✅ Completed |
| Face Recognition | ✅ Completed |
| AI Retail Chatbot | ✅ Completed |
| FastAPI Integration | 🔄 In Progress |

---

# 🚀 Future Enhancements

- Web Dashboard
- Voice-enabled Retail Assistant
- Customer Recommendation System
- Sales Prediction
- Inventory Forecasting
- Cloud Deployment (AWS/GCP/Azure)

---

# ▶️ How to Run the Project

```bash
git clone https://github.com/your-username/Smart-Retail-Customer-Intelligence-Platform.git

cd Smart-Retail-Customer-Intelligence-Platform

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

# 📜 License

This project is developed for **academic and educational purposes**.

---

# 👩‍💻 Author

**Priyal Saxena**

BTech – Computer Science & Engineering 

---

⭐ **If you found this project helpful, consider giving it a Star on GitHub!**
