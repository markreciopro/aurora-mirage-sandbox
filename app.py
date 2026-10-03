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
        "Step 1: 4-Month Daily Time Schedule & Deliverables",
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

# --- STEP 1: 4-MONTH DAILY TIME SCHEDULE & DELIVERABLES ---
if module_choice == "Step 1: 4-Month Daily Time Schedule & Deliverables":
    st.title("🎯 Step 1: 4-Month Master Daily Time-Stamped Schedule & Deliverables")
    st.markdown(
        "**Core Objective:** Execute a disciplined, hour-by-hour time-blocked daily routine across four months to calibrate, stress-test, optimize, and audit the **Aurora Mirage Digital Twin**."
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🏢 Property Configuration Guidelines")
        st.markdown(
            """
        * **Aurora Mirage Resort & Casino (400 Rooms):** Best for high-volume convention compression, complex F&B labor flexing, and multi-channel revenue audits.
        * **Boutique Expansion Asset (150 Rooms):** Ideal for testing nimble direct-booking pushes and lean staffing models.
        """
        )

    with col2:
        st.subheader("📊 Intelligence Module Rotation")
        st.markdown(
            """
        * **Morning Block:** Check **Module 1** (Overview) & **Module 3** (Workforce).
        * **Midday Block:** Audit **Module 2** (Revenue & Channels).
        * **Evening Block:** Review **Module 4** (AI Governance & Export).
        """
        )

    st.markdown("---")
    st.subheader(
        "⏰ Time-Stamped Master Daily Operational Schedule (Months 1–4)"
    )
    st.markdown(
        "This schedule provides exact time-stamped hourly intervals, daily operational instructions, accountable roles, concrete examples, and mandatory daily deliverables."
    )

    time_schedule_df = pd.DataFrame(
        {
            "Month & Phase": [
                "Month 1: Baseline Calibration & Telemetry Setup",
                "Month 2: Workforce & Labor Stress-Testing",
                "Month 3: Revenue & Channel Margin Optimization",
                "Month 4: AI Governance & Final Audit",
            ],
            "Time-Stamped Daily Schedule": [
                "**09:00 - 09:30:** System Sync & Init\n**09:30 - 11:00:** Baseline Audit",
                "**09:00 - 09:30:** Shock Setup\n**09:30 - 11:30:** Labor Flexing Test",
                "**09:00 - 10:00:** Channel Toggle\n**10:00 - 12:00:** Commission Audit",
                "**09:00 - 10:30:** Extreme Shock Test\n**10:30 - 12:00:** HITL & CSV Export",
            ],
            "Daily Operational Instructions": [
                "Set Demand Shift to 0%, select 400-Room Property. Verify PMS, RMS, and HRIS telemetry sync across Modules 1–3.",
                "Apply daily demand shocks ($\pm 10\\%$ to $\pm 20\\%$) with Labor Flexing ON/OFF. Log HPOR & LPR shifts in Module 3.",
                "Switch distribution channel strategies between OTAs and Direct Push. Audit net commission leakage in Module 2.",
                "Trigger extreme market shocks ($>15\\%$) with AI Guardrails ON/OFF. Review HITL logs and export session CSVs.",
            ],
            "Concrete Example & Action": [
                "**Example:** Keep Demand Shift at $0\\%$. *Action:* Open Module 1, verify baseline occupancy is locked at $85\\%$, and record baseline headcount.",
                "**Example:** Set Demand Shift to $+18\\%$, toggle Labor Flexing ON. *Action:* Check Module 3 to verify HPOR drops to $2.1$ hrs and F&B absorbs turnover.",
                "**Example:** Switch Channel Strategy to *OTA Dependent Compression*. *Action:* Go to Module 2 and record margin compression from $18\\%$ OTA commissions.",
                "**Example:** Set Demand Shift to $+22\\%$ with Guardrails ON. *Action:* Verify Module 4 displays the red HITL override alert and download audit CSV.",
            ],
            "Daily Deliverable": [
                "Signed Baseline Telemetry Verification Sign-off.",
                "Departmental Labor & Headcount Variance Sheet.",
                "Channel Profitability & Net RevPAR Audit Report.",
                "Final Executive AI Governance Audit Deck.",
            ],
        }
    )
    st.table(time_schedule_df)

    # CSV Download for Time Schedule
    time_csv = time_schedule_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Time-Stamped Schedule & Deliverables (CSV)",
        data=time_csv,
        file_name="aurora_mirage_time_schedule_deliverables.csv",
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