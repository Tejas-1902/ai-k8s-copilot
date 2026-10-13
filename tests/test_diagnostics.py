
from main import Incident, diagnose


def test_image_pull_backoff():
    incident = Incident(
        pod_name="broken-demo",
        namespace="ai-copilot-lab",
        status="ErrImagePull ImagePullBackOff",
        image="nginx:does-not-exist",
        events="manifest unknown",
    )

    result = diagnose(incident)

    assert result["incident"] == "ImagePullBackOff"
    assert result["severity"] == "Medium"
    assert len(result["recommended_actions"]) > 0


def test_crash_loop_backoff():
    incident = Incident(
        pod_name="crashing-demo",
        namespace="ai-copilot-lab",
        status="CrashLoopBackOff",
    )

    result = diagnose(incident)

    assert result["incident"] == "CrashLoopBackOff"
    assert result["severity"] == "High"


def test_unknown_incident():
    incident = Incident(
        pod_name="unknown-demo",
        namespace="ai-copilot-lab",
        status="UnknownState",
    )

    result = diagnose(incident)

    assert result["incident"] == "Unknown"
    assert result["recommended_actions"]
