import streamlit as st


def render():

    # ==========================================
    # LANDING PAGE CSS
    # ==========================================
    st.markdown("""
    <style>

    /* ==========================================
       GLOBAL PAGE
       ========================================== */

    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* ==========================================
       HERO SECTION
       ========================================== */

    .main-header {
        position: relative;
        overflow: hidden;

        text-align: center;
        padding: 4.2rem 2.5rem;

        background:
            radial-gradient(
                circle at 88% 15%,
                rgba(255, 193, 7, 0.28),
                transparent 30%
            ),
            radial-gradient(
                circle at 12% 85%,
                rgba(244, 63, 94, 0.18),
                transparent 32%
            ),
            linear-gradient(
                135deg,
                #0f172a 0%,
                #1e3a8a 38%,
                #2563eb 72%,
                #06b6d4 100%
            );

        color: white;
        border-radius: 30px;

        margin-bottom: 2rem;

        border: 1px solid rgba(255,255,255,0.16);

        box-shadow:
            0 25px 60px rgba(15,23,42,0.35),
            inset 0 1px 0 rgba(255,255,255,0.12);

        transform: perspective(1000px) rotateX(0deg);
        transition: all 0.35s ease;
    }

    .main-header:hover {
        transform: perspective(1000px) translateY(-5px);
        box-shadow:
            0 35px 75px rgba(15,23,42,0.42),
            inset 0 1px 0 rgba(255,255,255,0.15);
    }

    .hero-badge {
        display: inline-block;

        padding: 8px 18px;
        margin-bottom: 20px;

        border-radius: 50px;

        background: rgba(255,193,7,0.14);
        border: 1px solid rgba(255,193,7,0.45);

        color: #fef3c7;

        font-size: 13px;
        font-weight: 700;

        letter-spacing: 0.4px;
    }

    .main-header h1 {
        font-size: 3.4rem;
        font-weight: 850;

        letter-spacing: -1.5px;

        margin-bottom: 12px;

        color: #ffffff;

        text-shadow:
            0 3px 15px rgba(0,0,0,0.20);
    }

    .main-header h3 {
        font-size: 1.3rem;
        font-weight: 500;

        color: #e0f2fe;

        margin-bottom: 15px;
    }

    .main-header p {
        max-width: 720px;
        margin: auto;

        color: #dbeafe;

        font-size: 1rem;
        line-height: 1.7;
    }

    /* ==========================================
       TEXT HIGHLIGHT
       ========================================== */

    .highlight-yellow {
        color: #facc15;
        font-weight: 800;
    }

    .highlight-orange {
        color: #fb923c;
        font-weight: 800;
    }

    .highlight-pink {
        color: #f9a8d4;
        font-weight: 800;
    }

    .underline-blue {
        text-decoration: underline;
        text-decoration-color: #38bdf8;
        text-decoration-thickness: 2px;
        text-underline-offset: 4px;
    }

    .underline-yellow {
        text-decoration: underline;
        text-decoration-color: #facc15;
        text-decoration-thickness: 2px;
        text-underline-offset: 4px;
    }

    /* ==========================================
       BUTTON
       ========================================== */

    .stButton > button {
        min-height: 55px;

        border-radius: 15px;

        font-size: 16px;
        font-weight: 750;

        border: 1px solid rgba(255,255,255,0.2);

        box-shadow:
            0 10px 25px rgba(37,99,235,0.22);

        transition:
            transform 0.25s ease,
            box-shadow 0.25s ease;
    }

    .stButton > button:hover {
        transform: translateY(-3px) scale(1.01);

        box-shadow:
            0 16px 35px rgba(37,99,235,0.32);
    }

    /* ==========================================
       SECTION HEADER
       ========================================== */

    .section-title {
        text-align: center;

        margin-top: 3rem;
        margin-bottom: 1.7rem;
    }

    .section-title h2 {
        font-size: 2rem;

        font-weight: 800;

        color: #0f172a;

        margin-bottom: 7px;
    }

    .section-title p {
        color: #64748b;

        font-size: 14px;

        line-height: 1.6;
    }

    .section-line {
        width: 65px;
        height: 4px;

        margin: 10px auto 0;

        border-radius: 20px;

        background: linear-gradient(
            90deg,
            #2563eb,
            #06b6d4,
            #facc15
        );
    }

    /* ==========================================
       FEATURE CARDS
       ========================================== */

    .feature-card {
        position: relative;

        min-height: 310px;

        padding: 28px;

        border-radius: 24px;

        background:
            linear-gradient(
                145deg,
                rgba(255,255,255,0.98),
                rgba(248,250,252,0.98)
            );

        border: 1px solid #e2e8f0;

        box-shadow:
            0 10px 25px rgba(15,23,42,0.07),
            0 2px 5px rgba(15,23,42,0.04);

        transition:
            transform 0.30s cubic-bezier(.2,.8,.2,1),
            box-shadow 0.30s ease,
            border-color 0.30s ease;

        transform:
            perspective(1000px)
            translateZ(0);
    }

    .feature-card:hover {
        transform:
            perspective(1000px)
            translateY(-12px)
            translateZ(25px)
            scale(1.025);

        box-shadow:
            0 30px 60px rgba(15,23,42,0.16),
            0 10px 25px rgba(37,99,235,0.10);

        border-color: #93c5fd;

        z-index: 10;
    }

    .feature-card::before {
        content: "";

        position: absolute;

        top: 0;
        left: 25px;
        right: 25px;

        height: 3px;

        border-radius: 0 0 10px 10px;

        background: linear-gradient(
            90deg,
            #2563eb,
            #06b6d4
        );

        opacity: 0.85;
    }

    .feature-card:nth-child(2)::before {
        background: linear-gradient(
            90deg,
            #facc15,
            #fb923c
        );
    }

    .feature-card:nth-child(3)::before {
        background: linear-gradient(
            90deg,
            #f472b6,
            #ef4444
        );
    }

    .card-icon {
        width: 55px;
        height: 55px;

        display: flex;
        align-items: center;
        justify-content: center;

        border-radius: 16px;

        margin-bottom: 18px;

        background:
            linear-gradient(
                135deg,
                #dbeafe,
                #cffafe
            );

        color: #1e3a8a;

        font-size: 0;
    }

    .card-icon::after {
        content: "";

        width: 21px;
        height: 21px;

        border-radius: 7px;

        background: linear-gradient(
            135deg,
            #2563eb,
            #06b6d4
        );

        box-shadow:
            8px 8px 0 rgba(37,99,235,0.15);
    }

    .feature-card:nth-child(2) .card-icon {
        background:
            linear-gradient(
                135deg,
                #fef3c7,
                #ffedd5
            );
    }

    .feature-card:nth-child(2) .card-icon::after {
        background: linear-gradient(
            135deg,
            #facc15,
            #f97316
        );
    }

    .feature-card:nth-child(3) .card-icon {
        background:
            linear-gradient(
                135deg,
                #fce7f3,
                #fee2e2
            );
    }

    .feature-card:nth-child(3) .card-icon::after {
        background: linear-gradient(
            135deg,
            #f472b6,
            #ef4444
        );
    }

    .feature-card h3 {
        color: #0f172a;

        font-size: 20px;
        font-weight: 800;

        margin-bottom: 11px;
    }

    .feature-card p {
        color: #475569;

        font-size: 14px;

        line-height: 1.7;
    }

    .feature-card ul {
        padding-left: 20px;
        margin-top: 14px;
    }

    .feature-card li {
        color: #475569;

        font-size: 13px;

        line-height: 1.9;
    }

    .feature-card li::marker {
        color: #2563eb;
    }

    /* ==========================================
       SCORE CARDS
       ========================================== */

    .score-card {
        position: relative;

        padding: 23px 10px;

        text-align: center;

        border-radius: 19px;

        background:
            linear-gradient(
                145deg,
                #ffffff,
                #f8fafc
            );

        border: 1px solid #e2e8f0;

        box-shadow:
            0 8px 22px rgba(15,23,42,0.06);

        transition:
            transform 0.28s ease,
            box-shadow 0.28s ease,
            border-color 0.28s ease;
    }

    .score-card:hover {
        transform:
            perspective(900px)
            translateY(-9px)
            translateZ(18px)
            scale(1.04);

        box-shadow:
            0 22px 40px rgba(15,23,42,0.13);

        border-color: #93c5fd;

        z-index: 10;
    }

    .score-number {
        font-size: 27px;

        font-weight: 850;

        color: #2563eb;
    }

    .score-label {
        margin-top: 6px;

        font-size: 12px;

        font-weight: 650;

        color: #475569;
    }

    /* Different accent colors */

    .score-card:nth-child(1) .score-number {
        color: #2563eb;
    }

    .score-card:nth-child(2) .score-number {
        color: #f59e0b;
    }

    .score-card:nth-child(3) .score-number {
        color: #f97316;
    }

    .score-card:nth-child(4) .score-number {
        color: #ec4899;
    }

    .score-card:nth-child(5) .score-number {
        color: #ef4444;
    }

    /* ==========================================
       HOW IT WORKS
       ========================================== */

    .step-card {
        position: relative;

        min-height: 195px;

        padding: 27px;

        border-radius: 22px;

        background:
            linear-gradient(
                145deg,
                #ffffff,
                #f8fafc
            );

        border: 1px solid #e2e8f0;

        box-shadow:
            0 8px 25px rgba(15,23,42,0.06);

        transition:
            transform 0.30s cubic-bezier(.2,.8,.2,1),
            box-shadow 0.30s ease,
            border-color 0.30s ease;
    }

    .step-card:hover {
        transform:
            perspective(1000px)
            translateY(-11px)
            translateZ(25px)
            scale(1.025);

        box-shadow:
            0 28px 55px rgba(15,23,42,0.15);

        border-color: #bfdbfe;

        z-index: 10;
    }

    .step-number {
        width: 45px;
        height: 45px;

        display: flex;
        align-items: center;
        justify-content: center;

        border-radius: 14px;

        background:
            linear-gradient(
                135deg,
                #2563eb,
                #06b6d4
            );

        color: white;

        font-size: 14px;
        font-weight: 800;

        margin-bottom: 17px;

        box-shadow:
            0 8px 18px rgba(37,99,235,0.22);
    }

    .step-card:nth-child(2) .step-number {
        background:
            linear-gradient(
                135deg,
                #facc15,
                #f97316
            );

        box-shadow:
            0 8px 18px rgba(249,115,22,0.20);
    }

    .step-card:nth-child(3) .step-number {
        background:
            linear-gradient(
                135deg,
                #ec4899,
                #ef4444
            );

        box-shadow:
            0 8px 18px rgba(236,72,153,0.20);
    }

    .step-card h3 {
        color: #0f172a;

        font-size: 18px;
        font-weight: 800;

        margin-bottom: 8px;
    }

    .step-card p {
        color: #64748b;

        font-size: 14px;

        line-height: 1.7;
    }

    /* ==========================================
       PRIVACY CARD
       ========================================== */

    .privacy-card {
        position: relative;

        overflow: hidden;

        margin-top: 30px;

        padding: 31px;

        border-radius: 24px;

        background:
            radial-gradient(
                circle at 90% 20%,
                rgba(250,204,21,0.22),
                transparent 28%
            ),
            radial-gradient(
                circle at 10% 90%,
                rgba(244,63,94,0.15),
                transparent 30%
            ),
            linear-gradient(
                135deg,
                #0f172a,
                #1e293b
            );

        color: white;

        border: 1px solid rgba(255,255,255,0.10);

        box-shadow:
            0 18px 45px rgba(15,23,42,0.22);

        transition:
            transform 0.30s ease,
            box-shadow 0.30s ease;
    }

    .privacy-card:hover {
        transform:
            perspective(1000px)
            translateY(-7px)
            translateZ(20px);

        box-shadow:
            0 28px 60px rgba(15,23,42,0.30);
    }

    .privacy-card h3 {
        color: #ffffff;

        font-size: 21px;
        font-weight: 800;

        margin-bottom: 10px;
    }

    .privacy-card p {
        color: #cbd5e1;

        font-size: 14px;

        line-height: 1.75;

        margin-bottom: 0;
    }

    /* ==========================================
       FOOTER
       ========================================== */

    .developer-card {
        text-align: center;

        padding: 32px;

        margin-top: 38px;

        border-radius: 24px;

        background:
            linear-gradient(
                135deg,
                #0f172a,
                #1e293b
            );

        color: white;

        border: 1px solid rgba(255,255,255,0.08);

        box-shadow:
            0 15px 40px rgba(15,23,42,0.20);
    }

    .developer-card h3 {
        color: #ffffff;

        font-size: 19px;

        font-weight: 800;

        margin-bottom: 8px;
    }

    .developer-role {
        color: #93c5fd;

        font-size: 14px;

        margin-bottom: 18px;
    }

    .developer-card a {
        color: #fef3c7;

        text-decoration: underline;

        text-decoration-color: #facc15;

        text-decoration-thickness: 1px;

        text-underline-offset: 4px;

        margin: 0 12px;

        font-size: 14px;

        font-weight: 650;

        transition: color 0.2s ease;
    }

    .developer-card a:hover {
        color: #facc15;
    }

    .copyright {
        margin-top: 20px;

        font-size: 12px;

        color: #94a3b8;
    }

    /* ==========================================
       MOBILE
       ========================================== */

    @media (max-width: 768px) {

        .main-header {
            padding: 3rem 1.5rem;
        }

        .main-header h1 {
            font-size: 2.35rem;
        }

        .main-header h3 {
            font-size: 1.05rem;
        }

        .feature-card {
            min-height: auto;
            margin-bottom: 20px;
        }

        .score-card {
            margin-bottom: 15px;
        }

        .step-card {
            margin-bottom: 20px;
        }

    }

    </style>
    """, unsafe_allow_html=True)


    # ==========================================
    # HERO SECTION
    # ==========================================

    st.markdown("""
    <div class="main-header">

        <div class="hero-badge">
            AI-POWERED RESUME ANALYSIS
        </div>

        <h1>
            ATS Resume Scorer
        </h1>

        <h3>
            Optimize Your Resume for
            <span class="highlight-yellow">
                Applicant Tracking Systems
            </span>
        </h3>

        <p>
            Get instant feedback on your resume's
            <span class="underline-blue">
                ATS compatibility
            </span>
            with intelligent,
            <span class="highlight-yellow">
                AI-powered analysis
            </span>.
        </p>

    </div>
    """, unsafe_allow_html=True)


    # ==========================================
    # CALL TO ACTION
    # ==========================================

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        if st.button(
            "Start Analyzing Your Resume",
            use_container_width=True,
            type="primary"
        ):
            st.session_state.current_view = 'scorer'
            st.rerun()


    st.markdown("---")


    # ==========================================
    # FEATURES
    # ==========================================

    st.markdown("""
    <div class="section-title">

        <h2>
            Key Features
        </h2>

        <p>
            Powerful tools to make your resume
            <span class="underline-blue">
                ATS-ready
            </span>
        </p>

        <div class="section-line"></div>

    </div>
    """, unsafe_allow_html=True)


    col1, col2, col3 = st.columns(3)


    with col1:
        st.markdown("""
        <div class="feature-card">

            <div class="card-icon"></div>

            <h3>
                Comprehensive Scoring
            </h3>

            <p>
                Get detailed scores across
                <span class="highlight-orange">
                    five key dimensions
                </span>
                that influence ATS compatibility.
            </p>

            <ul>
                <li>Formatting — <b>20%</b></li>
                <li>Keywords & Skills — <b>25%</b></li>
                <li>Content Quality — <b>25%</b></li>
                <li>Skill Validation — <b>15%</b></li>
                <li>ATS Compatibility — <b>15%</b></li>
            </ul>

        </div>
        """, unsafe_allow_html=True)


    with col2:
        st.markdown("""
        <div class="feature-card">

            <div class="card-icon"></div>

            <h3>
                AI Skill Validation
            </h3>

            <p>
                Verify that your claimed skills are
                <span class="highlight-orange">
                    actually demonstrated
                </span>
                through your projects and experience.
            </p>

            <ul>
                <li>Semantic skill analysis</li>
                <li>Project & experience validation</li>
                <li>Unsupported skill detection</li>
                <li>Evidence-based feedback</li>
            </ul>

        </div>
        """, unsafe_allow_html=True)


    with col3:
        st.markdown("""
        <div class="feature-card">

            <div class="card-icon"></div>

            <h3>
                Privacy First
            </h3>

            <p>
                Resume analysis runs locally,
                helping keep your resume information
                <span class="highlight-pink">
                    within your own environment
                </span>.
            </p>

            <ul>
                <li>No external API calls</li>
                <li>Local analysis</li>
                <li>Resume data stays private</li>
                <li>Secure workflow</li>
            </ul>

        </div>
        """, unsafe_allow_html=True)


    # ==========================================
    # SCORING DIMENSIONS
    # ==========================================

    st.markdown("""
    <div class="section-title">

        <h2>
            What We Analyze
        </h2>

        <p>
            Your resume is evaluated across
            <span class="underline-yellow">
                five important dimensions
            </span>
        </p>

        <div class="section-line"></div>

    </div>
    """, unsafe_allow_html=True)


    c1, c2, c3, c4, c5 = st.columns(5)


    with c1:
        st.markdown("""
        <div class="score-card">

            <div class="score-number">
                20%
            </div>

            <div class="score-label">
                Formatting
            </div>

        </div>
        """, unsafe_allow_html=True)


    with c2:
        st.markdown("""
        <div class="score-card">

            <div class="score-number">
                25%
            </div>

            <div class="score-label">
                Keywords & Skills
            </div>

        </div>
        """, unsafe_allow_html=True)


    with c3:
        st.markdown("""
        <div class="score-card">

            <div class="score-number">
                25%
            </div>

            <div class="score-label">
                Content Quality
            </div>

        </div>
        """, unsafe_allow_html=True)


    with c4:
        st.markdown("""
        <div class="score-card">

            <div class="score-number">
                15%
            </div>

            <div class="score-label">
                Skill Validation
            </div>

        </div>
        """, unsafe_allow_html=True)


    with c5:
        st.markdown("""
        <div class="score-card">

            <div class="score-number">
                15%
            </div>

            <div class="score-label">
                ATS Compatibility
            </div>

        </div>
        """, unsafe_allow_html=True)


    # ==========================================
    # HOW IT WORKS
    # ==========================================

    st.markdown("""
    <div class="section-title">

        <h2>
            How It Works
        </h2>

        <p>
            Analyze and improve your resume in
            <span class="underline-blue">
                three simple steps
            </span>
        </p>

        <div class="section-line"></div>

    </div>
    """, unsafe_allow_html=True)


    col1, col2, col3 = st.columns(3)


    with col1:
        st.markdown("""
        <div class="step-card">

            <div class="step-number">
                01
            </div>

            <h3>
                Upload Your Resume
            </h3>

            <p>
                Upload your resume in PDF, DOC,
                or DOCX format and start the
                analysis process.
            </p>

        </div>
        """, unsafe_allow_html=True)


    with col2:
        st.markdown("""
        <div class="step-card">

            <div class="step-number">
                02
            </div>

            <h3>
                AI Analysis
            </h3>

            <p>
                Local AI models analyze your resume
                across multiple ATS-focused dimensions.
            </p>

        </div>
        """, unsafe_allow_html=True)


    with col3:
        st.markdown("""
        <div class="step-card">

            <div class="step-number">
                03
            </div>

            <h3>
                Get Actionable Feedback
            </h3>

            <p>
                Receive detailed recommendations
                to improve your resume and make it
                more ATS-ready.
            </p>

        </div>
        """, unsafe_allow_html=True)


    # ==========================================
    # PRIVACY SECTION
    # ==========================================

    st.markdown("""
    <div class="privacy-card">

        <h3>
            Your Resume. Your Data. Your Privacy.
        </h3>

        <p>
            All analysis runs locally with no external
            API calls. Your resume data stays within
            <span class="highlight-yellow">
                your system
            </span>
            while you receive intelligent,
            ATS-focused feedback.
        </p>

    </div>
    """, unsafe_allow_html=True)


    # ==========================================
    # FOOTER
    # ==========================================

    st.markdown("""
    <div class="developer-card">

        <h3>
            Developed by Sunil Kumar Yadav
        </h3>

        <div class="developer-role">
            AI & Full Stack Developer
        </div>

        <div>

            <a href="https://github.com/wineerteam"
               target="_blank">
                GitHub
            </a>

            <a href="https://www.linkedin.com/in/sunil-kumar-yadav-abb468303/"
               target="_blank">
                LinkedIn
            </a>

        </div>

        <div class="copyright">
            © 2026 All Rights Reserved
        </div>

    </div>
    """, unsafe_allow_html=True)
