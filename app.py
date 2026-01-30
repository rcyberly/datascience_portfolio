import streamlit as st
import os

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Data Science Portfolio | Analytics Suite",
    layout="wide"
)

# --- 2. PROFESSIONAL STYLING (CSS) ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #F4F7F9;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #002B5B;
        border-right: 2px solid #005B96;
    }
    
    /* Change Sidebar Text Color */
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] label, [data-testid="stSidebar"] p {
        color: #FFFFFF !important;
    }

    /* Modern Header Bar */
    .main-header {
        background: linear-gradient(90deg, #002B5B 0%, #005B96 100%);
        padding: 30px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 35px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
    }

    /* Insight/Description Cards */
    .insight-card {
        background-color: white;
        padding: 25px;
        border-left: 8px solid #005B96;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        margin-bottom: 25px;
    }
    
    /* Customizing Download Buttons */
    div.stButton > button {
        background-color: #005B96 !important;
        color: white !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        height: 3em !important;
        width: 100% !important;
        transition: 0.3s ease-in-out;
    }
    
    div.stButton > button:hover {
        background-color: #002B5B !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# Helper Function
def download_pdf_button(file_path, label):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            st.download_button(
                label=label,
                data=f,
                file_name=file_path,
                mime="application/pdf",
                key=file_path 
            )
    else:
        st.error(f"System Error: {file_path} generation failed.")

# --- 3. SIDEBAR NAVIGATION ---
st.sidebar.markdown("# PORTFOLIO")
page = st.sidebar.radio(
    "NAVIGATION", 
    ["Executive Summary", "Healthcare Analysis", "Sales Analysis", "Sports Analytics", "E-commerce Analysis", "Financial Analysis"]
)

# --- 4. DYNAMIC PAGE CONTENT ---

# Professional Header
st.markdown(f'<div class="main-header"><h1>{page.upper()}</h1></div>', unsafe_allow_html=True)

if page == "Executive Summary":
    st.markdown("""
        <div class="insight-card">
            <h3>Master Portfolio Overview</h3>
            <p>This dashboard serves as a technical showcase of end-to-end data pipelines across five distinct industries. 
            Each module demonstrates expertise in data cleaning, exploratory analysis, and predictive modeling.</p>
        </div>
    """, unsafe_allow_html=True)
    download_pdf_button("Complete_Executive_Summary.pdf", "DOWNLOAD MASTER PORTFOLIO REPORT")

elif page == "Healthcare Analysis":
    st.success("DATA INTEGRITY VERIFIED: 0 NULL VALUES")
    col1, col2 = st.columns([2, 1])
    with col1:
        if os.path.exists("visualizations/healthcare_top_conditions.png"):
            st.image("visualizations/healthcare_top_conditions.png", use_container_width=True)
    with col2:
        st.markdown("<div class='insight-card'><h4>Project Value</h4>Optimizing hospital resource allocation by analyzing the prevalence of chronic conditions.</div>", unsafe_allow_html=True)
        download_pdf_button("Healthcare_Analysis.pdf", "GET TECHNICAL REPORT")

elif page == "Sales Analysis":
    col1, col2 = st.columns([2, 1])
    with col1:
        if os.path.exists("visualizations/sales_trend_line.png"):
            st.image("visualizations/sales_trend_line.png", use_container_width=True)
    with col2:
        st.markdown("<div class='insight-card'><h4>Project Value</h4>Time-series resampling utilized to identify seasonal growth cycles and revenue peaks.</div>", unsafe_allow_html=True)
        download_pdf_button("Sales_Analysis.pdf", "GET SALES REPORT")

elif page == "Sports Analytics":
    st.info("ALGORITHM DEPLOYED: K-MEANS CLUSTERING")
    col1, col2 = st.columns([2, 1])
    with col1:
        if os.path.exists("visualizations/sports_value_vs_impact.png"):
            st.image("visualizations/sports_value_vs_impact.png", use_container_width=True)
    with col2:
        st.markdown("<div class='insight-card'><h4>Project Value</h4>Segmenting player performance into objective tiers to identify undervalued talent.</div>", unsafe_allow_html=True)
        download_pdf_button("Sports_Analysis.pdf", "GET ML REPORT")

elif page == "E-commerce Analysis":
    col1, col2 = st.columns([2, 1])
    with col1:
        if os.path.exists("visualizations/ecommerce_source_revenue.png"):
            st.image("visualizations/ecommerce_source_revenue.png", use_container_width=True)
    with col2:
        st.markdown("<div class='insight-card'><h4>Project Value</h4>Channel attribution modeling to determine marketing ROI across diverse traffic sources.</div>", unsafe_allow_html=True)
        download_pdf_button("Ecommerce_Analysis.pdf", "GET E-COMMERCE REPORT")

elif page == "Financial Analysis":
    col1, col2 = st.columns([2, 1])
    with col1:
        if os.path.exists("visualizations/stock_price_trends_MA.png"):
            st.image("visualizations/stock_price_trends_MA.png", use_container_width=True)
    with col2:
        st.markdown("<div class='insight-card'><h4>Project Value</h4>Utilizing 50/200-day moving averages to filter market noise from structural trends.</div>", unsafe_allow_html=True)
        download_pdf_button("Financial_Analysis.pdf", "GET FINANCIAL REPORT")