# Publishing Guide for whatiz

Follow these steps to publish your CLI tool on GitHub and PyPI.

## Step 1: Initialize Git Repository

```bash
cd /home/shivam/Coding/Python/whatiz
git init
git add .
git commit -m "Initial commit: Add whatiz CLI tool"
```

## Step 2: Create GitHub Repository

1. Go to https://github.com/new
2. Create a new repository named `whatiz`
3. **Don't initialize with README** (we already have one)
4. Copy the URL (should be `https://github.com/yourusername/whatiz.git`)

## Step 3: Connect Local to GitHub

```bash
git remote add origin https://github.com/yourusername/whatiz.git
git branch -M main
git push -u origin main
```

## Step 4: Update pyproject.toml

Replace these placeholders with your actual info:
- `yourusername` → your GitHub username
- `Your Name` → your actual name
- `you@example.com` → your email

## Step 5: Register on PyPI

1. Go to https://pypi.org/account/register/
2. Create an account
3. Enable 2FA (recommended)
4. Create an API token:
   - Account settings → API tokens → "Create token for the entire account"
   - Copy the token (you'll only see it once!)

## Step 6: Add PyPI Secret to GitHub

1. Go to your repo on GitHub
2. Settings → Secrets and variables → Actions
3. Click "New repository secret"
4. Name: `PYPI_API_TOKEN`
5. Value: Paste your PyPI token
6. Click "Add secret"

## Step 7: Create a Release

When you're ready to publish:

```bash
# Update version in pyproject.toml if needed
# Commit and push
git add .
git commit -m "Bump version to 0.1.0"
git push

# Create a git tag
git tag v0.1.0
git push origin v0.1.0
```

This triggers the GitHub Actions workflow which automatically:
- Builds the package
- Publishes to PyPI
- Users can now `pip install whatiz`

## Step 8: Verify Installation

After 1-2 minutes:

```bash
# Anyone can now install it!
pip install whatiz
whatiz python
```

## Alternative: Manual Publishing

If you don't want to use GitHub Actions:

```bash
pip install build twine

# Build the package
python -m build

# Upload to PyPI (it will ask for your account)
twine upload dist/*
```

## Version Bumping

For subsequent releases:

1. Update `version` in `pyproject.toml`
2. Commit: `git commit -am "Bump to v0.2.0"`
3. Tag: `git tag v0.2.0`
4. Push: `git push origin main v0.2.0`

## Package Structure for Distribution

When users install your package:
```
whatiz/
├── src/
│   └── whatiz/
│       ├── __init__.py
│       └── main.py
├── tests/
├── pyproject.toml
├── README.md
└── LICENSE
```

The `[project.scripts]` entry in `pyproject.toml` creates:
```bash
whatiz = "whatiz.main:main"
```

This automatically:
✅ Installs `whatiz` command in the user's PATH
✅ Works in any shell (bash, fish, zsh, etc.)
✅ Functions like `cmatrix`, `sl`, etc.

## Troubleshooting

**Still can't find `whatiz` command after install?**
```bash
# Check if it's installed
python -m pip show whatiz

# Try adding to PATH manually (if needed)
export PATH="$PATH:$(python -m site --user-scripts)"
```

**Want to test locally first?**
```bash
# Install in editable mode
pip install -e .

# Now test
whatiz python
```

## Supporting Different Installation Methods

Users can install in multiple ways:

```bash
# Standard pip
pip install whatiz

# With pipx (keeps dependencies isolated)
pipx install whatiz

# From source
git clone https://github.com/yourusername/whatiz.git
pip install whatiz/

# With Poetry
poetry add whatiz
```

All work the same way!
