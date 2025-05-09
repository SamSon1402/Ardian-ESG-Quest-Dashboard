"""
Data generation utilities for Ardian ESG Dashboard
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
import random


def generate_mock_data() -> pd.DataFrame:
    """
    Generate mock ESG and financial data for portfolio companies.
    
    Returns:
        pd.DataFrame: DataFrame containing company data with ESG and financial metrics
    """
    companies = [
        'TechVenture SA', 
        'WindPower Europe', 
        'RetailNext Group', 
        'MedTech Solutions', 
        'LogiTrans International'
    ]
    sectors = [
        'Technology', 
        'Renewable Energy', 
        'Retail', 
        'Healthcare', 
        'Transportation'
    ]
    
    data = []
    for i, company in enumerate(companies):
        # Generate correlated metrics for more realistic data
        base_performance = np.random.uniform(0.4, 0.9)
        
        financial_data = {
            'Company': company,
            'Sector': sectors[i],
            'Market Cap (B)': np.random.uniform(10, 500) * base_performance,
            'Revenue (B)': np.random.uniform(5, 200) * base_performance,
            'P/E Ratio': np.random.uniform(10, 40),
            'Profit Margin (%)': np.random.uniform(5, 30) * base_performance,
            'Debt to Equity': np.random.uniform(0.3, 2.5) / base_performance,
            
            # ESG scores with some correlation to financial performance
            'ESG Total Score': min(100, np.random.uniform(40, 90) * base_performance * 1.1),
            'Environmental Score': min(100, np.random.uniform(30, 95) * base_performance),
            'Social Score': min(100, np.random.uniform(35, 90) * base_performance * 1.05),
            'Governance Score': min(100, np.random.uniform(40, 95) * base_performance * 1.1),
            
            # Specific ESG metrics
            'Carbon Emissions (MT)': np.random.uniform(1000, 50000) / base_performance,
            'Renewable Energy (%)': np.random.uniform(10, 80) * base_performance,
            'Employee Diversity (%)': np.random.uniform(20, 60) * base_performance,
            'Board Independence (%)': np.random.uniform(30, 90) * base_performance,
            'Safety Incidents': max(0, int(np.random.normal(10, 5) / base_performance)),
            
            # Additional metrics
            'Employee Satisfaction': np.random.uniform(60, 95) * base_performance,
            'Community Investment (M)': np.random.uniform(1, 50) * base_performance,
            'Waste Recycled (%)': np.random.uniform(20, 90) * base_performance,
            'Water Usage (M Liters)': np.random.uniform(100, 5000) / base_performance,
            'Innovation Score': np.random.uniform(40, 90) * base_performance
        }
        data.append(financial_data)
    
    return pd.DataFrame(data)


def generate_time_series(company: str, metric: str, days: int = 365) -> pd.DataFrame:
    """
    Generate time series data for a specific metric.
    
    Args:
        company: Company name
        metric: Metric to generate time series for
        days: Number of days to generate data for
        
    Returns:
        pd.DataFrame: Time series data with Date and metric columns
    """
    dates = [datetime.now() - timedelta(days=x) for x in range(days, 0, -1)]
    
    # Create realistic trends based on metric type
    if 'Score' in metric or 'ESG' in metric:
        base_value = np.random.uniform(50, 70)
        trend = np.random.uniform(0.01, 0.05)  # Positive trend for scores
    elif 'Emissions' in metric:
        base_value = np.random.uniform(30000, 50000)
        trend = np.random.uniform(-0.02, 0.01)  # Slight negative trend
    else:
        base_value = np.random.uniform(30, 80)
        trend = np.random.uniform(-0.01, 0.03)
    
    # Add seasonality and noise
    seasonal_factor = np.sin(np.linspace(0, 4*np.pi, days)) * 5
    noise = np.random.normal(0, 3, days)
    values = base_value + trend * np.arange(days) + seasonal_factor + noise
    
    # Ensure values stay within reasonable bounds
    if 'Score' in metric or '%' in metric:
        values = np.clip(values, 0, 100)
    elif 'Emissions' in metric:
        values = np.maximum(values, 1000)
    
    return pd.DataFrame({
        'Date': dates,
        metric: values
    })


def calculate_esg_score(environmental: float, social: float, governance: float) -> float:
    """
    Calculate weighted ESG score from component scores.
    
    Args:
        environmental: Environmental score (0-100)
        social: Social score (0-100)
        governance: Governance score (0-100)
        
    Returns:
        float: Weighted ESG score
    """
    weights = {'E': 0.35, 'S': 0.35, 'G': 0.30}
    return (environmental * weights['E'] + 
            social * weights['S'] + 
            governance * weights['G'])


def generate_sector_benchmarks() -> Dict[str, Dict[str, float]]:
    """
    Generate sector benchmark data for comparison.
    
    Returns:
        Dict: Sector benchmarks for various metrics
    """
    sectors = ['Technology', 'Renewable Energy', 'Retail', 'Healthcare', 'Transportation']
    benchmarks = {}
    
    for sector in sectors:
        benchmarks[sector] = {
            'ESG Average': np.random.uniform(50, 75),
            'Carbon Intensity': np.random.uniform(10, 100),
            'Diversity Average': np.random.uniform(30, 60),
            'Governance Average': np.random.uniform(60, 85),
            'Innovation Index': np.random.uniform(40, 80)
        }
    
    return benchmarks


def create_company_profiles() -> Dict[str, Dict[str, str]]:
    """
    Create detailed company profiles for additional context.
    
    Returns:
        Dict: Company profiles with descriptions and key facts
    """
    profiles = {
        'TechVenture SA': {
            'Description': 'Leading software solutions provider focused on AI and cloud computing',
            'Founded': '2010',
            'Headquarters': 'Paris, France',
            'Employees': '5,000+',
            'Key Initiative': 'Carbon-neutral data centers by 2025'
        },
        'WindPower Europe': {
            'Description': 'Renewable energy company specializing in offshore wind farms',
            'Founded': '2005',
            'Headquarters': 'Copenhagen, Denmark',
            'Employees': '3,500+',
            'Key Initiative': '10GW renewable capacity by 2030'
        },
        'RetailNext Group': {
            'Description': 'Innovative retail chain with focus on sustainable products',
            'Founded': '1995',
            'Headquarters': 'London, UK',
            'Employees': '15,000+',
            'Key Initiative': 'Zero-waste stores initiative'
        },
        'MedTech Solutions': {
            'Description': 'Medical technology company developing accessible healthcare solutions',
            'Founded': '2008',
            'Headquarters': 'Berlin, Germany',
            'Employees': '2,500+',
            'Key Initiative': 'Affordable diagnostics for developing markets'
        },
        'LogiTrans International': {
            'Description': 'Global logistics provider with green transportation focus',
            'Founded': '1985',
            'Headquarters': 'Amsterdam, Netherlands',
            'Employees': '8,000+',
            'Key Initiative': 'Electric vehicle fleet transformation'
        }
    }
    
    return profiles