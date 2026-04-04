# HeartScope: Advanced Heart Risk Predictor

**HeartScope** is an interactive **Streamlit web application** for predicting the risk of heart disease using machine learning models. The app leverages **Logistic Regression** and **Random Forest** classifiers along with extended health features to provide an accurate and user-friendly heart health assessment.

---

## 🧠 Features

1. Predicts heart disease risk based on patient input data.
2. Interactive risk gauges visualize probability scores.
3. Supports classic heart health features:

   * Age, Sex, Blood Pressure, Cholesterol, Fasting Blood Sugar, Max Heart Rate, Exercise-Induced Angina, ST Depression, Chest Pain Type, Thalassemia, Number of Major Vessels.
4. Additional lifestyle and medical risk features:

   * BMI, Smoking Status, Alcohol Intake, Physical Activity Level, Family History of Heart Disease, Diabetes, LDL, HDL, Triglycerides, ECG Abnormalities.
5. User-friendly Streamlit interface with input forms and visual output.
6. Risk probability (%) displayed for each model to help clinical understanding.

---

## ⚙️ Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/HeartScope.git
cd HeartScope
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

**requirements.txt example:**

```
streamlit
pandas
numpy
scikit-learn
plotly
```

3. Run the Streamlit app:

```bash
streamlit run app.py
```

---

## 📝 Usage

1. Open the app in your browser (Streamlit will provide a local URL).
2. Enter patient details in the input form, including lifestyle and clinical features.
3. View predictions from **Logistic Regression** and **Random Forest** models.
4. Check interactive risk gauges to see the probability (%) of heart disease.

---

## 📊 Screenshots

**Input Form:**

![Input Form](screenshots/input_form.png)

**Prediction & Risk Gauges:**

![Risk Gauges](screenshots/risk_gauges.png)

*(Add screenshots from your running app)*

---

## 🧩 How it Works

1. The dataset `heart.csv` is used to train Logistic Regression and Random Forest models.
2. The app scales all numeric features using `StandardScaler`.
3. User input is converted into the same feature format used for training.
4. Predictions are made, and probability scores are displayed along with visual gauges.

---

## 🧪 Technologies Used

* Python 3.x
* Streamlit for UI
* Scikit-learn for ML models
* Plotly for interactive gauges
* Pandas & NumPy for data handling

---

## 💡 Future Improvements

* Add **SHAP or LIME visualizations** for model explainability.
* Incorporate **more advanced ML models** (XGBoost, LightGBM).
* Connect with a **real clinical dataset** for higher accuracy.
* Add **risk mitigation tips** based on user input.

---



