import streamlit as st
import pandas as pd
import plotly.express as px

def page_patient_summary():
    st.title("Patient Summary")
    st.write("A unified snapshot of the patient’s demographics, vitals, labs, medications and recent encounters.")
    col1, col2, col3 = st.columns(3)
    with col1: st.text_input("Patient Name", "John Doe")
    with col2: st.date_input("Date of Birth")
    with col3: st.selectbox("Sex", ["Male","Female","Other"])
    st.markdown("---")
    sample_vitals=pd.DataFrame({"Date":["2025-01-01","2025-01-15","2025-02-01"],
                                "Systolic BP":[120,130,118],
                                "Diastolic BP":[80,85,79],
                                "Heart Rate":[76,88,70]})
    fig=px.line(sample_vitals, x="Date", y=["Systolic BP","Diastolic BP","Heart Rate"])
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("---")
    lab_df=pd.DataFrame({"Test":["HbA1c","Creatinine","Cholesterol"],
                         "Value":["6.1%","0.8 mg/dL","201 mg/dL"],
                         "Status":["Slightly High","Normal","High"]})
    st.dataframe(lab_df)
    st.markdown("---")
    st.write("Active medications: Metformin, Lisinopril, Atorvastatin")
