import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

CYBER_LAYOUT = dict(
    paper_bgcolor='rgba(10, 15, 36, 0.5)',
    plot_bgcolor='rgba(4, 6, 18, 0.65)',
    font=dict(color='#E2E8F0', family='Poppins, sans-serif'),
    margin=dict(l=50, r=50, t=75, b=60),
    xaxis=dict(gridcolor='rgba(0, 240, 255, 0.1)', zerolinecolor='rgba(0, 240, 255, 0.2)'),
    yaxis=dict(gridcolor='rgba(0, 240, 255, 0.1)', zerolinecolor='rgba(0, 240, 255, 0.2)'),
)

@st.cache_data
def create_line_chart():
    hours = [f"{i:02d}:00" for i in range(24)]
    legit_tps = [4200, 3800, 3100, 2800, 3500, 5200, 7800, 9400, 11200, 12500, 13100, 12800,
                 12100, 11800, 12400, 13500, 14200, 13800, 11500, 9800, 8400, 7200, 5800, 4900]
    fraud_alerts = [12, 8, 5, 4, 9, 14, 22, 35, 48, 52, 41, 38,
                    35, 42, 58, 64, 71, 55, 39, 28, 21, 18, 15, 11]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=hours, y=legit_tps, name='Legitimate TPS',
        line=dict(color='#00F0FF', width=3, shape='spline'),
        fill='tozeroy', fillcolor='rgba(0, 240, 255, 0.08)'
    ))
    fig.add_trace(go.Scatter(
        x=hours, y=fraud_alerts, name='Fraud Threats Blocked', yaxis='y2',
        line=dict(color='#EF4444', width=3, dash='dot'),
    ))

    layout = CYBER_LAYOUT.copy()
    layout.update(
        title=dict(text='⚡ 24-HOUR TRANSACTION VELOCITY & FRAUD BLOCK RATE', font=dict(size=14, color='#FFFFFF'), y=0.96),
        yaxis=dict(title='Legitimate Transactions / sec', gridcolor='rgba(0, 240, 255, 0.1)'),
        yaxis2=dict(title=dict(text='Blocked Threats', font=dict(color='#EF4444')), overlaying='y', side='right', showgrid=False),
        legend=dict(orientation='h', y=-0.22, x=0.15)
    )
    fig.update_layout(layout)
    return fig

@st.cache_data
def create_donut_chart():
    labels = ['Legitimate Txns', 'Blocked Frauds', 'Under Review']
    values = [284315, 492, 118]
    colors = ['#00F0FF', '#EF4444', '#F59E0B']

    fig = go.Figure(data=[go.Pie(
        labels=labels, values=values, hole=0.65,
        marker=dict(colors=colors, line=dict(color='#040612', width=2.5)),
        textinfo='percent',
        textfont=dict(color='#FFFFFF', size=12, family='Space Grotesk'),
        hoverinfo='label+value+percent'
    )])

    layout = CYBER_LAYOUT.copy()
    layout.update(
        title=dict(text='📊 TRANSACTION STATUS RATIO', font=dict(size=14, color='#FFFFFF'), y=0.96),
        showlegend=True,
        legend=dict(orientation='h', y=-0.2, x=0.0),
        annotations=[dict(text='284.8K<br><span style="font-size:10px">TOTAL</span>', x=0.5, y=0.5, font_size=15, font_color='#FFFFFF', showarrow=False)]
    )
    fig.update_layout(layout)
    return fig

@st.cache_data
def create_radar_chart():
    categories = ['V14 (Identity)', 'V10 (Device)', 'V12 (Geo Dist)', 'V4 (Velocity)', 'Amount Anomaly', 'V17 (Pattern)']
    fig = go.Figure()

    # Normal profile
    fig.add_trace(go.Scatterpolar(
        r=[0.2, 0.1, 0.15, 0.25, 0.1, 0.08], theta=categories, fill='toself',
        name='Normal Baseline', line=dict(color='#10B981', width=2), fillcolor='rgba(16, 185, 129, 0.15)'
    ))
    # Fraud threat vector profile
    fig.add_trace(go.Scatterpolar(
        r=[0.95, 0.88, 0.92, 0.78, 0.85, 0.90], theta=categories, fill='toself',
        name='High-Risk Fraud Vector', line=dict(color='#EF4444', width=2), fillcolor='rgba(239, 68, 68, 0.2)'
    ))

    layout = CYBER_LAYOUT.copy()
    layout.update(
        title=dict(text='🎯 THREAT VECTOR RADAR ANALYSIS', font=dict(size=14, color='#FFFFFF'), y=0.96),
        polar=dict(
            bgcolor='rgba(4, 6, 18, 0.65)',
            radialaxis=dict(visible=True, range=[0, 1], gridcolor='rgba(0, 240, 255, 0.15)', color='#94A3B8'),
            angularaxis=dict(gridcolor='rgba(0, 240, 255, 0.15)', color='#FFFFFF')
        ),
        legend=dict(orientation='h', y=-0.2, x=0.1)
    )
    fig.update_layout(layout)
    return fig

@st.cache_data
def create_bar_chart():
    countries = ['USA', 'India', 'Dubai', 'UK', 'Singapore', 'Germany', 'Japan']
    frauds = [189, 124, 39, 42, 38, 29, 31]

    fig = go.Figure(data=[go.Bar(
        x=countries, y=frauds,
        marker=dict(color=frauds, colorscale=[[0, '#00F0FF'], [1, '#8B5CF6']], line=dict(color='#00F0FF', width=1)),
        text=frauds, textposition='auto', textfont=dict(color='#FFFFFF', size=12)
    )])

    layout = CYBER_LAYOUT.copy()
    layout.update(
        title=dict(text='🌐 FRAUD INCIDENTS BY GEOGRAPHY', font=dict(size=14, color='#FFFFFF'), y=0.96),
        xaxis=dict(title='Region'),
        yaxis=dict(title='Detected Frauds')
    )
    fig.update_layout(layout)
    return fig

def create_gauge_chart(score_percent=12.5):
    color_val = "#22C55E" if score_percent < 30 else ("#F59E0B" if score_percent < 70 else "#EF4444")
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score_percent,
        number={'suffix': "%", 'font': {'color': color_val, 'size': 36}},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#00D4FF"},
            'bar': {'color': color_val, 'thickness': 0.3},
            'bgcolor': "rgba(5, 8, 22, 0.8)",
            'bordercolor': "rgba(0, 212, 255, 0.3)",
            'steps': [
                {'range': [0, 30], 'color': "rgba(34, 197, 94, 0.15)"},
                {'range': [30, 70], 'color': "rgba(245, 158, 11, 0.15)"},
                {'range': [70, 100], 'color': "rgba(239, 68, 68, 0.2)"}
            ],
        }
    ))
    
    layout = CYBER_LAYOUT.copy()
    layout.update(
        title=dict(text='🛡️ REAL-TIME AI RISK SCORE GAUGE', font=dict(size=14, color='#FFFFFF')),
        height=260
    )
    fig.update_layout(layout)
    return fig

@st.cache_data
def create_confusion_matrix_chart():
    from utils.model_loader import get_model_validation_metrics
    metrics = get_model_validation_metrics()
    cm = metrics["confusion_matrix"]
    tn, fp, fn, tp = metrics["tn"], metrics["fp"], metrics["fn"], metrics["tp"]
    
    z = [[tn, fp], [fn, tp]]
    x = ['Pred Legitimate', 'Pred Fraud']
    y = ['Actual Legitimate', 'Actual Fraud']
    
    annot_text = [
        [f"TN: {tn:,}<br><span style='font-size:10px'>Legit Correct</span>", f"FP: {fp:,}<br><span style='font-size:10px'>False Alarm</span>"],
        [f"FN: {fn:,}<br><span style='font-size:10px'>Missed Fraud</span>", f"TP: {tp:,}<br><span style='font-size:10px'>Fraud Blocked</span>"]
    ]
    
    fig = go.Figure(data=go.Heatmap(
        z=z, x=x, y=y,
        colorscale=[[0, '#040612'], [0.5, '#8B5CF6'], [1, '#00F0FF']],
        text=annot_text, texttemplate="%{text}", textfont={"size": 13, "color": "#FFFFFF"},
        showscale=False
    ))
    
    layout = CYBER_LAYOUT.copy()
    layout.update(
        title=dict(text=f'🎯 CONFUSION MATRIX (Test Holdout: {metrics["test_samples"]:,} Samples)', font=dict(size=14, color='#FFFFFF'), y=0.96),
        height=350
    )
    fig.update_layout(layout)
    return fig

@st.cache_data
def create_roc_curve_chart():
    from utils.model_loader import get_model_validation_metrics
    metrics = get_model_validation_metrics()
    fpr = metrics["roc_fpr"]
    tpr = metrics["roc_tpr"]
    auc_score = metrics["test_auc"]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=fpr, y=tpr, name=f'XGBoost (AUC = {auc_score:.4f})',
        line=dict(color='#00F0FF', width=3),
        fill='tozeroy', fillcolor='rgba(0, 240, 255, 0.1)'
    ))
    fig.add_trace(go.Scatter(
        x=[0, 1], y=[0, 1], name='Random Baseline (AUC = 0.50)',
        line=dict(color='#94A3B8', width=1.5, dash='dash')
    ))
    
    layout = CYBER_LAYOUT.copy()
    layout.update(
        title=dict(text=f'📈 ROC-AUC CURVE (AUC = {auc_score:.4f})', font=dict(size=14, color='#FFFFFF'), y=0.96),
        xaxis=dict(title='False Positive Rate (1 - Specificity)'),
        yaxis=dict(title='True Positive Rate (Recall)'),
        legend=dict(orientation='h', y=-0.22, x=0.05)
    )
    fig.update_layout(layout)
    return fig

@st.cache_data
def create_pr_curve_chart():
    from utils.model_loader import get_model_validation_metrics
    metrics = get_model_validation_metrics()
    precision = metrics["pr_precision"]
    recall = metrics["pr_recall"]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=recall, y=precision, name='Precision-Recall Curve',
        line=dict(color='#8B5CF6', width=3),
        fill='tozeroy', fillcolor='rgba(139, 92, 246, 0.1)'
    ))
    
    layout = CYBER_LAYOUT.copy()
    layout.update(
        title=dict(text='📊 PRECISION-RECALL CURVE (Imbalanced Target)', font=dict(size=14, color='#FFFFFF'), y=0.96),
        xaxis=dict(title='Recall (Catch Rate)'),
        yaxis=dict(title='Precision (Confidence)'),
        legend=dict(orientation='h', y=-0.22, x=0.15)
    )
    fig.update_layout(layout)
    return fig

@st.cache_data
def create_feature_importance_chart(top_n=10):
    from utils.model_loader import get_real_feature_importances
    df_imp = get_real_feature_importances().head(top_n)
    
    fig = go.Figure(go.Bar(
        x=df_imp['Importance'], y=df_imp['Feature'], orientation='h',
        marker=dict(color=df_imp['Importance'], colorscale=[[0, '#00F0FF'], [1, '#8B5CF6']], line=dict(color='#00F0FF', width=1)),
        text=[f"{v*100:.2f}%" for v in df_imp['Importance']], textposition='outside', textfont=dict(color='#FFFFFF', size=11)
    ))
    
    layout = CYBER_LAYOUT.copy()
    layout.update(
        title=dict(text=f'🧠 TOP {top_n} FEATURE IMPORTANCES (XGBoost Gini)', font=dict(size=14, color='#FFFFFF'), y=0.96),
        yaxis=dict(autorange="reversed"),
        xaxis=dict(title='Relative Importance Weight')
    )
    fig.update_layout(layout)
    return fig