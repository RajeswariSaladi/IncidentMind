from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.agent import triage_incident, resolve_incident
from app.memory import reflect_on_incidents


app = FastAPI(
    title="IncidentMind API",
    description="AI-powered incident response with persistent operational memory",
    version="1.0.0",
)


class TriageRequest(BaseModel):
    alert: str
    use_memory: bool = True


class ResolveRequest(BaseModel):
    incident_id: str
    alert: str
    root_cause: str
    fix_applied: str
    worked: bool
    minutes: int
    lesson: str = ""


@app.get("/")
def root():
    return {
        "name": "IncidentMind",
        "status": "running",
        "description": "AI incident-response agent with persistent memory",
    }


@app.post("/triage")
def triage(request: TriageRequest):
    if not request.alert.strip():
        raise HTTPException(
            status_code=400,
            detail="Alert cannot be empty.",
        )

    try:
        result = triage_incident(
            alert=request.alert,
            use_memory=request.use_memory,
        )

        memories = []

        for memory in result["memories"]:
            memories.append({
                "text": getattr(memory, "text", str(memory)),
                "type": getattr(memory, "type", "unknown"),
            })

        return {
            "answer": result["answer"],
            "memories": memories,
            "memory_enabled": request.use_memory,
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Incident analysis failed: {error}",
        )


@app.post("/resolve")
def resolve(request: ResolveRequest):
    try:
        result = resolve_incident(
            incident_id=request.incident_id,
            alert=request.alert,
            root_cause=request.root_cause,
            fix_applied=request.fix_applied,
            worked=request.worked,
            minutes=request.minutes,
            lesson=request.lesson,
        )

        return {
            "status": "stored",
            "incident_id": request.incident_id,
            "outcome": "WORKED" if request.worked else "FAILED",
            "memory_result": str(result),
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to store incident outcome: {error}",
        )


@app.get("/insights")
def insights():
    try:
        response = reflect_on_incidents(
            "What recurring root causes, failure patterns, "
            "successful fixes, and operational lessons can be "
            "identified across the team's past incidents?"
        )

        return {
            "insights": getattr(response, "text", str(response)),
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate insights: {error}",
        )
