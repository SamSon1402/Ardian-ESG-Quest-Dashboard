import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px

# Set page config
st.set_page_config(
    page_title="Ardian ESG Quest Dashboard",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for retro gaming aesthetic
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&display=swap');
    
    /* Main container */
    .stApp {
        background-color: #FFFFFF;
    }
    
    /* Headers with VT323 font */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'VT323', monospace !important;
        color: #000000 !important;
        text-transform: uppercase;
        letter-spacing: 3px;
        text-shadow: 3px 3px 0px #808080;
    }
    
    /* Body text */
    p, span, label, div {
        font-family: 'Space Mono', monospace !important;
        color: #000000 !important;
    }
    
    /* Retro buttons */
    .stButton > button {
        font-family: 'VT323', monospace !important;
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 4px solid #000000 !important;
        border-radius: 0px !important;
        box-shadow: 4px 4px 0px #000000 !important;
        text-transform: uppercase;
        font-size: 20px !important;
        letter-spacing: 2px;
        transition: all 0.1s ease !important;
    }
    
    .stButton > button:hover {
        transform: translate(2px, 2px);
        box-shadow: 2px 2px 0px #000000 !important;
    }
    
    /* Pixel-perfect containers */
    .metric-container {
        background-color: #FFFFFF;
        border: 4px solid #000000;
        border-radius: 0px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 6px 6px 0px #000000;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #F0F0F0 !important;
        border-right: 4px solid #000000 !important;
    }
    
    /* Metric cards */
    [data-testid="metric-container"] {
        background-color: #FFFFFF;
        border: 3px solid #000000;
        border-radius: 0px;
        box-shadow: 4px 4px 0px #000000;
        margin: 5px;
    }
    
    /* Select boxes */
    .stSelectbox > div > div {
        background-color: #FFFFFF !important;
        border: 2px solid #000000 !important;
        border-radius: 0px !important;
    }
    
    /* Sliders */
    .stSlider > div > div {
        background-color: #000000 !important;
    }
    
    /* Progress bars */
    .stProgress > div > div {
        background-color: #000000 !important;
    }
    
    /* 8-bit style divider */
    .pixel-divider {
        height: 8px;
        background-image: repeating-linear-gradient(
            to right,
            #000000,
            #000000 8px,
            #FFFFFF 8px,
            #FFFFFF 16px
        );
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# Generate mock data for companies
@st.cache_data
def generate_mock_data():
    # Using sectors mentioned in the Ardian internship description
    companies = ['TechVenture SA', 'WindPower Europe', 'RetailNext Group', 'MedTech Solutions', 'LogiTrans International']
    sectors = ['Technology', 'Renewable Energy', 'Retail', 'Healthcare', 'Transportation']
    
    data = []
    for i, company in enumerate(companies):
        # Financial metrics
        financial_data = {
            'Company': company,
            'Sector': sectors[i],
            'Market Cap (B)': np.random.uniform(10, 500),
            'Revenue (B)': np.random.uniform(5, 200),
            'P/E Ratio': np.random.uniform(10, 40),
            'Profit Margin (%)': np.random.uniform(5, 30),
            'Debt to Equity': np.random.uniform(0.3, 2.5),
            
            # ESG scores
            'ESG Total Score': np.random.uniform(40, 90),
            'Environmental Score': np.random.uniform(30, 95),
            'Social Score': np.random.uniform(35, 90),
            'Governance Score': np.random.uniform(40, 95),
            
            # Specific ESG metrics
            'Carbon Emissions (MT)': np.random.uniform(1000, 50000),
            'Renewable Energy (%)': np.random.uniform(10, 80),
            'Employee Diversity (%)': np.random.uniform(20, 60),
            'Board Independence (%)': np.random.uniform(30, 90),
            'Safety Incidents': np.random.randint(0, 20)
        }
        data.append(financial_data)
    
    return pd.DataFrame(data)

# Generate time series data
@st.cache_data
def generate_time_series(company, metric, days=365):
    dates = [datetime.now() - timedelta(days=x) for x in range(days)]
    base_value = np.random.uniform(50, 100)
    trend = np.random.uniform(-0.05, 0.1)
    noise = np.random.normal(0, 5, days)
    values = base_value + trend * np.arange(days) + noise
    
    return pd.DataFrame({
        'Date': dates,
        metric: values
    })

# Title with pixel art style
st.markdown("<h1 style='text-align: center; font-size: 64px;'>🎮 ARDIAN ESG QUEST 🎮</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; font-size: 32px;'>PORTFOLIO ANALYSIS DASHBOARD</h2>", unsafe_allow_html=True)
st.markdown("<div class='pixel-divider'></div>", unsafe_allow_html=True)

# Load data
df = generate_mock_data()

# Sidebar - Game Controls
st.sidebar.markdown("<h2>ARDIAN CONTROLS</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='font-size: 14px;'>PORTFOLIO NAVIGATOR</p>", unsafe_allow_html=True)

# Company selector
selected_company = st.sidebar.selectbox(
    "SELECT PORTFOLIO COMPANY",
    options=df['Company'].tolist(),
    index=0
)

# Sector filter
selected_sector = st.sidebar.selectbox(
    "FILTER BY SECTOR",
    options=['All'] + df['Sector'].unique().tolist(),
    index=0
)

# Metric focus
metric_focus = st.sidebar.selectbox(
    "ANALYSIS FOCUS",
    options=['ESG Overview', 'Environmental', 'Social', 'Governance', 'Financial'],
    index=0
)

# Add arcade-style button
if st.sidebar.button("🎯 ANALYZE PORTFOLIO"):
    st.sidebar.success("ARDIAN ANALYSIS ACTIVATED!")

st.sidebar.markdown("<div class='pixel-divider'></div>", unsafe_allow_html=True)

# Main content area
company_data = df[df['Company'] == selected_company].iloc[0]

# Score display with progress bars
st.markdown("<h2>COMPANY STATS</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='metric-container'>", unsafe_allow_html=True)
    st.markdown(f"<h3>{selected_company}</h3>", unsafe_allow_html=True)
    st.markdown(f"<p>SECTOR: {company_data['Sector']}</p>", unsafe_allow_html=True)
    st.markdown(f"<p>MARKET CAP: ${company_data['Market Cap (B)']:.1f}B</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='metric-container'>", unsafe_allow_html=True)
    st.markdown("<h3>ESG POWER LEVEL</h3>", unsafe_allow_html=True)
    esg_score = company_data['ESG Total Score']
    st.progress(esg_score/100)
    st.markdown(f"<p style='text-align: center; font-size: 24px;'>{esg_score:.0f}/100</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='metric-container'>", unsafe_allow_html=True)
    st.markdown("<h3>FINANCIAL HEALTH</h3>", unsafe_allow_html=True)
    health_score = min(100, company_data['Profit Margin (%)'] * 3)
    st.progress(health_score/100)
    st.markdown(f"<p style='text-align: center; font-size: 24px;'>{health_score:.0f}/100</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='pixel-divider'></div>", unsafe_allow_html=True)

# Detailed metrics based on selection
if metric_focus == 'ESG Overview':
    st.markdown("<h2>ESG STATS BREAKDOWN</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("<h3>ENVIRONMENTAL</h3>", unsafe_allow_html=True)
        env_score = company_data['Environmental Score']
        st.progress(env_score/100)
        st.metric("Score", f"{env_score:.0f}/100")
        st.metric("Carbon Emissions", f"{company_data['Carbon Emissions (MT)']:,.0f} MT")
        st.metric("Renewable Energy", f"{company_data['Renewable Energy (%)']:.0f}%")
    
    with col2:
        st.markdown("<h3>SOCIAL</h3>", unsafe_allow_html=True)
        social_score = company_data['Social Score']
        st.progress(social_score/100)
        st.metric("Score", f"{social_score:.0f}/100")
        st.metric("Employee Diversity", f"{company_data['Employee Diversity (%)']:.0f}%")
        st.metric("Safety Incidents", f"{company_data['Safety Incidents']}")
    
    with col3:
        st.markdown("<h3>GOVERNANCE</h3>", unsafe_allow_html=True)
        gov_score = company_data['Governance Score']
        st.progress(gov_score/100)
        st.metric("Score", f"{gov_score:.0f}/100")
        st.metric("Board Independence", f"{company_data['Board Independence (%)']:.0f}%")

elif metric_focus == 'Financial':
    st.markdown("<h2>FINANCIAL STATS</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Revenue", f"${company_data['Revenue (B)']:.1f}B")
        st.metric("P/E Ratio", f"{company_data['P/E Ratio']:.1f}")
    
    with col2:
        st.metric("Profit Margin", f"{company_data['Profit Margin (%)']:.1f}%")
        st.metric("Debt to Equity", f"{company_data['Debt to Equity']:.2f}")
    
    with col3:
        st.metric("Market Cap", f"${company_data['Market Cap (B)']:.1f}B")

st.markdown("<div class='pixel-divider'></div>", unsafe_allow_html=True)

# Comparative analysis
st.markdown("<h2>ARDIAN PORTFOLIO COMPARISON</h2>", unsafe_allow_html=True)

# Filter data based on sector selection
filtered_df = df if selected_sector == 'All' else df[df['Sector'] == selected_sector]

# Create radar chart
fig = go.Figure()

categories = ['Environmental Score', 'Social Score', 'Governance Score', 
              'Profit Margin (%)', 'Renewable Energy (%)']

for company in filtered_df['Company']:
    company_values = filtered_df[filtered_df['Company'] == company]
    values = [company_values[cat].iloc[0] for cat in categories]
    
    fig.add_trace(go.Scatterpolar(
        r=values + [values[0]],
        theta=categories + [categories[0]],
        fill='toself',
        name=company,
        line=dict(color='black' if company == selected_company else 'gray', width=3)
    ))

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 100],
            gridcolor='black',
            gridwidth=2
        ),
        angularaxis=dict(
            gridcolor='black',
            gridwidth=2
        )
    ),
    showlegend=True,
    template=None,
    plot_bgcolor='white',
    paper_bgcolor='white',
    font=dict(family='Space Mono', color='black')
)

st.plotly_chart(fig, use_container_width=True)

# Time series visualization
st.markdown("<h2>SCORE HISTORY</h2>", unsafe_allow_html=True)

time_series_data = generate_time_series(selected_company, 'ESG Score')

fig2 = go.Figure()

fig2.add_trace(go.Scatter(
    x=time_series_data['Date'],
    y=time_series_data['ESG Score'],
    mode='lines',
    line=dict(color='black', width=3),
    fill='tozeroy',
    fillcolor='rgba(0,0,0,0.1)'
))

fig2.update_layout(
    title=f"ARDIAN PORTFOLIO: {selected_company} ESG Score Evolution",
    xaxis_title="Time",
    yaxis_title="ESG Score",
    template=None,
    plot_bgcolor='white',
    paper_bgcolor='white',
    font=dict(family='Space Mono', color='black'),
    xaxis=dict(gridcolor='black', gridwidth=1),
    yaxis=dict(gridcolor='black', gridwidth=1)
)

st.plotly_chart(fig2, use_container_width=True)

# Footer
st.markdown("<div class='pixel-divider'></div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 16px;'>🕹️ ARDIAN ESG QUEST v1.0 - PRESS START TO INVEST RESPONSIBLY 🕹️</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 14px;'>DEVELOPED FOR ARDIAN DATA SCIENCE INTERNSHIP 2025</p>", unsafe_allow_html=True)