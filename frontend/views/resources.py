import streamlit as st


# ============================================================
# PREMIUM RESOURCES PAGE STYLES
# ============================================================

def _apply_styles():

    st.markdown(
        """
        <style>

        /* ====================================================
           GLOBAL
        ==================================================== */

        .block-container {
            max-width: 1220px;
            padding-top: 1.5rem;
            padding-bottom: 4rem;
        }

        /* ====================================================
           HERO
        ==================================================== */

        .resources-hero {
            position: relative;
            overflow: hidden;

            padding: 48px 44px;

            margin-bottom: 30px;

            border-radius: 30px;

            background:
                radial-gradient(
                    circle at 92% 15%,
                    rgba(250,204,21,0.25),
                    transparent 24%
                ),
                radial-gradient(
                    circle at 8% 85%,
                    rgba(236,72,153,0.20),
                    transparent 27%
                ),
                radial-gradient(
                    circle at 70% 100%,
                    rgba(6,182,212,0.18),
                    transparent 28%
                ),
                linear-gradient(
                    135deg,
                    #0f172a 0%,
                    #172554 36%,
                    #1d4ed8 70%,
                    #0891b2 100%
                );

            border:
                1px solid rgba(255,255,255,0.12);

            box-shadow:
                0 25px 65px rgba(15,23,42,0.28),
                inset 0 1px 0 rgba(255,255,255,0.10);

            transition:
                transform 0.3s ease,
                box-shadow 0.3s ease;
        }

        .resources-hero:hover {
            transform:
                translateY(-5px)
                scale(1.005);

            box-shadow:
                0 35px 80px rgba(15,23,42,0.35);
        }

        .resources-hero::before {
            content: "";

            position: absolute;

            width: 260px;
            height: 260px;

            right: -110px;
            top: -125px;

            border-radius: 50%;

            border:
                1px solid rgba(250,204,21,0.16);

            background:
                rgba(250,204,21,0.07);
        }

        .resources-hero::after {
            content: "";

            position: absolute;

            width: 190px;
            height: 190px;

            left: -95px;
            bottom: -110px;

            border-radius: 50%;

            border:
                1px solid rgba(236,72,153,0.15);

            background:
                rgba(236,72,153,0.07);
        }

        .hero-content {
            position: relative;
            z-index: 2;
        }

        .hero-badge {
            display: inline-block;

            padding: 8px 16px;

            margin-bottom: 17px;

            border-radius: 50px;

            background:
                rgba(250,204,21,0.12);

            border:
                1px solid rgba(250,204,21,0.40);

            color:
                #fef3c7;

            font-size:
                11px;

            font-weight:
                850;

            letter-spacing:
                1.4px;
        }

        .resources-hero h1 {
            color:
                #ffffff;

            font-size:
                3rem;

            font-weight:
                900;

            letter-spacing:
                -1.2px;

            line-height:
                1.1;

            margin:
                0 0 13px 0;
        }

        .resources-hero p {
            max-width:
                790px;

            color:
                #dbeafe;

            font-size:
                15px;

            line-height:
                1.75;

            margin:
                0;
        }

        .hero-highlight {
            color:
                #facc15;

            font-weight:
                850;

            text-decoration:
                underline;

            text-decoration-color:
                rgba(250,204,21,0.8);

            text-decoration-thickness:
                2px;

            text-underline-offset:
                4px;
        }

        /* ====================================================
           SECTION HEADER
        ==================================================== */

        .section-header {
            margin:
                34px 0 20px 0;
        }

        .section-header h2 {
            color:
                #0f172a;

            font-size:
                1.65rem;

            font-weight:
                900;

            letter-spacing:
                -0.5px;

            margin:
                0 0 5px 0;
        }

        .section-header p {
            color:
                #64748b;

            font-size:
                13px;

            line-height:
                1.65;

            margin:
                0;
        }

        .section-line {
            width:
                75px;

            height:
                4px;

            margin-top:
                11px;

            border-radius:
                50px;

            background:
                linear-gradient(
                    90deg,
                    #2563eb,
                    #06b6d4,
                    #facc15
                );

            box-shadow:
                0 4px 14px
                rgba(37,99,235,0.18);
        }

        /* ====================================================
           ATS SCORE CARDS
        ==================================================== */

        .score-card {
            position:
                relative;

            overflow:
                hidden;

            min-height:
                185px;

            padding:
                23px;

            border-radius:
                22px;

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

        .score-card:hover {
            transform:
                translateY(-10px)
                scale(1.015);

            box-shadow:
                0 28px 58px
                rgba(15,23,42,0.14);

            border-color:
                #93c5fd;
        }

        .score-number {
            color:
                #2563eb;

            font-size:
                30px;

            font-weight:
                900;

            line-height:
                1;

            margin-bottom:
                12px;
        }

        .score-card h3 {
            color:
                #0f172a;

            font-size:
                16px;

            font-weight:
                850;

            margin:
                0 0 7px 0;
        }

        .score-card p {
            color:
                #64748b;

            font-size:
                12px;

            line-height:
                1.6;

            margin:
                0;
        }

        .score-blue {
            border-top:
                4px solid #2563eb;
        }

        .score-cyan {
            border-top:
                4px solid #06b6d4;
        }

        .score-yellow {
            border-top:
                4px solid #facc15;
        }

        .score-pink {
            border-top:
                4px solid #ec4899;
        }

        .score-orange {
            border-top:
                4px solid #f97316;
        }

        /* ====================================================
           DO / DON'T
        ==================================================== */

        .guide-card {
            position:
                relative;

            overflow:
                hidden;

            min-height:
                365px;

            padding:
                28px;

            border-radius:
                24px;

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
                box-shadow 0.3s ease;
        }

        .guide-card:hover {
            transform:
                translateY(-10px)
                scale(1.015);

            box-shadow:
                0 30px 62px
                rgba(15,23,42,0.15);
        }

        .do-card {
            border-top:
                5px solid #22c55e;
        }

        .dont-card {
            border-top:
                5px solid #ef4444;
        }

        .guide-label {
            display:
                inline-block;

            padding:
                6px 12px;

            margin-bottom:
                12px;

            border-radius:
                50px;

            font-size:
                10px;

            font-weight:
                900;

            letter-spacing:
                0.8px;
        }

        .do-label {
            color:
                #166534;

            background:
                #dcfce7;
        }

        .dont-label {
            color:
                #b91c1c;

            background:
                #fee2e2;
        }

        .guide-card h3 {
            color:
                #0f172a;

            font-size:
                21px;

            font-weight:
                900;

            margin:
                0 0 17px 0;
        }

        .guide-list {
            list-style:
                none;

            padding:
                0;

            margin:
                0;
        }

        .guide-list li {
            position:
                relative;

            padding:
                9px 0 9px 24px;

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
            content:
                "✓";

            position:
                absolute;

            left:
                0;

            color:
                #16a34a;

            font-weight:
                900;
        }

        .dont-card .guide-list li::before {
            content:
                "×";

            position:
                absolute;

            left:
                1px;

            color:
                #dc2626;

            font-size:
                17px;

            font-weight:
                900;
        }

        /* ====================================================
           RESUME FLOW
        ==================================================== */

        .flow-card {
            position:
                relative;

            min-height:
                165px;

            padding:
                24px;

            text-align:
                center;

            border-radius:
                22px;

            background:
                #ffffff;

            border:
                1px solid #e2e8f0;

            box-shadow:
                0 9px 25px
                rgba(15,23,42,0.06);

            transition:
                transform 0.3s ease,
                box-shadow 0.3s ease;
        }

        .flow-card:hover {
            transform:
                translateY(-9px)
                scale(1.02);

            box-shadow:
                0 25px 52px
                rgba(15,23,42,0.14);
        }

        .flow-number {
            width:
                43px;

            height:
                43px;

            display:
                flex;

            align-items:
                center;

            justify-content:
                center;

            margin:
                0 auto 13px auto;

            border-radius:
                50%;

            background:
                linear-gradient(
                    135deg,
                    #2563eb,
                    #06b6d4
                );

            color:
                #ffffff;

            font-size:
                15px;

            font-weight:
                900;

            box-shadow:
                0 9px 22px
                rgba(37,99,235,0.22);
        }

        .flow-card h3 {
            color:
                #0f172a;

            font-size:
                15px;

            font-weight:
                850;

            margin:
                0 0 6px 0;
        }

        .flow-card p {
            color:
                #64748b;

            font-size:
                11px;

            line-height:
                1.55;

            margin:
                0;
        }

        /* ====================================================
           MISTAKE CARDS
        ==================================================== */

        .mistake-card {
            position:
                relative;

            min-height:
                190px;

            padding:
                23px;

            border-radius:
                20px;

            background:
                linear-gradient(
                    145deg,
                    #ffffff,
                    #fff7ed
                );

            border:
                1px solid #fed7aa;

            box-shadow:
                0 8px 23px
                rgba(15,23,42,0.05);

            transition:
                transform 0.3s ease,
                box-shadow 0.3s ease;
        }

        .mistake-card:hover {
            transform:
                translateY(-8px);

            box-shadow:
                0 23px 50px
                rgba(15,23,42,0.13);
        }

        .mistake-number {
            color:
                #f97316;

            font-size:
                27px;

            font-weight:
                900;

            margin-bottom:
                8px;
        }

        .mistake-card h3 {
            color:
                #0f172a;

            font-size:
                15px;

            font-weight:
                850;

            margin:
                0 0 7px 0;
        }

        .mistake-card p {
            color:
                #64748b;

            font-size:
                12px;

            line-height:
                1.6;

            margin:
                0;
        }

        /* ====================================================
           KEYWORD CARDS
        ==================================================== */

        .keyword-card {
            min-height:
                255px;

            padding:
                27px;

            border-radius:
                23px;

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
                box-shadow 0.3s ease;
        }

        .keyword-card:hover {
            transform:
                translateY(-9px)
                scale(1.015);

            box-shadow:
                0 27px 55px
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
                900;

            margin:
                0 0 9px 0;
        }

        .keyword-card p {
            color:
                #64748b;

            font-size:
                12px;

            margin:
                0 0 15px 0;
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
            display:
                inline-block;

            padding:
                7px 11px;

            border-radius:
                50px;

            background:
                #eff6ff;

            border:
                1px solid #dbeafe;

            color:
                #1d4ed8;

            font-size:
                11px;

            font-weight:
                750;

            transition:
                transform 0.2s ease,
                box-shadow 0.2s ease;
        }

        .keyword:hover {
            transform:
                translateY(-3px);

            box-shadow:
                0 7px 15px
                rgba(37,99,235,0.12);
        }

        .keyword-yellow-tag {
            background:
                #fef3c7;

            border-color:
                #fde68a;

            color:
                #b45309;
        }

        .keyword-pink-tag {
            background:
                #fce7f3;

            border-color:
                #fbcfe8;

            color:
                #be185d;
        }

        /* ====================================================
           TABS
        ==================================================== */

        .stTabs [data-baseweb="tab-list"] {
            gap:
                8px;

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

        /* ====================================================
           CHECKLIST
        ==================================================== */

        .check-card {
            padding:
                25px;

            border-radius:
                22px;

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
        }

        .check-item {
            display:
                flex;

            align-items:
                center;

            gap:
                13px;

            padding:
                13px 0;

            border-bottom:
                1px solid #f1f5f9;

            color:
                #475569;

            font-size:
                13px;

            font-weight:
                650;
        }

        .check-item:last-child {
            border-bottom:
                none;
        }

        .check-box {
            width:
                24px;

            height:
                24px;

            flex-shrink:
                0;

            display:
                flex;

            align-items:
                center;

            justify-content:
                center;

            border-radius:
                8px;

            background:
                #dcfce7;

            border:
                1px solid #bbf7d0;

            color:
                #15803d;

            font-size:
                12px;

            font-weight:
                900;
        }

        /* ====================================================
           BEFORE AFTER
        ==================================================== */

        .comparison-card {
            padding:
                25px;

            border-radius:
                22px;

            background:
                #ffffff;

            border:
                1px solid #e2e8f0;

            box-shadow:
                0 9px 25px
                rgba(15,23,42,0.06);

            transition:
                transform 0.3s ease,
                box-shadow 0.3s ease;
        }

        .comparison-card:hover {
            transform:
                translateY(-7px);

            box-shadow:
                0 24px 50px
                rgba(15,23,42,0.12);
        }

        .comparison-label {
            display:
                inline-block;

            padding:
                6px 11px;

            border-radius:
                50px;

            font-size:
                10px;

            font-weight:
                900;

            letter-spacing:
                0.7px;

            margin-bottom:
                13px;
        }

        .bad-label {
            background:
                #fee2e2;

            color:
                #b91c1c;
        }

        .good-label {
            background:
                #dcfce7;

            color:
                #166534;
        }

        .comparison-card h3 {
            color:
                #0f172a;

            font-size:
                16px;

            font-weight:
                850;

            margin:
                0 0 10px 0;
        }

        .comparison-text {
            color:
                #64748b;

            font-size:
                12px;

            line-height:
                1.7;
        }

        /* ====================================================
           TEMPLATE / CTA
        ==================================================== */

        .template-card {
            position:
                relative;

            overflow:
                hidden;

            padding:
                34px;

            margin-top:
                25px;

            border-radius:
                26px;

            background:
                radial-gradient(
                    circle at 90% 15%,
                    rgba(250,204,21,0.18),
                    transparent 25%
                ),
                radial-gradient(
                    circle at 8% 100%,
                    rgba(236,72,153,0.12),
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
                0 14px 35px
                rgba(37,99,235,0.09);

            transition:
                transform 0.3s ease,
                box-shadow 0.3s ease;
        }

        .template-card:hover {
            transform:
                translateY(-8px);

            box-shadow:
                0 27px 58px
                rgba(37,99,235,0.14);
        }

        .template-card h3 {
            color:
                #0f172a;

            font-size:
                22px;

            font-weight:
                900;

            margin:
                0 0 8px 0;
        }

        .template-card p {
            max-width:
                800px;

            color:
                #64748b;

            font-size:
                13px;

            line-height:
                1.7;

            margin:
                0;
        }

        .coming-soon {
            display:
                inline-block;

            margin-top:
                17px;

            padding:
                8px 14px;

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
                900;

            letter-spacing:
                0.7px;
        }

        /* ====================================================
           SIDEBAR
        ==================================================== */

        [data-testid="stSidebar"] {
            background:
                linear-gradient(
                    180deg,
                    #f8fafc,
                    #eef2ff
                );
        }

        /* ====================================================
           DIVIDER
        ==================================================== */

        hr {
            border:
                none !important;

            height:
                1px !important;

            background:
                linear-gradient(
                    90deg,
                    transparent,
                    #cbd5e1,
                    transparent
                ) !important;

            margin:
                30px 0 !important;
        }

        /* ====================================================
           RESPONSIVE
        ==================================================== */

        @media (max-width: 768px) {

            .block-container {
                padding-left:
                    1rem;

                padding-right:
                    1rem;
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

            .score-card {
                margin-bottom:
                    15px;
            }

            .flow-card {
                margin-bottom:
                    15px;
            }

            .mistake-card {
                margin-bottom:
                    15px;
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


# ============================================================
# RENDER
# ============================================================

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
                    Learn how to build a
                    <span class="hero-highlight">
                        clean, ATS-friendly resume
                    </span>
                    that is easy for applicant tracking
                    systems and recruiters to understand.
                </p>

            </div>

        </div>
        """
    )

    # ========================================================
    # ATS SCORE DIMENSIONS
    # ========================================================

    st.html(
        """
        <div class="section-header">

            <h2>
                Understand Your ATS Score
            </h2>

            <p>
                A strong resume is more than just keywords.
                ATS evaluation can involve multiple dimensions.
            </p>

            <div class="section-line"></div>

        </div>
        """
    )

    score_cols = st.columns(
        5,
        gap="medium",
    )

    score_data = [
        (
            "20%",
            "Formatting",
            "Clean structure, readable layout and consistent formatting.",
            "score-blue",
        ),
        (
            "25%",
            "Keywords & Skills",
            "Relevant skills and job-specific terminology.",
            "score-cyan",
        ),
        (
            "25%",
            "Content Quality",
            "Clear, measurable and relevant professional content.",
            "score-yellow",
        ),
        (
            "15%",
            "Skill Validation",
            "Evidence that demonstrates your claimed abilities.",
            "score-pink",
        ),
        (
            "15%",
            "ATS Compatibility",
            "Machine-readable structure and recruiter-friendly formatting.",
            "score-orange",
        ),
    ]

    for column, data in zip(
        score_cols,
        score_data,
    ):

        percentage, title, description, css_class = data

        with column:

            st.html(
                f"""
                <div class="score-card {css_class}">

                    <div class="score-number">
                        {percentage}
                    </div>

                    <h3>
                        {title}
                    </h3>

                    <p>
                        {description}
                    </p>

                </div>
                """
            )

    st.markdown("---")

    # ========================================================
    # RESUME STRUCTURE
    # ========================================================

    st.html(
        """
        <div class="section-header">

            <h2>
                Recommended Resume Structure
            </h2>

            <p>
                Keep your resume organized so both ATS systems
                and recruiters can quickly find important information.
            </p>

            <div class="section-line"></div>

        </div>
        """
    )

    flow_cols = st.columns(
        6,
        gap="small",
    )

    flow_data = [
        (
            "01",
            "Contact",
            "Name, email, phone and professional links.",
        ),
        (
            "02",
            "Summary",
            "Short overview of your professional profile.",
        ),
        (
            "03",
            "Skills",
            "Relevant technical and professional skills.",
        ),
        (
            "04",
            "Experience",
            "Roles, responsibilities and measurable impact.",
        ),
        (
            "05",
            "Projects",
            "Practical work with technologies and outcomes.",
        ),
        (
            "06",
            "Education",
            "Degree, institution and relevant details.",
        ),
    ]

    for column, data in zip(
        flow_cols,
        flow_data,
    ):

        number, title, description = data

        with column:

            st.html(
                f"""
                <div class="flow-card">

                    <div class="flow-number">
                        {number}
                    </div>

                    <h3>
                        {title}
                    </h3>

                    <p>
                        {description}
                    </p>

                </div>
                """
            )

    st.markdown("---")

    # ========================================================
    # DO'S / DON'TS
    # ========================================================

    st.html(
        """
        <div class="section-header">

            <h2>
                ATS Optimization Do's & Don'ts
            </h2>

            <p>
                Follow these practical formatting and content rules.
            </p>

            <div class="section-line"></div>

        </div>
        """
    )

    col1, col2 = st.columns(
        2,
        gap="large",
    )

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
                        Arial, Calibri or Times New Roman
                    </li>

                    <li>
                        Save your resume as PDF or DOCX
                    </li>

                </ul>

            </div>
            """
        )

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
                        Avoid unnecessary images and graphics
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
                        Avoid unexplained abbreviations
                    </li>

                </ul>

            </div>
            """
        )

    st.markdown("---")

    # ========================================================
    # TOP MISTAKES
    # ========================================================

    st.html(
        """
        <div class="section-header">

            <h2>
                Common Resume Mistakes
            </h2>

            <p>
                These issues can make your resume harder to
                parse, understand or evaluate.
            </p>

            <div class="section-line"></div>

        </div>
        """
    )

    mistakes = [
        (
            "01",
            "Too Much Design",
            "Heavy graphics, icons and decorative elements can reduce readability."
        ),
        (
            "02",
            "Missing Keywords",
            "A resume may be relevant but still miss important job-specific terminology."
        ),
        (
            "03",
            "Weak Bullet Points",
            "Generic responsibilities are less effective than measurable achievements."
        ),
        (
            "04",
            "Unclear Structure",
            "Inconsistent headings and formatting make information harder to scan."
        ),
        (
            "05",
            "Keyword Stuffing",
            "Repeating keywords unnaturally can make content look forced and reduce quality."
        ),
        (
            "06",
            "No Quantifiable Impact",
            "Numbers help communicate the scale and results of your work."
        ),
    ]

    mistake_cols = st.columns(
        3,
        gap="medium",
    )

    for index, data in enumerate(mistakes):

        number, title, description = data

        with mistake_cols[index % 3]:

            st.html(
                f"""
                <div class="mistake-card">

                    <div class="mistake-number">
                        {number}
                    </div>

                    <h3>
                        {title}
                    </h3>

                    <p>
                        {description}
                    </p>

                </div>
                """
            )

    st.markdown("---")

    # ========================================================
    # KEYWORD EXPLORER
    # ========================================================

    st.html(
        """
        <div class="section-header">

            <h2>
                Common ATS Keywords by Industry
            </h2>

            <p>
                Use keywords naturally when they genuinely
                represent your skills and experience.
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
                    Example relevant technologies and methodologies
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
                    Example professional skills and competencies
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
                    Example design and creative skills
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
    # ATS CHECKLIST
    # ========================================================

    st.html(
        """
        <div class="section-header">

            <h2>
                Final ATS Checklist
            </h2>

            <p>
                Before submitting your resume, quickly verify
                these important points.
            </p>

            <div class="section-line"></div>

        </div>
        """
    )

    checklist_left, checklist_right = st.columns(
        2,
        gap="large",
    )

    checklist_left_items = [
        "Standard section headings are used",
        "Important contact information is readable",
        "Relevant job keywords are included naturally",
        "Skills are explicitly listed",
        "Achievements contain measurable results",
    ]

    checklist_right_items = [
        "Formatting is consistent throughout",
        "No important information is hidden in graphics",
        "Font is professional and readable",
        "Resume uses a simple structure",
        "File is saved in an accepted format",
    ]

    with checklist_left:

        st.html(
            '<div class="check-card">'
        )

        for item in checklist_left_items:

            st.html(
                f"""
                <div class="check-item">

                    <div class="check-box">
                        ✓
                    </div>

                    <div>
                        {item}
                    </div>

                </div>
                """
            )

        st.html(
            '</div>'
        )

    with checklist_right:

        st.html(
            '<div class="check-card">'
        )

        for item in checklist_right_items:

            st.html(
                f"""
                <div class="check-item">

                    <div class="check-box">
                        ✓
                    </div>

                    <div>
                        {item}
                    </div>

                </div>
                """
            )

        st.html(
            '</div>'
        )

    st.markdown("---")

    # ========================================================
    # BEFORE / AFTER
    # ========================================================

    st.html(
        """
        <div class="section-header">

            <h2>
                Write Stronger Resume Content
            </h2>

            <p>
                Focus on measurable impact instead of only
                describing responsibilities.
            </p>

            <div class="section-line"></div>

        </div>
        """
    )

    before_col, after_col = st.columns(
        2,
        gap="large",
    )

    with before_col:

        st.html(
            """
            <div class="comparison-card">

                <span class="comparison-label bad-label">
                    WEAKER
                </span>

                <h3>
                    Generic Description
                </h3>

                <div class="comparison-text">
                    Worked on a web application and
                    helped improve its functionality.
                </div>

            </div>
            """
        )

    with after_col:

        st.html(
            """
            <div class="comparison-card">

                <span class="comparison-label good-label">
                    STRONGER
                </span>

                <h3>
                    Impact-Focused Description
                </h3>

                <div class="comparison-text">
                    Developed and optimized a web application,
                    improving page performance and delivering
                    key features using modern development tools.
                </div>

            </div>
            """
        )

    st.markdown("---")

    # ========================================================
    # TEMPLATES
    # ========================================================

    st.html(
        """
        <div class="section-header">

            <h2>
                ATS-Friendly Resume Templates
            </h2>

            <p>
                Simple templates designed around clean structure,
                readable typography and recruiter-friendly formatting.
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
                will be available here soon. These templates
                will focus on clean sections, readable
                typography, relevant keywords and simple
                machine-readable formatting.
            </p>

            <span class="coming-soon">
                COMING SOON
            </span>

        </div>
        """
    )
