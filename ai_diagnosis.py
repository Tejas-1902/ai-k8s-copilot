
from openai import OpenAI
import json

client = OpenAI(
    base_url="http://localhost:12434/engines/v1",
    api_key="not-needed",
    timeout=60.0,
)

MODEL = "docker.io/ai/smollm2:360M-Q4_K_M"


def explain_incident(incident: dict) -> str:
    evidence = {
        "pod_name": incident.get("pod_name"),
        "namespace": incident.get("namespace"),
        "status": incident.get("status"),
        "image": incident.get("image"),
        "events": incident.get("events"),
        "rule_based_diagnosis": incident.get("rule_based_diagnosis"),
    }

    prompt = f"""
You are a cautious Kubernetes troubleshooting assistant.

Analyze this incident using only the supplied evidence:
{json.dumps(evidence, indent=2)}

Follow these rules:
1. Explain the problem in 1-2 simple sentences.
2. Identify the likely cause, but do not claim it is confirmed.
3. Give exactly 3 safe, read-only troubleshooting checks.
4. Use commands such as kubectl describe pod and kubectl get events.
5. Do not invent event messages, errors, or root causes.
6. Do not suggest deleting resources or changing deployments.
7. If evidence is insufficient, explicitly say what is missing.
8. Keep the complete answer under 120 words.

Format:
Explanation:
Likely cause:
Safe checks:
- Check 1
- Check 2
- Check 3
"""

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You provide concise Kubernetes incident explanations. "
                        "Never invent evidence or execute commands."
                    ),
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.1,
            max_tokens=180,
        )

        answer = response.choices[0].message.content
        return answer.strip() if answer else "AI returned an empty explanation."

    except Exception as exc:
        return (
            f"AI explanation unavailable: {type(exc).__name__}. "
            "Check Docker Model Runner."
        )
