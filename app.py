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

# --- SIDEBAR: CONTROLS & INSTRUCTIONS ---
st.sidebar.header("🏨 Aurora Mirage Control Center")
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

# Module Selection (Includes Polished Step 1 Protocol & Schedule)
module_choice = st.sidebar.selectbox(
    "Select Intelligence Module",
    [
        "Step 1: Testing Protocol & Monthly Schedule",
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
with st.sidebar.expander("2-Person Sprint Instructions"):
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
        "🛡️️ **AI Governance Active:** Human-in-the-loop variance testing enabled for algorithmic yield recommendations."
    )
else:
    st.warning(
        "⚠️ **AI Governance Disabled:** Automated algorithms operating without strict variance guardrails."
    )

# Compute dynamic scaling factors based on demand shift
demand_multiplier = 1 + (st.session_state.demand_shift / 100.0)

# --- STEP 1: TESTING PROTOCOL & MONTHLY SCHEDULE ---
if module_choice == "Step 1: Testing Protocol & Monthly Schedule":
    st.title("🎯 Step 1: Test and Interact with the Live Sandbox Controls")
    st.markdown(
        "**Core Objective:** Establish operational control parameters and simulate real-time decision-making within the simulated 400-room Aurora Mirage luxury property."
    )

    st.markdown("---")

    # Detailed Testing Instructions Layout
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("👷 Testing Workforce & Labor Metrics")
        st.markdown(
            """
        * **Demand-Driven Scheduling:** Simulate high-compression days (e.g., Thursday arrivals and departures) to test demand-driven scheduling instead of fixed headcount guesses.
        * **Foundational Labor KPIs:** Monitor **Labor Cost Percentage of Revenue (LPR)**, **Hours Per Occupied Room (HPOR)**, and **Revenue Per Available Labor Hour (REVPALH)** across operational shifts.
        * **Cross-Departmental Flex Protocols:** Test cross-departmental flex protocols where front-of-house and F&B staff support housekeeping during turnover spikes before overtime is approved.
        """
        )

        st.subheader("💰 Evaluating Revenue & Channel Mix")
        st.markdown(
            """
        * **Margin Leak Identification:** Track ADR and RevPAR alongside TRevPAR and Net RevPAR to identify margin leaks caused by heavy OTA commissions.
        * **Channel Shift Simulations:** Switch distribution channel strategies toward direct bookings to observe immediate margin protection without altering base room rates.
        """
        )

    with col2:
        st.subheader("🤖 Simulating AI Governance & Guardrails")
        st.markdown(
            """
        * **Variance Limit Testing:** Test automated rate and scheduling recommendations against strict variance limits (e.g., max percentage changes allowed without human sign-off).
        * **HITL Escalation Pathways:** Trigger out-of-bounds algorithmic actions (such as sharp rate drops from cancelled group blocks) to test human-in-the-loop escalation pathways and override logging.
        """
        )

        st.info(
            "💡 **Two-Party Execution Tip:** Use the sidebar controls to test parameters together during daily standups, then check Modules 1–4 to observe telemetry ripples and export audit logs."
        )

    st.markdown("---")
    st.subheader(
        "📅 Recommended Monthly Research Schedule (Two-Party Execution)"
    )

    monthly_schedule_df = pd.DataFrame(
        {
            "Sprint Phase": [
                "Phase 1: Week 1",
                "Phase 2: Week 2",
                "Phase 3: Week 3",
                "Phase 4: Week 4",
            ],
            "Focus & Objective": [
                "Baseline Calibration & System Sync",
                "Workforce & Labor Stress-Testing",
                "Revenue & Channel Mix Optimization",
                "AI Governance, HITL & Final Export",
            ],
            "Principal Consultant Actions (You)": [
                "Define property boundary parameters and verify PMS/HRIS data stream baseline integrity.",
                "Review departmental headcounts and approve/reject simulated overtime requests under stress.",
                "Evaluate gross vs. net asset profitability and set channel acquisition targets.",
                "Review HITL override logs and sign off on governance audit reports for publication.",
            ],
            "Graduate Researcher Actions": [
                "Initialize sandbox environment at 0% demand shift and record initial baseline metrics.",
                "Apply $\pm 15\%$ demand shocks via sidebar slider; log HPOR, LPR, and flexing impacts.",
                "Switch channel strategies between OTA and direct push; record net margin variances.",
                "Execute final extreme shock runs (>15%), compile anomaly logs, and export session CSVs.",
            ],
        }
    )
    st.table(monthly_schedule_df)


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