import streamlit as st
from agent import analyze_incident

st.set_page_config(
    page_title="IncidentMind",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 IncidentMind")
st.subheader("AI-Powered Incident Response with Operational Memory")

st.write(
    "Describe a production incident and IncidentMind will use "
    "historical incident memory to suggest evidence-based next steps."
)

st.divider()

incident = st.text_area(
    "Describe the incident",
    placeholder=(
        "Example: Payment API is returning 500 errors. "
        "Database connection pool is exhausted."
    ),
    height=150
)

if st.button("🔍 Analyze Incident"):

    if not incident.strip():
        st.warning("Please describe the incident first.")
    else:
        with st.spinner("Recalling historical incidents and analyzing..."):

            try:
                result = analyze_incident(incident)

                st.success("Incident analysis completed.")

                st.markdown("### 🧠 IncidentMind Analysis")
                st.write(result)

                st.info(
                    "⚠️ Recommendations should be reviewed and verified "
                    "by an engineer before taking action."
                )

            except Exception as e:
                st.error("Something went wrong while analyzing the incident.")
                st.code(str(e))

st.divider()

st.caption(
    "IncidentMind • Historical incident memory + AI reasoning • "
    "Human verification required"
)
