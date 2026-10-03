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

# Property Selector
property_choice = st.sidebar.selectbox(
    "Property Configuration",
    [
        "Aurora Mirage Resort & Casino (400 Rooms)",
        "Boutique Expansion Asset (150 Rooms)",
    ],
)

# Module Selection
module_choice = st.sidebar.selectbox(
    "Select Intelligence Module",
    [
        "Step 1: Control Center Guide & 4-Month Daily Schedule",
        "Module 1: Executive Overview & Daily Workflow",
        "Module 2: Net RevPAR & Revenue Audit",
        "Module 3: Workforce Intelligence & Labor Optimization",
        "Module 4: AI Governance & Stress-Testing Sandbox",
    ],
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

# --- STEP 1: CONTROL CENTER GUIDE & 4-MONTH DAILY SCHEDULE ---
if module_choice == "Step 1: Control Center Guide & 4-Month Daily Schedule":
    st.title("🎯 Step 1: Aurora Control Center Guide & Daily Action Blueprint")
    st.markdown(
        "**Core Objective:** Master the sidebar **Aurora Control Center** parameters and execute a structured, day-by-day operational testing protocol across the 400-room Aurora Mirage property."
    )

    st.markdown("---")

    # Detailed Control Center Breakdown
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🎛️ How to Use the Aurora Control Center")
        st.markdown(
            """
        * **Market Demand Shift Slider:** Drag between $-25\%$ and $+25\%$ to simulate group cancellations or heavy convention compression.
        * **AI Algorithmic Drift Guardrails:** Toggle ON to enforce strict $15\%$ variance limits that trigger Human-In-The-Loop (HITL) locks.
        * **Distribution Channel Strategy:** Switch between *Balanced*, *Aggressive Direct Push*, and *OTA Dependent Compression* to analyze commission margin leaks.
        * **Cross-Departmental Labor Flexing:** Toggle ON to let F&B staff support housekeeping during turnover spikes, lowering Hours Per Occupied Room (HPOR).
        """
        )

    with col2:
        st.subheader("👥 Two-Party Daily Execution Workflow")
        st.markdown(
            """
        * **Daily Standup (10 Mins):** Principal Consultant sets the target market shock parameter in the sidebar. Graduate researcher runs the simulation.
        * **Data Logging:** Record changes in ADR, RevPAR, GOPPAR, and LPR across Modules 1 through 3.
        * **Audit & Export:** Use Module 4 to review AI drift logs and export session CSV datasets for client reporting.
        """
        )

    st.markdown("---")
    st.subheader(
        "📅 4-Month Master Daily Operational Schedule & Example Scenarios"
    )
    st.markdown(
        "The following dataset provides granular daily instructions, responsible parties, concrete operational examples, and tangible deliverables for each phase."
    )

    master_daily_df = pd.DataFrame(
        {
            "Month & Timeline": [
                "Month 1: Baseline Calibration & Control Setup",
                "Month 2: Workforce & Labor Stress-Testing",
                "Month 3: Revenue & Channel Margin Optimization",
                "Month 4: AI Governance & Final Audit",
            ],
            "Daily Operational Focus": [
                "Establish 0% demand baseline; verify PMS, RMS, and HRIS telemetry sync in Modules 1–3.",
                "Execute daily demand shocks ($\pm 10\\%$ to $\pm 20\\%$); test labor flexing protocols under compression.",
                "Simulate channel strategy shifts daily; audit net commission leakage and direct booking acquisition costs.",
                "Trigger extreme market shocks ($>15\\%$) with guardrails ON/OFF; review HITL overrides and export CSVs.",
            ],
            "Responsible Party": [
                "Principal Consultant & Researcher",
                "Graduate Researcher (Daily Execution)",
                "Principal Consultant & Researcher",
                "Principal Consultant (Final Sign-Off)",
            ],
            "Concrete Example & Action": [
                "**Example:** Leave Demand Shift at $0\\%$, AI Guardrails ON. *Action:* Inspect Module 1 occupancy ($85\\%$) and baseline headcount tables in Module 3.",
                "**Example:** Set Demand Shift to $+18\\%$, toggle Labor Flexing ON. *Action:* Observe HPOR drop from $2.5$ hrs to $2.1$ hrs and note F&B headcount reallocation.",
                "**Example:** Switch Channel Strategy to *OTA Dependent Compression*. *Action:* Check Module 2 to verify Net RevPAR drop due to $18\\%$ OTA commissions.",
                "**Example:** Set Demand Shift to $+20\\%$ with Guardrails ON. *Action:* Verify automated system lock triggers in Module 4 and export audit log CSV.",
            ],
            "Deliverables & Output": [
                "Signed Baseline Telemetry Validation Checklist.",
                "Workforce Headcount & LPR Variance Log Sheet.",
                "Channel Profitability & Net RevPAR Audit Deck.",
                "Final Governance Audit Report & CSV Export.",
            ],
        }
    )
    st.table(master_daily_df)

    # CSV Download for Master Daily Schedule
    daily_csv = master_daily_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download 4-Month Daily Operational Schedule (CSV)",
        data=daily_csv,
        file_name="aurora_mirage_4_month_daily_schedule.csv",
        mime="text/csv",
    )


# --- MODULE 1: EXECUTIVE OVERVIEW ---
elif module_choice == "Module 1: Executive Overview & Daily Workflow":
    st.title("📊 Module 1: Executive Overview & Daily Workflow")
    st.markdown(
        "Welcome to the **Aurora Mirage Digital Twin**. This dashboard tracks real-time synchronization across Property Management Systems (PMS), Revenue Management (RMS), and Human Resources (HRIS)."
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
        "Evaluate net asset profitability by balancing channel acquisition costs and distribution fees against traditional RevPAR metrics."
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
        "Monitor labor cost percentages (LPR), hours per occupied room (HPOR), and cross-departmental flexing protocols."
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
        "Evaluate automated algorithmic recommendations, review Human-In-The-Loop (HITL) audit trails, and test system reaction limits."
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
            "Parameter": [
                "Demand Shift (%)",
                "AI Guardrails Active",
                "Channel Strategy",
                "Labor Flexing Active",
            ],
            "Value": [
                st.session_state.demand_shift,
                st.session_state.ai_guardrails,
                st.session_state.channel_mix,
                st.session_state.labor_flexing,
            ],
        }
    )

    csv_data = export_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Current Simulation State (CSV)",
        data=csv_data,
        file_name="aurora_mirage_simulation_log.csv",
        mime="text/csv",
    )