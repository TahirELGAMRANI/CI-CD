# Project Structure

Complete CI/CD pipeline project with both JavaScript and Python lab options.

```
CI CD/
│
├── README.md                    # Main project overview
├── QUICK_START.md               # Quick start guide
├── SUBMISSION_GUIDE.md          # Submission instructions
├── PROJECT_STRUCTURE.md         # This file
├── .gitignore                   # Git ignore rules
│
├── javascript-lab/              # JavaScript Lab Option
│   ├── README.md                # JavaScript lab specific guide
│   │
│   ├── app/                     # Application source code
│   │   ├── src/
│   │   │   ├── index.js         # Main application file
│   │   │   └── index.test.js    # Test file
│   │   ├── Dockerfile           # Docker build instructions
│   │   ├── .dockerignore        # Docker ignore rules
│   │   ├── package.json         # Node.js dependencies
│   │   ├── package-lock.json    # Locked dependencies
│   │   └── jest.config.js       # Jest test configuration
│   │
│   ├── .github/
│   │   └── workflows/
│   │       └── ci-cd.yml        # GitHub Actions workflow
│   │
│   ├── tekton/                  # Tekton pipeline definitions
│   │   ├── tasks.yaml           # Tekton tasks (build, test, deploy)
│   │   ├── pipeline.yaml        # Tekton pipeline definition
│   │   └── pipeline-run.yaml    # Pipeline run configuration
│   │
│   └── openshift/               # OpenShift deployment configs
│       ├── deployment.yaml      # Deployment resource
│       ├── service.yaml         # Service resource
│       └── route.yaml           # Route resource
│
└── python-lab/                  # Python Lab Option
    ├── README.md                # Python lab specific guide
    │
    ├── app/                     # Application source code
    │   ├── src/
    │   │   ├── app.py           # Main application file
    │   │   └── test_app.py      # Test file
    │   ├── Dockerfile           # Docker build instructions
    │   ├── .dockerignore        # Docker ignore rules
    │   ├── requirements.txt     # Python dependencies
    │   └── requirements-dev.txt # Development dependencies
    │
    ├── .github/
    │   └── workflows/
    │       └── ci-cd.yml        # GitHub Actions workflow
    │
    ├── tekton/                  # Tekton pipeline definitions
    │   ├── tasks.yaml           # Tekton tasks (build, test, deploy)
    │   ├── pipeline.yaml        # Tekton pipeline definition
    │   └── pipeline-run.yaml    # Pipeline run configuration
    │
    └── openshift/               # OpenShift deployment configs
        ├── deployment.yaml      # Deployment resource
        ├── service.yaml         # Service resource
        └── route.yaml           # Route resource
```

## Key Components

### Applications
- **JavaScript Lab**: Node.js Express application with REST API endpoints
- **Python Lab**: Python Flask application with REST API endpoints

### CI/CD Components
1. **GitHub Actions**: Automated build, test, and deployment workflows
2. **Tekton**: Kubernetes-native CI/CD pipeline tasks
3. **OpenShift**: Container platform deployment configurations

### Application Features
Both applications include:
- Health check endpoint (`/health`)
- Root endpoint (`/`)
- API info endpoint (`/api/info`)
- Docker containerization
- Unit tests
- Production-ready configuration

## File Descriptions

### Application Files
- `index.js` / `app.py`: Main application entry point
- `*.test.js` / `test_*.py`: Unit test files
- `Dockerfile`: Container build instructions
- `package.json` / `requirements.txt`: Dependencies

### CI/CD Files
- `.github/workflows/ci-cd.yml`: GitHub Actions workflow definition
- `tekton/tasks.yaml`: Individual Tekton task definitions
- `tekton/pipeline.yaml`: Tekton pipeline orchestration
- `tekton/pipeline-run.yaml`: Pipeline execution configuration

### Deployment Files
- `openshift/deployment.yaml`: Kubernetes Deployment resource
- `openshift/service.yaml`: Kubernetes Service resource
- `openshift/route.yaml`: OpenShift Route for external access

## Usage

1. Choose your lab option (JavaScript or Python)
2. Follow the README in the chosen lab directory
3. Set up GitHub Actions with required secrets
4. Deploy Tekton pipelines to OpenShift
5. Deploy application using OpenShift configurations
6. Capture outputs for submission (see SUBMISSION_GUIDE.md)

