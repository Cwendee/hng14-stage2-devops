# hng14-stage2-devops

## 🚀 DevOps CI/CD Pipeline Project

This project demonstrates the design and implementation of a complete CI/CD pipeline for a containerized application using FastAPI, Redis, and a background worker.

It covers the full lifecycle of modern DevOps workflows including linting, testing, containerization, security scanning, integration testing, and deployment.

## 📌 Project Overview

The system consists of:

API (FastAPI) – Accepts job requests and tracks status
Worker – Processes jobs asynchronously from a Redis queue
Redis – Acts as the message broker

The pipeline ensures that every change is validated, tested, secured, and deployable.

## 🏗️ Architecture

'''text

Client → FastAPI → Redis Queue → Worker
   ↑                ↓
   |         Redis (Job Status)
   |__________________________|
        (status check via API)
        
'''text


## ⚙️ Tech Stack
- Python 3.11
- FastAPI
- Redis
- Docker & Docker Compose
- GitHub Actions (CI/CD)
- Trivy (Security scanning)
- Pytest (Testing)
- Flake8 & ESLint (Linting)

## 🔄 CI/CD Pipeline Stages

The pipeline is implemented using GitHub Actions and includes:

1. Linting
Python code checked with flake8
Frontend checked with eslint
Dockerfiles checked with hadolint

2. Testing
Unit tests written with pytest
Redis is mocked to isolate logic
Ensures API behaves correctly

3. Build
Docker images built for:
API
Worker
Images tagged with:
latest
Git commit SHA
Pushed to local registry

4. Security Scan
Images scanned using Trivy
Pipeline fails on CRITICAL vulnerabilities

5. Integration Test
Full system started with Docker Compose
API is called to create a job
Worker processes the job
Pipeline verifies job status becomes completed

6. Deployment
Simulated rolling update using Docker Compose
Services updated without restarting the entire system

🧪 API Endpoints
Create Job
'''bash
POST /jobs

Response:

'''bash
{
  "job_id": "uuid"
}


Get Job Status

'''bash
GET /jobs/{job_id}

Response:

'''bash
{
  "job_id": "uuid",
  "status": "completed"
}


▶️ Running Locally
1. Clone the repository

'''bash
git clone <your-repo-url>
cd <repo-name>

2. Start services

'''bash
docker compose up --build


3. Access API docs

'''bash
http://localhost:8000/docs


4. Test the flow
- Create a job via Swagger UI
- Check job status after a few seconds


## 🧾 Key Design Decisions
- Redis used as queue for simplicity and reliability
- Worker separated from API for scalability
- Mocking in tests ensures fast and isolated unit tests
- Docker used throughout for consistency across environments
- Pipeline enforces quality before deployment


## 🛠️ Fixes & Debugging

Key issues encountered and resolved are documented in:

'''bash
FIXES.md

This includes:

- Dependency issues
- Docker configuration problems
- CI pipeline errors
- Linting and formatting fixes


## 🎯 What This Project Demonstrates
- End-to-end CI/CD pipeline design
- Container-based application deployment
- Automated testing and validation
- Security-first development approach
-  Real-world DevOps troubleshooting


## 📈 Future Improvements
- Push images to Docker Hub or a cloud registry
- Add environment-based deployments (staging/production)
- Introduce monitoring and logging (Prometheus/Grafana)
- Add caching to CI pipeline for speed

## 👤 Author

- Prudence Anumudu

## ✅ Status

✔️ Complete
✔️ Fully automated pipeline
✔️ Production-style workflow implemented
