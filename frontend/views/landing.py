import streamlit as st


def render():

    # =========================================================
    # PAGE CSS
    # =========================================================

    st.markdown("""
    <style>

    /* =====================================================
       GLOBAL
       ===================================================== */

    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    * {
        box-sizing: border-box;
    }


    /* =====================================================
       HERO SECTION
       ===================================================== */

    .main-header {
        position: relative;
        overflow: hidden;

        text-align: center;

        padding: 4.2rem 2rem;

        margin-bottom: 1.5rem;

        border-radius: 30px;

        background:
            radial-gradient(
                circle at 88% 12%,
                rgba(250, 204, 21, 0.22),
                transparent 25%
            ),
            radial-gradient(
                circle at 10% 88%,
                rgba(236, 72, 153, 0.18),
                transparent 28%
            ),
            linear-gradient(
                135deg,
                #0f172a 0%,
                #1e3a8a 35%,
                #2563eb 70%,
                #06b6d4 100%
            );

        border: 1px solid rgba(255,255,255,0.15);

        box-shadow:
            0 25px 65px rgba(15,23,42,0.35),
            inset 0 1px 0 rgba(255,255,255,0.12);

        transition:
            transform 0.3s ease,
            box-shadow 0.3s ease;
    }


    .main-header:hover {
        transform:
            translateY(-5px)
            scale(1.005);

        box-shadow:
            0 35px 80px rgba(15,23,42,0.42);
    }


    .main-header::before {
        content: "";

        position: absolute;

        width: 260px;
        height: 260px;

        top: -160px;
        right: -80px;

        border-radius: 50%;

        background: rgba(250,204,21,0.12);

        filter: blur(18px);

        pointer-events: none;
    }


    .main-header::after {
        content: "";

        position: absolute;

        width: 230px;
        height: 230px;

        bottom: -150px;
        left: -90px;

        border-radius: 50%;

        background: rgba(236,72,153,0.12);

        filter: blur(18px);

        pointer-events: none;
    }


    .hero-content {
        position: relative;
        z-index: 2;
    }


    .hero-badge {
        display: inline-block;

        padding: 8px 18px;

        margin-bottom: 20px;

        border-radius: 50px;

        background: rgba(250,204,21,0.13);

        border: 1px solid rgba(250,204,21,0.50);

        color: #fef3c7;

        font-size: 12px;

        font-weight: 800;

        letter-spacing: 1.2px;

        box-shadow:
            0 7px 22px rgba(250,204,21,0.10);
    }


    .main-header h1 {
        color: #ffffff;

        font-size: 3.5rem;

        font-weight: 850;

        letter-spacing: -1.5px;

        line-height: 1.1;

        margin: 0 0 15px 0;

        text-shadow:
            0 5px 22px rgba(0,0,0,0.25);
    }


    .main-header h3 {
        color: #e0f2fe;

        font-size: 1.25rem;

        font-weight: 500;

        line-height: 1.5;

        margin: 0 0 16px 0;
    }


    .main-header p {
        max-width: 730px;

        margin: auto;

        color: #dbeafe;

        font-size: 1rem;

        line-height: 1.75;
    }


    /* =====================================================
       TEXT ACCENTS
       ===================================================== */

    .yellow-text {
        color: #facc15;

        font-weight: 800;
    }


    .orange-text {
        color: #fb923c;

        font-weight: 800;
    }


    .pink-text {
        color: #f9a8d4;

        font-weight: 800;
    }


    .blue-text {
        color: #38bdf8;

        font-weight: 800;
    }


    .blue-underline {
        text-decoration: underline;

        text-decoration-color: #38bdf8;

        text-decoration-thickness: 2px;

        text-underline-offset: 4px;
    }


    .yellow-underline {
        text-decoration: underline;

        text-decoration-color: #facc15;

        text-decoration-thickness: 2px;

        text-underline-offset: 4px;
    }


    /* =====================================================
       SECTION HEADING
       ===================================================== */

    .section-heading {
        text-align: center;

        margin-top: 3.2rem;

        margin-bottom: 1.8rem;
    }


    .section-heading h2 {
        color: #0f172a;

        font-size: 2rem;

        font-weight: 850;

        letter-spacing: -0.5px;

        margin: 0 0 8px 0;
    }


    .section-heading p {
        color: #64748b;

        font-size: 14px;

        line-height: 1.6;

        margin: 0;
    }


    .section-line {
        width: 75px;

        height: 4px;

        margin: 12px auto 0;

        border-radius: 50px;

        background:
            linear-gradient(
                90deg,
                #2563eb,
                #06b6d4,
                #facc15
            );

        box-shadow:
            0 3px 12px rgba(37,99,235,0.20);
    }


    /* =====================================================
       CTA BUTTON
       ===================================================== */

    .stButton > button {
        min-height: 56px;

        border-radius: 16px;

        font-size: 16px;

        font-weight: 750;

        box-shadow:
            0 10px 28px rgba(37,99,235,0.22);

        transition:
            transform 0.25s ease,
            box-shadow 0.25s ease;
    }


    .stButton > button:hover {
        transform:
            translateY(-4px)
            scale(1.015);

        box-shadow:
            0 18px 42px rgba(37,99,235,0.35);
    }


    /* =====================================================
       FEATURE CARDS
       ===================================================== */

    .feature-card {
        position: relative;

        overflow: hidden;

        min-height: 330px;

        padding: 29px;

        border-radius: 25px;

        background:
            linear-gradient(
                145deg,
                #ffffff 0%,
                #f8fafc 100%
            );

        border: 1px solid #e2e8f0;

        box-shadow:
            0 10px 28px rgba(15,23,42,0.07);

        transform:
            perspective(1000px)
            translateZ(0);

        transition:
            transform 0.3s ease,
            box-shadow 0.3s ease,
            border-color 0.3s ease;
    }


    .feature-card:hover {
        transform:
            perspective(1000px)
            translateY(-12px)
            translateZ(25px)
            scale(1.025)
            rotateX(1deg);

        box-shadow:
            0 30px 65px rgba(15,23,42,0.20);

        border-color: #93c5fd;

        z-index: 10;
    }


    .feature-card::after {
        content: "";

        position: absolute;

        width: 170px;
        height: 170px;

        right: -90px;
        bottom: -90px;

        border-radius: 50%;

        opacity: 0.10;

        transition:
            transform 0.4s ease,
            opacity 0.4s ease;
    }


    .feature-card:hover::after {
        transform: scale(1.5);

        opacity: 0.18;
    }


    .blue-card {
        border-top: 4px solid #2563eb;
    }


    .blue-card::after {
        background: #06b6d4;
    }


    .yellow-card {
        border-top: 4px solid #facc15;
    }


    .yellow-card::after {
        background: #f97316;
    }


    .pink-card {
        border-top: 4px solid #ec4899;
    }


    .pink-card::after {
        background: #ef4444;
    }


    /* =====================================================
       CARD ICON
       ===================================================== */

    .card-icon {
        width: 56px;
        height: 56px;

        display: flex;

        align-items: center;
        justify-content: center;

        border-radius: 17px;

        margin-bottom: 19px;

        transition:
            transform 0.3s ease;
    }


    .feature-card:hover .card-icon {
        transform:
            translateY(-5px)
            rotate(5deg)
            scale(1.08);
    }


    .blue-icon {
        background:
            linear-gradient(
                135deg,
                #dbeafe,
                #cffafe
            );
    }


    .yellow-icon {
        background:
            linear-gradient(
                135deg,
                #fef3c7,
                #ffedd5
            );
    }


    .pink-icon {
        background:
            linear-gradient(
                135deg,
                #fce7f3,
                #fee2e2
            );
    }


    .icon-shape {
        width: 22px;
        height: 22px;

        border-radius: 7px;

        transform: rotate(45deg);
    }


    .blue-shape {
        background:
            linear-gradient(
                135deg,
                #2563eb,
                #06b6d4
            );

        box-shadow:
            7px 7px 0 rgba(37,99,235,0.13);
    }


    .yellow-shape {
        background:
            linear-gradient(
                135deg,
                #facc15,
                #f97316
            );

        box-shadow:
            7px 7px 0 rgba(249,115,22,0.13);
    }


    .pink-shape {
        background:
            linear-gradient(
                135deg,
                #ec4899,
                #ef4444
            );

        box-shadow:
            7px 7px 0 rgba(236,72,153,0.13);
    }


    /* =====================================================
       FEATURE CONTENT
       ===================================================== */

    .feature-content {
        position: relative;

        z-index: 2;
    }


    .feature-card h3 {
        color: #0f172a;

        font-size: 20px;

        font-weight: 800;

        line-height: 1.3;

        margin: 0 0 11px 0;
    }


    .feature-card p {
        color: #475569;

        font-size: 14px;

        line-height: 1.75;

        margin: 0 0 10px 0;
    }


    .feature-card ul {
        padding-left: 20px;

        margin: 13px 0 0 0;
    }


    .feature-card li {
        color: #475569;

        font-size: 13px;

        line-height: 1.9;
    }


    .blue-card li::marker {
        color: #2563eb;
    }


    .yellow-card li::marker {
        color: #f97316;
    }


    .pink-card li::marker {
        color: #ec4899;
    }


    /* =====================================================
       SCORE CARDS
       ===================================================== */

    .score-card {
        position: relative;

        overflow: hidden;

        text-align: center;

        padding: 24px 8px;

        border-radius: 20px;

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
            transform 0.3s ease,
            box-shadow 0.3s ease,
            border-color 0.3s ease;
    }


    .score-card:hover {
        transform:
            translateY(-10px)
            scale(1.05);

        box-shadow:
            0 25px 48px rgba(15,23,42,0.17);

        border-color: #93c5fd;

        z-index: 10;
    }


    .score-card::before {
        content: "";

        position: absolute;

        left: 25%;
        right: 25%;

        bottom: 0;

        height: 3px;

        border-radius: 20px;
    }


    .score-blue::before {
        background: #2563eb;
    }


    .score-yellow::before {
        background: #facc15;
    }


    .score-orange::before {
        background: #f97316;
    }


    .score-pink::before {
        background: #ec4899;
    }


    .score-red::before {
        background: #ef4444;
    }


    .score-number {
        font-size: 29px;

        font-weight: 850;

        margin-bottom: 6px;
    }


    .score-label {
        color: #475569;

        font-size: 12px;

        font-weight: 650;

        line-height: 1.4;
    }


    .score-blue {
        color: #2563eb;
    }


    .score-yellow {
        color: #eab308;
    }


    .score-orange {
        color: #f97316;
    }


    .score-pink {
        color: #ec4899;
    }


    .score-red {
        color: #ef4444;
    }


    /* =====================================================
       HOW IT WORKS
       ===================================================== */

    .step-card {
        position: relative;

        min-height: 205px;

        padding: 28px;

        border-radius: 23px;

        background:
            linear-gradient(
                145deg,
                #ffffff,
                #f8fafc
            );

        border: 1px solid #e2e8f0;

        box-shadow:
            0 9px 25px rgba(15,23,42,0.06);

        transition:
            transform 0.3s ease,
            box-shadow 0.3s ease,
            border-color 0.3s ease;
    }


    .step-card:hover {
        transform:
            translateY(-12px)
            scale(1.025);

        box-shadow:
            0 30px 58px rgba(15,23,42,0.18);

        border-color: #93c5fd;

        z-index: 10;
    }


    .step-number {
        width: 46px;
        height: 46px;

        display: flex;

        align-items: center;
        justify-content: center;

        border-radius: 14px;

        color: #ffffff;

        font-size: 14px;

        font-weight: 850;

        margin-bottom: 18px;

        box-shadow:
            0 8px 18px rgba(15,23,42,0.14);

        transition:
            transform 0.3s ease;
    }


    .step-card:hover .step-number {
        transform:
            translateY(-4px)
            rotate(-4deg)
            scale(1.08);
    }


    .step-blue {
        background:
            linear-gradient(
                135deg,
                #2563eb,
                #06b6d4
            );
    }


    .step-yellow {
        background:
            linear-gradient(
                135deg,
                #facc15,
                #f97316
            );
    }


    .step-pink {
        background:
            linear-gradient(
                135deg,
                #ec4899,
                #ef4444
            );
    }


    .step-card h3 {
        color: #0f172a;

        font-size: 18px;

        font-weight: 800;

        line-height: 1.35;

        margin: 0 0 9px 0;
    }


    .step-card p {
        color: #64748b;

        font-size: 14px;

        line-height: 1.7;

        margin: 0;
    }


    /* =====================================================
       PRIVACY CARD
       ===================================================== */

    .privacy-card {
        position: relative;

        overflow: hidden;

        margin-top: 32px;

        padding: 34px;

        border-radius: 26px;

        background:
            radial-gradient(
                circle at 92% 15%,
                rgba(250,204,21,0.22),
                transparent 27%
            ),
            radial-gradient(
                circle at 8% 90%,
                rgba(236,72,153,0.17),
                transparent 30%
            ),
            linear-gradient(
                135deg,
                #0f172a,
                #1e293b
            );

        border: 1px solid rgba(255,255,255,0.10);

        box-shadow:
            0 20px 50px rgba(15,23,42,0.24);

        transition:
            transform 0.3s ease,
            box-shadow 0.3s ease;
    }


    .privacy-card:hover {
        transform:
            translateY(-8px)
            scale(1.01);

        box-shadow:
            0 32px 65px rgba(15,23,42,0.32);
    }


    .privacy-content {
        position: relative;

        z-index: 2;
    }


    .privacy-card h3 {
        color: #ffffff;

        font-size: 22px;

        font-weight: 800;

        margin: 0 0 11px 0;
    }


    .privacy-card p {
        color: #cbd5e1;

        font-size: 14px;

        line-height: 1.8;

        margin: 0;
    }


    /* =====================================================
       FOOTER
       ===================================================== */

    .developer-card {
        text-align: center;

        padding: 32px;

        margin-top: 40px;

        border-radius: 25px;

        background:
            linear-gradient(
                135deg,
                #0f172a,
                #1e293b
            );

        border: 1px solid rgba(255,255,255,0.10);

        box-shadow:
            0 16px 42px rgba(15,23,42,0.20);

        transition:
            transform 0.3s ease,
            box-shadow 0.3s ease;
    }


    .developer-card:hover {
        transform:
            translateY(-7px);

        box-shadow:
            0 25px 55px rgba(15,23,42,0.28);
    }


    .developer-card h4 {
        color: #ffffff;

        font-size: 19px;

        font-weight: 800;

        margin: 0 0 8px 0;
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

        margin: 0 13px;

        font-size: 14px;

        font-weight: 650;

        transition:
            color 0.2s ease;
    }


    .developer-card a:hover {
        color: #facc15;
    }


    .copyright {
        margin-top: 20px;

        color: #94a3b8;

        font-size: 12px;
    }


    /* =====================================================
       MOBILE
       ===================================================== */

    @media (max-width: 768px) {

        .main-header {
            padding: 3rem 1.4rem;
        }

        .main-header h1 {
            font-size: 2.35rem;
        }

        .main-header h3 {
            font-size: 1.05rem;
        }

        .feature-card,
        .step-card {
            min-height: auto;
            margin-bottom: 20px;
        }

        .score-card {
            margin-bottom: 15px;
        }

        .privacy-card {
            padding: 25px;
        }

        .developer-card {
            padding: 25px 15px;
        }
    }

    </style>
    """, unsafe_allow_html=True)


    # =========================================================
    # HERO
    # =========================================================

    st.html("""
    <div class="main-header">

        <div class="hero-content">

            <div class="hero-badge">
                AI-POWERED RESUME ANALYSIS
            </div>

            <h1>
                ATS Resume Scorer
            </h1>

            <h3>
                Optimize Your Resume for
                <span class="yellow-text">
                    Applicant Tracking Systems
                </span>
            </h3>

            <p>
                Get instant feedback on your resume's
                <span class="blue-underline">
                    ATS compatibility
                </span>
                with
                <span class="yellow-text">
                    AI-powered analysis
                </span>.
            </p>

        </div>

    </div>
    """)


    # =========================================================
    # CTA BUTTON
    # =========================================================

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        # =====================================================
        # ORIGINAL NAVIGATION LOGIC - UNCHANGED
        # =====================================================

        if st.button(
            "Start Analyzing Your Resume",
            use_container_width=True,
            type="primary"
        ):

            st.session_state.current_view = 'scorer'

            st.rerun()


    st.markdown("---")


    # =========================================================
    # KEY FEATURES HEADING
    # =========================================================

    st.html("""
    <div class="section-heading">

        <h2>
            Key Features
        </h2>

        <p>
            Powerful tools to make your resume
            <span class="blue-underline">
                ATS-ready
            </span>
        </p>

        <div class="section-line"></div>

    </div>
    """)


    # =========================================================
    # FEATURE CARDS
    # =========================================================

    col1, col2, col3 = st.columns(3)


    with col1:

        st.html("""
        <div class="feature-card blue-card">

            <div class="feature-content">

                <div class="card-icon blue-icon">
                    <div class="icon-shape blue-shape"></div>
                </div>

                <h3>
                    Comprehensive Scoring
                </h3>

                <p>
                    Get detailed scores across
                    <span class="orange-text">
                        5 key dimensions
                    </span>
                    that influence ATS compatibility.
                </p>

                <ul>
                    <li>Formatting — <b>20%</b></li>
                    <li>Keywords &amp; Skills — <b>25%</b></li>
                    <li>Content Quality — <b>25%</b></li>
                    <li>Skill Validation — <b>15%</b></li>
                    <li>ATS Compatibility — <b>15%</b></li>
                </ul>

            </div>

        </div>
        """)


    with col2:

        st.html("""
        <div class="feature-card yellow-card">

            <div class="feature-content">

                <div class="card-icon yellow-icon">
                    <div class="icon-shape yellow-shape"></div>
                </div>

                <h3>
                    AI Skill Validation
                </h3>

                <p>
                    Verify that your claimed skills are
                    <span class="orange-text">
                        actually demonstrated
                    </span>
                    through your projects and experience.
                </p>

                <ul>
                    <li>Semantic skill analysis</li>
                    <li>Project &amp; experience validation</li>
                    <li>Unsupported skill detection</li>
                    <li>Evidence-based feedback</li>
                </ul>

            </div>

        </div>
        """)


    with col3:

        st.html("""
        <div class="feature-card pink-card">

            <div class="feature-content">

                <div class="card-icon pink-icon">
                    <div class="icon-shape pink-shape"></div>
                </div>

                <h3>
                    Privacy First
                </h3>

                <p>
                    Resume analysis runs locally,
                    keeping your resume information
                    <span class="pink-text">
                        within your environment
                    </span>.
                </p>

                <ul>
                    <li>No external API calls</li>
                    <li>Local analysis</li>
                    <li>Resume data stays private</li>
                    <li>Secure workflow</li>
                </ul>

            </div>

        </div>
        """)


    # =========================================================
    # WHAT WE ANALYZE
    # =========================================================

    st.html("""
    <div class="section-heading">

        <h2>
            What We Analyze
        </h2>

        <p>
            Your resume is evaluated across
            <span class="yellow-underline">
                five important dimensions
            </span>
        </p>

        <div class="section-line"></div>

    </div>
    """)


    c1, c2, c3, c4, c5 = st.columns(5)


    with c1:

        st.html("""
        <div class="score-card">

            <div class="score-number score-blue">
                20%
            </div>

            <div class="score-label">
                Formatting
            </div>

        </div>
        """)


    with c2:

        st.html("""
        <div class="score-card">

            <div class="score-number score-yellow">
                25%
            </div>

            <div class="score-label">
                Keywords &amp; Skills
            </div>

        </div>
        """)


    with c3:

        st.html("""
        <div class="score-card">

            <div class="score-number score-orange">
                25%
            </div>

            <div class="score-label">
                Content Quality
            </div>

        </div>
        """)


    with c4:

        st.html("""
        <div class="score-card">

            <div class="score-number score-pink">
                15%
            </div>

            <div class="score-label">
                Skill Validation
            </div>

        </div>
        """)


    with c5:

        st.html("""
        <div class="score-card">

            <div class="score-number score-red">
                15%
            </div>

            <div class="score-label">
                ATS Compatibility
            </div>

        </div>
        """)


    # =========================================================
    # HOW IT WORKS
    # =========================================================

    st.html("""
    <div class="section-heading">

        <h2>
            How It Works
        </h2>

        <p>
            Analyze and improve your resume in
            <span class="blue-underline">
                three simple steps
            </span>
        </p>

        <div class="section-line"></div>

    </div>
    """)


    col1, col2, col3 = st.columns(3)


    with col1:

        st.html("""
        <div class="step-card">

            <div class="step-number step-blue">
                01
            </div>

            <h3>
                Upload Your Resume
            </h3>

            <p>
                Upload your resume in PDF, DOC,
                or DOCX format to begin analysis.
            </p>

        </div>
        """)


    with col2:

        st.html("""
        <div class="step-card">

            <div class="step-number step-yellow">
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
        """)


    with col3:

        st.html("""
        <div class="step-card">

            <div class="step-number step-pink">
                03
            </div>

            <h3>
                Get Actionable Feedback
            </h3>

            <p>
                Receive detailed recommendations
                to improve your resume.
            </p>

        </div>
        """)


    # =========================================================
    # PRIVACY SECTION
    # =========================================================

    st.html("""
    <div class="privacy-card">

        <div class="privacy-content">

            <h3>
                Your Resume. Your Data. Your Privacy.
            </h3>

            <p>
                All analysis runs locally with no external
                API calls. Your resume data stays within
                <span class="yellow-text">
                    your system
                </span>
                while you receive intelligent,
                ATS-focused feedback.
            </p>

        </div>

    </div>
    """)


    # =========================================================
    # FOOTER
    # =========================================================

    st.html("""
    <div class="developer-card">

        <h4>
            Developed by Sunil Kumar Yadav
        </h4>

        <div class="developer-role">
            AI &amp; Full Stack Developer
        </div>

        <div>

            <a
                href="https://github.com/wineerteam"
                target="_blank"
            >
                GitHub
            </a>

            <a
                href="https://www.linkedin.com/in/sunil-kumar-yadav-abb468303/"
                target="_blank"
            >
                LinkedIn
            </a>

        </div>

        <div class="copyright">
            © 2026 All Rights Reserved
        </div>

    </div>
    """)
