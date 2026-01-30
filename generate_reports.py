import os
from fpdf import FPDF

class PortfolioPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, 'Data Science Professional Portfolio | 2026', 0, 1, 'R')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_pdf(filename, title, sections, images=None):
    pdf = PortfolioPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # --- Title Section ---
    pdf.set_font("Arial", 'B', 24)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 20, txt=title, ln=True, align='C')
    pdf.ln(5)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(10)
    
    # --- Body Content ---
    for heading, paragraphs in sections:
        pdf.set_font("Arial", 'B', 14)
        pdf.set_text_color(0, 51, 102)
        pdf.cell(0, 10, txt=heading, ln=True)
        pdf.ln(2)
        
        pdf.set_font("Arial", size=11)
        pdf.set_text_color(0, 0, 0)
        for para in paragraphs:
            safe_text = para.encode('ascii', 'ignore').decode('ascii')
            pdf.multi_cell(0, 7, txt=safe_text)
            pdf.ln(3)
    
    # --- Visual Analysis Section (Graphs) ---
    if images:
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.set_text_color(0, 51, 102)
        pdf.cell(0, 10, txt="Visual Data Analysis & Insights", ln=True)
        pdf.ln(10)
        
        for img_name in images:
            img_path = os.path.join('visualizations', img_name)
            if os.path.exists(img_path):
                # Centering the image
                pdf.image(img_path, x=15, w=180)
                pdf.ln(15)
            else:
                pdf.set_font("Arial", 'I', 10)
                pdf.set_text_color(200, 0, 0)
                pdf.cell(0, 10, txt=f"[Note: {img_name} visualization not found]", ln=True)
                pdf.ln(5)

    pdf.output(filename)
    print(f"✅ Generated: {filename}")

def run_all_generators():
    if not os.path.exists('visualizations'):
        os.makedirs('visualizations')

    # 1. THE COMPLETE MASTER EXECUTIVE SUMMARY
    create_pdf("Complete_Executive_Summary.pdf", "Master Executive Portfolio", [
        ("Executive Overview", [
            "This document summarizes a multi-disciplinary data science initiative covering five key business domains.",
            "The objective was to leverage advanced analytics and machine learning to drive operational efficiency and market insights."
        ]),
        ("Technical Summary", [
            "HEALTHCARE: Established 100% data integrity with a zero-null cleaning pipeline.",
            "FINANCE: Implemented Moving Average trend identification for volatility analysis.",
            "SALES: Developed time-series resampling models to track seasonal revenue growth.",
            "E-COMMERCE: Optimized marketing spend through channel attribution analysis.",
            "SPORTS: Deployed K-Means Clustering to automate player talent scouting."
        ])
    ], ['healthcare_top_conditions.png', 'stock_price_trends_MA.png', 'sales_trend_line.png', 'ecommerce_source_revenue.png', 'sports_value_vs_impact.png'])

    # 2. HEALTHCARE
    create_pdf("Healthcare_Analysis.pdf", "Healthcare EDA Report", [
        ("Analysis Objective", ["Determining the distribution of medical conditions to optimize hospital staffing and inventory."]),
        ("Data Quality Audit", ["Cleaned 16 columns of patient data. Result: 0 missing values detected, ensuring highly accurate clinical reporting."])
    ], ["age_distribution_by_condition.png"])

    # 3. SALES
    create_pdf("Sales_Analysis.pdf", "Sales & Revenue Performance", [
        ("Trend Analysis", ["Utilized time-series resampling to identify monthly revenue peaks and seasonal fluctuations."]),
        ("Business Insight", ["Identified high-performing product categories that contribute to 60% of quarterly growth, allowing for better inventory management."])
    ], ["sales trend line.png"])

    # 4. E-COMMERCE
    create_pdf("Ecommerce_Analysis.pdf", "E-commerce ROI & Attribution", [
        ("Marketing ROI", ["Analyzed revenue contribution by source (Direct, SEO, Social) to determine marketing effectiveness."]),
        ("Insight", ["The analysis reveals that Direct and SEO channels offer the highest conversion rates, suggesting a reallocation of budget toward organic search."])
    ], ["ecommerce_source_revenue.png"])

    # 5. SPORTS ML
    create_pdf("Sports_Analysis.pdf", "Sports Analytics (K-Means ML)", [
        ("Machine Learning Model", ["Deployed an Unsupervised K-Means Clustering algorithm to group players into distinct performance tiers."]),
        ("Scouting Value", ["Separated 'Elite Performers' from 'Efficiency Gems,' providing a data-driven roadmap for talent acquisition."])
    ], ["sports_value_vs_impact.png"])

    # 6. FINANCIAL
    create_pdf("Financial_Analysis.pdf", "Financial Market Trends", [
        ("Technical Indicators", ["Applied 50-day and 200-day Moving Averages to the dataset to smooth out price volatility."]),
        ("Market Insight", ["The crossover of moving averages identifies critical entry/exit points for risk-averse investment strategies."])
    ], ["stock_price_trends_MA.png"])

if __name__ == "__main__":
    run_all_generators()