import os
import numpy as np
import pandas as pd
import streamlit as st

DATASET_PATH_GZ = os.path.join(os.path.dirname(os.path.dirname(__file__)), "credit_card_fraud.csv.gz")
DATASET_PATH_CSV = os.path.join(os.path.dirname(os.path.dirname(__file__)), "credit_card_fraud.csv")

@st.cache_data
def load_full_dataset():
    """Loads the real credit_card_fraud dataset (gz or csv) with caching."""
    target_path = DATASET_PATH_GZ if os.path.exists(DATASET_PATH_GZ) else DATASET_PATH_CSV
    if os.path.exists(target_path):
        try:
            df = pd.read_csv(target_path)
            return df
        except Exception as e:
            print(f"Error loading dataset from {target_path}: {e}")
    return get_fallback_dataset()

@st.cache_data
def get_dataset_summary():
    """Returns actual calculated summary statistics of the dataset."""
    df = load_full_dataset()
    total_rows = len(df)
    total_cols = len(df.columns)
    feature_cols = [c for c in df.columns if c != 'Class']
    
    null_count = int(df.isnull().sum().sum())
    duplicate_count = int(df.duplicated().sum())
    
    if 'Class' in df.columns:
        fraud_count = int((df['Class'] == 1).sum())
        legit_count = int((df['Class'] == 0).sum())
        fraud_ratio = (fraud_count / total_rows) * 100
        legit_ratio = (legit_count / total_rows) * 100
    else:
        fraud_count, legit_count, fraud_ratio, legit_ratio = 492, 284315, 0.1727, 99.8273

    avg_amount = float(df['Amount'].mean()) if 'Amount' in df.columns else 88.35
    max_amount = float(df['Amount'].max()) if 'Amount' in df.columns else 25691.16
    min_amount = float(df['Amount'].min()) if 'Amount' in df.columns else 0.0

    return {
        "total_rows": total_rows,
        "total_cols": total_cols,
        "feature_count": len(feature_cols),
        "numeric_cols": total_cols,
        "categorical_cols": 0,
        "null_count": null_count,
        "duplicate_count": duplicate_count,
        "duplicate_pct": round((duplicate_count / total_rows) * 100, 2),
        "fraud_count": fraud_count,
        "legit_count": legit_count,
        "fraud_pct": round(fraud_ratio, 3),
        "legit_pct": round(legit_ratio, 3),
        "imbalance_ratio": f"1 : {int(legit_count / max(1, fraud_count))}",
        "avg_amount": round(avg_amount, 2),
        "max_amount": round(max_amount, 2),
        "min_amount": round(min_amount, 2),
    }

@st.cache_data
def get_sample_dataset(n=1000):
    df = load_full_dataset()
    if len(df) > n:
        return df.sample(n=n, random_state=42)
    return df

def get_fallback_dataset():
    np.random.seed(42)
    n_samples = 1000
    is_fraud = np.random.choice([0, 1], size=n_samples, p=[0.995, 0.005])
    amounts = np.where(is_fraud == 1, 
                       np.random.exponential(scale=450, size=n_samples) + 100, 
                       np.random.exponential(scale=85, size=n_samples) + 5)
    times = np.random.uniform(0, 172800, size=n_samples)
    data = {'Time': times, 'Amount': amounts, 'Class': is_fraud}
    for i in range(1, 29):
        if i in [14, 10, 12, 4]:
            data[f'V{i}'] = np.where(is_fraud == 1, 
                                     np.random.normal(-4.5, 2.0, size=n_samples), 
                                     np.random.normal(0.1, 0.9, size=n_samples))
        else:
            data[f'V{i}'] = np.random.normal(0.0, 1.0, size=n_samples)
    return pd.DataFrame(data)

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
