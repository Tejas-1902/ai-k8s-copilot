\# AI Kubernetes Copilot



An AI-assisted Kubernetes troubleshooting tool built with Python, FastAPI, Docker, and Kubernetes. The project detects common pod failures, provides troubleshooting recommendations, and generates AI-assisted explanations to help engineers investigate incidents faster.



\## Features



\- \*\*Kubernetes Diagnostics:\*\* Identifies common pod issues such as `ImagePullBackOff` and `CrashLoopBackOff`.

\- \*\*Incident Severity:\*\* Assigns severity levels to detected incidents.

\- \*\*Troubleshooting Recommendations:\*\* Provides practical diagnostic steps and commands.

\- \*\*AI-Assisted Explanations:\*\* Uses an OpenAI-compatible API to generate incident explanations.

\- \*\*FastAPI REST API:\*\* Exposes diagnostic endpoints and interactive API documentation.

\- \*\*Automated Testing:\*\* Includes pytest tests for diagnostic logic.

\- \*\*CI Pipeline:\*\* GitHub Actions runs tests and builds the Docker image.



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

| ImagePullBackOff | Helps investigate image names, tags, registry access, and pod events |

| CrashLoopBackOff | Helps investigate container logs, startup failures, configuration, and resource issues |

| Unknown | Provides basic diagnostic guidance for other pod states |



\## API Endpoints



| Endpoint | Method | Description |

|---|---|---|

| `/` | GET | Root endpoint |

| `/diagnose` | POST | Diagnose a supplied incident |

| `/scan` | GET | Scan the configured Kubernetes namespace for pod incidents |

| `/docs` | GET | Interactive FastAPI Swagger documentation |



\## Run Locally



\### 1. Clone the repository



```bash

git clone https://github.com/Tejas-1902/ai-k8s-copilot.git

cd ai-k8s-copilot

```



\### 2. Create a Python virtual environment



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



Open the interactive API documentation:



http://127.0.0.1:8000/docs



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



\*\*Note:\*\* The container needs access to a Kubernetes cluster and its configuration to perform live scans. AI explanations also depend on the configured AI service being reachable.



\## Run Automated Tests



```bash

python -m pytest -v

```



The GitHub Actions workflow runs the tests and builds the Docker image when changes are pushed to the `main` branch or a pull request targets `main`.



\## Kubernetes Testing



The project can be tested against a Kubernetes cluster such as Minikube. A sample broken workload using an invalid container image can help demonstrate the `ImagePullBackOff` diagnosis.



Use a dedicated test namespace and avoid experimenting with broken workloads in production clusters.



\## Project Goals



\- Practice Kubernetes troubleshooting and pod diagnostics.

\- Apply Python API development to DevOps workflows.

\- Build a containerized application.

\- Implement automated testing and CI with GitHub Actions.

\- Explore AI-assisted incident analysis.



\## Future Improvements



\- Add more Kubernetes failure scenarios.

\- Improve structured logging and error handling.

\- Add monitoring and metrics.

\- Publish versioned Docker images to a container registry.

\- Deploy the application to Kubernetes with read-only RBAC.

\- Add integration tests and security scanning.



\## Repository



GitHub: https://github.com/Tejas-1902/ai-k8s-copilot



