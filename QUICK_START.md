# Quick Start Guide

This guide will help you get started quickly with the CI/CD pipeline project.

## Prerequisites Check

Before starting, ensure you have:

```bash
# Check Node.js (for JavaScript lab)
node --version  # Should be v18 or higher

# Check Python (for Python lab)
python3 --version  # Should be 3.8 or higher

# Check Docker
docker --version

# Check OpenShift CLI
oc version

# Check if logged into OpenShift
oc whoami
```

## Choose Your Lab Option

### Option 1: JavaScript Lab

```bash
cd javascript-lab
```

**Local Testing:**
```bash
cd app
npm install
npm start
# Visit http://localhost:3000
```

**Run Tests:**
```bash
npm test
```

**Build Docker Image:**
```bash
docker build -t ci-cd-javascript-app:latest .
docker run -p 3000:3000 ci-cd-javascript-app:latest
```

### Option 2: Python Lab

```bash
cd python-lab
```

**Local Testing:**
```bash
cd app
pip install -r requirements.txt
python src/app.py
# Visit http://localhost:5000
```

**Run Tests:**
```bash
pip install -r requirements-dev.txt
pytest src/test_app.py
```

**Build Docker Image:**
```bash
docker build -t ci-cd-python-app:latest .
docker run -p 5000:5000 ci-cd-python-app:latest
```

## GitHub Actions Setup

1. **Create a GitHub Repository:**
   ```bash
   git init
   git add .
   git commit -m "Initial CI/CD pipeline setup"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Configure GitHub Secrets:**
   - Go to your repository → Settings → Secrets and variables → Actions
   - Add the following secrets:
     - `OPENSHIFT_SERVER_URL`: Your OpenShift cluster URL
     - `OPENSHIFT_TOKEN`: Your OpenShift authentication token

3. **Trigger Workflow:**
   - Push code to main/master branch
   - Or create a pull request
   - Check Actions tab for workflow execution

## Tekton Pipeline Setup

1. **Verify Tekton Installation:**
   ```bash
   oc get pods -n tekton-pipelines
   ```

2. **Apply Tekton Resources:**
   ```bash
   # For JavaScript lab
   oc apply -f javascript-lab/tekton/
   
   # For Python lab
   oc apply -f python-lab/tekton/
   ```

3. **Run Pipeline:**
   ```bash
   # For JavaScript lab
   oc create -f javascript-lab/tekton/pipeline-run.yaml
   
   # For Python lab
   oc create -f python-lab/tekton/pipeline-run.yaml
   ```

4. **Monitor Pipeline:**
   ```bash
   # Watch pipeline status
   oc get pipelinerun -w
   
   # View logs
   oc logs -f pipelinerun/ci-cd-pipeline-run
   ```

## OpenShift Deployment

1. **Create/Select Namespace:**
   ```bash
   oc new-project ci-cd-project
   # or
   oc project <existing-project>
   ```

2. **Deploy Application:**
   ```bash
   # For JavaScript lab
   oc apply -f javascript-lab/openshift/
   
   # For Python lab
   oc apply -f python-lab/openshift/
   ```

3. **Check Deployment Status:**
   ```bash
   oc get deployment
   oc get pods
   oc get service
   oc get route
   ```

4. **Get Application URL:**
   ```bash
   # For JavaScript lab
   oc get route ci-cd-javascript-app -o jsonpath='{.spec.host}'
   
   # For Python lab
   oc get route ci-cd-python-app -o jsonpath='{.spec.host}'
   ```

5. **Test Application:**
   ```bash
   # Replace <route-url> with your actual route URL
   curl https://<route-url>/health
   curl https://<route-url>/
   curl https://<route-url>/api/info
   ```

## Troubleshooting

### GitHub Actions Not Triggering
- Check workflow file is in `.github/workflows/` directory
- Verify branch name matches workflow trigger (main/master)
- Check workflow file syntax (YAML)

### Tekton Pipeline Failing
- Verify Tekton is installed: `oc get pods -n tekton-pipelines`
- Check task definitions: `oc get task`
- View task logs: `oc logs taskrun/<task-name>`

### OpenShift Deployment Issues
- Check pod logs: `oc logs <pod-name>`
- Verify image exists: `oc get imagestream`
- Check resource quotas: `oc describe quota`

### Application Not Accessible
- Verify route exists: `oc get route`
- Check service endpoints: `oc get endpoints`
- Test service directly: `oc port-forward svc/<service-name> 8080:80`

## Next Steps

1. Complete the pipeline setup following the steps above
2. Capture screenshots and outputs as described in `SUBMISSION_GUIDE.md`
3. Submit your deliverables via the Coursera platform

## Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Tekton Documentation](https://tekton.dev/docs/)
- [OpenShift Documentation](https://docs.openshift.com/)

