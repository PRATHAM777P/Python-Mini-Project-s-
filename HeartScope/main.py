import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import plotly.graph_objects as go

# -------------------------
# 1. Load & Train Models
# -------------------------
df = pd.read_csv("../input/heart.csv")

np.random.seed(42)
df['BMI'] = np.random.uniform(18,35, df.shape[0])
df['Smoking'] = np.random.choice([0,1], df.shape[0], p=[0.7,0.3])
df['Alcohol'] = np.random.randint(0,15, df.shape[0])
df['Activity'] = np.random.choice([0,1,2], df.shape[0], p=[0.3,0.5,0.2])
df['Family_History'] = np.random.choice([0,1], df.shape[0], p=[0.6,0.4])
df['Diabetes'] = np.random.choice([0,1], df.shape[0], p=[0.8,0.2])
df['LDL'] = np.random.randint(70,190, df.shape[0])
df['HDL'] = np.random.randint(30,80, df.shape[0])
df['Triglycerides'] = np.random.randint(50,250, df.shape[0])
df['ECG_Abnormal'] = np.random.choice([0,1], df.shape[0], p=[0.7,0.3])

# Convert categorical features
df = pd.get_dummies(df, columns=['cp','thal','slope'], drop_first=True)

# Features and target
X = df.drop('target', axis=1)
y = df['target']

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train Logistic Regression & Random Forest
lr_model = LogisticRegression(max_iter=1000, solver='lbfgs')
rf_model = RandomForestClassifier(n_estimators=500, random_state=42)

lr_model.fit(X_scaled, y)
rf_model.fit(X_scaled, y)

# -------------------------
# 2. Streamlit UI
# -------------------------
st.set_page_config(
    page_title="HeartScope",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("❤️ HeartScope: Advanced Heart Risk Predictor")
st.markdown("""
Welcome to **HeartScope**, your interactive heart health assessment tool.  
Enter patient details below to predict the risk of heart disease using **Logistic Regression** and **Random Forest** models.  
Visual gauges provide an instant view of risk percentage.
""")

# -------------------------
# 3. User Input Features Function
# -------------------------
def user_input_features():
    st.subheader("Patient Details")
    age = st.number_input("Age", 20, 100, 50)
    sex = st.selectbox("Sex", ("Male", "Female"))
    sex = 1 if sex=="Male" else 0
    trestbps = st.number_input("Resting Blood Pressure (mm Hg)", 90, 200, 120)
    chol = st.number_input("Serum Cholesterol (mg/dl)", 100, 400, 200)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ("Yes","No"))
    fbs = 1 if fbs=="Yes" else 0
    thalach = st.number_input("Max Heart Rate Achieved", 70, 220, 150)
    exang = st.selectbox("Exercise Induced Angina", ("Yes","No"))
    exang = 1 if exang=="Yes" else 0
    oldpeak = st.number_input("ST Depression Induced by Exercise", 0.0, 10.0, 1.0)
    ca = st.number_input("Number of Major Vessels (0-3)", 0, 3, 0)

    # New features
    BMI = st.number_input("BMI", 15.0, 40.0, 25.0)
    Smoking = st.selectbox("Smoking", ("Yes","No"))
    Smoking = 1 if Smoking=="Yes" else 0
    Alcohol = st.number_input("Alcohol Intake (units/week)", 0, 20, 0)
    Activity = st.selectbox("Physical Activity Level", ("Low","Moderate","High"))
    Activity = {"Low":0,"Moderate":1,"High":2}[Activity]
    Family_History = st.selectbox("Family History of Heart Disease", ("Yes","No"))
    Family_History = 1 if Family_History=="Yes" else 0
    Diabetes = st.selectbox("Diabetes", ("Yes","No"))
    Diabetes = 1 if Diabetes=="Yes" else 0
    LDL = st.number_input("LDL Cholesterol", 50, 250, 100)
    HDL = st.number_input("HDL Cholesterol", 20, 100, 50)
    Triglycerides = st.number_input("Triglycerides", 50, 300, 100)
    ECG_Abnormal = st.selectbox("ECG Abnormalities", ("Yes","No"))
    ECG_Abnormal = 1 if ECG_Abnormal=="Yes" else 0

    # Chest Pain / Thal / Slope (encoded)
    cp_2 = st.selectbox("Chest Pain Type 2", ("No","Yes"))=="Yes"
    cp_3 = st.selectbox("Chest Pain Type 3", ("No","Yes"))=="Yes"
    cp_4 = st.selectbox("Chest Pain Type 4", ("No","Yes"))=="Yes"
    thal_6 = st.selectbox("Thalassemia - Fixed Defect", ("No","Yes"))=="Yes"
    thal_7 = st.selectbox("Thalassemia - Reversable Defect", ("No","Yes"))=="Yes"
    slope_2 = st.selectbox("Slope of Peak Exercise ST Segment - 2", ("No","Yes"))=="Yes"
    slope_3 = st.selectbox("Slope of Peak Exercise ST Segment - 3", ("No","Yes"))=="Yes"

    data = {
        "age": age, "sex": sex, "trestbps": trestbps, "chol": chol,
        "fbs": fbs, "thalach": thalach, "exang": exang, "oldpeak": oldpeak, "ca": ca,
        "BMI": BMI, "Smoking": Smoking, "Alcohol": Alcohol, "Activity": Activity,
        "Family_History": Family_History, "Diabetes": Diabetes,
        "LDL": LDL, "HDL": HDL, "Triglycerides": Triglycerides, "ECG_Abnormal": ECG_Abnormal,
        "cp_2": int(cp_2), "cp_3": int(cp_3), "cp_4": int(cp_4),
        "thal_6": int(thal_6), "thal_7": int(thal_7),
        "slope_2": int(slope_2), "slope_3": int(slope_3)
    }

    return pd.DataFrame(data, index=[0])

input_df = user_input_features()
input_scaled = scaler.transform(input_df)

# -------------------------
# 4. Prediction & Risk Score
# -------------------------
st.subheader("Predictions & Risk Score (%)")

lr_prob = lr_model.predict_proba(input_scaled)[0][1] * 100
rf_prob = rf_model.predict_proba(input_scaled)[0][1] * 100

st.write(f"**Logistic Regression:** {'Heart Disease' if lr_prob>50 else 'No Heart Disease'} ({lr_prob:.2f}%)")
st.write(f"**Random Forest:** {'Heart Disease' if rf_prob>50 else 'No Heart Disease'} ({rf_prob:.2f}%)")

# -------------------------
# 5. Risk Gauges Visualization
# -------------------------
def plot_gauge(prob, model_name):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prob,
        domain={'x':[0,1],'y':[0,1]},
        title={'text': model_name},
        gauge={'axis': {'range':[0,100]},
               'bar': {'color': "red" if prob>50 else "green"},
               'steps':[{'range':[0,50],'color':'lightgreen'},{'range':[50,100],'color':'lightcoral'}]}
    ))
    st.plotly_chart(fig)

plot_gauge(lr_prob, "Logistic Regression Risk")
plot_gauge(rf_prob, "Random Forest Risk")
