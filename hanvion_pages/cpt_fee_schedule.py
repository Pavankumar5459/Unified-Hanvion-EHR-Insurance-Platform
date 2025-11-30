import streamlit as st
import pandas as pd

def page_cpt_fee():
    st.title("CPT Fee Schedule")
    try:
        df=pd.read_csv("data/cms_price_transparency.csv")
        st.dataframe(df)
    except:
        st.error("Upload cms_price_transparency.csv")
