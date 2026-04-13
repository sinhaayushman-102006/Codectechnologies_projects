# 💳 Fraud Detection System (End-to-End ML + Web App)

🚀 A production-ready, full-stack machine learning system for detecting fraudulent financial transactions using real-time analytics, explainable AI, and a modern web dashboard.

---

## 📌 Overview

Financial fraud is a major challenge in digital transactions. This project builds a complete **fraud detection pipeline** that not only predicts fraud but also explains the reasoning behind each prediction.

The system combines:
- Machine Learning
- Explainable AI (SHAP)
- Real-time streaming
- Full-stack web development

---

## 🎯 Key Features

### 🧠 Machine Learning
- Random Forest classifier
- Feature scaling & preprocessing
- Fraud probability prediction

### ⚖️ Imbalanced Data Handling
- Designed for highly imbalanced datasets (~0.17% fraud cases)
- Ready for SMOTE / advanced balancing

### 🧠 Explainable AI
- SHAP-based feature importance
- Transparent predictions

### 🌐 Web Application
- Flask backend (REST APIs)
- HTML, CSS, JavaScript frontend
- Interactive dashboard

### 📡 Real-Time Fraud Detection
- Live transaction streaming simulation
- Instant fraud alerts

### 📁 Batch Processing
- Upload CSV → detect fraud in bulk

### 🔐 Authentication
- Simple login system (extendable)

### 🎬 Premium UI
- Glassmorphism design
- Lottie animations
- Interactive charts

---

## 🏗️ Architecture

---

## 📁 Folder Structure
fraud-detection-system/
│
├── app.py
├── model_train.py
├── requirements.txt
├── README.md
│
├── data/
│ └── creditcard.csv
│
├── saved_models/
│ └── model.pkl
│
├── templates/
│ └── index.html
│
├── static/
  ├── styles.css
  └── script.js


---

## 📊 Dataset

This project uses the Credit Card Fraud Detection dataset:

🔗 https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

⚠️ Dataset is not included due to size.  
Download it manually and place it in:


---

## ⚙️ Setup & Installation

### 1️⃣ Clone Repository

### 2️⃣ Install Dependencies
### 3️⃣ Train Model
### 4️⃣ Run Application
### 5️⃣ Open in Browser


---

## 📊 Model Details

| Feature        | Description |
|---------------|------------|
| Model         | Random Forest |
| Input         | Amount, Time |
| Output        | Fraud (1) / Legit (0) |
| Explainability| SHAP |

---

## 🧪 Functional Modules

### 🔍 Prediction
- Enter transaction details
- Get fraud probability instantly

### 📡 Live Streaming
- Real-time simulated transactions
- Fraud alerts

### 🧠 Explainability
- SHAP chart for feature impact

### 📁 Batch Upload
- Upload CSV file
- Detect fraud in bulk

---

## 📸 Screenshots

> Add screenshots here before submission:
- Dashboard UI  
- Prediction output  
- SHAP visualization  
- Live transaction feed  

---

## 🚀 Future Improvements

- 🔐 JWT Authentication + Database (MongoDB)
- 📊 Advanced analytics dashboard
- ⚡ WebSockets for real-time streaming
- 🌍 Cloud deployment (Render / AWS / Vercel)
- 📈 XGBoost + Autoencoder models
- 📧 Email/SMS fraud alerts

---

## 🏆 Why This Project Stands Out

✅ End-to-end ML system  
✅ Real-time fraud detection  
✅ Explainable AI integration  
✅ Full-stack implementation  
✅ Production-ready structure  

💡 Most projects stop at notebooks — this is a working product.

---

## 💼 Resume Description

Built a full-stack Fraud Detection System using Machine Learning and Flask, featuring real-time transaction monitoring, SHAP-based explainability, and an interactive dashboard for detecting fraudulent financial transactions.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---

## 🔥 Final Note

For best impact:
- Add screenshots 📸  
- Add demo video 🎥  
- Deploy live 🌍  
