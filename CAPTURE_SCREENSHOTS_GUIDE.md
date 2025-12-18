# Guide: How to Capture Required Screenshots

This guide provides step-by-step instructions for capturing all required screenshots for your submission.

---

## Screenshot 1: OpenShift PersistentVolumeClaim Details

**File Name:** `oc-pipelines-console-pvc-details.png` (or `.jpg`)

### Method 1: Using OpenShift Web Console (Recommended)

1. **Login to OpenShift:**
   - Open your browser and go to your OpenShift console URL
   - Login with your credentials

2. **Navigate to PVCs:**
   - Click on **Storage** in the left sidebar
   - Click on **PersistentVolumeClaims**
   - Or search for "PVC" in the search bar

3. **Find Pipeline PVC:**
   - Look for PVCs related to pipelines (e.g., `pipeline-pvc`, `workspace-pvc`, or similar)
   - Click on the PVC name

4. **Capture Screenshot:**
   - Make sure the following information is visible:
     - ✅ PVC Name
     - ✅ Namespace
     - ✅ Status (Bound/Available)
     - ✅ Storage Class
     - ✅ Capacity
     - ✅ Access Modes
     - ✅ Volume Name
   - Press `Cmd+Shift+4` (Mac) or `Windows+Shift+S` (Windows) to take screenshot
   - Save as: `oc-pipelines-console-pvc-details.png`

### Method 2: Using Command Line

```bash
# Get PVC details
oc get pvc -n <your-namespace> -o wide

# Describe PVC
oc describe pvc <pvc-name> -n <your-namespace>

# Save to file
oc get pvc <pvc-name> -n <your-namespace> -o yaml > oc-pipelines-console-pvc-details.yaml
oc describe pvc <pvc-name> -n <your-namespace> > oc-pipelines-console-pvc-details.txt
```

**What to Include:**
- PVC name
- Namespace
- Status
- Storage class
- Capacity (e.g., 5Gi)
- Access modes
- Volume name

---

## Screenshot 2: OpenShift Pipeline Details

**File Name:** `oc-pipelines-oc-final.png` (or `.jpg`)

### Method 1: Using OpenShift Web Console (Recommended)

1. **Navigate to Pipelines:**
   - Click on **Pipelines** in the left sidebar
   - Click on **Pipelines** (not Pipeline Runs)

2. **Select Your Pipeline:**
   - Find your pipeline (e.g., `ci-cd-pipeline`)
   - Click on the pipeline name

3. **Capture Screenshot:**
   - Make sure the following is visible:
     - ✅ Pipeline name
     - ✅ Pipeline definition
     - ✅ Tasks list (test, build, deploy, cleanup)
     - ✅ Parameters
     - ✅ Resources (if any)
   - Take screenshot
   - Save as: `oc-pipelines-oc-final.png`

### Method 2: Using Command Line

```bash
# Get pipeline details
oc get pipeline -n <your-namespace>

# Describe pipeline
oc describe pipeline <pipeline-name> -n <your-namespace>

# Get YAML
oc get pipeline <pipeline-name> -n <your-namespace> -o yaml > oc-pipelines-oc-final.yaml
```

**What to Include:**
- Pipeline name
- Tasks (test-task, build-task, deploy-task, cleanup-task)
- Parameters
- Pipeline structure/flow

---

## Screenshot 3: OpenShift Pipeline Running Successfully (GREEN)

**File Name:** `oc-pipelines-oc-green.png` (or `.jpg`)

### Step-by-Step:

1. **Start a Pipeline Run:**
   ```bash
   oc create -f javascript-lab/tekton/pipeline-run.yaml
   # OR
   oc create -f python-lab/tekton/pipeline-run.yaml
   ```

2. **Monitor the Run:**
   ```bash
   oc get pipelinerun -n <your-namespace> -w
   ```

3. **In Web Console:**
   - Go to **Pipelines** → **Pipeline Runs**
   - Click on your pipeline run (should show "Running" or "Succeeded")

4. **Wait for Success:**
   - Wait until all tasks show ✅ (green checkmarks)
   - Status should show **"Succeeded"** (green)

5. **Capture Screenshot:**
   - Make sure the following is visible:
     - ✅ Pipeline Run name
     - ✅ Status: **Succeeded** (in green)
     - ✅ All tasks showing ✅ (green checkmarks)
     - ✅ Completion time/duration
     - ✅ Task execution order
   - Take screenshot
   - Save as: `oc-pipelines-oc-green.png`

### What Success Looks Like:

```
Pipeline Run: ci-cd-pipeline-run-xxxxx
Status: Succeeded ✅
Duration: 2m 15s

Tasks:
✅ test-task (Succeeded)
✅ build-task (Succeeded)
✅ deploy-task (Succeeded)
✅ cleanup-task (Succeeded)
```

### Alternative: Command Line Output

```bash
# Get successful pipeline run
oc get pipelinerun -n <namespace> | grep Succeeded

# Describe successful run
oc describe pipelinerun <run-name> -n <namespace> > oc-pipelines-oc-green.txt
```

---

## Screenshot Tips

### General Tips:
1. **Use Full Screen:** Maximize your browser window
2. **Zoom Level:** Use 100% zoom for clarity
3. **Clear View:** Hide browser bookmarks/toolbars if possible
4. **High Resolution:** Ensure screenshot is clear and readable
5. **File Format:** Use PNG for better quality, or JPG if file size is an issue

### Mac Screenshot:
- **Full Screen:** `Cmd + Shift + 3`
- **Selected Area:** `Cmd + Shift + 4`
- **Window:** `Cmd + Shift + 4`, then press `Space`, click window

### Windows Screenshot:
- **Full Screen:** `Windows + Print Screen`
- **Selected Area:** `Windows + Shift + S`
- **Snipping Tool:** Search for "Snipping Tool" in Start menu

### Linux Screenshot:
- **Full Screen:** `Print Screen`
- **Selected Area:** `Shift + Print Screen`
- **Tool:** Use `gnome-screenshot` or `scrot`

---

## Verification Checklist

Before submitting, verify:

- [ ] `oc-pipelines-console-pvc-details.png` - Shows PVC details clearly
- [ ] `oc-pipelines-oc-final.png` - Shows pipeline definition with tasks
- [ ] `oc-pipelines-oc-green.png` - Shows successful pipeline run with green status
- [ ] All screenshots are readable
- [ ] File names match exactly as specified
- [ ] Screenshots show required information

---

## Troubleshooting

### Can't find PVC:
```bash
# List all PVCs
oc get pvc --all-namespaces

# Check Tekton namespace
oc get pvc -n tekton-pipelines
```

### Pipeline not showing:
```bash
# List pipelines
oc get pipeline --all-namespaces

# Check if Tekton is installed
oc get pods -n tekton-pipelines
```

### Pipeline run not succeeding:
- Check task logs: `oc logs taskrun/<task-name> -n <namespace>`
- Check pipeline run status: `oc describe pipelinerun <run-name> -n <namespace>`
- Verify all tasks are defined correctly

---

## Example Screenshot Locations

### OpenShift Console URLs (adjust for your cluster):
- PVC: `https://<console-url>/k8s/ns/<namespace>/persistentvolumeclaims`
- Pipeline: `https://<console-url>/k8s/ns/<namespace>/tekton.dev~v1beta1~Pipeline`
- Pipeline Run: `https://<console-url>/k8s/ns/<namespace>/tekton.dev~v1beta1~PipelineRun`

---

Good luck with your submission! 🎯

