# CI/CD Final Project

This project demonstrates a complete CI/CD pipeline setup using GitHub Actions, Tekton, and OpenShift.

## Project Structure

```
.
├── javascript-lab/          # JavaScript lab option
│   ├── app/                 # Sample JavaScript application
│   ├── .github/workflows/   # GitHub Actions workflows
│   ├── tekton/              # Tekton pipeline definitions
│   └── openshift/           # OpenShift deployment configs
├── python-lab/              # Python lab option
│   ├── app/                 # Sample Python application
│   ├── .github/workflows/   # GitHub Actions workflows
│   ├── tekton/              # Tekton pipeline definitions
│   └── openshift/           # OpenShift deployment configs
└── README.md                # This file
```

## Lab Options

### Option 1: JavaScript Lab
A Node.js application with Express.js framework.

### Option 2: Python Lab
A Python Flask application.

## Prerequisites

- GitHub account
- Access to OpenShift Cluster
- Tekton installed on OpenShift
- Docker (for local testing)
- Node.js (for JavaScript lab)
- Python 3.8+ (for Python lab)

## Setup Instructions

### 1. Choose Your Lab Option
Navigate to either `javascript-lab/` or `python-lab/` directory.

### 2. GitHub Actions Setup
- Workflows are located in `.github/workflows/`
- Configure GitHub secrets for:
  - `OPENSHIFT_SERVER_URL`
  - `OPENSHIFT_TOKEN`
  - `DOCKER_REGISTRY`

### 3. Tekton Pipeline Setup
- Apply Tekton resources from `tekton/` directory:
  ```bash
  kubectl apply -f tekton/
  ```

### 4. OpenShift Deployment
- Apply OpenShift resources from `openshift/` directory:
  ```bash
  oc apply -f openshift/
  ```

## Evaluation Criteria

Your submission should include:
1. GitHub Actions workflow execution screenshots
2. Tekton pipeline run outputs
3. OpenShift deployment URLs
4. Terminal outputs showing successful pipeline execution

## Next Steps

1. Review the lab-specific README in your chosen lab directory
2. Follow the step-by-step instructions
3. Save all outputs as required by the review criteria
4. Submit your deliverables via Option 1 (AI-Graded) or Option 2 (Peer-Graded)

