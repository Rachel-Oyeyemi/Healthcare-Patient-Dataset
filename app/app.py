"""Streamlit portfolio application."""
from __future__ import annotations
import json
from pathlib import Path
import sys
import joblib
import pandas as pd
import streamlit as st

ROOT=Path(__file__).resolve().parents[1]; sys.path.append(str(ROOT/"src"))
from feature_engineering import MODEL_FEATURES, engineer_features
from preprocess import preprocess_dataframe
from train_model import split_data, train_baseline

st.set_page_config(page_title="Healthcare Patient Analytics",page_icon="🏥",layout="wide")

@st.cache_resource
def load_baseline():
    path=ROOT/"models/baseline_logistic_regression.joblib"
    if path.exists(): return joblib.load(path)
    sample=ROOT/"data/sample_data/healthcare_sample.csv"
    if not sample.exists(): return None
    features=engineer_features(preprocess_dataframe(pd.read_csv(sample)))
    X_train,_,y_train,_=split_data(features); return train_baseline(X_train,y_train)

MODEL=load_baseline()
page=st.sidebar.radio("Navigate",["Home","Project Overview","Prediction Interface","Model Performance","Visualizations","Business Insights","About"])
st.sidebar.warning("Portfolio demonstration only. Synthetic data; not for clinical decisions.")

if page=="Home":
    st.title("Healthcare Patient Analytics & Test-Result Classification")
    cols=st.columns(4); cols[0].metric("Official rows","55,500"); cols[1].metric("Columns","15"); cols[2].metric("Target classes","3"); cols[3].metric("Duplicates","534")
    st.info("Use the compact preview immediately or download the official Kaggle file and rerun the pipeline.")
elif page=="Project Overview":
    st.header("Project Overview"); st.markdown("**Question:** Can routine admission attributes predict Normal, Abnormal, or Inconclusive test results?\n\n**Governance finding:** performance near chance is an important result—not a modeling failure.")
elif page=="Prediction Interface":
    st.header("Prediction Interface")
    if MODEL is None: st.error("Model artifact missing. Run `python run_pipeline.py`.")
    else:
        with st.form("prediction"):
            age=st.slider("Age",13,89,52); gender=st.selectbox("Gender",["Female","Male"]); blood=st.selectbox("Blood Type",["A+","A-","B+","B-","AB+","AB-","O+","O-"]); condition=st.selectbox("Medical Condition",["Arthritis","Asthma","Cancer","Diabetes","Hypertension","Obesity"]); insurer=st.selectbox("Insurance Provider",["Aetna","Blue Cross","Cigna","Medicare","UnitedHealthcare"]); billing=st.number_input("Billing Amount",value=25000.0); room=st.number_input("Room Number",101,500,300); admission=st.selectbox("Admission Type",["Elective","Emergency","Urgent"]); medication=st.selectbox("Medication",["Aspirin","Ibuprofen","Lipitor","Paracetamol","Penicillin"]); los=st.slider("Length of Stay",1,30,15); month=st.slider("Admission Month",1,12,6); year=st.slider("Admission Year",2019,2026,2024); submitted=st.form_submit_button("Predict")
        if submitted:
            record=pd.DataFrame([{"age":age,"gender":gender,"blood_type":blood,"medical_condition":condition,"insurance_provider":insurer,"billing_amount":billing,"room_number":room,"admission_type":admission,"medication":medication,"length_of_stay":los,"admission_month":month,"admission_year":year,"is_negative_billing":int(billing<0)}])[MODEL_FEATURES]
            pred=MODEL.predict(record)[0]; prob=MODEL.predict_proba(record)[0]
            st.success(f"Predicted class: **{pred}**"); st.dataframe(pd.DataFrame({"Class":MODEL.classes_,"Probability":prob}).sort_values("Probability",ascending=False),hide_index=True)
            st.caption("Low confidence is expected because the synthetic target contains little predictive signal.")
elif page=="Model Performance":
    st.header("Model Performance"); metrics=ROOT/"reports/benchmark_metrics.json"
    if metrics.exists(): st.dataframe(pd.DataFrame(json.loads(metrics.read_text())["models"]).set_index("model"))
    st.image(str(ROOT/"visuals/model_comparison.svg"),use_container_width=True); st.markdown("**Decision:** do not use clinically.")
elif page=="Visualizations":
    st.header("Visualizations")
    for name in ["target_distribution.svg","billing_distribution.svg","admissions_by_condition.svg","monthly_admissions.svg","length_of_stay_distribution.svg","correlation_heatmap.svg"]:
        path=ROOT/"visuals"/name
        if path.exists(): st.image(str(path),caption=name.replace("_"," ").replace(".svg","").title(),use_container_width=True)
elif page=="Business Insights":
    st.header("Business Insights"); st.markdown("1. Synthetic uniformity limits inference.\n2. Negative billing requires validation.\n3. Duplicates require deduplication and surrogate IDs.\n4. Near-chance accuracy indicates weak signal.\n5. Real governed data is required before deployment.")
else:
    st.header("About"); st.markdown("Built by Rachel Oyeyemi as a recruiter-ready Data Analytics & AI portfolio project.")
