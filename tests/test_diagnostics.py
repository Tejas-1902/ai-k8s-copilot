
from main import Incident, diagnose, get_troubleshooting_checks


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


def test_image_pull_backoff_checks():
    checks = get_troubleshooting_checks("ImagePullBackOff")

    assert len(checks) == 3
    assert any("describe pod" in check for check in checks)
    assert any("image name and tag" in check for check in checks)


def test_crash_loop_backoff_checks():
    checks = get_troubleshooting_checks("CrashLoopBackOff")

    assert len(checks) == 3
    assert any("logs" in check for check in checks)


def test_unknown_incident_checks():
    checks = get_troubleshooting_checks("Unknown")

    assert len(checks) == 2
    assert any("describe pod" in check for check in checks)
