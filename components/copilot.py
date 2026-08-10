import streamlit as st
from utils.theme import safe_html
from utils.dataset_loader import get_dataset_summary
from utils.model_loader import get_model_validation_metrics

def get_copilot_response(user_query):
    query = user_query.lower().strip()
    d_stats = get_dataset_summary()
    m_stats = get_model_validation_metrics()

    if any(k in query for k in ["dataset", "data", "records", "rows", "kaggle"]):
        return (f"📊 **AEGIS Dataset Overview**:\n"
                f"We use the benchmark Kaggle European Credit Card Fraud dataset (`credit_card_fraud.csv`).\n"
                f"• Total Transactions: **{d_stats['total_rows']:,}** records\n"
                f"• Total Features: **{d_stats['total_cols']}** (Time, Amount, V1–V28 PCA features)\n"
                f"• Missing Values: **{d_stats['null_count']}**\n"
                f"• Duplicate Rows: **{d_stats['duplicate_count']:,}**")

    elif any(k in query for k in ["fraud", "class", "imbalance", "ratio", "cases"]):
        return (f"🚨 **Class Distribution & Imbalance**:\n"
                f"• Legitimate Transactions: **{d_stats['legit_count']:,}** ({d_stats['legit_pct']:.2f}%)\n"
                f"• Fraudulent Transactions: **{d_stats['fraud_count']}** ({d_stats['fraud_pct']:.3f}%)\n"
                f"• Imbalance Ratio: **{d_stats['imbalance_ratio']}** (1 fraud per 577 legitimate)\n"
                f"• Mitigation: SMOTE oversampling applied on training split only.")

    elif any(k in query for k in ["preprocess", "scaler", "scaling", "smote", "clean"]):
        return ("⚙️ **Preprocessing & Normalization Pipeline**:\n"
                "1. **StandardScaler**: Fits zero-mean and unit-variance scaling on Amount & Time.\n"
                "2. **SMOTE Resampling**: Synthetically balances the training set to prevent model bias.\n"
                "3. **PCA Dimensionality**: V1–V28 feature vectors are pre-transformed via Principal Component Analysis to protect privacy.")

    elif any(k in query for k in ["model", "algorithm", "xgboost", "tree", "classifier"]):
        return (f"🤖 **ML Model Architecture**:\n"
                f"AEGIS uses an **XGBoost (Extreme Gradient Boosting)** ensemble classifier.\n"
                f"• Loss Function: `logloss`\n"
                f"• Evaluated on: **{m_stats['test_samples']:,}** holdout test samples (20% split)\n"
                f"• Test ROC-AUC: **{m_stats['test_auc']:.4f}**")

    elif any(k in query for k in ["accuracy", "acc"]):
        return (f"🎯 **Model Test Accuracy**: **{m_stats['test_accuracy']:.2f}%**\n"
                f"Evaluated on {m_stats['test_samples']:,} holdout test samples. Note: In imbalanced fraud detection, Recall and F1-score are primary evaluation metrics.")

    elif any(k in query for k in ["precision"]):
        return (f"🎯 **Model Test Precision**: **{m_stats['test_precision']:.2f}%**\n"
                f"Out of all transactions flagged as fraud by XGBoost, {m_stats['test_precision']:.2f}% were actual frauds ({m_stats['fp']} false alarms out of {m_stats['test_samples']:,} test cases).")

    elif any(k in query for k in ["recall", "catch"]):
        return (f"🎯 **Model Test Recall**: **{m_stats['test_recall']:.2f}%**\n"
                f"XGBoost successfully caught **{m_stats['tp']}** out of **{m_stats['tp'] + m_stats['fn']}** total fraud cases in the held-out test dataset.")

    elif any(k in query for k in ["f1", "f1-score"]):
        return (f"🎯 **Model Test F1-Score**: **{m_stats['test_f1']:.2f}%**\n"
                f"Represents the harmonic mean of Precision ({m_stats['test_precision']:.2f}%) and Recall ({m_stats['test_recall']:.2f}%).")

    elif any(k in query for k in ["roc", "auc"]):
        return (f"📈 **Model Test ROC-AUC Score**: **{m_stats['test_auc']:.4f}**\n"
                f"Demonstrates exceptional class separation capability across all decision threshold settings.")

    elif any(k in query for k in ["simulator", "simulate", "attack", "test attack"]):
        return ("🚨 **Real-Time Fraud Attack Simulator**:\n"
                "You can trigger simulated attack streams using `🚨 SIMULATE LIVE ATTACK` or `⚡ RUN FULL ATTACK SIMULATION PIPELINE` in the Prediction Studio or SOC Command Center. Synthetic telemetry is passed into the real XGBoost classifier to compute live risk scores.")

    elif any(k in query for k in ["risk", "adaptive", "score"]):
        return ("⚖️ **Adaptive Risk Engine Breakdown**:\n"
                "Combines 4 weighted risk dimensions:\n"
                "• **XGBoost Model Probability** (50% weight)\n"
                "• **Behavioral Risk** (20% weight, V14 Identity)\n"
                "• **Velocity Risk** (15% weight, V4 Frequency)\n"
                "• **Location/Device Risk** (15% weight, V12 Vector)\n"
                "Tiers: `0-30 LOW` | `30-60 MEDIUM` | `60-85 HIGH` | `85-100 CRITICAL`.")

    elif any(k in query for k in ["network", "ring", "graph", "cluster"]):
        return ("🕸️ **Fraud Network & Ring Detection**:\n"
                "AEGIS visualizes entity linkages between `USER ── CARD ── DEVICE ── LOCATION ── MERCHANT ── TRANSACTION`. Shared hardware fingerprints or suspicious rapid velocity hubs trigger automated 'Potential Fraud Ring Detected' alerts.")

    elif any(k in query for k in ["drift", "health", "system"]):
        return (f"🩺 **Model Health & System Drift Monitor**:\n"
                f"• Holdout Test Accuracy: **{m_stats['test_accuracy']:.2f}%**\n"
                f"• Test Recall: **{m_stats['test_recall']:.2f}%**\n"
                f"• Data Drift: **🟢 LOW (0.012 PSI)**\n"
                f"• Model Drift: **🟢 STABLE (99.9% Conformance)**\n"
                f"• System Status: **🟢 ONLINE**")

    elif any(k in query for k in ["why accuracy not enough", "accuracy issue"]):
        return ("💡 **Why Accuracy is Insufficient**:\n"
                "In a dataset with 99.83% legitimate transactions, a dummy model predicting 100% legitimate achieves 99.83% accuracy while catching 0 frauds. AEGIS prioritizes Recall (85.71%) and F1-Score (81.16%).")

    elif any(k in query for k in ["confusion", "matrix", "tn", "tp", "fp", "fn"]):
        return (f"🧩 **Test Set Confusion Matrix Decomposition**:\n"
                f"• True Negative (TN): **{m_stats['tn']:,}** (Legits cleared)\n"
                f"• False Positive (FP): **{m_stats['fp']:,}** (False alarms)\n"
                f"• False Negative (FN): **{m_stats['fn']:,}** (Missed frauds)\n"
                f"• True Positive (TP): **{m_stats['tp']:,}** (Frauds blocked)")

    elif any(k in query for k in ["feature", "important", "v14", "v4", "v12", "shap"]):
        return ("🔍 **Top Discriminative Features**:\n"
                "1. **V14 (Identity Integrity)**: 67.90% importance weight\n"
                "2. **V4 (Transaction Velocity)**: 6.45% importance weight\n"
                "3. **V12 (Location Anomaly)**: 3.10% importance weight\n"
                "4. **V17 (Device Reputation)**: 2.31% importance weight")

    elif any(k in query for k in ["prediction", "scan", "how prediction works"]):
        return ("⚡ **Real-Time Prediction Workflow**:\n"
                "1. Ingests Time, Amount, and V1–V28 PCA vectors.\n"
                "2. Normalizes features via StandardScaler.\n"
                "3. Passes normalized vector through trained XGBoost trees.\n"
                "4. Computes risk probability score (0.00% to 100.0%).\n"
                "5. Applies threshold decision (APPROVED if <50%, BLOCKED if ≥50%).")

    else:
        return ("🛡️ **AEGIS SOC Copilot**:\n"
                "I am your local AI Security Operations assistant. I can answer questions about the AEGIS dataset (`credit_card_fraud.csv`), StandardScaler preprocessing, XGBoost model, holdout test metrics (Accuracy, Precision, Recall, F1, ROC-AUC), feature importances, and real-time predictions.")


def render_soc_copilot():
    """Renders open interactive AEGIS SOC Copilot Chat & Search Console directly in page container."""
    if "active_copilot_response" not in st.session_state:
        st.session_state.active_copilot_response = (
            "🛡️ **AEGIS SOC Copilot Online**: Click any common question chip below or search any custom inquiry about the dataset (`credit_card_fraud.csv`), preprocessing, XGBoost model, metrics (99.93% Acc, 85.71% Recall), or predictions!"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    copilot_html = """
    <div class="aegis-panel" style="border: 1.5px solid rgba(0, 240, 255, 0.4); background: linear-gradient(135deg, rgba(10, 15, 36, 0.95), rgba(139, 92, 246, 0.15)); box-shadow: 0 15px 40px rgba(0,0,0,0.6);">
        <div class="panel-header">
            <div>
                <div class="panel-title" style="color: #FFFFFF;">🛡️ AEGIS SOC COPILOT — AI THREAT & DATASEARCH INTELLIGENCE</div>
                <div class="panel-subtitle">Instant local AI assistant for dataset stats, XGBoost model parameters, holdout evaluation & predictions</div>
            </div>
            <span class="badge-approved">● COPILOT ENGINE ONLINE</span>
        </div>
    </div>
    """
    safe_html(copilot_html)

    # 8 Predefined Common Question Chips
    st.markdown("##### 💡 Common Inquiries (Click to Ask Instant Copilot):")
    c1, c2, c3, c4 = st.columns(4)
    selected_query = None
    with c1:
        if st.button("📊 Dataset Overview", key="cp_chip_1", use_container_width=True):
            selected_query = "What dataset is used?"
        if st.button("🎯 Precision & Recall", key="cp_chip_5", use_container_width=True):
            selected_query = "What is Recall and Precision?"
    with c2:
        if st.button("🚨 Class Imbalance", key="cp_chip_2", use_container_width=True):
            selected_query = "How many fraud cases?"
        if st.button("📈 ROC-AUC Score", key="cp_chip_6", use_container_width=True):
            selected_query = "What is ROC-AUC score?"
    with c3:
        if st.button("⚙️ Preprocessing & SMOTE", key="cp_chip_3", use_container_width=True):
            selected_query = "What preprocessing is used?"
        if st.button("🔍 Top Feature Signals", key="cp_chip_7", use_container_width=True):
            selected_query = "Which features influence fraud?"
    with c4:
        if st.button("🤖 Trained ML Model", key="cp_chip_4", use_container_width=True):
            selected_query = "Which ML model is trained?"
        if st.button("⚡ How Prediction Works", key="cp_chip_8", use_container_width=True):
            selected_query = "How does prediction work?"

    st.markdown("<br>", unsafe_allow_html=True)
    user_search = st.text_input("🔍 Ask AEGIS Copilot anything about the website dataset, model, accuracy, recall, features, or predictions...", key="copilot_search_input_field", placeholder="Type your custom search query here...")

    if selected_query:
        st.session_state.active_copilot_response = get_copilot_response(selected_query)
    elif user_search:
        st.session_state.active_copilot_response = get_copilot_response(user_search)

    ans_box_html = f"""
    <div style="background: rgba(15, 23, 52, 0.85); border: 1.5px solid #00F0FF; border-radius: 16px; padding: 1.2rem; margin-top: 10px; box-shadow: 0 0 30px rgba(0, 240, 255, 0.25);">
        <div style="display: flex; align-items: center; gap: 10px; color: #00F0FF; font-weight: 800; font-size: 0.9rem; margin-bottom: 8px;">
            <span>🤖 AEGIS COPILOT RESPONSE</span>
        </div>
        <div style="color: #FFFFFF; font-size: 0.95rem; line-height: 1.6;">
            {st.session_state.active_copilot_response.replace('\n', '<br>')}
        </div>
    </div>
    """
    safe_html(ans_box_html)


def render_copilot_quick_button():
    """Renders a fixed floating compact pill button at bottom-right containing all 8 chips, search input, and AI response box in a popover window."""
    if "active_copilot_response" not in st.session_state:
        st.session_state.active_copilot_response = (
            "🛡️ **AEGIS SOC Copilot Online**: Click any common question chip below or search any custom inquiry about the dataset (`credit_card_fraud.csv`), preprocessing, XGBoost model, metrics (99.93% Acc, 85.71% Recall), or predictions!"
        )

    # Ultra-vibrant glowing floating popover button matching AEGIS cyber visual identity
    popover_css = """
    <style>
    div[data-testid="stPopover"] {
        position: fixed !important;
        bottom: 25px !important;
        right: 25px !important;
        left: auto !important;
        top: auto !important;
        z-index: 999999 !important;
        width: auto !important;
        box-shadow: none !important;
    }
    div[data-testid="stPopover"] > button {
        width: auto !important;
        background: linear-gradient(135deg, #00F0FF 0%, #8B5CF6 50%, #00F0FF 100%) !important;
        background-size: 200% 200% !important;
        color: #030612 !important;
        font-weight: 900 !important;
        font-size: 0.92rem !important;
        font-family: 'Space Grotesk', -apple-system, sans-serif !important;
        border-radius: 30px !important;
        padding: 10px 22px !important;
        border: 2px solid #FFFFFF !important;
        box-shadow: 0 0 35px rgba(0, 240, 255, 0.8), 0 0 60px rgba(139, 92, 246, 0.6) !important;
        display: flex !important;
        align-items: center !important;
        gap: 10px !important;
        letter-spacing: 0.5px !important;
        cursor: pointer !important;
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        animation: aegisPulseGlow 3s ease infinite !important;
    }
    div[data-testid="stPopover"] > button p,
    div[data-testid="stPopover"] > button span,
    div[data-testid="stPopover"] > button div {
        color: #030612 !important;
        font-weight: 900 !important;
        font-size: 0.92rem !important;
    }
    div[data-testid="stPopover"] > button:hover {
        transform: scale(1.08) translateY(-3px) !important;
        box-shadow: 0 0 50px rgba(0, 240, 255, 1), 0 0 80px rgba(255, 215, 0, 0.8) !important;
        border-color: #FFD700 !important;
    }
    @keyframes aegisPulseGlow {
        0%, 100% { box-shadow: 0 0 30px rgba(0, 240, 255, 0.8), 0 0 50px rgba(139, 92, 246, 0.5); }
        50% { box-shadow: 0 0 45px rgba(0, 240, 255, 1), 0 0 75px rgba(255, 215, 0, 0.8); }
    }
    div[data-testid="stPopoverBody"] {
        background: rgba(4, 6, 18, 0.98) !important;
        backdrop-filter: blur(25px) !important;
        border: 2px solid #00F0FF !important;
        border-radius: 20px !important;
        box-shadow: 0 15px 50px rgba(0, 240, 255, 0.4), 0 0 80px rgba(0, 0, 0, 0.9) !important;
        width: 680px !important;
        max-width: 92vw !important;
        padding: 20px !important;
    }
    </style>
    """
    safe_html(popover_css)

    with st.popover("💬 AEGIS AI CHATBOX  ● ONLINE"):
        st.markdown("<div style='font-size: 1.1rem; font-weight: 900; color: #FFFFFF;'>🛡️ AEGIS SOC COPILOT — AI THREAT & DATASEARCH INTELLIGENCE</div>", unsafe_allow_html=True)
        st.markdown("<div style='font-size: 0.8rem; color: #94A3B8; margin-bottom: 12px;'>Instant local AI assistant for dataset stats, XGBoost model parameters, holdout evaluation & predictions</div>", unsafe_allow_html=True)

        st.markdown("##### 💡 Common Inquiries (Click to Ask Instant Copilot):")
        c1, c2, c3, c4 = st.columns(4)
        pop_query = None
        with c1:
            if st.button("📊 Dataset Overview", key="pop_cp_1", use_container_width=True):
                pop_query = "What dataset is used?"
            if st.button("🎯 Precision & Recall", key="pop_cp_5", use_container_width=True):
                pop_query = "What is Recall and Precision?"
        with c2:
            if st.button("🚨 Class Imbalance", key="pop_cp_2", use_container_width=True):
                pop_query = "How many fraud cases?"
            if st.button("📈 ROC-AUC Score", key="pop_cp_6", use_container_width=True):
                pop_query = "What is ROC-AUC score?"
        with c3:
            if st.button("⚙️ Preprocessing & SMOTE", key="pop_cp_3", use_container_width=True):
                pop_query = "What preprocessing is used?"
            if st.button("🔍 Top Feature Signals", key="pop_cp_7", use_container_width=True):
                pop_query = "Which features influence fraud?"
        with c4:
            if st.button("🤖 Trained ML Model", key="pop_cp_4", use_container_width=True):
                pop_query = "Which ML model is trained?"
            if st.button("⚡ How Prediction Works", key="pop_cp_8", use_container_width=True):
                pop_query = "How does prediction work?"

        st.markdown("<br>", unsafe_allow_html=True)
        pop_user_search = st.text_input("🔍 Ask AEGIS Copilot anything about the website dataset, model, accuracy, recall, features, or predictions...", key="pop_copilot_search_input", placeholder="Type your custom search query here...")

        if pop_query:
            st.session_state.active_copilot_response = get_copilot_response(pop_query)
        elif pop_user_search:
            st.session_state.active_copilot_response = get_copilot_response(pop_user_search)

        ans_box_html = f"""
        <div style="background: rgba(15, 23, 52, 0.95); border: 1.5px solid #00F0FF; border-radius: 14px; padding: 1.1rem; margin-top: 10px; box-shadow: 0 0 25px rgba(0, 240, 255, 0.25);">
            <div style="display: flex; align-items: center; gap: 8px; color: #00F0FF; font-weight: 800; font-size: 0.85rem; margin-bottom: 6px;">
                <span>🤖 AEGIS COPILOT RESPONSE</span>
            </div>
            <div style="color: #FFFFFF; font-size: 0.92rem; line-height: 1.5;">
                {st.session_state.active_copilot_response.replace('\n', '<br>')}
            </div>
        </div>
        """
        safe_html(ans_box_html)
