import streamlit as st
from utils.theme import safe_html

LIVE_FEED_ITEMS = [
    {"country": "India", "flag": "🇮🇳", "amount": "₹25,000", "status": "APPROVED", "class": "badge-approved", "time": "Just now", "type": "POS Checkout"},
    {"country": "USA", "flag": "🇺🇸", "amount": "₹95,000 ($1,150)", "status": "BLOCKED", "class": "badge-blocked", "time": "2s ago", "type": "CNP Online"},
    {"country": "Japan", "flag": "🇯🇵", "amount": "¥450,000", "status": "REVIEW REQUIRED", "class": "badge-review", "time": "4s ago", "type": "ATM Withdrawal"},
    {"country": "Germany", "flag": "🇩🇪", "amount": "€12,500", "status": "APPROVED", "class": "badge-approved", "time": "6s ago", "type": "Wire Transfer"},
    {"country": "Dubai", "flag": "🇦🇪", "amount": "$45,000", "status": "BLOCKED", "class": "badge-blocked", "time": "9s ago", "type": "Luxury Crypto POS"},
    {"country": "UK", "flag": "🇬🇧", "amount": "£8,200", "status": "APPROVED", "class": "badge-approved", "time": "12s ago", "type": "E-commerce"},
    {"country": "Singapore", "flag": "🇸🇬", "amount": "$14,000", "status": "REVIEW REQUIRED", "class": "badge-review", "time": "15s ago", "type": "Cross-Border FX"},
]

def render_world_network():
    network_svg = """
    <div class="aegis-panel" style="position: relative; overflow: hidden; min-height: 400px; display: flex; flex-direction: column; justify-content: space-between;">
        <div class="panel-header">
            <div>
                <div class="panel-title">🌐 GLOBAL FINANCIAL THREAT MONITOR</div>
                <div class="panel-subtitle">Continuous real-time packet surveillance across 7 major banking nodes</div>
            </div>
            <span class="badge-approved">🟢 100% NODE SYNCHRONIZED</span>
        </div>
        
        <svg viewBox="0 0 1000 380" style="width: 100%; height: 320px; background: rgba(3, 6, 18, 0.6); border-radius: 16px; border: 1px solid rgba(0, 212, 255, 0.1);">
            <path d="M 180 180 Q 380 90 520 180" stroke="rgba(0, 212, 255, 0.3)" stroke-width="1.5" fill="none" stroke-dasharray="6 4" />
            <path d="M 520 180 Q 680 120 820 160" stroke="rgba(124, 58, 237, 0.4)" stroke-width="1.5" fill="none" />
            <path d="M 520 180 Q 420 280 280 250" stroke="rgba(0, 212, 255, 0.3)" stroke-width="1.5" fill="none" />
            <path d="M 520 180 Q 640 280 750 260" stroke="rgba(0, 212, 255, 0.3)" stroke-width="1.5" fill="none" />
            
            <circle cx="180" cy="180" class="network-node" />
            <text x="180" y="210" fill="#FFFFFF" font-size="12" font-weight="700" text-anchor="middle">🇺🇸 USA (NYC)</text>
            
            <circle cx="520" cy="180" r="14" fill="#00D4FF" filter="drop-shadow(0 0 15px #00D4FF)" />
            <text x="520" y="145" fill="#00D4FF" font-size="14" font-weight="900" text-anchor="middle">🛡️ AEGIS AI CORE</text>
            <text x="520" y="215" fill="#FFFFFF" font-size="11" text-anchor="middle">🇩🇪 Germany & 🇬🇧 UK</text>
            
            <circle cx="420" cy="270" class="network-node" />
            <text x="420" y="300" fill="#FFFFFF" font-size="12" font-weight="700" text-anchor="middle">🇦🇪 Dubai</text>
            
            <circle cx="640" cy="270" class="network-node" />
            <text x="640" y="300" fill="#FFFFFF" font-size="12" font-weight="700" text-anchor="middle">🇮🇳 India (HYD/BOM)</text>
            
            <circle cx="750" cy="260" class="network-node" />
            <text x="750" y="290" fill="#FFFFFF" font-size="12" font-weight="700" text-anchor="middle">🇸🇬 Singapore</text>
            
            <circle cx="820" cy="160" class="network-node" />
            <text x="820" y="190" fill="#FFFFFF" font-size="12" font-weight="700" text-anchor="middle">🇯🇵 Japan (Tokyo)</text>
            
            <circle cx="350" cy="140" r="4" class="data-packet">
                <animate attributeName="cx" values="180;520;180" dur="4s" repeatCount="indefinite" />
                <animate attributeName="cy" values="180;180;180" dur="4s" repeatCount="indefinite" />
            </circle>
            <circle cx="670" cy="150" r="4" class="data-packet" fill="#EF4444">
                <animate attributeName="cx" values="520;820;520" dur="3s" repeatCount="indefinite" />
                <animate attributeName="cy" values="180;160;180" dur="3s" repeatCount="indefinite" />
            </circle>
            <circle cx="580" cy="225" r="4" class="data-packet">
                <animate attributeName="cx" values="520;640;520" dur="3.5s" repeatCount="indefinite" />
                <animate attributeName="cy" values="180;270;180" dur="3.5s" repeatCount="indefinite" />
            </circle>
        </svg>
    </div>
    """
    safe_html(network_svg)

def render_live_feed():
    feed_items_html = ""
    for item in LIVE_FEED_ITEMS:
        feed_items_html += f"""
        <div class="feed-item">
            <div class="feed-country">
                <span style="font-size: 1.3rem;">{item['flag']}</span>
                <div>
                    <div>{item['country']}</div>
                    <div style="font-size: 0.75rem; color: #94A3B8;">{item['type']} • {item['time']}</div>
                </div>
            </div>
            <div style="text-align: right;">
                <div class="feed-amount">{item['amount']}</div>
                <span class="{item['class']}">{item['status']}</span>
            </div>
        </div>
        """

    feed_html = f"""
    <div class="aegis-panel" style="height: 100%;">
        <div class="panel-header">
            <div>
                <div class="panel-title">📡 LIVE TRANSACTION STREAM</div>
                <div class="panel-subtitle">Automated real-time fraud scoring</div>
            </div>
            <span class="badge-approved">LIVE STREAM</span>
        </div>
        <div class="live-feed-container">
            {feed_items_html}
        </div>
    </div>
    """
    safe_html(feed_html)
