# 🛡️ Spam Guard AI

Spam Guard AI is a Machine Learning-powered web application that detects whether an email is **Spam** or **Safe (Ham)** using Natural Language Processing (NLP). The project is built with **Python**, **Flask**, and **Scikit-learn**, providing fast and accurate email classification through an easy-to-use web interface.

---

## 🚀 Features

- 📧 Detect Spam and Safe Emails
- 🤖 Machine Learning-Based Classification
- 📝 TF-IDF Text Vectorization
- ⚡ Real-Time Email Analysis
- 🌐 User-Friendly Flask Web Interface
- 📊 High Accuracy Prediction
- 💻 Responsive and Modern UI

---
## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- TF-IDF Vectorizer
- Multinomial Naive Bayes
- HTML5
- CSS3
- JavaScript

---
## 📂 Project Structure

```
Spam-Guard-AI/
│
├── app.py
├── train_model.py
├── spam.csv
├── spam_model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
│
├── templates/
   └── index.html
```

---
## 📊 Machine Learning Workflow

- Load the dataset
- Clean and preprocess the text
- Convert text into numerical features using TF-IDF
- Train the model using Multinomial Naive Bayes
- Evaluate the model
- Save the trained model
- Deploy with Flask

---
## 🎯 How It Works

1. Enter or paste an email message.
2. Click **Analyze Email**.
3. The model processes the text using NLP.
4. The application predicts whether the email is **Spam** or **Safe**.
5. The prediction is displayed instantly.

---
