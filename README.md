# 🎯 Customer Churn Prediction & Segmentation Using Machine Learning

An intelligent AI system that predicts which customers are likely to leave your business and groups them into behavior-based segments to help improve retention strategies.

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit Learn](https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-121212?style=for-the-badge&logo=chainlink&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

## 📋 Overview

This project combines supervised and unsupervised machine learning techniques to provide actionable insights about customer behavior:

- **Churn Prediction**: Uses Random Forest classifier to predict which customers are likely to churn
- **Customer Segmentation**: Applies K-Means clustering to group customers into behavior-based segments
- **AI-Powered Recommendations**: Leverages LangChain to generate personalized retention strategies based on churn probability and customer segments

## ✨ Features

- 🔮 **Predictive Analytics**: Accurate churn prediction using Random Forest algorithm
- 👥 **Smart Segmentation**: Automatic customer grouping using K-Means clustering
- 🤖 **AI Recommendations**: LangChain-powered suggestions for retention strategies
- 📊 **Interactive Dashboard**: User-friendly Streamlit interface for real-time predictions

## 🛠️ Technologies Used

- **Supervised Learning**: Random Forest Classifier
- **Unsupervised Learning**: K-Means Clustering
- **AI Framework**: LangChain for intelligent recommendations
- **UI Framework**: Streamlit
- **Data Processing**: Pandas, NumPy

## 📦 Installation

### Prerequisites

- Python 3.12 or 3.13 (Python 3.12 is recommended)
- Git

### Setup Steps

1. **Clone the repository**
```bash
git clone https://github.com/Akchiche-Mohamed-Aymen/Customer-Churn-Prediction-Segmentation-Using-Machine-Learning.git

```
2. **Go to project folder**
```bash
cd Customer-Churn-Prediction-Segmentation-Using-Machine-Learning
```
3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 🚀 Usage

Follow these steps in order to set up and run the application:

### Step 1: Data Preparation
Clean and prepare the dataset for training:
```bash
py prep_data.py
```

### Step 2: Determine Optimal K for Clustering
Find the best number of clusters for customer segmentation:
```bash
py choosing_best_k.py
```

### Step 3: Train Unsupervised Model
Train the K-Means clustering model:
```bash
py unsupervised.py
```

### Step 4: Train Supervised Model
Train the Random Forest classifier for churn prediction:
```bash
py supervised.py
```
### Step 5 Getting Gemini API Key
1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click "Create API Key" to generate your Gemini API key
3. In your project folder, create a new file called keys.py
4. Add the following line to keys.py:
   ```bash
   key = "your_gemini_api_key_here"
   ```
5. Replace "your_gemini_api_key_here" with your actual API key from Google AI Studio
### Step 6: Launch the Application
Start the interactive Streamlit dashboard:
```bash
py -m streamlit run UI.py
```

The application will open in your default web browser, where you can:
- Input customer data
- Get churn predictions
- Receive AI-powered retention recommendations

## 📊 Project Structure

```
Customer-Churn-Prediction-Segmentation-Using-Machine-Learning/
├── prep_data.py              # Data cleaning and preprocessing
├── choosing_best_k.py        # K-Means optimization
├── unsupervised.py           # Customer segmentation training
├── supervised.py             # Churn prediction model training
├── UI.py                     # Streamlit dashboard
├── requirements.txt          # Python dependencies
└── README.md                # Project documentation
```

## 🎥 Demo

### Video Preview

Watch the application in action:

<video src="https://private-user-images.githubusercontent.com/170353978/530191711-57e595bd-1de7-4374-ae5b-8e2eb423b49c.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjY2NTg5NzcsIm5iZiI6MTc2NjY1ODY3NywicGF0aCI6Ii8xNzAzNTM5NzgvNTMwMTkxNzExLTU3ZTU5NWJkLTFkZTctNDM3NC1hZTViLThlMmViNDIzYjQ5Yy5tcDQ_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUxMjI1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MTIyNVQxMDMxMTdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0zYWVkM2Y0N2JmMWIyOTYwNTQ5YmE4ODU1YmQ0YjY2NjhiZmUxOWI0NDFjZWY1YTFiODM1NTVlN2Q0ODA0NGNhJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.O1cknuBfouqyZ7AbGMO_nGYYLNNsA9L3GJQp1COy2y8" controls="controls" style="max-width: 100%;">
</video>

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📧 Contact

For questions or feedback, please open an issue in the repository.

---

⭐ If you find this project helpful, please consider giving it a star!
