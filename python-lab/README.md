# Python Lab - CI/CD Pipeline

This directory contains the Python lab option for the CI/CD final project.

## Application Overview

A simple Python Flask application that serves a REST API.

## Project Structure

```
python-lab/
├── app/                     # Application source code
│   ├── src/
│   ├── requirements.txt
│   └── Dockerfile
├── .github/workflows/       # GitHub Actions workflows
│   └── ci-cd.yml
├── tekton/                  # Tekton pipeline definitions
│   ├── pipeline.yaml
│   ├── tasks.yaml
│   └── pipeline-run.yaml
└── openshift/               # OpenShift configurations
    ├── deployment.yaml
    ├── service.yaml
    └── route.yaml
```

## Setup Steps

### 1. Install Dependencies
```bash
cd app
pip install -r requirements.txt
```

### 2. Test Locally
```bash
python src/app.py
# Application runs on http://localhost:5000
```

### 3. Build Docker Image
```bash
docker build -t my-app:latest .
```

### 4. Configure GitHub Actions
- Add secrets in GitHub repository settings
- Push code to trigger workflow

### 5. Deploy Tekton Pipeline
```bash
oc apply -f tekton/
```

### 6. Run Pipeline
```bash
oc create -f tekton/pipeline-run.yaml
```

## Verification

- Check GitHub Actions workflow status
- Verify Tekton pipeline execution
- Access application via OpenShift route

