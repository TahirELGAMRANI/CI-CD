# How to Capture GitHub Actions Workflow Output

## Method 1: From GitHub Web Interface

1. Go to your repository: https://github.com/TahirELGAMRANI/CI-CD
2. Click on the **Actions** tab
3. Click on a workflow run (e.g., "JavaScript Lab CI/CD Pipeline" or "Python Lab CI/CD Pipeline")
4. Click on a job (e.g., "Build and Test JavaScript App")
5. Click on each step to expand and view the output
6. Copy the terminal output from each step

## Method 2: Using GitHub CLI

If you have GitHub CLI installed:

```bash
# List workflow runs
gh run list

# View a specific workflow run
gh run view <run-id>

# Get logs for a specific run
gh run view <run-id> --log > ci-cd-github-validate.txt
```

## Method 3: Manual Copy from GitHub

1. Navigate to: https://github.com/TahirELGAMRANI/CI-CD/actions
2. Click on the latest workflow run
3. Expand each step and copy the output
4. Save it to a file named `ci-cd-github-validate.txt` or `ci-cd-github-validate.md`

## What to Include in the Output File

Your `ci-cd-github-validate` file should contain:

1. **Workflow Run Summary**
   - Workflow name
   - Run status (success/failure)
   - Duration
   - Commit SHA

2. **Job Outputs**
   - Build job output
   - Test job output
   - Deploy job output (if applicable)

3. **Step-by-Step Outputs**
   - Checkout code
   - Setup environment (Node.js/Python)
   - Install dependencies
   - Run linter
   - Run tests
   - Build Docker image
   - Deploy to OpenShift (if applicable)

## Example Output Structure

```
GitHub Actions Workflow: JavaScript Lab CI/CD Pipeline
Run ID: [run-id]
Status: ✅ Success
Duration: 2m 15s
Commit: [commit-sha]

=== Job: Build and Test JavaScript App ===

Step: Checkout code
[output here]

Step: Setup Node.js
[output here]

Step: Install dependencies
[output here]

Step: Run linter
[output here]

Step: Run tests
[output here]

Step: Build Docker image
[output here]
```

