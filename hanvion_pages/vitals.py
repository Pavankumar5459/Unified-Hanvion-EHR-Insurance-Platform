import streamlit as st
import pandas as pd
import plotly.express as px

def page_vitals():
    st.title("Vitals Timeline")
    df=pd.DataFrame({"Date":["2025-01-01","2025-01-15","2025-02-01"],
                     "Systolic BP":[120,130,118],
                     "Diastolic BP":[80,85,78],
                     "Heart Rate":[76,88,70],
                     "Weight (lbs)":[170,169,168]})
    st.dataframe(df)
    fig=px.line(df,x="Date",y=["Systolic BP","Diastolic BP","Heart Rate","Weight (lbs)"])
    st.plotly_chart(fig,use_container_width=True)
