# 🧠 Stroke Risk Prediction App

An interactive Streamlit web app that predicts the risk of stroke based on user health and lifestyle information.  
It uses a machine learning model trained on healthcare data to provide instant predictions.

---

## 🚀 Features

- Predicts stroke risk based on:
  - Age
  - BMI
  - Average glucose level
  - Gender
  - Smoking status
  - Hypertension
  - Heart disease
  - Marital status
  - Residence type
  - Work type
- Friendly and simple user interface.
- Instant feedback with health advisory messages.
- Error handling for model loading.

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pickle (for loading ML model)
- NumPy

---

## 📥 Setup Instructions

1. **Clone this repository:**
   ```bash
   git clone https://github.com/VishalGaud17/Stroke.git
   cd Stroke
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app:**
   ```bash
   streamlit run stroke.py
   ```

---

## 📂 Project Structure

```plaintext
Stroke/
├── stroke.py         # Main Streamlit application
├── stroke.pkl        # Pre-trained machine learning model
└── README.md         # Project documentation (you are reading it)
```

---

## 🤔 How It Works

1. Enter your details such as age, BMI, glucose level, etc.
2. The app encodes the inputs appropriately.
3. Inputs are passed to the machine learning model.
4. The model predicts whether there is a stroke risk.
5. An advisory message is displayed based on the prediction.

---

## 👨‍💻 Author

- [Vishal Gaud](https://github.com/VishalGaud17)

---

## ⭐ Support

If you find this project useful, please consider giving it a ⭐ on GitHub!

---

## ⚠️ Disclaimer

This app is for educational and informational purposes only.  
It is not a substitute for professional medical advice, diagnosis, or treatment.  
Always seek the advice of your physician or other qualified health provider for any medical condition.

