# GitHub Actions Workflow Validation Output

## Workflow Run Summary

**Repository:** TahirELGAMRANI/CI-CD  
**Commit:** 64911bb102d5b5641808804b68b37ff10ab51fa2  
**Commit Message:** Add GitHub Actions workflows at repository root  
**Branch:** main  
**Run Date:** December 18, 2025, 14:32:50 UTC

---

## Workflow 1: JavaScript Lab CI/CD Pipeline

**Status:** ❌ Failure  
**Run ID:** 20340415542  
**Duration:** 22 seconds  
**Conclusion:** failure

### Job: Build and Test JavaScript App

#### Step 1: Set up job
```
Current runner version: '2.330.0'
Runner Image: ubuntu-24.04
Version: 20251215.174.1
Operating System: Ubuntu 24.04.3 LTS
```

#### Step 2: Checkout code
```
Run actions/checkout@v3
Repository: TahirELGAMRANI/CI-CD
Branch: main
Commit: 64911bb102d5b5641808804b68b37ff10ab51fa2
```

**Output:**
```
Syncing repository: TahirELGAMRANI/CI-CD
Working directory is '/home/runner/work/CI-CD/CI-CD'
git version 2.52.0
Initialized empty Git repository in /home/runner/work/CI-CD/CI-CD/.git/
Switched to a new branch 'main'
branch 'main' set up to track 'origin/main'.
```

#### Step 3: Setup Node.js
```
Run actions/setup-node@v3
with:
  node-version: 18
  cache: npm
  cache-dependency-path: javascript-lab/app/package-lock.json
```

**Output:**
```
Attempting to download 18...
Acquiring 18.20.8 - x64
Extracting ...
Adding to the cache ...
Environment details:
node: v18.20.8
npm: 10.8.2
yarn: 1.22.22
```

#### Step 4: Install dependencies
```
Working directory: ./javascript-lab/app
Run: npm ci
```

**Output:**
```
npm error code EUSAGE
npm error `npm ci` can only install packages when your package.json and package-lock.json or npm-shrinkwrap.json are in sync. Please update your lock file with `npm install` before continuing.
npm error Missing: eslint@8.57.1 from lock file
npm error Missing: express@4.22.1 from lock file
npm error Missing: jest@29.7.0 from lock file
npm error Missing: supertest@6.3.4 from lock file
[Additional dependencies missing...]
```

**Error:** The package-lock.json file is out of sync with package.json. The workflow failed because `npm ci` requires an exact match between package.json and package-lock.json.

**Exit Code:** 1

---

## Workflow 2: Python Lab CI/CD Pipeline

**Status:** ❌ Failure  
**Run ID:** 20340415578  
**Duration:** 15 seconds  
**Conclusion:** failure

### Job: Build and Test Python App

#### Step 1: Set up job
```
Current runner version: '2.330.0'
Runner Image: ubuntu-24.04
Version: 20251215.174.1
Operating System: Ubuntu 24.04.3 LTS
```

#### Step 2: Checkout code
```
Run actions/checkout@v3
Repository: TahirELGAMRANI/CI-CD
Branch: main
Commit: 64911bb102d5b5641808804b68b37ff10ab51fa2
```

**Output:**
```
Syncing repository: TahirELGAMRANI/CI-CD
Working directory is '/home/runner/work/CI-CD/CI-CD'
git version 2.52.0
Switched to a new branch 'main'
branch 'main' set up to track 'origin/main'.
```

#### Step 3: Setup Python
```
Run actions/setup-python@v4
with:
  python-version: 3.11
  cache: pip
  cache-dependency-path: python-lab/app/requirements.txt
```

**Output:**
```
Successfully set up CPython (3.11.14)
pip cache is not found
```

#### Step 4: Install dependencies
```
Working directory: ./python-lab/app
Run: 
  python -m pip install --upgrade pip
  pip install -r requirements.txt
  pip install pytest flake8
```

**Output:**
```
Requirement already satisfied: pip in /opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages (25.3)
Collecting Flask==2.3.2
  Downloading Flask-2.3.2-py3-none-any.whl (96 kB)
Collecting gunicorn==21.2.0
  Downloading gunicorn-21.2.0-py3-none-any.whl (80 kB)
Installing collected packages: packaging, MarkupSafe, itsdangerous, click, blinker, Werkzeug, Jinja2, gunicorn, Flask
Successfully installed Flask-2.3.2 Jinja2-3.1.6 MarkupSafe-3.0.3 Werkzeug-3.1.4 blinker-1.9.0 click-8.3.1 gunicorn-21.2.0 itsdangerous-2.2.0 packaging-25.0

Collecting pytest
  Downloading pytest-9.0.2-py3-none-any.whl (374 kB)
Collecting flake8
  Downloading flake8-7.3.0-py2.py3-none-any.whl (57 kB)
Successfully installed flake8-7.3.0 iniconfig-2.3.0 mccabe-0.7.0 pluggy-1.6.0 pycodestyle-2.14.0 pyflakes-3.4.0 pygments-2.19.2 pytest-9.0.2
```

**Status:** ✅ Success - All dependencies installed successfully

#### Step 5: Run linter
```
Working directory: ./python-lab/app
Run: flake8 src/ --count --select=E9,F63,F7,F82 --show-source --statistics || true
```

**Output:**
```
0
```

**Status:** ✅ Success - No linting errors found

#### Step 6: Run tests
```
Working directory: ./python-lab/app
Run: pytest || true
```

**Output:**
```
============================= test session starts ==============================
platform linux -- Python 3.11.14, pytest-9.0.2, pluggy-1.6.0
rootdir: /home/runner/work/CI-CD/CI-CD/python-lab/app
collected 3 items

src/test_app.py EEE                                                      [100%]

==================================== ERRORS ====================================
ERROR src/test_app.py::test_health_endpoint - AttributeError: module 'werkzeug' has no attribute '__version__'
ERROR src/test_app.py::test_root_endpoint - AttributeError: module 'werkzeug' has no attribute '__version__'
ERROR src/test_app.py::test_info_endpoint - AttributeError: module 'werkzeug' has no attribute '__version__'
============================= 3 errors in 0.26s ===============================
```

**Status:** ⚠️ Tests ran but failed due to Werkzeug version compatibility issue

#### Step 7: Build Docker image
```
Working directory: ./python-lab/app
Run: docker build -t TahirELGAMRANI/CI-CD-py:64911bb102d5b5641808804b68b37ff10ab51fa2 .
```

**Output:**
```
ERROR: failed to build: invalid tag "TahirELGAMRANI/CI-CD-py:64911bb102d5b5641808804b68b37ff10ab51fa2": repository name must be lowercase
```

**Error:** Docker image tag contains uppercase letters, which is not allowed. Docker repository names must be lowercase.

**Exit Code:** 1

---

## Summary

### JavaScript Workflow Issues:
1. **Package Lock File Sync:** The `package-lock.json` file is out of sync with `package.json`. Need to run `npm install` to regenerate the lock file.

### Python Workflow Issues:
1. **Docker Image Tag:** The image tag contains uppercase letters. Docker requires lowercase repository names.
2. **Test Failures:** Tests failed due to Werkzeug version compatibility issue with Flask 2.3.2.

### Successful Steps:
- ✅ Code checkout completed successfully for both workflows
- ✅ Node.js 18.20.8 setup completed
- ✅ Python 3.11.14 setup completed
- ✅ Python dependencies installed successfully
- ✅ Python linter passed with no errors

### Recommendations:
1. Regenerate `package-lock.json` for JavaScript lab by running `npm install`
2. Fix Docker image naming to use lowercase (e.g., `tahirelgamrani/ci-cd-py`)
3. Fix Werkzeug version compatibility issue in Python tests
4. Update workflow files to use lowercase image names

---

**Note:** This output was captured from actual GitHub Actions workflow runs on December 18, 2025. The workflows executed successfully through most steps but encountered errors that need to be addressed for complete CI/CD pipeline functionality.
