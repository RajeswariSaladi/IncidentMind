 IncidentMind

AI-Powered On-Call Incident Response Agent That Remembers Every Outage

Built for HackwithHyderabad 3.0 — AI Agents That Learn Using Hindsight

IncidentMind is an AI-powered incident-response agent that helps engineering teams investigate production incidents using persistent operational memory.

Instead of treating every alert as a completely new problem, IncidentMind recalls similar historical incidents, previously successful fixes, failed approaches, root causes, and lessons learned.

The goal is simple:

Every incident becomes knowledge for the next one.

⸻

 Demo Preview

Screenshots below will be added after the application is tested.

Incident Analysis

Historical Memory

Operational Insights

⸻

Problem

When a production incident occurs, engineers often have to investigate from scratch.

However, the solution to a similar problem may already exist in:

* Previous postmortems
* Incident notes
* Internal documentation
* Team discussions
* Engineers’ past experience

This leads to repeated investigation and loss of operational knowledge.

A generic AI assistant can provide troubleshooting suggestions, but it usually does not know what happened previously inside a particular engineering team or service.

⸻

 Solution

IncidentMind gives an AI incident-response agent persistent memory.

Every incident can become part of the team’s operational knowledge:

Incident
   ↓
Root Cause
   ↓
Fix Attempt
   ↓
Outcome
   ↓
Resolution
   ↓
Lesson Learned
   ↓
Persistent Memory

When a new alert arrives, IncidentMind can:

1. Recall similar historical incidents
2. Identify previously observed root causes
3. Surface successful fixes
4. Warn about previously failed fixes
5. Generate a structured incident analysis
6. Store the new incident outcome
7. Reflect across incidents to identify recurring patterns

⸻

 Core Concept

Traditional incident response often looks like:

Alert → Investigate → Fix → Forget

IncidentMind aims to make it:

Alert
  ↓
Remember
  ↓
Investigate
  ↓
Fix
  ↓
Learn
  ↓
Remember Better

⸻

How IncidentMind Works

                 NEW PRODUCTION ALERT
                         │
                         ▼
                ┌─────────────────┐
                │   IncidentMind   │
                │      Agent       │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │     RECALL      │
                │    Historical   │
                │     Memory      │
                └────────┬────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Historical Incidents│
              │                     │
              │ • Root Causes       │
              │ • Successful Fixes  │
              │ • Failed Fixes      │
              │ • Lessons Learned   │
              └──────────┬──────────┘
                         │
                         ▼
                ┌─────────────────┐
                │     Groq LLM    │
                │    Reasoning    │
                └────────┬────────┘
                         │
                         ▼
                 INCIDENT ANALYSIS
                         │
                         ▼
                 ENGINEER VERIFIES
                         │
                         ▼
                  INCIDENT RESOLVED
                         │
                         ▼
                ┌─────────────────┐
                │      RETAIN     │
                │   New Outcome   │
                └────────┬────────┘
                         │
                         ▼
                  FUTURE MEMORY

⸻

 Hindsight-Powered Memory

IncidentMind uses Hindsight as its persistent memory layer.

Retain

Stores incident knowledge including:

* Alerts
* Symptoms
* Root causes
* Fix attempts
* Fix results
* Resolutions
* Lessons learned

Recall

Retrieves relevant historical incidents when a new alert arrives.

Reflect

Identifies higher-level patterns across the team’s incident history.

                 HINDSIGHT MEMORY
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
       RETAIN         RECALL        REFLECT
          │             │             │
        Store         Retrieve      Discover
        Memory        Evidence      Patterns

⸻

 Remembering Failed Fixes

One of IncidentMind’s important concepts is that failed approaches are also valuable knowledge.

For example:

Previous Incident
Service:
Payment API
Problem:
Database connection pool exhausted
Fix Attempt:
Restarted the API
Result:
Failed / temporary recovery
Actual Resolution:
Increased connection-pool capacity
and reduced connection leakage

When a similar incident occurs, IncidentMind can use this historical evidence to help engineers avoid repeating an unsuccessful approach.

⸻

 Key Features

Feature	Description
-> Incident Triage	Analyze new production alerts
-> Persistent Memory	Remember previous incidents
-> Historical Recall	Find relevant similar incidents
-> Failed-Fix Memory	Remember unsuccessful approaches
-> Resolution Capture	Store incident outcomes
-> Lessons Learned	Preserve operational knowledge
-> Operational Insights	Identify recurring patterns
-> AI Reasoning	Generate structured incident analysis
-> Continuous Learning	Add new outcomes to future memory
-> Memory Isolation	Support separate team/service memory banks

⸻

 Architecture

IncidentMind consists of five main layers:

1. Streamlit Interface

Provides the user interface for submitting incidents, viewing AI analysis, reviewing historical memories, recording resolutions, and generating operational insights.

2. FastAPI Backend

Handles communication between the frontend and the IncidentMind agent through REST API endpoints.

3. IncidentMind Agent

Coordinates the incident-response workflow by:

* Receiving a new production alert
* Recalling relevant historical incidents
* Providing historical evidence to the LLM
* Generating an incident analysis
* Recording the final resolution

4. Hindsight Memory

Provides persistent operational memory through:

* Retain — stores incidents, resolutions, and lessons
* Recall — retrieves relevant historical incidents
* Reflect — identifies recurring patterns and insights

5. Groq LLM

Analyzes the new alert together with historical evidence and generates a structured response for the engineer.

Incident Response Flow

New Alert → Historical Recall → AI Analysis → Engineer Verification → Resolution → Memory Retention

⸻

Project Structure

app/

Contains the core IncidentMind application.

* agent.py — Incident triage and resolution workflow
* config.py — Application configuration and environment variables
* llm.py — Groq LLM integration
* main.py — FastAPI application and API endpoints
* memory.py — Hindsight memory operations
* __init__.py — Python package initializer

data/

Contains the historical incident dataset.

* incidents.json — Synthetic production incident records

scripts/

Contains project setup and dataset utilities.

* seed_incidents.py — Loads historical incidents into Hindsight
* generate_incidents.py — Validates the incident dataset

ui/

Contains the Streamlit frontend.

* app.py — IncidentMind user interface

Root Configuration Files

* .env.example — Environment-variable template
* .gitignore — Prevents secrets and unnecessary files from being committed
* requirements.txt — Python dependencies
* README.md — Project documentation

Tech Stack

Backend

* Python
* FastAPI
* Pydantic
* Uvicorn

AI

* Groq API
* Configurable primary and fallback LLM models

Memory

* Hindsight
* Persistent incident memory
* Recall
* Reflection

Frontend

* Streamlit

Data

* JSON-based synthetic incident dataset

⸻

 Incident Dataset

IncidentMind includes a synthetic incident dataset containing 30 realistic production-style incidents.

Each incident contains:

Incident ID
Service
Severity
Symptoms
Root Cause
Fix Attempted
Fix Result
Resolution
Lessons Learned

The dataset is designed to demonstrate:

* Similar recurring incidents
* Different root causes
* Successful resolutions
* Failed fixes
* Operational lessons

The data is synthetic and intended for hackathon demonstration purposes.

⸻

 Example

Suppose a new alert arrives:

Payment API is returning 504 timeouts.
Database connection usage is at the limit.

IncidentMind searches its historical memory.

It may retrieve a previous incident:

Service:
Payment API
Root Cause:
Database connection-pool exhaustion
Previous Fix:
Restarted the Payment API
Result:
Failed / temporary recovery
Resolution:
Increased connection-pool capacity
and reduced connection leakage

IncidentMind can then include this historical evidence in its analysis.

The key difference is that the agent is not relying only on generic troubleshooting knowledge.

It can use the team’s own operational history.

⸻

Continuous Learning Loop

       New Production Incident
                  │
                  ▼
       Recall Similar Incidents
                  │
                  ▼
       AI Analysis & Reasoning
                  │
                  ▼
        Engineer Verification
                  │
                  ▼
          Incident Resolution
                  │
                  ▼
       Retain New Incident Data
                  │
                  ▼
          Future Incidents

Each resolved incident can therefore contribute to the system’s future knowledge.

⸻

 Operational Insights

IncidentMind can use reflection over stored incidents to identify patterns such as:

* Recurring root causes
* Repeated failure patterns
* Frequently successful fixes
* Common operational lessons
* Service-level incident patterns

This allows individual incident memories to become higher-level operational knowledge.

⸻

Setup

1. Clone the repository

git clone https://github.com/RajeswariSaladi/IncidentMind.git
cd IncidentMind

2. Create a virtual environment

Windows

python -m venv venv
venv\Scripts\activate

macOS / Linux

python3 -m venv venv
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Configure environment variables

Create a .env file in the project root using .env.example as a template.

HINDSIGHT_API_KEY=your_hindsight_api_key
HINDSIGHT_BASE_URL=https://api.hindsight.vectorize.io
GROQ_API_KEY=your_groq_api_key
LLM_MODEL=gpt-oss-120b
FALLBACK_MODEL=qwen3-32b
BANK_ID=incidentmind-team

Never commit your real API keys or .env file to GitHub.

⸻

Seed Historical Memory

Run:

python scripts/seed_incidents.py

This loads the historical incident dataset into the configured Hindsight memory bank.

⸻

 Run the Backend

From the project root:

uvicorn app.main:app --reload

The FastAPI backend will start locally.

⸻

Run the Frontend

Open another terminal while the backend is running:

streamlit run ui/app.py

The IncidentMind interface will open in your browser.

⸻

API Endpoints

GET /

Returns basic IncidentMind application information.

⸻

POST /triage

Analyzes a new production incident.

Example:

{
  "alert": "Payment API is returning 500 errors and database connections are exhausted.",
  "use_memory": true
}

⸻

POST /resolve

Stores the outcome of a resolved incident.

Example:

{
  "incident_id": "INC-LIVE-001",
  "alert": "Payment API database connection exhaustion",
  "root_cause": "Connection pool exhaustion",
  "fix_applied": "Increased pool capacity and fixed connection leakage",
  "worked": true,
  "minutes": 35,
  "lesson": "Monitor connection pool usage during traffic spikes."
}

⸻

GET /insights

Generates higher-level operational insights from stored incident memory.

⸻

 Demo Flow

1. Start the FastAPI backend
             ↓
2. Start the Streamlit UI
             ↓
3. Seed historical incidents
             ↓
4. Submit a new production alert
             ↓
5. IncidentMind recalls relevant incidents
             ↓
6. AI generates an evidence-based analysis
             ↓
7. Engineer verifies and resolves the incident
             ↓
8. Resolution is stored in memory
             ↓
9. Future incidents can use the new knowledge

⸻

 Human Verification

IncidentMind is designed as an engineering decision-support system.

AI-generated recommendations should be:

* Reviewed by an engineer
* Verified against current system conditions
* Evaluated for operational risk
* Applied only after appropriate validation

IncidentMind is specifically designed not to invent historical evidence and to distinguish historical information from AI reasoning.

⸻

 Future Roadmap

PagerDuty Integration

Automatically receive production alerts from incident-management platforms.

Slack Integration

Connect incident discussions and resolutions to the team’s operational memory.

Automatic Runbook Generation

Generate or update troubleshooting runbooks from recurring incident patterns.

Per-Engineer Preference Memory

Allow IncidentMind to remember useful engineer-specific operational preferences.

Expanded Operational Analytics

Track incident trends, recurring services, resolution times, and failure patterns.

⸻

Hackathon Concept

IncidentMind demonstrates how an AI agent can combine:

LLM Reasoning
      +
Persistent Memory
      +
Historical Evidence
      +
Outcome Tracking
      +
Reflection

The result is an incident-response system designed to learn from operational history rather than starting from zero every time.

⸻

 Project

Project: IncidentMind

Theme: AI Agents That Learn Using Hindsight

Event: HackwithHyderabad 3.0

⸻

 Disclaimer

IncidentMind is a hackathon prototype using synthetic incident data.

It demonstrates persistent-memory-based AI incident response and should not be treated as a production incident-management system without additional security, reliability, access-control, observability, and validation mechanisms.

⸻

The Vision

Every incident becomes knowledge for the next one.

IncidentMind turns incident history into reusable operational intelligence — helping teams remember what happened, what worked, what failed, and what they learned.
