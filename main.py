
from fastapi import FastAPI
from pydantic import BaseModel

from k8s_client import get_pod_diagnostics
from ai_diagnosis import explain_incident


app = FastAPI(
    title="AI Kubernetes Copilot",
    description="Kubernetes incident diagnosis API",
    version="0.1.0",
)


class Incident(BaseModel):
    pod_name: str
    namespace: str = "default"
    status: str
    image: str = ""
    events: str = ""


def get_troubleshooting_checks(incident_type: str) -> list[str]:
    """Return safe troubleshooting checks for a known incident type."""

    if incident_type == "ImagePullBackOff":
        return [
            "Run kubectl describe pod <pod-name> -n <namespace> and inspect Events.",
            "Verify the image name and tag in the pod specification.",
            "Check registry connectivity and image pull credentials if Events indicate an authentication or network error.",
        ]

    if incident_type == "CrashLoopBackOff":
        return [
            "Run kubectl describe pod <pod-name> -n <namespace> and inspect Events.",
            "Run kubectl logs <pod-name> -n <namespace> --previous to inspect the previous container crash.",
            "Review startup errors, configuration, resource limits, and health probes.",
        ]

    return [
        "Run kubectl describe pod <pod-name> -n <namespace> to inspect Events.",
        "Run kubectl logs <pod-name> -n <namespace> to inspect container output.",
    ]


def diagnose(incident: Incident) -> dict:
    """Identify common Kubernetes incidents using rule-based diagnosis."""

    evidence = f"{incident.status} {incident.events}".lower()

    if (
        "errimagepull" in evidence
        or "imagepullbackoff" in evidence
        or "manifest unknown" in evidence
    ):
        return {
            "incident": "ImagePullBackOff",
            "severity": "Medium",
            "probable_cause": (
                "The container image or tag may not exist, "
                "or the registry cannot be accessed."
            ),
            "evidence": incident.image or incident.events,
            "recommended_actions": [
                "Verify the image name and tag.",
                "Check registry access and image pull credentials.",
                "Confirm the cause from pod Events before changing the deployment.",
            ],
        }

    if "crashloopbackoff" in evidence:
        return {
            "incident": "CrashLoopBackOff",
            "severity": "High",
            "probable_cause": (
                "The container repeatedly exits after starting."
            ),
            "evidence": incident.events or incident.status,
            "recommended_actions": [
                "Inspect current and previous container logs.",
                "Check application configuration and startup errors.",
                "Review resource limits and health probes.",
            ],
        }

    return {
        "incident": "Unknown",
        "severity": "Needs investigation",
        "probable_cause": "No matching diagnostic rule was found.",
        "evidence": incident.events or incident.status,
        "recommended_actions": [
            "Inspect pod events and container logs.",
            "Check pod status, configuration, and resource usage.",
        ],
    }


@app.get("/")
def home():
    return {
        "message": "AI Kubernetes Copilot is running",
        "version": "0.1.0",
    }


@app.post("/diagnose")
def diagnose_incident(incident: Incident):
    result = diagnose(incident)
    result["pod_name"] = incident.pod_name
    result["namespace"] = incident.namespace
    result["troubleshooting_checks"] = get_troubleshooting_checks(
        result["incident"]
    )
    return result


@app.get("/scan")
def scan_kubernetes():
    diagnostics = get_pod_diagnostics("ai-copilot-lab")

    if isinstance(diagnostics, dict) and "error" in diagnostics:
        return diagnostics

    reports = []

    for item in diagnostics:
        incident = Incident(
            pod_name=item["pod_name"],
            namespace=item["namespace"],
            status=item["reason"],
            image=item["image"],
            events=item["message"],
        )

        report = diagnose(incident)

        report.update(
            {
                "pod_name": item["pod_name"],
                "namespace": item["namespace"],
                "pod_phase": item["pod_phase"],
                "container": item["container"],
                "image": item["image"],
                "troubleshooting_checks": get_troubleshooting_checks(
                    report["incident"]
                ),
            }
        )

        report["ai_explanation"] = explain_incident(
            {
                "pod_name": incident.pod_name,
                "namespace": incident.namespace,
                "status": incident.status,
                "image": incident.image,
                "events": incident.events,
                "rule_based_diagnosis": report,
            }
        )

        reports.append(report)

    return {
        "namespace": "ai-copilot-lab",
        "incidents_found": len(reports),
        "incidents": reports,
    }
