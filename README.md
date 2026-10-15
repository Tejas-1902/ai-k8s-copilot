\# AI Kubernetes Copilot



An AI-assisted Kubernetes troubleshooting tool built with Python, FastAPI, Docker, and Kubernetes.



\## Features



\- Detects common Kubernetes pod failures.

\- Classifies incident severity.

\- Provides troubleshooting recommendations.

\- Generates AI-assisted incident explanations.

\- Exposes REST APIs using FastAPI.

\- Runs automated tests with pytest.

\- Builds Docker images through GitHub Actions.



\## Technology Stack



\- Python 3.12

\- FastAPI

\- Kubernetes

\- Docker

\- Minikube

\- pytest

\- GitHub Actions



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

&#x20;       +--> Incident Diagnosis

&#x20;       +--> Troubleshooting Recommendations

&#x20;       +--> AI-Assisted Explanation

&#x20;       |

&#x20;       v

JSON API Response

```



\## Supported Incidents



| Incident | Description |

|---|---|

| ImagePullBackOff | Investigates container image pull failures |

| CrashLoopBackOff | Investigates repeated container crashes |

| Unknown | Provides basic diagnostic guidance |



\## API Endpoints



| Endpoint | Method | Description |

|---|---|---|

| `/` | GET | Root endpoint |

| `/diagnose` | POST | Diagnose an incident |

| `/scan` | GET | Scan the configured Kubernetes namespace |

| `/docs` | GET | Interactive API documentation |



\## Run Locally



Clone the repository:



```bash

git clone https://github.com/Tejas-1902/ai-k8s-copilot.git

cd ai-k8s-copilot

```



Create a virtual environment:



```powershell

python -m venv .venv

.\\.venv\\Scripts\\Activate.ps1

```



Install dependencies:



```bash

python -m pip install -r requirements.txt

```



Start the API:



```bash

uvicorn main:app --reload

```



Open http://127.0.0.1:8000/docs.



\## Run with Docker



Build the image:



```bash

docker build -t ai-k8s-copilot:latest .

```



Start the container:



```bash

docker run --rm -p 8000:8000 ai-k8s-copilot:latest

```



\## Run Tests



```bash

python -m pytest -v

```



\## Continuous Integration



GitHub Actions runs automated tests and builds the Docker image when code is pushed to the `main` branch or a pull request targets `main`.



\## Future Improvements



\- Support more Kubernetes incident types.

\- Add monitoring and structured logging.

\- Publish Docker images to a container registry.

\- Add integration tests and security scanning.



\## Repository



https://github.com/Tejas-1902/ai-k8s-copilot



\---



