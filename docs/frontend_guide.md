# 🎨 Frontend Architecture Guide (Streamlit App)

This guide provides a comprehensive walkthrough of the frontend architecture of the **ATS Resume Scorer & Analyzer** application.

---

## 1. Streamlit Framework
### 🔍 What
**Streamlit** is an open-source Python framework used to create interactive, data-driven web applications quickly. It allows developers to write frontend code entirely in Python without needing to write HTML, CSS, or JavaScript manually.

### 💡 Why
- **Rapid Prototyping**: We can build interactive dashboards in hours rather than days.
- **Python Integration**: Seamlessly binds with our backend data models and NLP utilities.
- **State Management**: Built-in mechanisms to manage state between interactions.

### 💻 Syntax Example
```python
import streamlit as st

st.title("🎯 ATS Resume Scorer")
if st.button("Analyze"):
    st.write("Analyzing...")
```

### 🔄 Alternates
- **React.js / Next.js**: More powerful and customizable, but requires writing separate JavaScript/TypeScript and managing complex API communication.
- **Gradio**: Good for ML model demos, but less flexible for multi-page business dashboards.

### 🎭 Analogy
Streamlit is like a **prefab house builder**. Instead of laying bricks, running plumbing, and painting walls yourself (React/HTML/CSS), you choose pre-built rooms (widgets like buttons, text fields) and assemble them using simple Python instructions.

---

## 2. Session State Management
### 🔍 What
**Session State** is Streamlit's way of sharing variables across user interactions (reruns). Since Streamlit runs the entire script from top to bottom on every user interaction, normal Python variables get reset. Session State preserves them.

### 💡 Why
- **Auth Persistence**: Stores the logged-in user's `access_token`, `refresh_token`, and `user_id` so they don't get logged out on every button click.
- **Page Navigation**: Tracks which page/view (`landing`, `scorer`, `history`, `resources`) the user is currently looking at.

### 💻 Syntax Example
```python
# Initialize state
if "current_view" not in st.session_state:
    st.session_state.current_view = "landing"

# Modify state
if st.button("Go to Scorer"):
    st.session_state.current_view = "scorer"
    st.rerun()
```

### 🔄 Alternates
- **Redux / Context API (in React)**: Much more complex boilerplates.
- **Cookies / LocalStorage**: Standard web storage (requires JS integration in Streamlit).

### 🎭 Analogy
Session State is like a **waiter with a notepad**. Because Streamlit has short-term memory loss (runs the script fresh every time you click a button), the notepad (Session State) keeps track of your order, your login details, and which table you are sitting at.

---

## 3. Custom CSS Injection (Saberali App Style)
### 🔍 What
Injected custom CSS overrides the default Streamlit UI styling to achieve a high-end, premium SaaS appearance (curated dark modes, glassmorphism, responsive grids, and modern typography).

### 💡 Why
- **Visual Impact**: Stock Streamlit pages look like simple science projects. Custom CSS turns the app into a premium commercial SaaS tool.
- **Premium Cards & Gradients**: Provides smooth animations, gradients, and custom box-shadows.

### 💻 Syntax Example
```python
st.markdown("""
<style>
    .metric-card {
        background: #FFFFFF;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        padding: 1.5rem;
        transition: transform 0.2s;
    }
    .metric-card:hover {
        transform: translateY(-5px);
    }
</style>
""", unsafe_allow_html=True)
```

### 🔄 Alternates
- **Tailwind CSS**: Highly popular utility-first framework (requires custom HTML packaging or custom Streamlit components).
- **Streamlit Themes**: Built-in config (`config.toml`) theme variables, which are limited in scope.

### 🎭 Analogy
Custom CSS is like **custom car wraps and spoilers**. The engine and frame (Streamlit) work the same, but the wrapper (CSS) makes it look like a sleek luxury sports car instead of a default factory sedan.

---

## 4. API Client (`api_client.py`)
### 🔍 What
A custom HTTP client using the `requests` library to communicate asynchronously or synchronously with our FastAPI backend on `http://localhost:8000`.

### 💡 Why
- **Decoupled Architecture**: Keeps frontend views independent of backend logic.
- **Token Passing**: Automatically attaches the Supabase JWT `Authorization: Bearer <token>` to requests so the backend can verify user identity.

### 💻 Syntax Example
```python
import requests

def analyze_resume(file_bytes, filename, jd_text, token):
    headers = {"Authorization": f"Bearer {token}"}
    files = {"file": (filename, file_bytes)}
    data = {"job_description": jd_text}
    response = requests.post("http://localhost:8000/api/v1/analyze-resume", 
                             headers=headers, files=files, data=data)
    return response.json()
```

### 🔄 Alternates
- **httpx**: Supports async/await requests (highly recommended for performance-oriented systems).
- **Axios**: Standard client for frontend JavaScript frameworks.

### 🎭 Analogy
The API Client is like a **courier driver**. It takes the packages (resume files and job descriptions) from the office (Frontend UI), drives them to the factory (Backend API), and brings back the completed results (analysis scores).

---

## 5. Supabase Client (`supabase_client.py`)
### 🔍 What
A service wrapper around the official Supabase Python SDK to manage user authentication, session exchange, and sign-ups.

### 💡 Why
- **Secure Authentication**: Handles user password hashing, verification emails, and secure tokens.
- **OAuth Support**: Generates Google OAuth redirection URLs for passwordless authentication.
- **Mock Fallback**: Automatically provides mock sessions on local development if Supabase credentials are not configured.

### 💻 Syntax Example
```python
from supabase import create_client

def sign_in_with_password(email, password):
    client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)
    return client.auth.sign_in_with_password({"email": email, "password": password})
```

### 🔄 Alternates
- **Firebase Auth**: Google's authentication platform.
- **Auth0**: Enterprise-grade identity provider.

### 🎭 Analogy
The Supabase Client is like a **bouncer at a private club**. It checks your ID card (email/password or Google account) and hands you a wristband (JWT token) that lets you pass security checks (FastAPI routes) inside the club.
