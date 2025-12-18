# GitHub Setup Instructions

Your local repository is ready! Follow these steps to push to GitHub:

## Step 1: Create a GitHub Repository

1. Go to [GitHub.com](https://github.com) and sign in
2. Click the "+" icon in the top right corner
3. Select "New repository"
4. Fill in the repository details:
   - **Repository name**: `ci-cd-pipeline-project` (or your preferred name)
   - **Description**: "CI/CD Pipeline Project with JavaScript and Python lab options"
   - **Visibility**: Choose Public or Private
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
5. Click "Create repository"

## Step 2: Add Remote and Push

After creating the repository, GitHub will show you the repository URL. Use one of these methods:

### Option A: Using HTTPS (Recommended)
```bash
cd "/Users/tahirelgamrani/CI CD"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

### Option B: Using SSH
```bash
cd "/Users/tahirelgamrani/CI CD"
git remote add origin git@github.com:YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual GitHub username and repository name.

## Step 3: Verify Push

After pushing, refresh your GitHub repository page. You should see all your files!

## Step 4: Configure GitHub Actions Secrets

For the CI/CD pipeline to work, you need to add secrets:

1. Go to your repository on GitHub
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret** and add:
   - **Name**: `OPENSHIFT_SERVER_URL`
     **Value**: Your OpenShift cluster URL (e.g., `https://api.your-cluster.openshift.com`)
   
   - **Name**: `OPENSHIFT_TOKEN`
     **Value**: Your OpenShift authentication token

To get your OpenShift token:
```bash
oc whoami -t
```

## Troubleshooting

### Authentication Issues
If you get authentication errors:
- For HTTPS: Use a Personal Access Token instead of password
  - Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
  - Generate a new token with `repo` scope
  - Use the token as your password when pushing

- For SSH: Make sure your SSH key is added to GitHub
  - Check: `ssh -T git@github.com`
  - Add key: GitHub Settings → SSH and GPG keys → New SSH key

### Branch Name Issues
If your default branch is `master` instead of `main`:
```bash
git branch -m master main
git push -u origin main
```

## Next Steps

After pushing to GitHub:
1. The GitHub Actions workflows will be available
2. You can trigger workflows by pushing code
3. Set up your OpenShift secrets as described above
4. Follow the QUICK_START.md guide to deploy your pipelines

