# AI Kubernetes Copilot

An AI-assisted Kubernetes troubleshooting tool built with Python, FastAPI, Docker, and Kubernetes. It identifies common pod failures, provides troubleshooting recommendations, and generates AI-assisted explanations to help engineers investigate incidents.

## Features

- **Kubernetes Diagnostics:** Detects common pod issues such as `ImagePullBackOff` and `CrashLoopBackOff`.
- **Incident Severity:** Assigns severity levels to detected incidents.
- **Troubleshooting Recommendations:** Provides practical diagnostic steps and commands.
- **AI-Assisted Explanations:** Generates incident explanations using an OpenAI-compatible API.
- **FastAPI REST API:** Provides diagnostic endpoints and interactive API documentation.
- **Automated Testing:** Uses pytest to test diagnostic logic.
- **Continuous Integration:** GitHub Actions runs automated tests and builds the Docker image.

## Architecture

```text
Kubernetes Cluster
        |
        v
Kubernetes Client
        |
        v
FastAPI Application
        |
        +--> Incident Diagnosis
        |
        +--> Troubleshooting Recommendations
        |
        +--> AI-Assisted Explanation
        |
        v
JSON API Response
```

## Technology Stack

- Python 3.12
- FastAPI
- Kubernetes Python Client
- Docker
- Minikube
- pytest
- GitHub Actions
- Docker Model Runner / OpenAI-compatible API

## Supported Incidents

| Incident | Description |
|---|---|
| `ImagePullBackOff` | Investigates image names, tags, registry access, and pod events |
| `CrashLoopBackOff` | Investigates container logs, startup failures, configuration, and resource issues |
| `Unknown` | Provides basic diagnostic guidance for other pod states |

## API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Root endpoint |
| `/diagnose` | POST | Diagnoses a supplied incident |
| `/scan` | GET | Scans the configured Kubernetes namespace for pod incidents |
| `/docs` | GET | Interactive FastAPI Swagger documentation |

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Tejas-1902/ai-k8s-copilot.git
cd ai-k8s-copilot
```

### 2. Create a Python virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Start the API

```bash
uvicorn main:app --reload
```

Open the interactive API documentation:

http://127.0.0.1:8000/docs

**Note:** Live Kubernetes scans require access to a configured Kubernetes cluster. AI explanations require the configured AI service to be reachable.

## Run with Docker

### Build the Docker image

```bash
docker build -t ai-k8s-copilot:latest .
```

### Run the container

```bash
docker run --rm -p 8000:8000 ai-k8s-copilot:latest
```

Open the API documentation:

http://localhost:8000/docs

## Run Automated Tests

Run the test suite:

```bash
python -m pytest -v
```

The GitHub Actions workflow runs the tests and builds the Docker image on pushes to the `main` branch and pull requests targeting `main`.

## Kubernetes Testing

The project can be tested using Minikube. A sample workload with an invalid container image can demonstrate `ImagePullBackOff` detection.

Use a dedicated test namespace and avoid introducing broken workloads into production clusters.

## Future Improvements

- Support additional Kubernetes incident types.
- Improve structured logging and error handling.
- Add monitoring and metrics.
- Publish versioned Docker images to a container registry.
- Deploy the application with read-only Kubernetes RBAC.
- Add integration tests and security scanning.

## Skills Demonstrated

- Linux and Kubernetes troubleshooting concepts
- Python REST API development
- Containerization with Docker
- Automated testing with pytest
- CI pipeline development with GitHub Actions
- AI-assisted incident analysis

## Repository

[AI Kubernetes Copilot on GitHub](https://github.com/Tejas-1902/ai-k8s-copilot)

---

**Disclaimer:** This project is for learning and demonstration. Verify AI-generated explanations against actual Kubernetes events, logs, and configuration before taking action.