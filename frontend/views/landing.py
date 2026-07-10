import streamlit as st


def render():
    
    # Landing page CSS
    st.markdown("""
    <style>
        .main-header {
            text-align: center;
            padding: 3rem 2rem;
            background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 50%, #9333EA 100%);
            color: white;
            border-radius: 16px;
            margin-bottom: 2rem;
            box-shadow: 0 10px 40px rgba(79, 70, 229, 0.3);
        }
        .main-header h1 {
            font-size: 2.8rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Hero Section
    st.markdown("""
    <div class="main-header">
        <h1>🎯 ATS Resume Scorer</h1>
        <h3>Optimize Your Resume for Applicant Tracking Systems</h3>
        <p>Get instant feedback on your resume's ATS compatibility with AI-powered analysis</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Call-to-Action Button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Start Analyzing Your Resume", use_container_width=True, type="primary"):
            st.session_state.current_view = 'scorer'
            st.rerun()
    
    st.markdown("---")
    
    # Features Overview
    st.markdown("## ✨ Key Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 📊 Comprehensive Scoring
        Get detailed scores across 5 key dimensions:
        - Formatting (20%)
        - Keywords & Skills (25%)
        - Content Quality (25%)
        - Skill Validation (15%)
        - ATS Compatibility (15%)
        """)
    
    with col2:
        st.markdown("""
        ### 🔍 Skill Validation
        Verify that your claimed skills are demonstrated in your projects and experience using AI-powered semantic analysis.
        
        **No more empty claims!**
        """)
    
    with col3:
        st.markdown("""
        ### 🔒 Privacy First
        All analysis runs locally with no external API calls. Your resume data never leaves your system.
        
        **100% Private & Secure**
        """)
    
    st.markdown("---")
    
    # How It Works
    st.markdown("## 🚀 How It Works")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        #### 1️⃣ Upload Your Resume
        Support for PDF, DOC, and DOCX formats
        """)
    
    with col2:
        st.markdown("""
        #### 2️⃣ AI Analysis
        Our local AI models analyze your resume across multiple dimensions
        """)
    
    with col3:
        st.markdown("""
        #### 3️⃣ Get Actionable Feedback
            Receive detailed recommendations to improve your resume
            """)
    st.markdown("---")

    st.markdown(
        """
    <div style="
        text-align: center;
        padding: 20px;
        margin-top: 20px;
        border-radius: 15px;
        background: linear-gradient(135deg, #1e293b, #334155);
        color: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    ">
        <h4 style="margin-bottom: 5px;">
            🚀 Developed by Sunil Kumar Yadav
        </h4>

        <p style="color: #cbd5e1; margin: 5px 0;">
            AI & Full Stack Developer
        </p>

        <p style="margin-top: 12px;">

            <a href="https://github.com/wineerteam"
               target="_blank"
               style="
                    color: #ffffff;
                    text-decoration: none;
                    margin-right: 20px;
                    font-size: 15px;
               ">
                🔗 GitHub
            </a>

            <a href="https://www.linkedin.com/in/sunil-kumar-yadav-abb468303/"
               target="_blank"
               style="
                    color: #ffffff;
                    text-decoration: none;
                    font-size: 15px;
               ">
                💼 LinkedIn
            </a>

        </p>

        <p style="font-size: 13px; color: #94a3b8;">
            © 2026 All Rights Reserved
        </p>

    </div>
    """,
        unsafe_allow_html=True
        )
