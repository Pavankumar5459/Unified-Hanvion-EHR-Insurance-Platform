import os
import streamlit as st
import requests

# ----------------------------
# IMPORT ALL PAGES
# ----------------------------

# Clinical (EHR)
from hanvion_pages.ehr.patient_summary import page_patient_summary
from hanvion_pages.ehr.encounter import page_ehr_encounter
from hanvion_pages.ehr.labs import page_labs
from hanvion_pages.ehr.vitals import page_vitals
from hanvion_pages.ehr.medications import page_medications
from hanvion_pages.ehr.icd10_explorer import page_icd10_explorer
from hanvion_pages.ehr.cpt_fee_schedule import page_cpt_fee

# Insurance
from hanvion_pages.insurance.overview import page_overview
from hanvion_pages.insurance.health_profile import page_health_profile
from hanvion_pages.insurance.symptom_checker import page_symptom_checker
from hanvion_pages.insurance.insurance_eligibility import page_insurance_checker
from hanvion_pages.insurance.doctor_costs import page_doctor_costs
from hanvion_pages.insurance.medication_prices import page_medication_prices
from hanvion_pages.insurance.cms_costs import page_cms_costs

# AI
from hanvion_pages.ai.chatbot import page_chatbot


# ----------------------------
# GLOBAL CONFIG
# ----------------------------
st.set_page_config(
    page_title="Hanvion EHR Platform",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------
# PREMIUM GLOBAL CSS
# ----------------------------
st.markdown("""
<style>

/* Disable text selection for headings */
h1, h2, h3, h4, h5, h6,
.sidebar-app-title,
.sidebar-group-label {
    user-select: none;
    cursor: default;
}

/* Sidebar Styling */
.sidebar-app-title {
    font-size: 26px;
    font-weight: 800;
    padding-top: 10px;
    padding-bottom: 4px;
}

.sidebar-group-label {
    margin-top: 22px;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    color: #64748b;
    letter-spacing: 0.6px;
}

/* Block Container */
.block-container {
    max-width: 1300px !important;
}

/* Light Mode */
@media (prefers-color-scheme: light) {
    [data-testid="stSidebar"] {
        background-color: #f8fafc !important;
        border-right: 1px solid #e2e8f0 !important;
    }
    .sidebar-app-title {
        color: #1e293b !important;
    }
}

/* Dark Mode */
@media (prefers-color-scheme: dark) {
    [data-testid="stSidebar"] {
        background-color: #0f172a !important;
        border-right: 1px solid #334155 !important;
    }
    .sidebar-app-title {
        color: #f1f5f9 !important;
    }
    .sidebar-group-label {
        color: #94a3b8 !important;
    }
}
</style>
""", unsafe_allow_html=True)


# ----------------------------
# SIDEBAR NAVIGATION
# ----------------------------
with st.sidebar:
    st.markdown('<div class="sidebar-app-title">Hanvion Health</div>', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-group-label">Dashboard</div>', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-group-label">Clinical</div>', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-group-label">Coding & Documentation</div>', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-group-label">Insurance & Cost Tools</div>', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-group-label">Assessment Tools</div>', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-group-label">AI Assistant</div>', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-group-label">Settings</div>', unsafe_allow_html=True)

    page = st.radio(
        "",
        [
            "Patient Summary",
            "Encounter Notes",
            "Lab Results",
            "Vitals Timeline",
            "Medications",

            "ICD-10 Explorer",
            "CPT Fee Schedule",

            "Insurance Eligibility",
            "Doctor Visit Costs",
            "Medication Prices",
            "CMS Hospital Prices",

            "Symptom Checker",
            "Health Profile",

            "AI Chatbot",
        ]
    )


# ----------------------------
# PAGE ROUTING
# ----------------------------
if page == "Patient Summary":
    page_patient_summary()

elif page == "Encounter Notes":
    page_ehr_encounter()

elif page == "Lab Results":
    page_labs()

elif page == "Vitals Timeline":
    page_vitals()

elif page == "Medications":
    page_medications()

elif page == "ICD-10 Explorer":
    page_icd10_explorer()

elif page == "CPT Fee Schedule":
    page_cpt_fee()

elif page == "Insurance Eligibility":
    page_insurance_checker()

elif page == "Doctor Visit Costs":
    page_doctor_costs()

elif page == "Medication Prices":
    page_medication_prices()

elif page == "CMS Hospital Prices":
    page_cms_costs()

elif page == "Symptom Checker":
    page_symptom_checker()

elif page == "Health Profile":
    page_health_profile()

elif page == "AI Chatbot":
    page_chatbot()
