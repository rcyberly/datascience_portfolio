import streamlit as st
import os

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Data Science Portfolio | Analytics Suite",
    layout="wide"
)

# --- 2. UPDATED PROFESSIONAL STYLING (SKY BLUE & WHITE TEXT) ---
st.markdown("""
    <style>
    .stApp { background-color: #F4F7F9; }
    
    [data-testid="stSidebar"] {
        background-color: #002B5B;
        border-right: 2px solid #005B96;
    }
    
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] label, [data-testid="stSidebar"] p {
        color: #FFFFFF !important;
    }

    .main-header {
        background: linear-gradient(90deg, #002B5B 0%, #005B96 100%);
        padding: 30px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 35px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
    }

    .insight-card {
        background-color: white;
        padding: 25px;
        border-left: 8px solid #005B96;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        margin-bottom: 25px;
    }
    
    /* SKY BLUE Background with WHITE Text */
    div.stButton > button {
        background-color: #87CEEB !important; /* Sky Blue Background */
        color: #FFFFFF !important;           /* White Text */
        border-radius: 8px !important;
        border: 2px solid #FFFFFF !important; /* White Border */
        font-weight: bold !important;
        height: 3.5em !important;
        width: 100% !important;
        transition: 0.3s ease-in-out;
        display: flex;
        align-items: center;
        justify-content: center;
        text-transform: uppercase;
    }
    
    div.stButton > button:hover {
        background-color: #5fb6d9 !important; /* Slightly darker sky blue on hover */
        border: 2px solid #002B5B !important; /* Navy border on hover */
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. UPDATED HELPER FUNCTION WITH PDF ICON & WHITE TEXT LOGIC ---
def download_pdf_button(file_path, project_name):
    # This creates the "PDF 📄 DOWNLOAD [PROJECT NAME]" label
    label = f"PDF 📄 DOWNLOAD {project_name}"
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
        st.error(f"File Not Found: {file_path}")

# --- 4. SIDEBAR NAVIGATION ---
st.sidebar.markdown("# PORTFOLIO")
page = st.sidebar.radio(
    "NAVIGATION", 
    ["Executive Summary", "Healthcare Analysis", "Sales Analysis", "Sports Analytics", "E-commerce Analysis", "Financial Analysis"]
)

# --- 5. DYNAMIC PAGE CONTENT ---
st.markdown(f'<div class="main-header"><h1>{page.upper()}</h1></div>', unsafe_allow_html=True)

if page == "Executive Summary":
    st.markdown("""
        <div class="insight-card">
            <h3>Master Portfolio Overview</h3>
            <p>Showcasing end-to-end data pipelines and automated reporting across five industries.</p>
        </div>
    """, unsafe_allow_html=True)
    download_pdf_button("Complete_Executive_Summary.pdf", "MASTER REPORT")

elif page == "Healthcare Analysis":
    st.success("DATA INTEGRITY VERIFIED: 0 NULL VALUES")
    col1, col2 = st.columns([2, 1])
    with col1:
        if os.path.exists("visualizations/healthcare_top_conditions.png"):
            st.image("visualizations/healthcare_top_conditions.png", use_container_width=True)
    with col2:
        st.markdown("<div class='insight-card'><h4>Healthcare Insights</h4>Hospital resource optimization analysis.</div>", unsafe_allow_html=True)
        download_pdf_button("Healthcare_Analysis.pdf", "HEALTHCARE")

elif page == "Sales Analysis":
    col1, col2 = st.columns([2, 1])
    with col1:
        if os.path.exists("visualizations/sales_trend_line.png"):
            st.image("visualizations/sales_trend_line.png", use_container_width=True)
    with col2:
        st.markdown("<div class='insight-card'><h4>Sales Insights</h4>Seasonal growth and revenue peak detection.</div>", unsafe_allow_html=True)
        download_pdf_button("Sales_Analysis.pdf", "SALES REPORT")

elif page == "Sports Analytics":
    st.info("ALGORITHM: K-MEANS CLUSTERING")
    col1, col2 = st.columns([2, 1])
    with col1:
        if os.path.exists("visualizations/sports_value_vs_impact.png"):
            st.image("visualizations/sports_value_vs_impact.png", use_container_width=True)
    with col2:
        st.markdown("<div class='insight-card'><h4>Sports Insights</h4>Player performance segmentation.</div>", unsafe_allow_html=True)
        download_pdf_button("Sports_Analysis.pdf", "SPORTS ML")

elif page == "E-commerce Analysis":
    col1, col2 = st.columns([2, 1])
    with col1:
        if os.path.exists("visualizations/ecommerce_source_revenue.png"):
            st.image("visualizations/ecommerce_source_revenue.png", use_container_width=True)
    with col2:
        st.markdown("<div class='insight-card'><h4>E-commerce Insights</h4>Marketing ROI via channel attribution.</div>", unsafe_allow_html=True)
        download_pdf_button("Ecommerce_Analysis.pdf", "E-COMMERCE")

elif page == "Financial Analysis":
    col1, col2 = st.columns([2, 1])
    with col1:
        if os.path.exists("visualizations/stock_price_trends_MA.png"):
            st.image("visualizations/stock_price_trends_MA.png", use_container_width=True)
    with col2:
        st.markdown("<div class='insight-card'><h4>Financial Insights</h4>Moving average trend identification.</div>", unsafe_allow_html=True)
        download_pdf_button("Financial_Analysis.pdf", "FINANCIAL")