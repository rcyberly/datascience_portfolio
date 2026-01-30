# Multi-Domain Data Science Portfolio & ML Dashboard

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-FF4B4B.svg)
![Machine Learning](https://img.shields.io/badge/ML-K--Means%20Clustering-green.svg)
![Reporting](https://img.shields.io/badge/PDF-Automated%20Reporting-orange.svg)

### About this project :

Overcoming Technical Challenges: The "Behind the Scenes"
Building the Multi-Domain Data Science Portfolio was as much about software engineering as it was about analytics. Two specific challenges stood out:

1. The Unicode Encoding Hurdle
While building the Automated PDF Engine, I hit a roadblock where the FPDF library would crash when encountering non-standard characters in the dataset.

The Fix: I developed a sanitization pipeline using .encode('ascii', 'ignore') within the report generator. This ensured that the system remains 100% stable regardless of the raw data input, providing a "bulletproof" deliverable for stakeholders.

2. State Management & Dynamic UI
In the Streamlit Dashboard, I had to ensure that the reporting logic was perfectly synced with the UI.

The Fix: I implemented a robust OS-path verification system. The app doesn't just "try" to show a graph; it checks for existence first and provides a clear "Action Required" message if files are missing. This prevents the "Red Screen of Death" in Streamlit and ensures a smooth user experience.


##  Project Overview
This project is an end-to-end Data Science ecosystem that delivers actionable business intelligence across five distinct industries. It features an interactive **Streamlit Dashboard** and a custom **PDF Reporting Engine** that generates executive-level summaries on demand.

The portfolio demonstrates a full-stack data lifecycle: from rigorous **Data Cleaning** and **Exploratory Data Analysis (EDA)** to **Unsupervised Machine Learning**.

---
### Key Modules & Domain Insights
### Healthcare Analysis
Focus: Patient condition distribution and resource optimization.

Integrity: Verified 0 missing values across a 16-column dataset to ensure clinical accuracy.

### Sports Analytics (Machine Learning)
Model: K-Means Clustering (Unsupervised Learning).

Outcome: Segmented player performance into objective tiers to identify undervalued talent ("Moneyball" strategy).

### Financial Market Analysis
Indicators: 50-day and 200-day Moving Averages (MA).

Value: Smoothed price volatility to identify structural market trends and crossover signals.

### Sales Trend Analysis
Methodology: Time-series resampling and periodic aggregation.

Outcome: Isolated seasonal revenue peaks and calculated monthly growth rates to guide inventory forecasting.

### E-commerce Analytics (New Module)
Focus: Marketing channel attribution and user engagement correlations.

Outcome: Quantified ROI across SEO, Social, and Direct traffic; identified a high correlation between session duration and total purchase value to optimize the conversion funnel.

---

##  Technical Architecture



### Tech Stack
* **Frontend:** Streamlit (Custom CSS-injected UI)
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (K-Means)
* **Visualization:** Matplotlib, Seaborn
* **Automated Reporting:** FPDF (with Unicode sanitization)

---

##  File Structure
```text
├── app.py                # The interactive Streamlit Dashboard
├── generate_reports.py   # PDF Engine (Generates 6 unique reports)
├── visualizations/       # Stored PNG charts for reports and UI
├── data/                 # Raw datasets (Healthcare, Sales, etc.)
└── README.md             # Project documentation


git clone [https://github.com/your-username/datascience-portfolio.git](https://github.com/your-username/datascience-portfolio.git)

pip install streamlit fpdf pandas matplotlib seaborn scikit-learn

streamlit run app.py

1. Mathematical LogicThe K-Means algorithm works by partitioning $n$ observations into $k$ clusters. It follows an iterative process:Initialization: The model randomly selects $k$ centroids.Assignment: Each data point is assigned to the nearest centroid based on the Squared Euclidean Distance:$$d(p, q) = \sqrt{\sum_{i=1}^{n} (q_i - p_i)^2}$$Update: The centroids are recalculated as the mean of all points in that cluster.Convergence: This repeats until the centroids no longer move significantly.2. Technical ImplementationFeature Scaling: Before clustering, I applied StandardScaler to the data. This is a critical step because K-Means is distance-based; without scaling, a feature with a larger range (like Market Value) would dominate the model.Optimal 'K' Selection: I utilized the Elbow Method (Sum of Squared Distances) to determine that $k=3$ was the ideal number of clusters for this specific dataset.3. Business TranslationThe model effectively identified three distinct tiers:Elite Performers: High impact, high cost.Efficiency Gems: High impact, low cost (the primary target for scouting).Prospects: Developing players with lower current impact and value.

 Project FAQQ: Why was K-Means chosen over other clustering algorithms like DBSCAN?A: K-Means was selected due to its computational efficiency and clear interpretability for player tiering. Since our dataset has well-defined numerical features (Performance vs. Value) and we aimed for distinct "tiers" (e.g., Elite, Value, Prospect), K-Means provided more stable and actionable clusters compared to density-based methods which are better suited for non-spherical data.Q: How did you handle the 50/200-day Moving Average calculation in Finance?A: I utilized the Pandas .rolling(window=n).mean() function. This method was chosen to smooth out short-term price fluctuations (noise) and highlight the long-term trend (signal). The 50/200-day crossover is a standard industry "Golden Cross" or "Death Cross" signal, making the analysis relevant to financial stakeholders.Q: Why use a custom PDF engine instead of just taking screenshots?A: Automation and Scalability. By using the FPDF library in Python, the portfolio can handle new data updates instantly. If the source data changes, the user simply reruns the script, and all six executive reports are updated with new text and graphs in seconds. This demonstrates a "Production-First" mindset.Q: How did you ensure the "0 Null Values" claim in the Healthcare project?A: I implemented a multi-stage cleaning pipeline:Detection: Using .isnull().sum() to identify gaps.Imputation: Using median/mode strategies where appropriate for minor gaps.Verification: A final assertion check that raises an error if the null count is $> 0$ before the report is generated.

 # 1. Update your visual assets and reports
python generate_reports.py

# 2. Launch your colorful, professional UI
streamlit run app.py

