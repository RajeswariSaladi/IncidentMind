import requests
import streamlit as st


API_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="IncidentMind",
    page_icon="🧠",
    layout="wide",
)


# ---------- Header ----------

st.title("🧠 IncidentMind")
st.subheader(
    "AI-Powered Incident Response with Persistent Operational Memory"
)

st.write(
    "IncidentMind helps engineers investigate production incidents "
    "by recalling similar historical incidents, successful fixes, "
    "and previously failed approaches."
)

st.divider()


# ---------- Sidebar ----------

with st.sidebar:
    st.header("⚙️ IncidentMind")

    use_memory = st.toggle(
        "Use historical memory",
        value=True,
    )

    st.info(
        "When enabled, IncidentMind recalls relevant historical "
        "incidents before generating its analysis."
    )

    st.caption(
        "Powered by Hindsight memory + Groq LLM"
    )


# ---------- Incident Input ----------

st.header("🚨 New Production Incident")

alert = st.text_area(
    "Describe the incident",
    placeholder=(
        "Example:\n"
        "Payment API is returning 500 errors. "
        "Database connection pool is exhausted."
    ),
    height=160,
)


if st.button(
    "🔍 Analyze Incident",
    type="primary",
    use_container_width=True,
):

    if not alert.strip():
        st.warning("Please describe the incident first.")

    else:

        with st.spinner(
            "Recalling historical incidents and analyzing..."
        ):

            try:
                response = requests.post(
                    f"{API_URL}/triage",
                    json={
                        "alert": alert,
                        "use_memory": use_memory,
                    },
                    timeout=120,
                )

                response.raise_for_status()

                data = response.json()

                st.session_state["analysis"] = data
                st.session_state["current_alert"] = alert

            except Exception as error:
                st.error(
                    "Could not connect to the IncidentMind backend."
                )

                st.code(str(error))


# ---------- Analysis ----------

if "analysis" in st.session_state:

    data = st.session_state["analysis"]

    st.divider()

    st.header("🧠 IncidentMind Analysis")

    st.markdown(data["answer"])


    # ---------- Historical Memory ----------

    st.divider()

    st.header("📚 Recalled Historical Incidents")

    memories = data.get("memories", [])

    if memories:

        st.success(
            f"{len(memories)} relevant historical memories found."
        )

        for index, memory in enumerate(memories, start=1):

            with st.expander(
                f"Historical Incident {index}"
            ):

                st.write(
                    memory.get(
                        "text",
                        "No incident details available.",
                    )
                )

    else:

        st.info(
            "No relevant historical incidents were found."
        )


    # ---------- Resolve Incident ----------

    st.divider()

    st.header("✅ Record Incident Resolution")

    st.write(
        "After the incident is resolved, record what happened. "
        "IncidentMind will retain this outcome for future incidents."
    )

    with st.form("resolution_form"):

        incident_id = st.text_input(
            "Incident ID",
            value="INC-LIVE-001",
        )

        root_cause = st.text_area(
            "Root Cause",
            placeholder="What caused the incident?",
        )

        fix_applied = st.text_area(
            "Fix Applied",
            placeholder="What action resolved the incident?",
        )

        worked = st.radio(
            "Did the fix work?",
            ["Yes", "No"],
            horizontal=True,
        )

        minutes = st.number_input(
            "Resolution Time (minutes)",
            min_value=0,
            value=30,
        )

        lesson = st.text_area(
            "Lesson Learned",
            placeholder=(
                "What should the team remember "
                "for the next similar incident?"
            ),
        )

        submitted = st.form_submit_button(
            "💾 Save Resolution",
            use_container_width=True,
        )

        if submitted:

            if not root_cause.strip() or not fix_applied.strip():

                st.warning(
                    "Please provide the root cause and fix."
                )

            else:

                try:

                    resolve_response = requests.post(
                        f"{API_URL}/resolve",
                        json={
                            "incident_id": incident_id,
                            "alert": st.session_state.get(
                                "current_alert",
                                alert,
                            ),
                            "root_cause": root_cause,
                            "fix_applied": fix_applied,
                            "worked": worked == "Yes",
                            "minutes": minutes,
                            "lesson": lesson,
                        },
                        timeout=120,
                    )

                    resolve_response.raise_for_status()

                    st.success(
                        "Resolution stored in IncidentMind memory."
                    )

                except Exception as error:

                    st.error(
                        "Could not store the incident resolution."
                    )

                    st.code(str(error))


# ---------- Insights ----------

st.divider()

st.header("📊 Operational Insights")

st.write(
    "Ask IncidentMind to identify recurring root causes, "
    "failure patterns, successful fixes, and lessons across "
    "the team's incident history."
)

if st.button(
    "💡 Generate Team Insights",
    use_container_width=True,
):

    with st.spinner(
        "Reflecting across historical incidents..."
    ):

        try:

            response = requests.get(
                f"{API_URL}/insights",
                timeout=120,
            )

            response.raise_for_status()

            insights = response.json()["insights"]

            st.success("Team insights generated.")

            st.markdown(insights)

        except Exception as error:

            st.error(
                "Could not generate operational insights."
            )

            st.code(str(error))


# ---------- Footer ----------

st.divider()

st.caption(
    "IncidentMind • Persistent incident memory • "
    "Historical evidence + AI reasoning • "
    "Human verification required"
)
