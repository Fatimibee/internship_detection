import streamlit as st
import joblib
import pandas as pd

#Load pre-trained model
model=joblib.load(r"D:\Desktop\ML PROJECTS\Internship_Fraud_detection\Internship_model1.pkl")

st.title("🎯Internship Fraud Detection🎯")

st.subheader("Predicting Internship is Scam or Genuine")

st.write("Enter the details below to check if the internship is fraud or genuine:")

Title=st.text_input("Enter Title Of Internship")
Description=st.text_area("Enter Description of Internship", height=200)

if st.button("Predict"):
    if Title and Description:

        Input_data=pd.DataFrame({
            "Title":[Title],
            "Description":[Description]
        })

        prediction=model.predict(Input_data)
        prob = model.predict_proba(Input_data)[0]
        # Extracting probabilities
        scam_prob = prob[1]   # Probability of being scam
        genuine_prob = prob[0]  # Probability of being genuine

        if prediction==1:
            st.error(f" This Internship is a Scam ❌ \n\nConfidence: {scam_prob:.2%}")
        else:
            st.success(f" This Internship is Genuine ✅ \n\nConfidence: {genuine_prob:.2%}")
    
    else:
        st.warning("Please fill in all fields to make a prediction.")