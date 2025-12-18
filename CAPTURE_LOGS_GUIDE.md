# Guide: How to Capture OpenShift Application Logs

**File Name:** `oc-application-logs.txt`

This guide shows you how to capture application logs from your deployed application in OpenShift.

---

## Method 1: Using Command Line (Recommended)

### Step 1: Find Your Application Pod

```bash
# List all pods in your namespace
oc get pods -n <your-namespace>

# Filter by application name
oc get pods -n <your-namespace> | grep ci-cd-javascript-app
# OR
oc get pods -n <your-namespace> | grep ci-cd-python-app
```

### Step 2: Get Logs from Pod

```bash
# Get logs from specific pod
oc logs <pod-name> -n <your-namespace> > oc-application-logs.txt

# Example for JavaScript app
oc logs ci-cd-javascript-app-xxxxx-xxxxx -n <your-namespace> > oc-application-logs.txt

# Example for Python app
oc logs ci-cd-python-app-xxxxx-xxxxx -n <your-namespace> > oc-application-logs.txt
```

### Step 3: Get Logs from Deployment (Easier)

```bash
# Get logs from deployment (automatically uses latest pod)
oc logs deployment/ci-cd-javascript-app -n <your-namespace> > oc-application-logs.txt

# OR for Python app
oc logs deployment/ci-cd-python-app -n <your-namespace> > oc-application-logs.txt
```

### Step 4: Get Recent Logs (Last 100 lines)

```bash
# Get last 100 lines of logs
oc logs deployment/ci-cd-javascript-app -n <your-namespace> --tail=100 > oc-application-logs.txt
```

### Step 5: Follow Logs (Real-time)

```bash
# Follow logs in real-time (press Ctrl+C to stop)
oc logs deployment/ci-cd-javascript-app -n <your-namespace> -f

# Then copy the output manually
```

---

## Method 2: Using OpenShift Web Console

1. **Login to OpenShift Console**
2. **Navigate to Workloads → Pods**
3. **Find Your Application Pod:**
   - Look for pods with name like `ci-cd-javascript-app-xxxxx` or `ci-cd-python-app-xxxxx`
4. **Click on Pod Name**
5. **Click on "Logs" Tab**
6. **Copy Logs:**
   - Select all logs (Cmd+A / Ctrl+A)
   - Copy (Cmd+C / Ctrl+C)
   - Paste into text file: `oc-application-logs.txt`

---

## Method 3: Get Logs from Multiple Containers

If your pod has multiple containers:

```bash
# List containers in pod
oc get pod <pod-name> -n <namespace> -o jsonpath='{.spec.containers[*].name}'

# Get logs from specific container
oc logs <pod-name> -c <container-name> -n <namespace> > oc-application-logs.txt
```

---

## What Logs Should Include

Your `oc-application-logs.txt` should show:

### For JavaScript App:
```
Server is running on port 3000
GET /health 200
GET / 200
GET /api/info 200
```

### For Python App:
```
Starting gunicorn
Listening at: http://0.0.0.0:5000
GET /health 200
GET / 200
GET /api/info 200
```

### Example Log Output:

```
2025-12-18T14:30:00.000Z Server is running on port 3000
2025-12-18T14:30:05.123Z GET /health 200 2ms
2025-12-18T14:30:10.456Z GET / 200 3ms
2025-12-18T14:30:15.789Z GET /api/info 200 4ms
```

---

## Complete Example Commands

### For JavaScript Application:

```bash
# Set namespace (replace with your namespace)
export NAMESPACE="your-namespace"

# Get deployment logs
oc logs deployment/ci-cd-javascript-app -n $NAMESPACE > oc-application-logs.txt

# Verify logs were captured
cat oc-application-logs.txt
```

### For Python Application:

```bash
# Set namespace
export NAMESPACE="your-namespace"

# Get deployment logs
oc logs deployment/ci-cd-python-app -n $NAMESPACE > oc-application-logs.txt

# Verify logs were captured
cat oc-application-logs.txt
```

---

## Troubleshooting

### No Pods Found:
```bash
# Check if deployment exists
oc get deployment -n <namespace>

# Check deployment status
oc describe deployment/<deployment-name> -n <namespace>

# Check if pods are being created
oc get pods -n <namespace> -w
```

### Pod Not Ready:
```bash
# Check pod status
oc describe pod <pod-name> -n <namespace>

# Check pod events
oc get events -n <namespace> --field-selector involvedObject.name=<pod-name>
```

### No Logs Available:
```bash
# Check if pod is running
oc get pod <pod-name> -n <namespace>

# Check container status
oc describe pod <pod-name> -n <namespace> | grep -A 10 "Containers:"
```

### Access Denied:
```bash
# Check your permissions
oc auth can-i get pods -n <namespace>
oc auth can-i get logs -n <namespace>

# Switch to correct project
oc project <namespace>
```

---

## Advanced: Get Logs with Timestamps

```bash
# Get logs with timestamps
oc logs deployment/ci-cd-javascript-app -n <namespace> --timestamps > oc-application-logs.txt
```

## Advanced: Get Logs from Previous Container Instance

```bash
# Get logs from previous instance (if pod restarted)
oc logs deployment/ci-cd-javascript-app -n <namespace> --previous > oc-application-logs.txt
```

---

## Verification

After capturing logs, verify:

- [ ] File `oc-application-logs.txt` exists
- [ ] File contains application startup messages
- [ ] File contains request logs (if any requests were made)
- [ ] File shows application is running
- [ ] File size is reasonable (not empty, not too large)

---

## Example Complete Workflow

```bash
# 1. Login to OpenShift
oc login <your-openshift-url>

# 2. Set namespace
oc project <your-namespace>

# 3. Verify deployment exists
oc get deployment

# 4. Get application logs
oc logs deployment/ci-cd-javascript-app -n <your-namespace> --tail=200 > oc-application-logs.txt

# 5. Verify logs
head -20 oc-application-logs.txt
tail -20 oc-application-logs.txt

# 6. Check file size
ls -lh oc-application-logs.txt
```

---

## File Format

Save the logs as a plain text file:
- **File Name:** `oc-application-logs.txt`
- **Format:** Plain text (.txt)
- **Encoding:** UTF-8
- **Size:** Should be reasonable (few KB to few MB)

---

Good luck! 🚀

