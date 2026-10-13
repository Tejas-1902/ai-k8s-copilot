
from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException


def get_pod_diagnostics(namespace: str = "ai-copilot-lab"):
    try:
        config.load_kube_config()
        v1 = client.CoreV1Api()

        pods = v1.list_namespaced_pod(namespace=namespace)
        results = []

        for pod in pods.items:
            container_statuses = pod.status.container_statuses or []

            for container in container_statuses:
                waiting = container.state.waiting

                if waiting and waiting.reason:
                    reason = waiting.reason

                    results.append({
                        "pod_name": pod.metadata.name,
                        "namespace": namespace,
                        "pod_phase": pod.status.phase,
                        "container": container.name,
                        "image": container.image,
                        "reason": reason,
                        "message": waiting.message or "",
                    })

        return results

    except ConfigException as exc:
        return {"error": f"Kubernetes configuration error: {exc}"}
    except Exception as exc:
        return {"error": f"Unable to query Kubernetes: {exc}"}


if __name__ == "__main__":
    import json
    print(json.dumps(get_pod_diagnostics(), indent=2))
