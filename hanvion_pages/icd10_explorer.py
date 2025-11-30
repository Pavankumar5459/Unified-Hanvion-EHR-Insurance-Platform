import streamlit as st
import pandas as pd

def page_icd10_explorer():
    st.title("ICD-10 Explorer")
    try:
        df=pd.read_excel("data/section111validicd10.xlsx")
        q=st.text_input("Search ICD-10")
        if q:
            res=df[df.apply(lambda r: r.astype(str).str.contains(q,case=False).any(),axis=1)]
            st.dataframe(res)
        else:
            st.info("Type a keyword or code.")
    except:
        st.error("Upload section111validicd10.xlsx")
