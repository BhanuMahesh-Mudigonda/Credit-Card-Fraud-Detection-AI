import numpy as np
import pandas as pd
import streamlit as st

@st.cache_data
def get_sample_dataset():
    # Generate representative dataset summary for fast interactive analytics
    np.random.seed(42)
    n_samples = 1000
    
    # 99.8% Legitimate, 0.2% Fraud
    is_fraud = np.random.choice([0, 1], size=n_samples, p=[0.995, 0.005])
    
    amounts = np.where(is_fraud == 1, 
                       np.random.exponential(scale=450, size=n_samples) + 100, 
                       np.random.exponential(scale=85, size=n_samples) + 5)
    
    times = np.random.uniform(0, 172800, size=n_samples)
    
    data = {'Time': times, 'Amount': amounts, 'Class': is_fraud}
    
    for i in range(1, 29):
        if i in [14, 10, 12, 4]: # Key discriminatory features
            data[f'V{i}'] = np.where(is_fraud == 1, 
                                     np.random.normal(-4.5, 2.0, size=n_samples), 
                                     np.random.normal(0.1, 0.9, size=n_samples))
        else:
            data[f'V{i}'] = np.random.normal(0.0, 1.0, size=n_samples)
            
    df = pd.DataFrame(data)
    return df

def get_country_fraud_stats():
    return [
        {"country": "India", "code": "IN", "flag": "🇮🇳", "total": "1,420,500", "fraud": 124, "status": "SECURE", "volume": "₹4.8B"},
        {"country": "USA", "code": "US", "flag": "🇺🇸", "total": "2,150,000", "fraud": 189, "status": "ELEVATED", "volume": "$12.4B"},
        {"country": "UK", "code": "GB", "flag": "🇬🇧", "total": "890,200", "fraud": 42, "status": "SECURE", "volume": "£3.2B"},
        {"country": "Singapore", "code": "SG", "flag": "🇸🇬", "total": "640,000", "fraud": 38, "status": "MONITORED", "volume": "$2.1B"},
        {"country": "Germany", "code": "DE", "flag": "🇩🇪", "total": "780,400", "fraud": 29, "status": "SECURE", "volume": "€4.5B"},
        {"country": "Japan", "code": "JP", "flag": "🇯🇵", "total": "920,100", "fraud": 31, "status": "SECURE", "volume": "¥520B"},
        {"country": "Dubai", "code": "AE", "flag": "🇦🇪", "total": "510,800", "fraud": 39, "status": "ALERT", "volume": "$4.9B"},
    ]
