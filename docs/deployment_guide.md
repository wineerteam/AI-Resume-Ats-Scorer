# 🌐 Public Hosting & Cloud Deployment Guide

This guide details the step-by-step process of hosting the **ATS Resume Scorer & Analyzer** on public free servers (FastAPI Backend on Render & Streamlit Frontend on Streamlit Cloud).

---

## Live Deployments
* **Live Web App URL**: [https://ai-resume-ats-scorer-pw3ws5usjnha5pdz9uyswx.streamlit.app/](https://ai-resume-ats-scorer-pw3ws5usjnha5pdz9uyswx.streamlit.app/)
* **Live API Backend URL**: [https://ai-resume-ats-backend.onrender.com](https://ai-resume-ats-backend.onrender.com)
* **GitHub Codebase**: [https://github.com/wineerteam/ai-resume-ats-scorer](https://github.com/wineerteam/ai-resume-ats-scorer)

---

## 1. Step 1: Git Repository & GitHub Synchronization
### 🔍 What
Uploading our local version-controlled files to a public Git hosting platform (GitHub) under the repository `https://github.com/wineerteam/ai-resume-ats-scorer.git`.

### 💡 Why
- **Source of Truth**: Streamlit Cloud and Render do not build code from local folders; they pull directly from a GitHub repository to build.
- **Security Check**: Git allows us to verify that no secret keys (like `.env` or `secrets.toml`) are uploaded to GitHub.

### 💻 Syntax / Process
```bash
# 1. Initialize local repository
git init

# 2. Add remote URL
git remote add origin https://github.com/wineerteam/ai-resume-ats-scorer.git

# 3. Add files and commit
git add .
git commit -m "Configure production environment and mock modes"

# 4. Push code to main branch
git push -u origin main
```

### 🔄 Alternates
- **GitLab**: Popular enterprise alternative with built-in CI/CD pipelines.
- **Bitbucket**: Atlassian's Git provider, well-integrated with Jira.

### 🎭 Analogy
Git Push is like **loading a cargo ship and sending it to a central distribution warehouse (GitHub)**. The local machine is your private factory, and the remote repository is the central depot where builders (Render and Streamlit Cloud) can pick up the materials to build your live websites.

---

## 2. Step 2: Backend Deployment on Render.com
### 🔍 What
Deploying our FastAPI backend Python application as a public Web Service on **Render.com**.

### 💡 Why
- **Free Tier**: Render offers a generous free tier hosting web servers without database limitations.
- **Automatic Builds**: On every new `git push` to GitHub, Render automatically triggers a rebuild.

### 💻 Syntax / Configuration
- **Build Command**: `pip install -r requirements.txt` (Downloads packages).
- **Start Command**: `python -m uvicorn backend.main:app --host 0.0.0.0 --port 10000` (Binds the app to port 10000 which Render routes automatically).
- **Environment Variables**:
  - `MOCK_MODE` = `true` (Runs the backend locally/mocked without cloud credentials).

### 🔄 Alternates
- **Hugging Face Spaces**: Offers 16GB RAM for free CPU spaces (excellent for AI models).
- **Railway.app**: Paid/credit-based, but extremely fast with zero cold-starts.
- **AWS Elastic Beanstalk**: Enterprise cloud deployment, paid.

### 🎭 Analogy
Render is like **renting a kitchen in a ghost kitchen restaurant**. Render sets up the cooking equipment (installs python packages), tells the chef what instructions to follow to cook (Uvicorn startup command), and opens a window (URL) where customers can place orders.

---

## 3. Step 3: Frontend Deployment on Streamlit Cloud
### 🔍 What
Deploying our Streamlit Python application on **Streamlit Community Cloud** and connecting it to our Render backend API.

### 💡 Why
- **Seamless Streamlit Support**: Built by Streamlit specifically to host Streamlit web interfaces, making the deployment process a one-click action.
- **Fast Build Times**: Streamlit caches dependencies, rendering pages in under a minute.

### 💻 Syntax / Configuration
1. Go to `https://share.streamlit.io/`.
2. Connect repository `wineerteam/ai-resume-ats-scorer` and select `frontend/streamlit_app.py` as the entry file.
3. In **Advanced Settings**, define the backend URL secret:
   ```toml
   [backend]
   url = "https://ai-resume-ats-backend.onrender.com"
   ```

### 🔄 Alternates
- **Vercel**: Deploys frontend interfaces; requires custom build packs for Streamlit.
- **Dockerizing on AWS**: Complex container configuration, paid.

### 🎭 Analogy
Streamlit Cloud is like **building the dining room and order counter for your restaurant**. The dining room sits on a beautiful public street (Streamlit Cloud URL). When a customer comes in and places an order, the cashier uses a walkie-talkie (API client) to send the order to the ghost kitchen (Render Backend) to get it cooked.

---

## 4. Step 4: Environment Variables & Secrets Management
### 🔍 What
A mechanism to pass sensitive configuration parameters (like API keys) to the application at runtime without hardcoding them in the source code.

### 💡 Why
- **Security**: Storing passwords and API keys in source code commits allows hackers to steal them easily.
- **Dynamic Configuration**: We can change database servers or LLM models instantly in the hosting dashboard without changing any code.

### 💻 Syntax / Example
- In **Streamlit Dashboard (Secrets Settings)**:
  ```toml
  [supabase]
  SUPABASE_URL = "https://your-supabase-url.supabase.co"
  SUPABASE_ANON_KEY = "eyJhbGciOi..."
  ```
- In **Render Dashboard (Environment Variables Settings)**:
  - `GROQ_API_KEY` = `gsk_...`

### 🔄 Alternates
- **AWS Secrets Manager**: Advanced paid secrets vaults.
- **Vault (HashiCorp)**: On-premise enterprise secret management tool.

### 🎭 Analogy
Secrets settings are like **giving the staff a security passcode for the building**. The passcodes are never printed on the building's posters (GitHub code); instead, when the manager opens the doors in the morning (runtime boot), he whispers the passcode to the workers (environment variables) so they can enter the vault.
