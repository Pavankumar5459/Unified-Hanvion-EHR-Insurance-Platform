import streamlit as st
import pandas as pd
import plotly.express as px

def page_labs():
    st.title("Lab Results")
    labs_df=pd.DataFrame({"Date":["2025-01-01","2025-02-01","2025-03-01"],
                          "HbA1c":[6.1,6.2,6.5],
                          "Creatinine":[0.8,0.9,0.9],
                          "Cholesterol":[201,215,220]})
    st.dataframe(labs_df)
    fig=px.line(labs_df, x="Date", y=["HbA1c","Creatinine","Cholesterol"])
    st.plotly_chart(fig,use_container_width=True)
