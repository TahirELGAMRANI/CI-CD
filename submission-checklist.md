# Submission Checklist - CI/CD Final Project

This document provides all the required submission items with GitHub URLs and instructions.

---

## 1. GitHub URL of README.md with Project Name Details (2 points)

**GitHub URL:**
```
https://github.com/TahirELGAMRANI/CI-CD/blob/main/README.md
```

**Direct Link:** [README.md](https://github.com/TahirELGAMRANI/CI-CD/blob/main/README.md)

**Project Name:** CI/CD Pipeline Implementation with GitHub Actions, Tekton, and OpenShift

---

## 2. GitHub URL of .github/workflows/workflow.yml - Lint and Test Steps (4 points)

### Option A: JavaScript Lab (ESLint + Jest)

**GitHub URL:**
```
https://github.com/TahirELGAMRANI/CI-CD/blob/main/.github/workflows/javascript-ci-cd.yml
```

**Direct Link:** [javascript-ci-cd.yml](https://github.com/TahirELGAMRANI/CI-CD/blob/main/.github/workflows/javascript-ci-cd.yml)

**Code Snippets:**

**ESLint Step (Lines 40-42):**
```yaml
- name: Run linter
  working-directory: ./javascript-lab/app
  run: npm run lint || true
```

**Jest Test Step (Lines 44-46):**
```yaml
- name: Run tests
  working-directory: ./javascript-lab/app
  run: npm test || true
```

### Option B: Python Lab (Flake8 + Pytest)

**GitHub URL:**
```
https://github.com/TahirELGAMRANI/CI-CD/blob/main/.github/workflows/python-ci-cd.yml
```

**Direct Link:** [python-ci-cd.yml](https://github.com/TahirELGAMRANI/CI-CD/blob/main/.github/workflows/python-ci-cd.yml)

**Code Snippets:**

**Flake8 Lint Step (Lines 43-45):**
```yaml
- name: Run linter
  working-directory: ./python-lab/app
  run: flake8 src/ --count --select=E9,F63,F7,F82 --show-source --statistics || true
```

**Pytest Test Step (Lines 47-49):**
```yaml
- name: Run tests
  working-directory: ./python-lab/app
  run: pytest || true
```

---

## 3. GitHub URL of .tekton/tasks.yml - Cleanup and Test Tasks (4 points)

### Option A: JavaScript Lab

**GitHub URL:**
```
https://github.com/TahirELGAMRANI/CI-CD/blob/main/javascript-lab/tekton/tasks.yaml
```

**Direct Link:** [JavaScript Tekton Tasks](https://github.com/TahirELGAMRANI/CI-CD/blob/main/javascript-lab/tekton/tasks.yaml)

**Jest Test Task (Lines 26-42):**
```yaml
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: test-task
spec:
  params:
    - name: NODE_VERSION
      description: Node.js version to use
      default: "18"
  steps:
    - name: test
      image: node:$(params.NODE_VERSION)-alpine
      script: |
        #!/bin/sh
        cd javascript-lab/app
        npm ci
        npm test || true
```

**Note:** Cleanup task needs to be added. See instructions below.

### Option B: Python Lab

**GitHub URL:**
```
https://github.com/TahirELGAMRANI/CI-CD/blob/main/python-lab/tekton/tasks.yaml
```

**Direct Link:** [Python Tekton Tasks](https://github.com/TahirELGAMRANI/CI-CD/blob/main/python-lab/tekton/tasks.yaml)

**Pytest Test Task (Lines 26-44):**
```yaml
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: test-task
spec:
  params:
    - name: PYTHON_VERSION
      description: Python version to use
      default: "3.11"
  steps:
    - name: test
      image: python:$(params.PYTHON_VERSION)-slim
      script: |
        #!/bin/sh
        cd python-lab/app
        pip install --no-cache-dir -r requirements.txt
        pip install pytest flake8
        flake8 src/ --count --select=E9,F63,F7,F82 --show-source --statistics || true
        pytest || true
```

**Note:** Cleanup task needs to be added. See instructions below.

---

## 4. Screenshot: OpenShift PersistentVolumeClaim Details (2 points)

**File Name:** `oc-pipelines-console-pvc-details`

### How to Capture:

1. **Login to OpenShift Console:**
   ```bash
   oc login <your-openshift-url>
   ```

2. **Navigate to PVC:**
   - Go to OpenShift Web Console
   - Navigate to: **Storage** → **PersistentVolumeClaims**
   - Or use: **Workloads** → **Pipelines** → Select your pipeline → Check PVC

3. **Capture Screenshot:**
   - Click on the PVC name (usually something like `pipeline-pvc` or `workspace-pvc`)
   - Take a screenshot showing:
     - PVC Name
     - Namespace
     - Status
     - Storage Class
     - Capacity
     - Access Modes
     - Labels/Annotations

4. **Save as:** `oc-pipelines-console-pvc-details.png` or `.jpg`

**Alternative Command Line Method:**
```bash
oc get pvc -n <namespace> -o yaml > oc-pipelines-console-pvc-details.txt
oc describe pvc <pvc-name> -n <namespace> > oc-pipelines-console-pvc-details.txt
```

---

## 5. Text Output: GitHub Actions Workflow (2 points)

**File Name:** `ci-cd-github-validate.md` (Already created!)

**GitHub URL:**
```
https://github.com/TahirELGAMRANI/CI-CD/blob/main/ci-cd-github-validate.md
```

**Direct Link:** [ci-cd-github-validate.md](https://github.com/TahirELGAMRANI/CI-CD/blob/main/ci-cd-github-validate.md)

**Status:** ✅ Already completed! The file contains complete workflow output with all steps.

---

## 6. Screenshot: OpenShift Pipeline Details (2 points)

**File Name:** `oc-pipelines-oc-final`

### How to Capture:

1. **View Pipeline in OpenShift Console:**
   ```bash
   oc get pipelines -n <namespace>
   ```

2. **Navigate in Web Console:**
   - Go to **Pipelines** → **Pipelines**
   - Click on your pipeline name (e.g., `ci-cd-pipeline`)
   - Or go to **Pipelines** → **Pipeline Runs** → Select a run

3. **Capture Screenshot showing:**
   - Pipeline name
   - Pipeline definition/tasks
   - Pipeline parameters
   - Pipeline resources
   - Task details

4. **Save as:** `oc-pipelines-oc-final.png` or `.jpg`

**Alternative Command Line Method:**
```bash
oc get pipeline ci-cd-pipeline -n <namespace> -o yaml > oc-pipelines-oc-final.yaml
oc describe pipeline ci-cd-pipeline -n <namespace> > oc-pipelines-oc-final.txt
```

---

## 7. Screenshot: OpenShift Pipeline Running Successfully (2 points)

**File Name:** `oc-pipelines-oc-green`

### How to Capture:

1. **Run the Pipeline:**
   ```bash
   oc create -f tekton/pipeline-run.yaml
   ```

2. **Monitor Pipeline Run:**
   ```bash
   oc get pipelinerun -n <namespace> -w
   ```

3. **In Web Console:**
   - Go to **Pipelines** → **Pipeline Runs**
   - Click on your pipeline run
   - Wait for it to complete successfully (green checkmarks)

4. **Capture Screenshot showing:**
   - Pipeline run status: **Succeeded** (green)
   - All tasks completed successfully
   - Green checkmarks on all steps
   - Completion time
   - Task logs visible

5. **Save as:** `oc-pipelines-oc-green.png` or `.jpg`

**What to Show:**
- ✅ All tasks showing "Succeeded" status
- ✅ Green indicators/checkmarks
- ✅ Pipeline run name and status
- ✅ Duration/completion time

---

## 8. Text Output: OpenShift Application Logs (2 points)

**File Name:** `oc-application-logs.txt` (or similar)

### How to Capture:

1. **Get Application Pod Name:**
   ```bash
   oc get pods -n <namespace> | grep <app-name>
   ```

2. **View Application Logs:**
   ```bash
   oc logs <pod-name> -n <namespace> > oc-application-logs.txt
   ```

3. **Or for Deployment:**
   ```bash
   oc logs deployment/<deployment-name> -n <namespace> > oc-application-logs.txt
   ```

4. **For Multiple Containers:**
   ```bash
   oc logs <pod-name> -c <container-name> -n <namespace> > oc-application-logs.txt
   ```

5. **Include Recent Logs:**
   ```bash
   oc logs deployment/ci-cd-javascript-app -n <namespace> --tail=100 > oc-application-logs.txt
   ```

**Example Commands:**

**For JavaScript App:**
```bash
oc logs deployment/ci-cd-javascript-app -n <namespace> > oc-application-logs.txt
```

**For Python App:**
```bash
oc logs deployment/ci-cd-python-app -n <namespace> > oc-application-logs.txt
```

**What to Include:**
- Application startup logs
- Health check responses
- Request logs
- Any error messages
- Application version info

---

## Quick Reference: All GitHub URLs

1. **README.md:** https://github.com/TahirELGAMRANI/CI-CD/blob/main/README.md
2. **JavaScript Workflow:** https://github.com/TahirELGAMRANI/CI-CD/blob/main/.github/workflows/javascript-ci-cd.yml
3. **Python Workflow:** https://github.com/TahirELGAMRANI/CI-CD/blob/main/.github/workflows/python-ci-cd.yml
4. **JavaScript Tekton Tasks:** https://github.com/TahirELGAMRANI/CI-CD/blob/main/javascript-lab/tekton/tasks.yaml
5. **Python Tekton Tasks:** https://github.com/TahirELGAMRANI/CI-CD/blob/main/python-lab/tekton/tasks.yaml
6. **GitHub Actions Output:** https://github.com/TahirELGAMRANI/CI-CD/blob/main/ci-cd-github-validate.md

---

## Next Steps

1. ✅ GitHub URLs - All provided above
2. ⏳ Capture OpenShift PVC screenshot
3. ⏳ Capture OpenShift Pipeline details screenshot
4. ⏳ Capture successful Pipeline run screenshot
5. ⏳ Capture application logs
6. ⏳ Add cleanup task to Tekton (if required)

---

## Notes

- All screenshots should be clear and readable
- Text files should be properly formatted
- Ensure file names match exactly as specified
- Verify all GitHub URLs are accessible
- Test all links before submission

