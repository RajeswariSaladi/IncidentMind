import json
from pathlib import Path


OUTPUT_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "incidents.json"
)


INCIDENTS = [
    {
        "id": "INC-001",
        "service": "payment-api",
        "severity": "SEV-1",
        "timestamp": "2026-01-12T09:15:00",
        "alert": "Payment API returning 500 errors. Database connection pool exhausted.",
        "root_cause": "Database connection leak caused connections to remain open.",
        "fix": "Restarted payment service and fixed connection handling.",
        "outcome": "WORKED",
        "lesson": "Check database connection usage when payment API shows repeated 500 errors."
    },
    {
        "id": "INC-002",
        "service": "payment-api",
        "severity": "SEV-2",
        "timestamp": "2026-01-19T14:30:00",
        "alert": "Payment requests timing out during peak traffic.",
        "root_cause": "Database connection pool reached its configured limit.",
        "fix": "Increased connection pool temporarily.",
        "outcome": "WORKED",
        "lesson": "Connection pool saturation can appear as payment request timeouts."
    },
    {
        "id": "INC-003",
        "service": "user-api",
        "severity": "SEV-2",
        "timestamp": "2026-02-03T11:10:00",
        "alert": "User profile requests returning 503 errors.",
        "root_cause": "User service pods were repeatedly restarting because of memory pressure.",
        "fix": "Increased pod memory limit and restarted affected pods.",
        "outcome": "WORKED",
        "lesson": "Check pod memory usage before changing application logic."
    },
    {
        "id": "INC-004",
        "service": "orders-api",
        "severity": "SEV-1",
        "timestamp": "2026-02-10T16:45:00",
        "alert": "Order creation failing with database timeout errors.",
        "root_cause": "Database CPU usage reached saturation.",
        "fix": "Reduced expensive queries and scaled database resources.",
        "outcome": "WORKED",
        "lesson": "Database saturation should be checked before restarting the application."
    },
    {
        "id": "INC-005",
        "service": "notification-service",
        "severity": "SEV-3",
        "timestamp": "2026-02-18T10:20:00",
        "alert": "Email notifications delayed by more than 20 minutes.",
        "root_cause": "Message queue contained a large backlog.",
        "fix": "Increased consumer workers and processed the backlog.",
        "outcome": "WORKED",
        "lesson": "Inspect queue depth when notification delivery is delayed."
    },
    {
        "id": "INC-006",
        "service": "payment-api",
        "severity": "SEV-1",
        "timestamp": "2026-02-24T13:05:00",
        "alert": "Payment API latency increased significantly.",
        "root_cause": "A slow database query caused request threads to remain occupied.",
        "fix": "Added an index and optimized the query.",
        "outcome": "WORKED",
        "lesson": "Slow database queries can cause application-wide latency."
    },
    {
        "id": "INC-007",
        "service": "search-service",
        "severity": "SEV-2",
        "timestamp": "2026-03-02T09:40:00",
        "alert": "Product searches returning incomplete results.",
        "root_cause": "Search index synchronization failed.",
        "fix": "Rebuilt the affected search index.",
        "outcome": "WORKED",
        "lesson": "Check index synchronization status when search results look incomplete."
    },
    {
        "id": "INC-008",
        "service": "orders-api",
        "severity": "SEV-2",
        "timestamp": "2026-03-09T15:25:00",
        "alert": "Order API returning intermittent 502 errors.",
        "root_cause": "One unhealthy application instance was receiving traffic.",
        "fix": "Removed unhealthy instance from the load balancer.",
        "outcome": "WORKED",
        "lesson": "Check individual instances when errors are intermittent."
    },
    {
        "id": "INC-009",
        "service": "user-api",
        "severity": "SEV-2",
        "timestamp": "2026-03-15T12:00:00",
        "alert": "Authentication requests becoming slow.",
        "root_cause": "Cache hit rate dropped after a configuration change.",
        "fix": "Restored cache configuration.",
        "outcome": "WORKED",
        "lesson": "Configuration changes can unexpectedly reduce cache effectiveness."
    },
    {
        "id": "INC-010",
        "service": "notification-service",
        "severity": "SEV-2",
        "timestamp": "2026-03-22T18:10:00",
        "alert": "Notification delivery failures increased.",
        "root_cause": "Third-party email provider rejected requests because of rate limits.",
        "fix": "Reduced request rate and enabled retry backoff.",
        "outcome": "WORKED",
        "lesson": "External provider rate limits require controlled retries."
    }
]


def generate_incidents():
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        json.dump(INCIDENTS, file, indent=4)

    print(f"Generated {len(INCIDENTS)} incidents.")
    print(f"Saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    generate_incidents()
