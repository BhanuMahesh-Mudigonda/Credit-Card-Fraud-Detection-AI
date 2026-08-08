import streamlit as st
from utils.theme import safe_html

METRICS_DATA = [
    {"title": "Transactions", "val": "284,807", "delta": "+18.4%", "icon": "💳", "type": "positive", "spark": "M0,25 Q15,10 30,20 T60,5 T90,15 T120,0"},
    {"title": "Fraud Cases", "val": "492", "delta": "-4.2%", "icon": "🚨", "type": "negative", "spark": "M0,5 Q15,20 30,10 T60,25 T90,10 T120,25"},
    {"title": "Accuracy", "val": "99.95%", "delta": "+0.3%", "icon": "🎯", "type": "positive", "spark": "M0,20 Q15,5 30,15 T60,0 T90,10 T120,0"},
    {"title": "Recall", "val": "89.20%", "delta": "+1.5%", "icon": "🔍", "type": "positive", "spark": "M0,25 Q15,15 30,5 T60,15 T90,5 T120,0"},
    {"title": "Precision", "val": "98.40%", "delta": "+0.8%", "icon": "⚡", "type": "positive", "spark": "M0,20 Q15,10 30,0 T60,10 T90,5 T120,0"},
    {"title": "Latency", "val": "1.20 ms", "delta": "-0.4ms", "icon": "⏱️", "type": "neutral", "spark": "M0,10 Q15,10 30,10 T60,10 T90,10 T120,10"},
    {"title": "Risk Score", "val": "2.4 %", "delta": "LOW", "icon": "🛡️", "type": "positive", "spark": "M0,25 Q15,20 30,15 T60,10 T90,5 T120,0"},
]

from utils.dataset_loader import get_dataset_summary
from utils.model_loader import get_model_validation_metrics

def render_metric_cards():
    d_stats = get_dataset_summary()
    m_stats = get_model_validation_metrics()
    
    metrics = [
        {"title": "Total Records", "val": f"{d_stats['total_rows']:,}", "delta": "Verified Dataset", "icon": "💳", "type": "positive", "spark": "M0,25 Q15,10 30,20 T60,5 T90,15 T120,0"},
        {"title": "Fraud Cases", "val": f"{d_stats['fraud_count']:,}", "delta": f"{d_stats['fraud_pct']}% Imbalance", "icon": "🚨", "type": "negative", "spark": "M0,5 Q15,20 30,10 T60,25 T90,10 T120,25"},
        {"title": "Test Accuracy", "val": f"{m_stats['test_accuracy']:.2f}%", "delta": "Holdout Test", "icon": "🎯", "type": "positive", "spark": "M0,20 Q15,5 30,15 T60,0 T90,10 T120,0"},
        {"title": "Test Recall", "val": f"{m_stats['test_recall']:.2f}%", "delta": f"TP: {m_stats['tp']} / FN: {m_stats['fn']}", "icon": "🔍", "type": "positive", "spark": "M0,25 Q15,15 30,5 T60,15 T90,5 T120,0"},
        {"title": "Test Precision", "val": f"{m_stats['test_precision']:.2f}%", "delta": f"FP: {m_stats['fp']}", "icon": "⚡", "type": "positive", "spark": "M0,20 Q15,10 30,0 T60,10 T90,5 T120,0"},
        {"title": "ROC-AUC Score", "val": f"{m_stats['test_auc']:.4f}", "delta": "State-of-Art", "icon": "📈", "type": "positive", "spark": "M0,10 Q15,10 30,10 T60,10 T90,10 T120,10"},
        {"title": "Avg Txn Amount", "val": f"${d_stats['avg_amount']:.2f}", "delta": f"Max: ${d_stats['max_amount']:,.0f}", "icon": "🛡️", "type": "neutral", "spark": "M0,25 Q15,20 30,15 T60,10 T90,5 T120,0"},
    ]
    
    cards_inner = ""
    for m in metrics:
        delta_class = f"delta-{m['type']}"
        stroke_color = "#10B981" if m['type'] == "positive" else ("#EF4444" if m['type'] == "negative" else "#FFD700")
        cards_inner += f"""
        <div class="aegis-metric-card">
            <div class="metric-card-header">
                <span class="metric-title">{m['title']}</span>
                <span class="metric-icon">{m['icon']}</span>
            </div>
            <div class="metric-value">{m['val']}</div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 6px;">
                <div class="metric-delta {delta_class}">
                    <span>{m['delta']}</span>
                </div>
                <svg width="60" height="20" viewBox="0 0 120 30" style="overflow: visible;">
                    <path d="{m['spark']}" fill="none" stroke="{stroke_color}" stroke-width="3" stroke-linecap="round"/>
                </svg>
            </div>
        </div>
        """

    safe_html(f'<div class="aegis-card-grid">{cards_inner}</div>')