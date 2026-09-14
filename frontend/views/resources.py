import streamlit as st


def _apply_styles():
    st.markdown(
        """
        <style>

        /* =========================================
           GLOBAL
        ========================================= */

        .block-container {
            max-width: 1220px;
            padding-top: 1.5rem;
            padding-bottom: 3rem;
        }

        /* =========================================
           HERO
        ========================================= */

        .resources-hero {
            position: relative;
            overflow: hidden;

            padding: 42px 42px;
            margin-bottom: 30px;

            border-radius: 30px;

            background:
                radial-gradient(
                    circle at 90% 15%,
                    rgba(250, 204, 21, 0.22),
                    transparent 25%
                ),
                radial-gradient(
                    circle at 10% 90%,
                    rgba(236, 72, 153, 0.18),
                    transparent 28%
                ),
                linear-gradient(
                    135deg,
                    #0f172a 0%,
                    #172554 38%,
                    #1d4ed8 72%,
                    #0891b2 100%
                );

            border: 1px solid rgba(255,255,255,0.12);

            box-shadow:
                0 25px 65px rgba(15,23,42,0.28),
                inset 0 1px 0 rgba(255,255,255,0.12);

            transition:
                transform 0.3s ease,
                box-shadow 0.3s ease;
        }

        .resources-hero:hover {
            transform: translateY(-5px) scale(1.005);

            box-shadow:
                0 35px 80px rgba(15,23,42,0.34);
        }

        .resources-hero::before {
            content: "";

            position: absolute;

            width: 230px;
            height: 230px;

            right: -100px;
            top: -110px;

            border-radius: 50%;

            border:
                1px solid rgba(250,204,21,0.15);

            background:
                rgba(250,204,21,0.08);
        }

        .resources-hero::after {
            content: "";

            position: absolute;

            width: 180px;
            height: 180px;

            left: -90px;
            bottom: -100px;

            border-radius: 50%;

            border:
                1px solid rgba(236,72,153,0.15);

            background:
                rgba(236,72,153,0.08);
        }

        .hero-content {
            position: relative;
            z-index: 2;
        }

        .hero-badge {
            display: inline-block;

            padding: 8px 15px;
            margin-bottom: 16px;

            border-radius: 50px;

            background:
                rgba(250,204,21,0.12);

            border:
                1px solid rgba(250,204,21,0.40);

            color:
                #fef3c7;

            font-size: 11px;

            font-weight: 800;

            letter-spacing: 1.4px;
        }

        .resources-hero h1 {
            color: #ffffff;

            font-size: 3rem;

            font-weight: 850;

            letter-spacing: -1px;

            margin: 0 0 12px 0;

            line-height: 1.12;
        }

        .resources-hero p {
            max-width: 780px;

            color: #dbeafe;

            font-size: 15px;

            line-height: 1.75;

            margin: 0;
        }

        .hero-highlight {
            color: #facc15;

            font-weight: 800;

            text-decoration: underline;

            text-decoration-color:
                rgba(250,204,21,0.75);

            text-decoration-thickness: 2px;

            text-underline-offset: 4px;
        }

        /* =========================================
           SECTION HEADER
        ========================================= */

        .section-header {
            margin: 32px 0 20px 0;
        }

        .section-header h2 {
            margin: 0 0 6px 0;

            color: #0f172a;

            font-size: 1.65rem;

            font-weight: 850;

            letter-spacing: -0.5px;
        }

        .section-header p {
            margin: 0;

            color: #64748b;

            font-size: 13px;

            line-height: 1.6;
        }

        .section-line {
            width: 72px;

            height: 4px;

            margin-top: 11px;

            border-radius: 50px;

            background:
                linear-gradient(
                    90deg,
                    #2563eb,
                    #06b6d4,
                    #facc15
                );
        }

        /* =========================================
           DO / DON'T CARDS
        ========================================= */

        .guide-card {
            position: relative;

            overflow: hidden;

            min-height: 345px;

            padding: 27px;

            border-radius: 24px;

            background:
                linear-gradient(
                    145deg,
                    #ffffff,
                    #f8fafc
                );

            border:
                1px solid #e2e8f0;

            box-shadow:
                0 10px 28px
                rgba(15,23,42,0.07);

            transition:
                transform 0.3s ease,
                box-shadow 0.3s ease,
                border-color 0.3s ease;
        }

        .guide-card:hover {
            transform:
                translateY(-10px)
                scale(1.015);

            box-shadow:
                0 28px 60px
                rgba(15,23,42,0.15);
        }

        .guide-card::after {
            content: "";

            position: absolute;

            width: 150px;
            height: 150px;

            right: -80px;
            bottom: -80px;

            border-radius: 50%;

            opacity: 0.10;

            transition:
                transform 0.35s ease;
        }

        .guide-card:hover::after {
            transform: scale(1.6);
        }

        .do-card {
            border-top:
                5px solid #22c55e;
        }

        .do-card::after {
            background:
                #22c55e;
        }

        .dont-card {
            border-top:
                5px solid #ef4444;
        }

        .dont-card::after {
            background:
                #ef4444;
        }

        .guide-label {
            display: inline-block;

            padding: 6px 12px;

            margin-bottom: 12px;

            border-radius: 50px;

            font-size: 10px;

            font-weight: 850;

            letter-spacing: 0.8px;
        }

        .do-label {
            color: #166534;

            background:
                #dcfce7;
        }

        .dont-label {
            color: #b91c1c;

            background:
                #fee2e2;
        }

        .guide-card h3 {
            color:
                #0f172a;

            font-size:
                21px;

            font-weight:
                850;

            margin:
                0 0 18px 0;
        }

        .guide-list {
            position: relative;

            z-index: 2;

            margin: 0;

            padding: 0;

            list-style: none;
        }

        .guide-list li {
            position: relative;

            padding:
                9px 0 9px 23px;

            color:
                #475569;

            font-size:
                13px;

            line-height:
                1.55;

            border-bottom:
                1px solid #f1f5f9;
        }

        .guide-list li:last-child {
            border-bottom:
                none;
        }

        .do-card .guide-list li::before {
            content: "✓";

            position: absolute;

            left: 0;

            color:
                #16a34a;

            font-weight:
                900;
        }

        .dont-card .guide-list li::before {
            content: "×";

            position: absolute;

            left: 2px;

            color:
                #dc2626;

            font-size:
                17px;

            font-weight:
                900;
        }

        /* =========================================
           KEYWORD INDUSTRY CARDS
        ========================================= */

        .keyword-card {
            position: relative;

            min-height: 245px;

            padding: 26px;

            border-radius: 22px;

            background:
                linear-gradient(
                    145deg,
                    #ffffff,
                    #f8fafc
                );

            border:
                1px solid #e2e8f0;

            box-shadow:
                0 9px 25px
                rgba(15,23,42,0.06);

            transition:
                transform 0.3s ease,
                box-shadow 0.3s ease,
                border-color 0.3s ease;
        }

        .keyword-card:hover {
            transform:
                translateY(-9px)
                scale(1.015);

            box-shadow:
                0 26px 55px
                rgba(15,23,42,0.14);
        }

        .keyword-blue {
            border-top:
                4px solid #2563eb;
        }

        .keyword-yellow {
            border-top:
                4px solid #facc15;
        }

        .keyword-pink {
            border-top:
                4px solid #ec4899;
        }

        .keyword-card h3 {
            color:
                #0f172a;

            font-size:
                18px;

            font-weight:
                850;

            margin:
                0 0 14px 0;
        }

        .keyword-card p {
            color:
                #64748b;

            font-size:
                12px;

            font-weight:
                700;

            margin:
                0 0 10px 0;
        }

        .keyword-list {
            display:
                flex;

            flex-wrap:
                wrap;

            gap:
                8px;
        }

        .keyword {
            padding:
                6px 10px;

            border-radius:
                50px;

            background:
                #eff6ff;

            color:
                #1d4ed8;

            border:
                1px solid #dbeafe;

            font-size:
                11px;

            font-weight:
                700;

            transition:
                transform 0.2s ease;
        }

        .keyword:hover {
            transform:
                translateY(-3px);
        }

        .keyword-yellow-tag {
            background:
                #fef3c7;

            color:
                #b45309;

            border-color:
                #fde68a;
        }

        .keyword-pink-tag {
            background:
                #fce7f3;

            color:
                #be185d;

            border-color:
                #fbcfe8;
        }

        /* =========================================
           TABS
        ========================================= */

        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;

            padding:
                7px;

            border-radius:
                16px;

            background:
                #f1f5f9;
        }

        .stTabs [data-baseweb="tab"] {
            height:
                43px;

            padding:
                0 20px;

            border-radius:
                11px;

            color:
                #475569;

            font-weight:
                750;

            transition:
                transform 0.2s ease;
        }

        .stTabs [data-baseweb="tab"]:hover {
            transform:
                translateY(-2px);
        }

        .stTabs [aria-selected="true"] {
            color:
                #1d4ed8 !important;

            background:
                #ffffff;

            box-shadow:
                0 5px 16px
                rgba(15,23,42,0.09);
        }

        /* =========================================
           TEMPLATE CARD
        ========================================= */

        .template-card {
            position: relative;

            overflow: hidden;

            padding:
                30px;

            margin-top:
                25px;

            border-radius:
                24px;

            background:
                radial-gradient(
                    circle at 90% 15%,
                    rgba(250,204,21,0.16),
                    transparent 25%
                ),
                linear-gradient(
                    135deg,
                    #eff6ff,
                    #f0fdfa
                );

            border:
                1px solid #bfdbfe;

            box-shadow:
                0 12px 32px
                rgba(37,99,235,0.08);

            transition:
                transform 0.3s ease,
                box-shadow 0.3s ease;
        }

        .template-card:hover {
            transform:
                translateY(-7px);

            box-shadow:
                0 25px 55px
                rgba(37,99,235,0.13);
        }

        .template-card h3 {
            color:
                #0f172a;

            font-size:
                20px;

            font-weight:
                850;

            margin:
                0 0 7px 0;
        }

        .template-card p {
            color:
                #64748b;

            font-size:
                13px;

            line-height:
                1.65;

            margin:
                0;
        }

        .coming-soon {
            display:
                inline-block;

            margin-top:
                15px;

            padding:
                7px 13px;

            border-radius:
                50px;

            background:
                #fef3c7;

            color:
                #92400e;

            border:
                1px solid #fde68a;

            font-size:
                10px;

            font-weight:
                850;

            letter-spacing:
                0.6px;
        }

        /* =========================================
           SIDEBAR
        ========================================= */

        [data-testid="stSidebar"] {
            background:
                linear-gradient(
                    180deg,
                    #f8fafc,
                    #eef2ff
                );
        }

        /* =========================================
           RESPONSIVE
        ========================================= */

        @media (max-width: 768px) {

            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }

            .resources-hero {
                padding:
                    30px 22px;
            }

            .resources-hero h1 {
                font-size:
                    2.25rem;
            }

            .resources-hero p {
                font-size:
                    14px;
            }

            .guide-card {
                min-height:
                    auto;

                margin-bottom:
                    18px;
            }

            .keyword-card {
                margin-bottom:
                    18px;
            }

            .section-header h2 {
                font-size:
                    1.4rem;
            }
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


def render():
    """Render the resources page"""

    _apply_styles()

    # ========================================================
    # HERO
    # ========================================================

    st.html(
        """
        <div class="resources-hero">

            <div class="hero-content">

                <div class="hero-badge">
                    RESUME OPTIMIZATION GUIDE
                </div>

                <h1>
                    Resources & Tips
                </h1>

                <p>
                    Learn how to create a
                    <span class="hero-highlight">
                        clean, ATS-friendly resume
                    </span>
                    that is easier for applicant tracking
                    systems to understand and evaluate.
                </p>

            </div>

        </div>
        """
    )

    # ========================================================
    # ATS TIPS
    # ========================================================

    st.html(
        """
        <div class="section-header">

            <h2>
                ATS Optimization Tips
            </h2>

            <p>
                Simple practices that can improve how
                applicant tracking systems process your resume.
            </p>

            <div class="section-line"></div>

        </div>
        """
    )

    col1, col2 = st.columns(
        2,
        gap="large",
    )

    # ========================================================
    # DO'S
    # ========================================================

    with col1:

        st.html(
            """
            <div class="guide-card do-card">

                <span class="guide-label do-label">
                    RECOMMENDED
                </span>

                <h3>
                    Do's
                </h3>

                <ul class="guide-list">

                    <li>
                        Use standard section headings
                    </li>

                    <li>
                        Include relevant keywords from
                        the job description
                    </li>

                    <li>
                        Use simple, clean formatting
                    </li>

                    <li>
                        List skills explicitly
                    </li>

                    <li>
                        Quantify achievements with numbers
                    </li>

                    <li>
                        Use standard fonts such as
                        Arial, Calibri and Times New Roman
                    </li>

                    <li>
                        Save your resume as PDF or DOCX
                    </li>

                </ul>

            </div>
            """
        )

    # ========================================================
    # DON'TS
    # ========================================================

    with col2:

        st.html(
            """
            <div class="guide-card dont-card">

                <span class="guide-label dont-label">
                    AVOID
                </span>

                <h3>
                    Don'ts
                </h3>

                <ul class="guide-list">

                    <li>
                        Avoid tables and text boxes
                    </li>

                    <li>
                        Do not place important information
                        inside headers or footers
                    </li>

                    <li>
                        Avoid images and unnecessary graphics
                    </li>

                    <li>
                        Do not use unusual fonts
                    </li>

                    <li>
                        Avoid complex multi-column layouts
                    </li>

                    <li>
                        Do not keyword stuff
                    </li>

                    <li>
                        Avoid abbreviations without spelling
                        them out first
                    </li>

                </ul>

            </div>
            """
        )

    st.markdown("---")

    # ========================================================
    # KEYWORDS
    # ========================================================

    st.html(
        """
        <div class="section-header">

            <h2>
                Common ATS Keywords by Industry
            </h2>

            <p>
                Examples of skills and technologies that
                can be relevant to different career paths.
            </p>

            <div class="section-line"></div>

        </div>
        """
    )

    tab1, tab2, tab3 = st.tabs(
        [
            "Technology",
            "Business",
            "Creative",
        ]
    )

    # ========================================================
    # TECH
    # ========================================================

    with tab1:

        st.html(
            """
            <div class="keyword-card keyword-blue">

                <h3>
                    Software Development
                </h3>

                <p>
                    Example ATS-friendly keywords
                </p>

                <div class="keyword-list">

                    <span class="keyword">
                        Python
                    </span>

                    <span class="keyword">
                        Java
                    </span>

                    <span class="keyword">
                        JavaScript
                    </span>

                    <span class="keyword">
                        React
                    </span>

                    <span class="keyword">
                        Django
                    </span>

                    <span class="keyword">
                        Spring
                    </span>

                    <span class="keyword">
                        Git
                    </span>

                    <span class="keyword">
                        Docker
                    </span>

                    <span class="keyword">
                        Kubernetes
                    </span>

                    <span class="keyword">
                        Agile
                    </span>

                    <span class="keyword">
                        Scrum
                    </span>

                    <span class="keyword">
                        CI/CD
                    </span>

                </div>

            </div>
            """
        )

    # ========================================================
    # BUSINESS
    # ========================================================

    with tab2:

        st.html(
            """
            <div class="keyword-card keyword-yellow">

                <h3>
                    Business & Management
                </h3>

                <p>
                    Example ATS-friendly keywords
                </p>

                <div class="keyword-list">

                    <span class="keyword keyword-yellow-tag">
                        Project Management
                    </span>

                    <span class="keyword keyword-yellow-tag">
                        Stakeholder Engagement
                    </span>

                    <span class="keyword keyword-yellow-tag">
                        Budget Management
                    </span>

                    <span class="keyword keyword-yellow-tag">
                        Strategic Planning
                    </span>

                    <span class="keyword keyword-yellow-tag">
                        Team Leadership
                    </span>

                </div>

            </div>
            """
        )

    # ========================================================
    # CREATIVE
    # ========================================================

    with tab3:

        st.html(
            """
            <div class="keyword-card keyword-pink">

                <h3>
                    Creative & Design
                </h3>

                <p>
                    Example ATS-friendly keywords
                </p>

                <div class="keyword-list">

                    <span class="keyword keyword-pink-tag">
                        Adobe Creative Suite
                    </span>

                    <span class="keyword keyword-pink-tag">
                        UI/UX Design
                    </span>

                    <span class="keyword keyword-pink-tag">
                        Wireframing
                    </span>

                    <span class="keyword keyword-pink-tag">
                        Prototyping
                    </span>

                    <span class="keyword keyword-pink-tag">
                        Brand Identity
                    </span>

                    <span class="keyword keyword-pink-tag">
                        Visual Communication
                    </span>

                </div>

            </div>
            """
        )

    st.markdown("---")

    # ========================================================
    # RESUME TEMPLATES
    # ========================================================

    st.html(
        """
        <div class="section-header">

            <h2>
                ATS-Friendly Resume Templates
            </h2>

            <p>
                Build your resume using simple structures
                that keep important information readable.
            </p>

            <div class="section-line"></div>

        </div>
        """
    )

    st.html(
        """
        <div class="template-card">

            <h3>
                ATS-Optimized Resume Templates
            </h3>

            <p>
                Downloadable ATS-friendly resume templates
                will be available here soon. The templates
                will focus on clean structure, readable
                typography and recruiter-friendly formatting.
            </p>

            <span class="coming-soon">
                COMING SOON
            </span>

        </div>
        """
    )
