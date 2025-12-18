# Submission Guide - CI/CD Final Project

This guide will help you prepare your deliverables for submission.

## What to Submit

Based on the evaluation criteria, you need to submit the following:

### 1. GitHub Actions Workflow Execution
**Screenshots/Outputs to capture:**
- GitHub Actions workflow run status (showing successful build and test)
- Workflow logs showing:
  - Code checkout
  - Dependency installation
  - Test execution
  - Docker image build
  - Deployment to OpenShift (if applicable)

**How to capture:**
1. Go to your GitHub repository
2. Click on "Actions" tab
3. Select a workflow run
4. Take screenshots of:
   - Overall workflow status (green checkmarks)
   - Individual job outputs
   - Any error messages (if troubleshooting)

### 2. Tekton Pipeline Execution
**Terminal outputs to capture:**
- Tekton pipeline run status
- Task execution logs
- Pipeline completion status

**Commands to run:**
```bash
# Apply Tekton resources
oc apply -f [javascript-lab|python-lab]/tekton/

# Create and run pipeline
oc create -f [javascript-lab|python-lab]/tekton/pipeline-run.yaml

# Check pipeline status
oc get pipelinerun

# View pipeline logs
oc logs -f pipelinerun/ci-cd-pipeline-run

# Get detailed task logs
oc get taskrun
oc logs taskrun/<task-run-name>
```

**Save outputs:**
- Copy terminal output showing pipeline execution
- Screenshot of OpenShift console showing Tekton pipeline status
- Logs from each task (test, build, deploy)

### 3. OpenShift Deployment
**URLs and outputs to capture:**
- Application route URL
- Deployment status
- Pod status

**Commands to run:**
```bash
# Apply OpenShift resources
oc apply -f [javascript-lab|python-lab]/openshift/

# Check deployment status
oc get deployment
oc get pods
oc get service
oc get route

# Get application URL
oc get route [ci-cd-javascript-app|ci-cd-python-app] -o jsonpath='{.spec.host}'

# Test the application
curl https://<route-url>/health
curl https://<route-url>/
curl https://<route-url>/api/info
```

**Save outputs:**
- Application route URL (screenshot or copy)
- Terminal output showing successful deployment
- curl command outputs showing application responses

### 4. Complete Pipeline Flow
**Documentation to create:**
- Step-by-step execution log
- Screenshots showing the complete flow:
  1. Code push to GitHub
  2. GitHub Actions triggered
  3. Tekton pipeline execution
  4. OpenShift deployment
  5. Application accessible via route

## Submission Checklist

Before submitting, ensure you have:

- [ ] GitHub Actions workflow execution screenshots/logs
- [ ] Tekton pipeline run terminal outputs
- [ ] Tekton task execution logs
- [ ] OpenShift deployment status screenshots
- [ ] Application route URL
- [ ] Application health check responses
- [ ] Complete pipeline flow documentation

## Formatting Your Submission

### Option 1: AI-Graded Submission
- Upload screenshots as images (PNG, JPG)
- Paste terminal outputs as text
- Include URLs as clickable links
- Organize deliverables clearly

### Option 2: Peer-Graded Submission
- Create a document (PDF, Markdown, or text file) with:
  - Screenshots embedded or attached
  - Terminal outputs formatted as code blocks
  - URLs clearly labeled
  - Step-by-step walkthrough

## Troubleshooting Tips

### GitHub Actions Issues
- Check repository secrets are configured
- Verify workflow file syntax
- Check branch names match workflow triggers

### Tekton Issues
- Verify Tekton is installed: `oc get pods -n tekton-pipelines`
- Check task definitions are correct
- Verify image registry access

### OpenShift Issues
- Verify you're logged in: `oc whoami`
- Check namespace exists: `oc get namespace`
- Verify resource quotas: `oc describe quota`

## Example Submission Structure

```
Submission/
├── 1-github-actions/
│   ├── workflow-status.png
│   ├── build-job-logs.txt
│   └── deploy-job-logs.txt
├── 2-tekton-pipeline/
│   ├── pipeline-run-output.txt
│   ├── task-logs.txt
│   └── pipeline-status.png
├── 3-openshift-deployment/
│   ├── deployment-status.txt
│   ├── route-url.txt
│   └── app-test-output.txt
└── README.md (summary document)
```

## Quick Reference Commands

### JavaScript Lab
```bash
cd javascript-lab
oc apply -f tekton/
oc create -f tekton/pipeline-run.yaml
oc apply -f openshift/
```

### Python Lab
```bash
cd python-lab
oc apply -f tekton/
oc create -f tekton/pipeline-run.yaml
oc apply -f openshift/
```

Good luck with your submission!

