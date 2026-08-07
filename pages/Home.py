import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
<style>

.stApp{
background:
radial-gradient(circle at 20% 20%,rgba(0,183,255,.18),transparent 25%),
radial-gradient(circle at 80% 30%,rgba(111,66,255,.15),transparent 25%),
linear-gradient(135deg,#040814,#08101d,#050b16);
overflow:hidden;
}

.hero{
position:relative;
height:92vh;
display:flex;
align-items:center;
justify-content:center;
border-radius:30px;
overflow:hidden;
background:rgba(255,255,255,.03);
backdrop-filter:blur(20px);
border:1px solid rgba(255,255,255,.08);
}

.hero::before{
content:"";
position:absolute;
width:900px;
height:900px;
border-radius:50%;
background:
radial-gradient(circle,
rgba(0,183,255,.28),
transparent 70%);
animation:pulse 8s infinite;
}

.hero::after{
content:"";
position:absolute;
width:500px;
height:500px;
border-radius:50%;
border:2px solid rgba(0,183,255,.25);
animation:rotate 20s linear infinite;
}

.card{
position:absolute;
width:360px;
height:220px;
border-radius:25px;
background:linear-gradient(135deg,#13203b,#1b2f55);
box-shadow:0 0 60px rgba(0,183,255,.25);
transform:rotate(-10deg);
animation:float 6s ease-in-out infinite;
padding:30px;
color:white;
}

.card h1{
font-size:28px;
margin:0;
}

.card p{
font-size:18px;
opacity:.8;
}

.scan{
position:absolute;
width:420px;
height:4px;
background:#00d4ff;
box-shadow:0 0 25px #00d4ff;
animation:scan 4s infinite;
}

.title{
position:absolute;
bottom:70px;
text-align:center;
}

.title h1{
font-size:72px;
margin:0;
color:white;
}

.title p{
font-size:22px;
color:#bcd8ff;
}

@keyframes rotate{
100%{transform:rotate(360deg);}
}

@keyframes pulse{
50%{
transform:scale(1.15);
}
}

@keyframes float{
50%{
transform:translateY(-20px) rotate(-10deg);
}
}

@keyframes scan{
0%{top:20%;}
100%{top:75%;}
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">

<div class="card">

<h1>💳 CREDIT CARD</h1>

<br>

<p>•••• •••• •••• 2458</p>

<br>

<p>LIVE AI MONITORING</p>

</div>

<div class="scan"></div>

<div class="title">

<h1>AEGIS AI</h1>

<p>Enterprise Fraud Intelligence Platform</p>

</div>

</div>
""", unsafe_allow_html=True)
st.markdown("---")

st.markdown("""
<h2 style='text-align:center;color:#00d4ff;'>
⚡ LIVE AI DEFENSE GRID
</h2>
<p style='text-align:center;color:#BFC9D9;'>
Every transaction is analysed by Artificial Intelligence before approval.
</p>
""", unsafe_allow_html=True)

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("💳 Transactions","284,807","+18%")

with col2:
    st.metric("🚨 Frauds","492","-2%")

with col3:
    st.metric("🎯 Accuracy","99.95%","+0.3%")

with col4:
    st.metric("⚡ Status","ONLINE","🟢")

st.markdown("<br>",unsafe_allow_html=True)

left,right=st.columns([2,1])

with left:

    st.markdown("""
<div class="network-box">

<h2>🧠 AI Decision Pipeline</h2>

<br>

💳 Transaction

⬇

📊 Feature Engineering

⬇

🤖 Random Forest

⬇

🚨 Fraud Score

⬇

✅ Final Decision

</div>
""",unsafe_allow_html=True)

with right:

    st.markdown("""
<div class="status-box">

<h3>🟢 SYSTEM STATUS</h3>

<hr>

✔ AI Engine

<br>

✔ Database Connected

<br>

✔ Prediction Ready

<br>

✔ Explain AI Enabled

<br>

✔ Monitoring Live

</div>
""",unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<h2 style="text-align:center;color:#00d9ff;">
🌍 GLOBAL FRAUD MONITOR
</h2>
<p style="text-align:center;color:#9db7d5;">
Live AI surveillance across worldwide financial transactions.
</p>
""", unsafe_allow_html=True)

col1, col2 = st.columns([3,2])

with col1:

    st.markdown("""
<div class="world-map">

<div class="pulse p1"></div>
<div class="pulse p2"></div>
<div class="pulse p3"></div>
<div class="pulse p4"></div>
<div class="pulse p5"></div>

<div class="line l1"></div>
<div class="line l2"></div>
<div class="line l3"></div>

<h2 class="center-ai">🛡️ AEGIS AI</h2>

</div>
""", unsafe_allow_html=True)

with col2:

    st.markdown("""
<div class="feed-box">

<h3>⚡ LIVE TRANSACTIONS</h3>

<hr>

🇮🇳 Hyderabad

₹12,450

✅ Approved

<br><br>

🇺🇸 New York

₹95,800

🚨 Blocked

<br><br>

🇬🇧 London

₹4,500

✅ Approved

<br><br>

🇸🇬 Singapore

₹38,900

🚨 Review

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.success("🌐 AI Network synchronized across global transaction nodes.")
st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<h2 style="text-align:center;color:#00d9ff;">
💳 AI CREDIT CARD SCANNER
</h2>

<p style="text-align:center;color:#A8B6D5;">
Every transaction is scanned before approval using Artificial Intelligence.
</p>
""", unsafe_allow_html=True)

left, right = st.columns([3,2])

with left:

    st.markdown("""
<div class="scanner-container">

<div class="scanner-ring ring1"></div>
<div class="scanner-ring ring2"></div>
<div class="scanner-ring ring3"></div>

<div class="credit-card">

<div class="chip"></div>

<h2>AEGIS BANK</h2>

<br><br>

<h3>•••• •••• •••• 2458</h3>

<p>BHANU MAHESH</p>

</div>

<div class="laser"></div>

</div>
""", unsafe_allow_html=True)

with right:

    st.markdown("""
<div class="scan-panel">

<h2>🧠 AI Scan Result</h2>

<hr>

✔ Card Verified

<br><br>

✔ Behaviour Analysed

<br><br>

✔ Device Trusted

<br><br>

✔ Risk Score : 2%

<br><br>

<h1 style="color:#3CFF8E;">SAFE</h1>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.button("🚀 START AI ANALYSIS", use_container_width=True)
st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<h2 style="text-align:center;color:#00d9ff;">
⚡ AI COMMAND CENTER
</h2>

<p style="text-align:center;color:#B7C8E6;">
Enterprise Fraud Intelligence Dashboard
</p>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
<div class="command-card">
<h3>🧠 AI ENGINE</h3>
<h1>ONLINE</h1>
<p>Random Forest Model Active</p>
</div>
""", unsafe_allow_html=True)

with c2:
    st.markdown("""
<div class="command-card">
<h3>💳 RISK SCORE</h3>
<h1>2%</h1>
<p>Current Transaction Risk</p>
</div>
""", unsafe_allow_html=True)

with c3:
    st.markdown("""
<div class="command-card">
<h3>🛡️ SECURITY</h3>
<h1>SECURED</h1>
<p>Threat Detection Enabled</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="timeline">

<div class="step active">💳 Transaction</div>

<div class="arrow">➜</div>

<div class="step active">📊 Analysis</div>

<div class="arrow">➜</div>

<div class="step active">🤖 AI Model</div>

<div class="arrow">➜</div>

<div class="step active">🚨 Detection</div>

<div class="arrow">➜</div>

<div class="step active">✅ Secure</div>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.success("✔ AI successfully completed fraud analysis pipeline.")