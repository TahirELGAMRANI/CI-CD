# JavaScript Lab - CI/CD Pipeline

This directory contains the JavaScript lab option for the CI/CD final project.

## Application Overview

A simple Node.js Express application that serves a REST API.

## Project Structure

```
javascript-lab/
├── app/                     # Application source code
│   ├── src/
│   ├── package.json
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
npm install
```

### 2. Test Locally
```bash
npm start
# Application runs on http://localhost:3000
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

