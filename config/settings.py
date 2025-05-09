"""
Configuration settings for Ardian ESG Dashboard
"""

# Application settings
APP_TITLE = "Ardian ESG Quest Dashboard"
APP_ICON = "🎮"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "Portfolio ESG Analysis Dashboard for Ardian Data Science Internship 2025"

# Visual settings
LAYOUT = {
    'wide_mode': True,
    'sidebar_state': 'expanded',
    'hide_streamlit_style': True
}

# Color scheme (Black & White theme)
COLORS = {
    'primary': '#000000',
    'secondary': '#FFFFFF',
    'background': '#FFFFFF',
    'text': '#000000',
    'shadow': '#808080',
    'accent': '#C0C0C0'
}

# Typography
FONTS = {
    'heading': 'VT323',
    'body': 'Space Mono',
    'code': 'Courier New'
}

# Data settings
SECTORS = [
    'Technology', 
    'Renewable Energy', 
    'Retail', 
    'Healthcare', 
    'Transportation'
]

METRICS = [
    'ESG Overview', 
    'Environmental', 
    'Social', 
    'Governance', 
    'Financial'
]

# Chart settings
CHART_CONFIG = {
    'theme': 'plotly_white',
    'height': 400,
    'margin': dict(t=40, b=40, l=40, r=40),
    'font_family': 'Space Mono',
    'font_color': '#000000',
    'gridcolor': '#000000',
    'linewidth': 3
}

# ESG Score weights
ESG_WEIGHTS = {
    'Environmental': 0.35,
    'Social': 0.35,
    'Governance': 0.30
}

# Metric thresholds
THRESHOLDS = {
    'esg_excellent': 80,
    'esg_good': 60,
    'esg_fair': 40,
    'carbon_low': 10000,
    'carbon_medium': 30000,
    'carbon_high': 50000,
    'diversity_high': 50,
    'diversity_medium': 35,
    'diversity_low': 20
}

# API settings (for future implementation)
API_CONFIG = {
    'alpha_vantage': {
        'base_url': 'https://www.alphavantage.co/query',
        'timeout': 30
    },
    'finnhub': {
        'base_url': 'https://finnhub.io/api/v1',
        'timeout': 30
    }
}

# Cache settings
CACHE_CONFIG = {
    'ttl': 3600,  # 1 hour
    'max_entries': 1000
}

# File paths
DATA_PATH = 'data/'
ASSETS_PATH = 'assets/'
SCREENSHOTS_PATH = 'assets/screenshots/'

# Feature flags
FEATURES = {
    'enable_api_integration': False,
    'enable_pdf_export': False,
    'enable_advanced_analytics': True,
    'enable_real_time_updates': False
}

# Logging configuration
LOGGING = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'file': 'logs/app.log'
}