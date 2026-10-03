import pandas as pd
import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="MAREC Insights | Aurora Mirage Digital Twin",
    page_icon="🏨",
    layout="wide",
)

# Initialize Session State for Global Controls & Team Sync
if "demand_shift" not in st.session_state:
    st.session_state.demand_shift = 0
if "ai_guardrails" not in st.session_state:
    st.session_state.ai_guardrails = True
if "channel_mix" not in st.session_state:
    st.session_state.channel_mix = "Balanced (Direct/OTA)"
if "labor_flexing" not in st.session_state:
    st.session_state.labor_flexing = False

# --- SIDEBAR: AURORA CONTROL CENTER ---
st.sidebar.header("🏨 Aurora Control Center")
st.sidebar.markdown(
    "*400-Room Luxury Property Simulation | MAREC Insights*"
)

# Property Selector with Guidance
property_choice = st.sidebar.selectbox(
    "Property Configuration",
    [
        "Aurora Mirage Resort & Casino (400 Rooms)",
        "Boutique Expansion Asset (150 Rooms)",
    ],
)
st.sidebar.caption(
    "💡 *Switch properties to test asset scalability across large casino resorts vs. boutique properties.*"
)

# Intelligence Module Selector with Guidance
module_choice = st.sidebar.selectbox(
    "Select Intelligence Module",
    [
        "Step 1: Daily Operational Guide & 30-Day Schedule",
        "Module 1: Executive Overview & Daily Workflow",
        "Module 2: Net RevPAR & Revenue Audit",
        "Module 3: Workforce Intelligence & Labor Optimization",
        "Module 4: AI Governance & Stress-Testing Sandbox",
    ],
)
st.sidebar.caption(
    "💡 *Rotate through Modules 1–4 daily to audit revenue, labor, and AI guardrails.*"
)

st.sidebar.markdown("---")
st.sidebar.subheader("🎛️ Live Digital Twin Parameters")

# Interactive Sliders & Toggles tied to session state
st.session_state.demand_shift = st.sidebar.slider(
    "Market Demand Shift (%)",
    min_value=-25,
    max_value=25,
    value=st.session_state.demand_shift,
    step=1,
    help="Simulates external market shocks, convention compression, or group cancellations.",
)

st.session_state.ai_guardrails = st.sidebar.toggle(
    "AI Algorithmic Drift Guardrails",
    value=st.session_state.ai_guardrails,
    help="Enables 12% variance limits requiring Human-In-The-Loop (HITL) sign-off.",
)

st.session_state.channel_mix = st.sidebar.selectbox(
    "Distribution Channel Strategy",
    [
        "Balanced (Direct/OTA)",
        "Aggressive Direct Push",
        "OTA Dependent Compression",
    ],
)

st.session_state.labor_flexing = st.sidebar.toggle(
    "Cross-Departmental Labor Flexing",
    value=st.session_state.labor_flexing,
    help="Allows F&B support to assist housekeeping during peak turnover windows.",
)

st.sidebar.markdown("---")
st.sidebar.subheader("👥 Research Team Guide")
with st.sidebar.expander("Two-Party Execution Protocol"):
    st.markdown(
        """
    * **Principal Consultant (You):** Define macro stress-test scenarios, govern AI override rules, and validate executive strategic alignment.
    * **Graduate Researcher:** Execute sandbox simulation runs, log quantitative metric changes, and compile CSV audit exports.
    """
    )


# --- MAIN CONTENT DYNAMIC RENDERING ---

# Header Banner based on state
if st.session_state.ai_guardrails:
    st.info(
        "🛡 **AI Governance Active:** Human-in-the-loop variance testing enabled for algorithmic yield recommendations."
    )
else:
    st.warning(
        "⚠️ **AI Governance Disabled:** Automated algorithms operating without strict variance guardrails."
    )

# Compute dynamic scaling factors based on demand shift
demand_multiplier = 1 + (st.session_state.demand_shift / 100.0)

# --- STEP 1: DAILY OPERATIONAL GUIDE & 30-DAY SCHEDULE ---
if module_choice == "Step 1: Daily Operational Guide & 30-Day Schedule":
    st.title(
        "🎯 Step 1: Aurora Control Center & Daily Operational Testing Blueprint"
    )
    st.markdown(
        "**Core Objective:** Master the daily workflow by combining **Property Configurations**, **Intelligence Modules**, and **Sidebar Controls** to execute a rigorous 30-day evaluation schedule."
    )

    st.markdown("---")

    # How-To Guide for Configurations and Modules
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🏢 How to Use Property Configurations")
        st.markdown(
            """
        * **Aurora Mirage Resort & Casino (400 Rooms):** Use for macro-level convention compression, high-volume F&B labor flexing, and complex gaming resort revenue audits.
        * **Boutique Expansion Asset (150 Rooms):** Switch to this property configuration when testing nimble direct-booking strategies and lean staffing models where overhead sensitivity is higher.
        * **Daily Workflow Rule:** Select your property configuration first thing every morning before adjusting market demand sliders.
        """
        )

    with col2:
        st.subheader("📊 How to Use Intelligence Modules Daily")
        st.markdown(
            """
        * **Module 1 (Executive Overview):** Review baseline occupancy, ADR, RevPAR, and 7-day forecast curves each morning.
        * **Module 2 (Revenue Audit):** Audit net commission leakage and switch distribution channel strategies mid-week.
        * **Module 3 (Workforce Intelligence):** Monitor HPOR and LPR; test labor flexing toggles during peak turnover days.
        * **Module 4 (AI Governance):** Review HITL anomaly alerts under market stress and export session CSV audit logs.
        """
        )

    st.markdown("---")
    st.subheader("📅 Day-to-Day Operational Testing Schedule (Days 1–30)")
    st.markdown(
        "Follow this exact day-by-day protocol to conduct structured testing, evaluate telemetry ripples, and generate client-ready deliverables."
    )

    day_schedule_df = pd.DataFrame(
        {
            "Day / Timeline": [
                "Days 1 – 5: Baseline Calibration",
                "Days 6 – 12: Workforce Stress-Testing",
                "Days 13 – 20: Channel Margin Optimization",
                "Days 21 – 30: AI Governance & Final Audit",
            ],
            "Daily Action Required": [
                "Set Demand Shift to 0%, select 400-Room Property. Verify telemetry sync across Modules 1–3.",
                "Apply daily demand shocks ($\pm 10\\%$ to $\pm 20\\%$) with Labor Flexing ON/OFF. Log HPOR & LPR shifts.",
                "Switch channel strategy between OTAs and Direct Push. Audit net margin impact in Module 2.",
                "Trigger extreme market shocks ($>15\\%$) with AI Guardrails ON/OFF. Review HITL logs and export CSV.",
            ],
            "Responsible Party": [
                "Principal Consultant & Researcher",
                "Graduate Researcher (Daily Execution)",
                "Principal Consultant & Researcher",
                "Principal Consultant (Final Sign-Off)",
            ],
            "Concrete Example & Action": [
                "**Example (Day 3):** Keep Demand Shift at $0\\%$. *Action:* Open Module 1, verify baseline occupancy is locked at $85\\%$, and record baseline headcount in Module 3.",
                "**Example (Day 8):** Set Demand Shift to $+18\\%$, toggle Labor Flexing ON. *Action:* Check Module 3 to verify HPOR drops to $2.1$ hrs and F&B staff absorbs housekeeping turnover.",
                "**Example (Day 15):** Switch Channel Strategy to *OTA Dependent Compression*. *Action:* Go to Module 2 and record the margin compression caused by $18\\%$ OTA commissions.",
                "**Example (Day 25):** Set Demand Shift to $+22\\%$ with Guardrails ON. *Action:* Verify Module 4 displays the red HITL override alert and download the audit CSV.",
            ],
            "Daily Deliverable": [
                "Baseline Telemetry Verification Sign-off.",
                "Departmental Labor & Headcount Variance Sheet.",
                "Channel Profitability & Net RevPAR Audit Report.",
                "Final Executive AI Governance Audit Deck.",
            ],
        }
    )
    st.table(day_schedule_df)

    # CSV Download for 30-Day Schedule
    schedule_csv = day_schedule_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Day-to-Day Operational Testing Schedule (CSV)",
        data=schedule_csv,
        file_name="aurora_mirage_30_day_operational_schedule.csv",
        mime="text/csv",
    )


# --- MODULE 1: EXECUTIVE OVERVIEW ---
elif module_choice == "Module 1: Executive Overview & Daily Workflow":
    st.title("📊 Module 1: Executive Overview & Daily Workflow")
    st.markdown(
        f"Active Property: **{property_choice}** | Tracking real-time synchronization across PMS, RMS, and HRIS."
    )

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        sim_occ = min(max(int(85 * demand_multiplier), 40), 100)
        st.metric(
            "Projected Occupancy",
            f"{sim_occ}%",
            f"{st.session_state.demand_shift}% vs Baseline",
        )
    with col2:
        sim_adr = round(250.00 * demand_multiplier, 2)
        st.metric(
            "Average Daily Rate (ADR)",
            f"${sim_adr}",
            f"{round(demand_multiplier * 2.5, 1)}%",
        )
    with col3:
        sim_revpar = round(sim_adr * (sim_occ / 100), 2)
        st.metric("RevPAR", f"${sim_revpar}")
    with col4:
        sim_goppar = round(94.20 * demand_multiplier, 2)
        st.metric(
            "GOPPAR", f"${sim_goppar}", "Target > $85.00", delta_color="normal"
        )

    st.markdown("---")
    st.subheader("📈 7-Day Simulated Demand Forecast Curve")

    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    forecast_data = []
    for i, day in enumerate(days):
        day_mult = demand_multiplier * (1 + (0.05 * (i % 3 - 1)))
        occ = min(max(int(85 * day_mult), 30), 100)
        adr = round(250.00 * day_mult, 2)
        revpar = round(adr * (occ / 100), 2)
        forecast_data.append(
            {
                "Day": day,
                "Projected Occupancy (%)": occ,
                "ADR ($)": adr,
                "RevPAR ($)": revpar,
            }
        )

    df_forecast = pd.DataFrame(forecast_data)
    st.dataframe(df_forecast, use_container_width=True)


# --- MODULE 2: NET REVPAR & REVENUE AUDIT ---
elif module_choice == "Module 2: Net RevPAR & Revenue Audit":
    st.title("💰 Module 2: Net RevPAR & Total Profit Audit")
    st.markdown(
        f"Active Property: **{property_choice}** | Evaluating net asset profitability and distribution channel acquisition costs."
    )

    ota_penalty = (
        0.18
        if st.session_state.channel_mix == "OTA Dependent Compression"
        else 0.08
    )
    if st.session_state.channel_mix == "Aggressive Direct Push":
        ota_penalty = 0.04

    base_gross = 215.00 * demand_multiplier
    net_revpar_val = round(base_gross * (1 - ota_penalty), 2)
    goppar_val = round(94.20 * demand_multiplier * (1 - (ota_penalty / 2)), 2)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Gross RevPAR", f"${round(base_gross, 2)}")
    with col2:
        st.metric(
            "Net RevPAR (post-acquisition)",
            f"${net_revpar_val}",
            f"Channel: {st.session_state.channel_mix}",
        )
    with col3:
        st.metric("GOPPAR", f"${goppar_val}")

    st.markdown("### 📈 Channel Mix Profitability Breakdown")
    channel_data = pd.DataFrame(
        {
            "Channel Strategy": [
                "Direct Website",
                "Corporate / Group",
                "Third-Party OTAs",
            ],
            "Commission Cost (%)": ["2%", "5%", "18%"],
            "Net Contribution (%)": [
                "45%",
                "35%",
                "20% (Shiftable)",
            ],
        }
    )
    st.table(channel_data)


# --- MODULE 3: WORKFORCE INTELLIGENCE ---
elif module_choice == "Module 3: Workforce Intelligence & Labor Optimization":
    st.title("👷 Module 3: Workforce Intelligence & Labor Optimization")
    st.markdown(
        f"Active Property: **{property_choice}** | Monitoring labor cost percentages (LPR), HPOR, and cross-departmental flexing."
    )

    hpor_val = round(2.5 if not st.session_state.labor_flexing else 2.1, 2)
    lpr_val = round(28.5 - (st.session_state.demand_shift * 0.2), 1)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            "Hours Per Occupied Room (HPOR)",
            f"{hpor_val} hrs",
            "Target: <= 2.5 hrs",
            delta_color="inverse",
        )
    with col2:
        st.metric(
            "Labor Cost % of Revenue (LPR)",
            f"{lpr_val}%",
            "Target: < 30%",
            delta_color="inverse",
        )
    with col3:
        flex_status = (
            "Active (F&B -> Housekeeping)"
            if st.session_state.labor_flexing
            else "Standard Departmental"
        )
        st.metric("Cross-Flex Protocol", flex_status)

    st.markdown("### ⚙️ Departmental Headcount Allocation Table")
    dept_data = pd.DataFrame(
        {
            "Department": [
                "Front Desk",
                "Housekeeping",
                "Food & Beverage",
                "Maintenance",
            ],
            "Base Headcount": [12, 35, 28, 8],
            "Adjusted Shift Headcount": [
                max(
                    int(
                        12 * demand_multiplier
                        if not st.session_state.labor_flexing
                        else 10 * demand_multiplier
                    ),
                    6,
                ),
                max(int(35 * demand_multiplier), 15),
                max(
                    int(
                        28 * demand_multiplier
                        if not st.session_state.labor_flexing
                        else 32 * demand_multiplier
                    ),
                    12,
                ),
                max(int(8 * demand_multiplier), 4),
            ],
        }
    )
    st.dataframe(dept_data, use_container_width=True)


# --- MODULE 4: AI GOVERNANCE & STRESS-TESTING ---
elif module_choice == "Module 4: AI Governance & Stress-Testing Sandbox":
    st.title("🤖 Module 4: AI Governance & Stress-Testing Sandbox")
    st.markdown(
        f"Active Property: **{property_choice}** | Reviewing automated algorithmic recommendations and HITL audit logs."
    )

    st.subheader("🚨 Live Governance Audit Log")

    if abs(st.session_state.demand_shift) > 15 and st.session_state.ai_guardrails:
        st.error(
            "🚨 **HITL Triggered:** Market demand shift exceeded the 15% variance ceiling. Automated pricing/scheduling locked pending Principal Consultant review."
        )
    elif (
        abs(st.session_state.demand_shift) > 15
        and not st.session_state.ai_guardrails
    ):
        st.warning(
            "⚠️ **Guardrails Bypassed:** Extreme demand shift executed automatically without human sign-off. Algorithmic drift risk is elevated."
        )
    else:
        st.success(
            "✅ **System Stable:** All automated pricing and labor algorithms operating safely within defined variance limits."
        )

    st.markdown("---")

    st.subheader("📁 Research Data Export")
    export_df = pd.DataFrame(
        {
            "Property Configuration": [property_choice],
            "Demand Shift (%)": [st.session_state.demand_shift],
            "AI Guardrails Active": [st.session_state.ai_guardrails],
            "Channel Strategy": [st.session_state.channel_mix],
            "Labor Flexing Active": [st.session_state.labor_flexing],
        }
    )

    csv_data = export_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Current Simulation State (CSV)",
        data=csv_data,
        file_name="aurora_mirage_simulation_log.csv",
        mime="text/csv",
    )