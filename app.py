import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIGURATION & EXECUTIVE THEME ---
st.set_page_config(
    page_title="MAREC Insights | Aurora Mirage Digital Twin Sandbox",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ADVANCED CUSTOM CSS STYLING ---
st.markdown("""
    <style>
        .main { background-color: #f1f5f9; font-family: 'Inter', sans-serif; }
        .executive-header {
            background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
            padding: 2.5rem;
            border-radius: 12px;
            color: white;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }
        .executive-header h1 { color: #ffffff; font-weight: 700; font-size: 2.2rem; margin-bottom: 0.5rem; }
        .executive-header p { color: #cbd5e1; font-size: 1.1rem; }
        .metric-card {
            background-color: white;
            padding: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            border-left: 4px solid #3b82f6;
        }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR: SANDBOX & SIMULATION CONTROLS ---
st.sidebar.header("Aurora Mirage Control Center")
st.sidebar.markdown("---")

property_profile = st.sidebar.selectbox(
    "Property Configuration",
    ["Aurora Mirage Resort & Casino (400 Keys)", "Boutique Luxury Annex (120 Keys)"]
)

module_selection = st.sidebar.selectbox(
    "Select Intelligence Module",
    [
        "Module 1: Workforce & Labor Optimization", 
        "Module 2: Net RevPAR & Revenue Audit", 
        "Module 3: Competitive & Scenario Indexing"
    ]
)

st.sidebar.markdown("### Stochastic Demand Shocks")
market_shock = st.sidebar.slider(
    "Market Demand Shift (%)",
    min_value=-30,
    max_value=30,
    value=0,
    step=5,
    help="Simulates macro-level convention surges or sudden economic shocks on booking curves."
)

ai_governance_mode = st.sidebar.toggle(
    "AI Algorithmic Drift Guardrails",
    value=True,
    help="Enables human-in-the-loop oversight to flag automated forecasting anomalies."
)

# --- MAIN EXECUTIVE HEADER ---
st.markdown(f"""
    <div class="executive-header">
        <h1>🏨 Aurora Mirage Digital Twin Sandbox</h1>
        <p><b>Executive Decision Intelligence Platform</b> | Simulating 400-room property operations, stochastic demand vectors, and cross-departmental labor optimization[cite: 13].</p>
    </div>
""", unsafe_allow_html=True)

# Status Feedback
if market_shock != 0:
    st.warning(f"⚠️ **Active Market Shock Detected:** Operating under a **{market_shock}%** demand variance. Labor efficiency metrics (HPOR/REVPALH) auto-adjusting.")

if ai_governance_mode:
    st.info("🛡️ **AI Governance Active:** Human-in-the-loop variance testing enabled for algorithmic yield recommendations.")

st.markdown("---")

# --- MODULE CONTENT RENDERING ---
if "Workforce" in module_selection:
    st.markdown("### 📊 Module 1: Demand-Driven Housekeeping & Labor Optimization")
    st.markdown("Calculate precise staffing requirements, HPOR, and labor cost ratios based on real-time property management data.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Target Occupancy", value="84.5%", delta=f"{market_shock}% shock")
    with col2:
        st.metric(label="Required Housekeeping FTEs", value="42", delta="-3 vs baseline")
    with col3:
        st.metric(label="Labor Cost per Occupied Room (HPOR)", value="$42.50", delta="-1.2%")

elif "Revenue" in module_selection:
    st.markdown("### 💰 Module 2: Net RevPAR & Total Profit Audit")
    st.markdown("Evaluate net asset profitability by balancing channel acquisition costs and GOPPAR against traditional RevPAR metrics[cite: 13].")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Gross RevPAR", value="$215.00", delta="+5.4%")
    with col2:
        st.metric(label="Net RevPAR (post-acquisition)", value="$178.50", delta="+3.1%")
    with col3:
        st.metric(label="GOPPAR", value="$94.20", delta="+4.0%")

else:
    st.markdown("### 🌐 Module 3: Competitive & Scenario Indexing")
    st.markdown("Benchmark performance metrics against competitive set indices under stochastic economic conditions.")
    
    # Sample visualization data
    chart_data = pd.DataFrame({
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "Aurora Mirage Index": [105, 110, 108, 115, 122, 125, 118],
        "Comp Set Average": [100, 100, 100, 100, 100, 100, 100]
    })
    fig = px.line(chart_data, x="Day", y=["Aurora Mirage Index", "Comp Set Average"], 
                  title="Fair Share Penetration Index (MPI/RGI Analysis)")
    st.plotly_chart(fig, use_container_width=True)
