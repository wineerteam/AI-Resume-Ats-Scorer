import requests
import streamlit as st

from frontend.services import api_client


# ============================================================
# PREMIUM ATS HISTORY - V4
# ============================================================

def _apply_styles() -> None:
    st.markdown(
        """
        <style>

        /* ====================================================
           GLOBAL
        ==================================================== */

        .block-container {
            max-width: 1250px;
            padding-top: 1.5rem;
            padding-bottom: 4rem;
        }

        /* ====================================================
           HERO
        ==================================================== */

        .history-hero {
            position: relative;
            overflow: hidden;

            padding: 44px 44px;
            margin-bottom: 28px;

            border-radius: 30px;

            background:
                radial-gradient(
                    circle at 90% 10%,
                    rgba(250,204,21,0.25),
                    transparent 25%
                ),
                radial-gradient(
                    circle at 10% 90%,
                    rgba(236,72,153,0.20),
                    transparent 28%
                ),
                linear-gradient(
                    135deg,
                    #0f172a 0%,
                    #172554 38%,
                    #1d4ed8 72%,
                    #0891b2 100%
                );

            border:
                1px solid rgba(255,255,255,0.12);

            box-shadow:
                0 25px 70px rgba(15,23,42,0.27);

            transition:
                transform 0.3s ease,
                box-shadow 0.3s ease;
        }

        .history-hero:hover {
            transform:
                translateY(-5px)
                scale(1.004);

            box-shadow:
                0 35px 85px rgba(15,23,42,0.34);
        }

        .history-hero::before {
            content: "";

            position: absolute;

            width: 280px;
            height: 280px;

            right: -130px;
            top: -140px;

            border-radius: 50%;

            background:
                rgba(250,204,21,0.06);

            border:
                1px solid rgba(250,204,21,0.16);
        }

        .history-hero::after {
            content: "";

            position: absolute;

            width: 210px;
            height: 210px;

            left: -105px;
            bottom: -120px;

            border-radius: 50%;

            background:
                rgba(236,72,153,0.06);

            border:
                1px solid rgba(236,72,153,0.14);
        }

        .history-hero-content {
            position: relative;
            z-index: 2;
        }

        .history-badge {
            display: inline-block;

            padding: 7px 14px;
            margin-bottom: 15px;

            border-radius: 50px;

            background:
                rgba(255,255,255,0.10);

            border:
                1px solid rgba(255,255,255,0.20);

            color:
                #dbeafe;

            font-size:
                10px;

            font-weight:
                900;

            letter-spacing:
                1.4px;
        }

        .history-hero h1 {
            color:
                #ffffff;

            font-size:
                2.8rem;

            font-weight:
                900;

            letter-spacing:
                -1px;

            line-height:
                1.1;

            margin:
                0 0 11px 0;
        }

        .history-hero p {
            max-width:
                780px;

            color:
                #dbeafe;

            font-size:
                14px;

            line-height:
                1.75;

            margin:
                0;
        }

        /* ====================================================
           SECTION
        ==================================================== */

        .section-header {
            margin:
                32px 0 18px 0;
        }

        .section-header h2 {
            color:
                #0f172a;

            font-size:
                1.55rem;

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
                12px;

            line-height:
                1.6;

            margin:
                0;
        }

        .section-line {
            width:
                72px;

            height:
                4px;

            margin-top:
                10px;

            border-radius:
                50px;

            background:
                linear-gradient(
                    90deg,
                    #2563eb,
                    #06b6d4,
                    #facc15
                );
        }

        /* ====================================================
           OVERVIEW CARDS
        ==================================================== */

        .overview-card {
            position:
                relative;

            overflow:
                hidden;

            min-height:
                150px;

            padding:
                25px;

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
                0 10px 28px
                rgba(15,23,42,0.06);

            transition:
                transform 0.3s ease,
                box-shadow 0.3s ease,
                border-color 0.3s ease;
        }

        .overview-card:hover {
            transform:
                perspective(900px)
                translateY(-9px)
                rotateX(2deg)
                scale(1.015);

            box-shadow:
                0 28px 60px
                rgba(15,23,42,0.14);

            border-color:
                #93c5fd;
        }

        .overview-label {
            color:
                #64748b;

            font-size:
                10px;

            font-weight:
                850;

            letter-spacing:
                0.8px;

            text-transform:
                uppercase;

            margin-bottom:
                9px;
        }

        .overview-value {
            color:
                #0f172a;

            font-size:
                32px;

            font-weight:
                900;

            line-height:
                1;

            margin-bottom:
                10px;
        }

        .overview-description {
            color:
                #94a3b8;

            font-size:
                11px;
        }

        .overview-blue {
            border-top:
                4px solid #2563eb;
        }

        .overview-cyan {
            border-top:
                4px solid #06b6d4;
        }

        .overview-yellow {
            border-top:
                4px solid #facc15;
        }

        /* ====================================================
           PROGRESS / TREND CARD
        ==================================================== */

        .trend-card {
            position:
                relative;

            overflow:
                hidden;

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
                rgba(15,23,42,0.06);

            transition:
                transform 0.3s ease,
                box-shadow 0.3s ease;
        }

        .trend-card:hover {
            transform:
                translateY(-7px);

            box-shadow:
                0 27px 58px
                rgba(15,23,42,0.13);
        }

        .trend-title {
            color:
                #0f172a;

            font-size:
                15px;

            font-weight:
                850;

            margin-bottom:
                20px;
        }

        .trend-track {
            display:
                flex;

            align-items:
                center;

            gap:
                8px;

            overflow-x:
                auto;

            padding:
                8px 2px 13px 2px;
        }

        .trend-point {
            min-width:
                72px;

            padding:
                11px 9px;

            text-align:
                center;

            border-radius:
                14px;

            background:
                #eff6ff;

            border:
                1px solid #dbeafe;
        }

        .trend-point-score {
            color:
                #1d4ed8;

            font-size:
                17px;

            font-weight:
                900;
        }

        .trend-point-label {
            color:
                #64748b;

            font-size:
                9px;

            margin-top:
                3px;
        }

        .trend-arrow {
            color:
                #94a3b8;

            font-size:
                17px;

            font-weight:
                900;
        }

        .improvement-box {
            margin-top:
                14px;

            padding:
                13px 16px;

            border-radius:
                14px;

            background:
                #ecfdf5;

            border:
                1px solid #bbf7d0;

            color:
                #166534;

            font-size:
                12px;

            font-weight:
                750;
        }

        .improvement-negative {
            background:
                #fff7ed;

            border-color:
                #fed7aa;

            color:
                #c2410c;
        }

        .improvement-neutral {
            background:
                #f8fafc;

            border-color:
                #e2e8f0;

            color:
                #64748b;
        }

        /* ====================================================
           LATEST ANALYSIS
        ==================================================== */

        .latest-card {
            position:
                relative;

            overflow:
                hidden;

            padding:
                29px;

            border-radius:
                26px;

            background:
                radial-gradient(
                    circle at 92% 15%,
                    rgba(250,204,21,0.15),
                    transparent 24%
                ),
                linear-gradient(
                    135deg,
                    #eff6ff,
                    #ecfeff
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

        .latest-card:hover {
            transform:
                translateY(-8px);

            box-shadow:
                0 29px 62px
                rgba(37,99,235,0.15);
        }

        .latest-label {
            display:
                inline-block;

            padding:
                6px 11px;

            border-radius:
                50px;

            background:
                #dbeafe;

            color:
                #1d4ed8;

            font-size:
                9px;

            font-weight:
                900;

            letter-spacing:
                0.8px;

            margin-bottom:
                11px;
        }

        .latest-filename {
            color:
                #0f172a;

            font-size:
                21px;

            font-weight:
                900;

            margin-bottom:
                5px;
        }

        .latest-date {
            color:
                #64748b;

            font-size:
                11px;
        }

        .latest-score {
            color:
                #1d4ed8;

            font-size:
                44px;

            font-weight:
                900;

            line-height:
                1;
        }

        .latest-score-label {
            color:
                #64748b;

            font-size:
                10px;

            font-weight:
                800;

            letter-spacing:
                0.7px;
        }

        .best-badge {
            display:
                inline-block;

            margin-top:
                10px;

            padding:
                6px 10px;

            border-radius:
                50px;

            background:
                #fef3c7;

            color:
                #92400e;

            border:
                1px solid #fde68a;

            font-size:
                9px;

            font-weight:
                900;
        }

        /* ====================================================
           ANALYSIS CARD
        ==================================================== */

        .analysis-card {
            position:
                relative;

            overflow:
                hidden;

            margin-bottom:
                15px;

            padding:
                22px;

            border-radius:
                21px;

            background:
                linear-gradient(
                    145deg,
                    #ffffff,
                    #f8fafc
                );

            border:
                1px solid #e2e8f0;

            box-shadow:
                0 8px 24px
                rgba(15,23,42,0.05);

            transition:
                transform 0.3s ease,
                box-shadow 0.3s ease,
                border-color 0.3s ease;
        }

        .analysis-card:hover {
            transform:
                translateY(-7px)
                scale(1.008);

            border-color:
                #93c5fd;

            box-shadow:
                0 27px 58px
                rgba(15,23,42,0.13);
        }

        .analysis-card::before {
            content:
                "";

            position:
                absolute;

            left:
                0;

            top:
                0;

            bottom:
                0;

            width:
                4px;

            background:
                linear-gradient(
                    180deg,
                    #2563eb,
                    #06b6d4
                );
        }

        .analysis-filename {
            color:
                #0f172a;

            font-size:
                16px;

            font-weight:
                850;

            margin-bottom:
                5px;
        }

        .analysis-date {
            color:
                #94a3b8;

            font-size:
                10px;
        }

        .analysis-score {
            display:
                inline-block;

            padding:
                8px 14px;

            border-radius:
                50px;

            background:
                #eff6ff;

            border:
                1px solid #bfdbfe;

            color:
                #1d4ed8;

            font-size:
                12px;

            font-weight:
                900;
        }

        .score-status {
            display:
                inline-block;

            margin-left:
                7px;

            padding:
                6px 10px;

            border-radius:
                50px;

            font-size:
                9px;

            font-weight:
                900;

            letter-spacing:
                0.4px;
        }

        .status-excellent {
            color:
                #166534;

            background:
                #dcfce7;

            border:
                1px solid #bbf7d0;
        }

        .status-good {
            color:
                #0369a1;

            background:
                #e0f2fe;

            border:
                1px solid #bae6fd;
        }

        .status-improve {
            color:
                #b45309;

            background:
                #fef3c7;

            border:
                1px solid #fde68a;
        }

        .status-low {
            color:
                #b91c1c;

            background:
                #fee2e2;

            border:
                1px solid #fecaca;
        }

        /* ====================================================
           METRICS
        ==================================================== */

        .metric-card {
            min-height:
                100px;

            padding:
                16px;

            border-radius:
                16px;

            background:
                #f8fafc;

            border:
                1px solid #e2e8f0;

            transition:
                transform 0.25s ease,
                box-shadow 0.25s ease;
        }

        .metric-card:hover {
            transform:
                translateY(-5px);

            box-shadow:
                0 15px 31px
                rgba(15,23,42,0.09);
        }

        .metric-label {
            color:
                #64748b;

            font-size:
                9px;

            font-weight:
                850;

            text-transform:
                uppercase;

            letter-spacing:
                0.5px;

            margin-bottom:
                7px;
        }

        .metric-value {
            color:
                #0f172a;

            font-size:
                21px;

            font-weight:
                900;
        }

        /* ====================================================
           JD MATCH
        ==================================================== */

        .jd-match-card {
            display:
                flex;

            align-items:
                center;

            justify-content:
                space-between;

            gap:
                15px;

            padding:
                17px 20px;

            margin-top:
                17px;

            border-radius:
                17px;

            background:
                linear-gradient(
                    135deg,
                    #eff6ff,
                    #ecfeff
                );

            border:
                1px solid #bae6fd;
        }

        .jd-match-label {
            color:
                #0e7490;

            font-size:
                10px;

            font-weight:
                850;

            letter-spacing:
                0.6px;
        }

        .jd-match-value {
            color:
                #0369a1;

            font-size:
                25px;

            font-weight:
                900;
        }

        /* ====================================================
           EMPTY
        ==================================================== */

        .empty-card {
            padding:
                48px 30px;

            text-align:
                center;

            border-radius:
                27px;

            background:
                linear-gradient(
                    145deg,
                    #ffffff,
                    #f8fafc
                );

            border:
                1px solid #e2e8f0;

            box-shadow:
                0 13px 35px
                rgba(15,23,42,0.07);
        }

        .empty-card h2 {
            color:
                #0f172a;

            font-size:
                23px;

            font-weight:
                900;

            margin:
                0 0 8px 0;
        }

        .empty-card p {
            color:
                #64748b;

            font-size:
                13px;

            line-height:
                1.7;

            margin:
                0;
        }

        /* ====================================================
           EXPANDER
        ==================================================== */

        [data-testid="stExpander"] {
            border:
                none !important;

            background:
                transparent !important;
        }

        [data-testid="stExpander"] details {
            border:
                none !important;
        }

        /* ====================================================
           BUTTON
        ==================================================== */

        div.stButton > button {
            border-radius:
                12px;

            font-weight:
                750;

            transition:
                transform 0.2s ease,
                box-shadow 0.2s ease;
        }

        div.stButton > button:hover {
            transform:
                translateY(-2px);

            box-shadow:
                0 9px 20px
                rgba(15,23,42,0.12);
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

            .history-hero {
                padding:
                    30px 22px;
            }

            .history-hero h1 {
                font-size:
                    2.2rem;
            }

            .overview-card {
                margin-bottom:
                    14px;
            }

            .latest-card {
                padding:
                    23px;
            }

            .analysis-card {
                padding:
                    19px;
            }

            .jd-match-card {
                flex-direction:
                    column;

                align-items:
                    flex-start;
            }
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# BACKEND ERROR
# ============================================================

def _show_backend_error(exc: Exception) -> None:

    if isinstance(exc, requests.ConnectionError):

        st.error(
            "Could not reach the backend. Is it running on port 8000?"
        )

    elif isinstance(exc, requests.HTTPError) and exc.response is not None:

        st.error(
            f"Backend returned "
            f"{exc.response.status_code}: "
            f"{exc.response.text}"
        )

    else:

        st.error(
            f"Unexpected error: {exc}"
        )


# ============================================================
# SCORE STATUS
# ============================================================

def _score_status(score: float):

    if score >= 90:
        return "Excellent", "status-excellent"

    if score >= 75:
        return "Strong", "status-good"

    if score >= 60:
        return "Needs Improvement", "status-improve"

    return "Needs Work", "status-low"


# ============================================================
# RENDER
# ============================================================

def render() -> None:

    _apply_styles()

    # ========================================================
    # HERO
    # ========================================================

    st.html(
        """
        <div class="history-hero">

            <div class="history-hero-content">

                <div class="history-badge">
                    ATS PERFORMANCE TRACKER
                </div>

                <h1>
                    Analysis History
                </h1>

                <p>
                    Track your resume performance, compare ATS scores,
                    identify improvements and understand how your
                    resume evolves over time.
                </p>

            </div>

        </div>
        """
    )

    # ========================================================
    # AUTH
    # ========================================================

    access_token = st.session_state.get(
        "access_token"
    )

    if not access_token:

        st.html(
            """
            <div class="empty-card">

                <h2>
                    Sign in to view your history
                </h2>

                <p>
                    Your previous resume analyses are available
                    after signing in from the sidebar.
                </p>

            </div>
            """
        )

        return

    # ========================================================
    # GET HISTORY
    # ========================================================

    try:

        history = api_client.get_history(
            access_token
        )

    except requests.RequestException as exc:

        _show_backend_error(
            exc
        )

        return

    # ========================================================
    # EMPTY HISTORY
    # ========================================================

    if not history:

        st.html(
            """
            <div class="empty-card">

                <h2>
                    Start Your Resume Journey
                </h2>

                <p>
                    You do not have any saved analyses yet.
                    Analyze your resume to start tracking
                    your ATS performance.
                </p>

            </div>
            """
        )

        st.markdown("")

        _, center, _ = st.columns(
            [1, 2, 1]
        )

        with center:

            if st.button(
                "Analyze My Resume",
                use_container_width=True,
                type="primary",
            ):

                st.session_state.current_view = "scorer"

                st.rerun()

        return

    # ========================================================
    # PREPARE DATA
    # ========================================================

    scores = []

    for entry in history:

        scores.append(
            float(
                entry.get(
                    "ats_score",
                    0,
                )
            )
        )

    total_analyses = len(history)

    average_score = (
        sum(scores) / len(scores)
        if scores
        else 0
    )

    best_score = (
        max(scores)
        if scores
        else 0
    )

    latest_entry = history[0]

    latest_score = float(
        latest_entry.get(
            "ats_score",
            0,
        )
    )

    # ========================================================
    # OVERVIEW
    # ========================================================

    st.html(
        """
        <div class="section-header">

            <h2>
                Performance Overview
            </h2>

            <p>
                A quick look at your resume analysis performance.
            </p>

            <div class="section-line"></div>

        </div>
        """
    )

    overview_cols = st.columns(
        3,
        gap="medium",
    )

    overview_data = [
        (
            "Total Analyses",
            f"{total_analyses}",
            "Saved resume analyses",
            "overview-blue",
        ),
        (
            "Average Score",
            f"{average_score:.0f}/100",
            "Average ATS performance",
            "overview-cyan",
        ),
        (
            "Best Score",
            f"{best_score:.0f}/100",
            "Highest score achieved",
            "overview-yellow",
        ),
    ]

    for column, data in zip(
        overview_cols,
        overview_data,
    ):

        label, value, description, css_class = data

        with column:

            st.html(
                f"""
                <div class="overview-card {css_class}">

                    <div class="overview-label">
                        {label}
                    </div>

                    <div class="overview-value">
                        {value}
                    </div>

                    <div class="overview-description">
                        {description}
                    </div>

                </div>
                """
            )

    # ========================================================
    # SCORE TREND
    # ========================================================

    if len(scores) >= 2:

        st.html(
            """
            <div class="section-header">

                <h2>
                    ATS Score Progress
                </h2>

                <p>
                    See how your resume score has changed across analyses.
                </p>

                <div class="section-line"></div>

            </div>
            """
        )

        # Show oldest -> newest
        trend_scores = list(
            reversed(scores)
        )

        trend_html = ""

        for index, score in enumerate(
            trend_scores
        ):

            trend_html += f"""
                <div class="trend-point">

                    <div class="trend-point-score">
                        {score:.0f}
                    </div>

                    <div class="trend-point-label">
                        Analysis {index + 1}
                    </div>

                </div>
            """

            if index < len(trend_scores) - 1:

                trend_html += """
                    <div class="trend-arrow">
                        →
                    </div>
                """

        first_score = trend_scores[0]
        current_score = trend_scores[-1]

        improvement = current_score - first_score

        if improvement > 0:

            improvement_text = (
                f"Your ATS score improved by "
                f"{improvement:.0f} points."
            )

            improvement_class = ""

        elif improvement < 0:

            improvement_text = (
                f"Your ATS score decreased by "
                f"{abs(improvement):.0f} points."
            )

            improvement_class = "improvement-negative"

        else:

            improvement_text = (
                "Your ATS score has remained consistent."
            )

            improvement_class = "improvement-neutral"

        st.html(
            f"""
            <div class="trend-card">

                <div class="trend-title">
                    Score Journey
                </div>

                <div class="trend-track">
                    {trend_html}
                </div>

                <div class="improvement-box {improvement_class}">
                    {improvement_text}
                </div>

            </div>
            """
        )

    # ========================================================
    # LATEST ANALYSIS
    # ========================================================

    latest_filename = latest_entry.get(
        "filename",
        "resume",
    )

    latest_created = latest_entry.get(
        "created_at",
        "",
    )

    latest_status, latest_status_class = _score_status(
        latest_score
    )

    is_best = latest_score >= best_score

    st.html(
        """
        <div class="section-header">

            <h2>
                Latest Analysis
            </h2>

            <p>
                Your most recent resume analysis.
            </p>

            <div class="section-line"></div>

        </div>
        """
    )

    latest_left, latest_right = st.columns(
        [3, 1],
        gap="large",
    )

    with latest_left:

        best_badge = (
            '<div class="best-badge">HIGHEST SCORE</div>'
            if is_best
            else ""
        )

        st.html(
            f"""
            <div class="latest-card">

                <div class="latest-label">
                    MOST RECENT ANALYSIS
                </div>

                <div class="latest-filename">
                    {latest_filename}
                </div>

                <div class="latest-date">
                    {latest_created}
                </div>

                {best_badge}

            </div>
            """
        )

    with latest_right:

        st.html(
            f"""
            <div class="latest-card">

                <div class="latest-score">
                    {latest_score:.0f}
                </div>

                <div class="latest-score-label">
                    ATS SCORE / 100
                </div>

                <div class="score-status {latest_status_class}"
                     style="margin-top: 10px; margin-left: 0;">
                    {latest_status.upper()}
                </div>

            </div>
            """
        )

    # ========================================================
    # ALL ANALYSES
    # ========================================================

    st.html(
        """
        <div class="section-header">

            <h2>
                All Analyses
            </h2>

            <p>
                Open any analysis to view its detailed scoring breakdown.
            </p>

            <div class="section-line"></div>

        </div>
        """
    )

    # ========================================================
    # HISTORY ENTRIES
    # ========================================================

    for idx, entry in enumerate(
        history
    ):

        filename = entry.get(
            "filename",
            "resume",
        )

        ats_score = float(
            entry.get(
                "ats_score",
                0,
            )
        )

        created_at = entry.get(
            "created_at",
            "",
        )

        analysis = (
            entry.get(
                "analysis_result",
                {},
            )
            or {}
        )

        component_scores = (
            analysis.get(
                "component_scores",
                {},
            )
            or {}
        )

        jd_comparison = (
            analysis.get(
                "jd_comparison"
            )
            or
            analysis.get(
                "jd_match_analysis"
            )
        )

        status, status_class = _score_status(
            ats_score
        )

        # ----------------------------------------------------
        # SCORE DIFFERENCE FROM PREVIOUS
        # ----------------------------------------------------

        improvement_html = ""

        if idx < len(history) - 1:

            previous_score = float(
                history[idx + 1].get(
                    "ats_score",
                    0,
                )
            )

            difference = ats_score - previous_score

            if difference > 0:

                improvement_html = f"""
                    <span class="score-status status-excellent">
                        +{difference:.0f} FROM PREVIOUS
                    </span>
                """

            elif difference < 0:

                improvement_html = f"""
                    <span class="score-status status-low">
                        {difference:.0f} FROM PREVIOUS
                    </span>
                """

            else:

                improvement_html = f"""
                    <span class="score-status status-good">
                        NO CHANGE
                    </span>
                """

        # ----------------------------------------------------
        # HISTORY CARD HEADER
        # ----------------------------------------------------

        st.html(
            f"""
            <div class="analysis-card">

                <div class="analysis-filename">
                    {filename}
                </div>

                <div class="analysis-date">
                    {created_at}
                </div>

                <div style="margin-top: 13px;">

                    <span class="analysis-score">
                        {ats_score:.0f}/100
                    </span>

                    <span class="score-status {status_class}">
                        {status.upper()}
                    </span>

                    {improvement_html}

                </div>

            </div>
            """
        )

        # ----------------------------------------------------
        # DETAILS
        # ----------------------------------------------------

        with st.expander(
            f"View detailed analysis — {filename}"
        ):

            st.markdown("")

            metric_data = [
                (
                    "Overall",
                    f"{ats_score:.0f}/100",
                ),
                (
                    "Formatting",
                    f"{component_scores.get('formatting', 0):.0f}/20",
                ),
                (
                    "Keywords",
                    f"{component_scores.get('keywords', 0):.0f}/25",
                ),
                (
                    "Content",
                    f"{component_scores.get('content', 0):.0f}/25",
                ),
                (
                    "Skill Validation",
                    f"{component_scores.get('skill_validation', 0):.0f}/15",
                ),
                (
                    "ATS Compatibility",
                    f"{component_scores.get('ats_compatibility', 0):.0f}/15",
                ),
            ]

            metric_cols = st.columns(
                3,
                gap="medium",
            )

            for metric_index, metric in enumerate(
                metric_data
            ):

                label, value = metric

                with metric_cols[
                    metric_index % 3
                ]:

                    st.html(
                        f"""
                        <div class="metric-card">

                            <div class="metric-label">
                                {label}
                            </div>

                            <div class="metric-value">
                                {value}
                            </div>

                        </div>
                        """
                    )

            # ------------------------------------------------
            # JD MATCH
            # ------------------------------------------------

            if jd_comparison:

                match_percentage = float(
                    jd_comparison.get(
                        "match_percentage",
                        0,
                    )
                )

                st.html(
                    f"""
                    <div class="jd-match-card">

                        <div>

                            <div class="jd-match-label">
                                JOB DESCRIPTION MATCH
                            </div>

                            <div style="
                                color:#475569;
                                font-size:11px;
                                margin-top:4px;
                            ">
                                Resume compatibility with the provided JD
                            </div>

                        </div>

                        <div class="jd-match-value">
                            {match_percentage:.0f}%
                        </div>

                    </div>
                    """
                )

            # ------------------------------------------------
            # DELETE
            # ------------------------------------------------

            entry_id = entry.get(
                "id"
            )

            if entry_id:

                st.markdown("")

                delete_col, _, _ = st.columns(
                    [1.2, 1, 2.8]
                )

                with delete_col:

                    if st.button(
                        "Delete Analysis",
                        key=f"delete_{idx}",
                        use_container_width=True,
                    ):

                        try:

                            api_client.delete_history_entry(
                                str(entry_id),
                                access_token,
                            )

                            st.success(
                                "Analysis deleted successfully."
                            )

                            st.rerun()

                        except requests.RequestException as exc:

                            _show_backend_error(
                                exc
                            )
