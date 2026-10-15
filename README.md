\# AI Kubernetes Copilot



An AI-assisted Kubernetes troubleshooting tool built with Python, FastAPI, Docker, and Kubernetes. It detects common pod failures, provides troubleshooting recommendations, and generates AI-assisted explanations to help engineers investigate incidents.



\## Features



\- \*\*Kubernetes Diagnostics:\*\* Identifies common pod issues such as `ImagePullBackOff` and `CrashLoopBackOff`.

\- \*\*Incident Severity:\*\* Assigns severity levels to detected incidents.

\- \*\*Troubleshooting Recommendations:\*\* Provides practical diagnostic steps and commands.

\- \*\*AI-Assisted Explanations:\*\* Generates incident explanations using an OpenAI-compatible API.

\- \*\*FastAPI REST API:\*\* Provides diagnostic endpoints and interactive API documentation.

\- \*\*Automated Testing:\*\* Includes pytest tests for diagnostic logic.

\- \*\*Continuous Integration:\*\* GitHub Actions runs tests and builds the Docker image.



\## Architecture



```text

Kubernetes Cluster

&#x20;       |

&#x20;       v

Kubernetes Client

&#x20;       |

&#x20;       v

FastAPI Application

&#x20;       |

&#x20;       +----> Incident Diagnosis

&#x20;       |

&#x20;       +----> Troubleshooting Recommendations

&#x20;       |

&#x20;       +----> AI-Assisted Explanation

&#x20;       |

&#x20;       v

JSON API Response

```



\## Technology Stack



\- Python 3.12

\- FastAPI

\- Kubernetes Python Client

\- Docker

\- Minikube

\- pytest

\- GitHub Actions

\- Docker Model Runner / OpenAI-compatible API



\## Supported Incidents



| Incident | Purpose |

|---|---|

| `ImagePullBackOff` | Investigates image names, tags, registry access, and pod events |

| `CrashLoopBackOff` | Investigates container logs, startup failures, configuration, and resource issues |

| `Unknown` | Provides basic diagnostic guidance for other pod states |



\## API Endpoints



| Endpoint | Method | Description |

|---|---|---|

| `/` | GET | Root endpoint |

| `/diagnose` | POST | Diagnoses a supplied incident |

| `/scan` | GET | Scans the configured Kubernetes namespace for pod incidents |

| `/docs` | GET | Interactive FastAPI Swagger documentation |



\## Getting Started



\### 1. Clone the repository



```bash

git clone https://github.com/Tejas-1902/ai-k8s-copilot.git

cd ai-k8s-copilot

```



\### 2. Create a virtual environment



Windows PowerShell:



```powershell

python -m venv .venv

.\\.venv\\Scripts\\Activate.ps1

```



\### 3. Install dependencies



```bash

python -m pip install -r requirements.txt

```



\### 4. Start the API



```bash

uvicorn main:app --reload

```



Open the API documentation at http://127.0.0.1:8000/docs.



\## Run with Docker



Build the image:



```bash

docker build -t ai-k8s-copilot:latest .

```



Run the container:



```bash

docker run --rm -p 8000:8000 ai-k8s-copilot:latest

```



Open http://localhost:8000/docs.



\*\*Note:\*\* Live Kubernetes scans require access to a configured Kubernetes cluster. AI explanations require the configured AI service to be reachable.



\## Run Automated Tests



```bash

python -m pytest -v

```



GitHub Actions automatically runs tests and builds the Docker image on pushes to `main` and pull requests targeting `main`.



\## Kubernetes Testing



The project can be tested with Minikube. A sample workload using an invalid container image can demonstrate `ImagePullBackOff` detection.



Use a dedicated test namespace and avoid introducing broken workloads into production clusters.



\## Future Improvements



\- Detect additional Kubernetes failure scenarios.

\- Add structured logging and monitoring.

\- Publish versioned Docker images to a container registry.

\- Deploy the application with read-only Kubernetes RBAC.

\- Add integration tests and security scanning.



\## Repository



\[View AI Kubernetes Copilot on GitHub](https://github.com/Tejas-1902/ai-k8s-copilot)



\---



