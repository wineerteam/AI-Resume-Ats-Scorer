from typing import Any, Dict

import streamlit as st


# ============================================================
# SCORE COMPONENTS
# Backend scores are on their original individual scales.
# ============================================================

COMPONENTS = [
    ("Formatting", "formatting", 20),
    ("Keywords & Skills", "keywords", 25),
    ("Content Quality", "content", 25),
    ("Skill Validation", "skill_validation", 15),
    ("ATS Compatibility", "ats_compatibility", 15),
]


# ============================================================
# HELPERS
# ============================================================

def _safe_number(value: Any) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def _clamp(
    value: float,
    minimum: float,
    maximum: float
) -> float:
    return max(minimum, min(value, maximum))


def _get_score_style(score: float):
    if score >= 90:
        return (
            "Excellent ATS Match",
            "#22c55e",
            "#052e16"
        )

    if score >= 80:
        return (
            "Strong ATS Match",
            "#06b6d4",
            "#083344"
        )

    if score >= 70:
        return (
            "Good ATS Match",
            "#38bdf8",
            "#082f49"
        )

    if score >= 60:
        return (
            "Moderate ATS Match",
            "#facc15",
            "#422006"
        )

    return (
        "Needs Improvement",
        "#fb7185",
        "#450a0a"
    )


def _get_component_style(percent: float):
    if percent >= 85:
        return (
            "Excellent",
            "#15803d",
            "#dcfce7"
        )

    if percent >= 70:
        return (
            "Strong",
            "#0369a1",
            "#e0f2fe"
        )

    if percent >= 60:
        return (
            "Moderate",
            "#a16207",
            "#fef3c7"
        )

    return (
        "Needs Work",
        "#c2410c",
        "#ffedd5"
    )


# ============================================================
# STYLES
# ============================================================

def _apply_styles():

    st.markdown(
        """
        <style>

        /* ==================================================
           TITLE
        ================================================== */

        .ats-title {
            font-size: 30px;
            font-weight: 900;
            color: #07152f;
            letter-spacing: -1px;
            margin-top: 15px;
            margin-bottom: 4px;
        }

        .ats-subtitle {
            color: #64748b;
            font-size: 12px;
            margin-bottom: 20px;
        }


        /* ==================================================
           HERO
        ================================================== */

        .ats-hero {
            position: relative;
            overflow: hidden;

            background:
                linear-gradient(
                    135deg,
                    #07152f 0%,
                    #0b2550 55%,
                    #123b6b 100%
                );

            border-radius: 28px;

            padding: 32px;

            min-height: 285px;

            box-shadow:
                0 22px 50px
                rgba(7, 21, 47, 0.20);

            border:
                1px solid
                rgba(255,255,255,.08);

            margin-bottom: 28px;
        }


        .ats-hero::before {
            content: "";

            position: absolute;

            width: 320px;
            height: 320px;

            border-radius: 50%;

            right: -150px;
            top: -180px;

            border:
                1px solid
                rgba(34,211,238,.16);

            box-shadow:
                0 0 0 45px
                rgba(34,211,238,.025),

                0 0 0 90px
                rgba(236,72,153,.02);
        }


        .ats-hero::after {
            content: "";

            position: absolute;

            width: 200px;
            height: 200px;

            border-radius: 50%;

            left: -130px;
            bottom: -130px;

            background:
                radial-gradient(
                    circle,
                    rgba(236,72,153,.13),
                    transparent 70%
                );
        }


        .ats-hero-grid {
            position: relative;

            z-index: 2;

            display: grid;

            grid-template-columns:
                260px
                1fr;

            align-items: center;

            gap: 40px;
        }


        /* ==================================================
           SCORE RING
        ================================================== */

        .ats-ring {
            width: 205px;
            height: 205px;

            border-radius: 50%;

            margin: auto;

            display: flex;

            align-items: center;
            justify-content: center;

            background:
                conic-gradient(
                    #06b6d4 0deg,
                    #2563eb 140deg,
                    #ec4899 270deg,
                    rgba(255,255,255,.09) 270deg
                );

            box-shadow:
                0 18px 40px
                rgba(0,0,0,.28);
        }


        .ats-ring-inner {
            width: 178px;
            height: 178px;

            border-radius: 50%;

            display: flex;

            flex-direction: column;

            align-items: center;
            justify-content: center;

            background:
                linear-gradient(
                    145deg,
                    #0a2042,
                    #06142d
                );

            box-shadow:
                inset 0 0 25px
                rgba(0,0,0,.25);
        }


        .ats-score-number {
            color: #ffffff;

            font-size: 58px;

            font-weight: 950;

            line-height: 1;

            letter-spacing: -4px;
        }


        .ats-score-label {
            color: #94a3b8;

            font-size: 9px;

            font-weight: 850;

            letter-spacing: 2px;

            margin-top: 8px;
        }


        /* ==================================================
           HERO CONTENT
        ================================================== */

        .ats-eyebrow {
            color: #67e8f9;

            font-size: 9px;

            font-weight: 900;

            letter-spacing: 2px;

            text-transform: uppercase;
        }


        .ats-status {
            color: white;

            font-size: 31px;

            font-weight: 950;

            line-height: 1.1;

            margin-top: 7px;
        }


        .ats-description {
            color: #cbd5e1;

            font-size: 11px;

            line-height: 1.7;

            max-width: 580px;

            margin-top: 10px;
        }


        .ats-pill {
            display: inline-block;

            margin-top: 16px;

            padding: 7px 13px;

            border-radius: 999px;

            font-size: 8px;

            font-weight: 900;
        }


        /* ==================================================
           BREAKDOWN
        ================================================== */

        .breakdown-title {
            color: #07152f;

            font-size: 23px;

            font-weight: 900;

            margin-bottom: 3px;
        }


        .breakdown-subtitle {
            color: #64748b;

            font-size: 10px;

            margin-bottom: 17px;
        }


        /* ==================================================
           COMPONENT CARDS
        ================================================== */

        .component-grid {
            display: grid;

            grid-template-columns:
                repeat(2, minmax(0, 1fr));

            gap: 16px;
        }


        .component-card {
            position: relative;

            overflow: hidden;

            background: #ffffff;

            border:
                1px solid
                #e2e8f0;

            border-radius: 21px;

            padding: 20px;

            box-shadow:
                0 8px 25px
                rgba(15,23,42,.055);

            transition:
                transform .22s ease,
                box-shadow .22s ease,
                border-color .22s ease;
        }


        .component-card:hover {
            transform:
                translateY(-7px);

            box-shadow:
                0 20px 40px
                rgba(15,23,42,.11);

            border-color:
                #93c5fd;
        }


        .component-card::before {
            content: "";

            position: absolute;

            top: 0;
            left: 0;

            width: 100%;
            height: 3px;

            background:
                linear-gradient(
                    90deg,
                    #06b6d4,
                    #2563eb,
                    #ec4899
                );
        }


        .component-header {
            display: flex;

            align-items: center;

            justify-content:
                space-between;
        }


        .component-name {
            color: #0f172a;

            font-size: 13px;

            font-weight: 900;
        }


        .component-weight {
            color: #94a3b8;

            font-size: 8px;

            font-weight: 850;

            letter-spacing: .5px;
        }


        .component-badge {
            display: inline-block;

            margin-top: 10px;

            padding: 4px 8px;

            border-radius: 999px;

            font-size: 7px;

            font-weight: 900;
        }


        .component-score-row {
            display: flex;

            align-items: baseline;

            margin-top: 12px;
        }


        .component-score {
            color: #07152f;

            font-size: 28px;

            font-weight: 950;

            letter-spacing: -1px;
        }


        .component-max {
            color: #94a3b8;

            font-size: 10px;

            margin-left: 4px;
        }


        .component-percent {
            color: #2563eb;

            font-size: 12px;

            font-weight: 900;

            margin-left: auto;
        }


        /* ==================================================
           PROGRESS BAR
        ================================================== */

        .progress-track {
            width: 100%;

            height: 8px;

            background: #e2e8f0;

            border-radius: 999px;

            overflow: hidden;

            margin-top: 11px;
        }


        .progress-value {
            height: 100%;

            border-radius: 999px;

            background:
                linear-gradient(
                    90deg,
                    #06b6d4,
                    #2563eb,
                    #6366f1
                );

            box-shadow:
                0 2px 8px
                rgba(37,99,235,.25);
        }


        .component-description {
            color: #64748b;

            font-size: 9px;

            line-height: 1.55;

            margin-top: 9px;
        }


        /* ==================================================
           HIGHLIGHTS
        ================================================== */

        .highlight-grid {
            display: grid;

            grid-template-columns:
                repeat(2, minmax(0, 1fr));

            gap: 16px;

            margin-top: 16px;
        }


        .highlight-card {
            background: #ffffff;

            border:
                1px solid
                #e2e8f0;

            border-radius: 20px;

            padding: 19px;

            box-shadow:
                0 8px 23px
                rgba(15,23,42,.05);

            transition:
                transform .2s ease,
                box-shadow .2s ease;
        }


        .highlight-card:hover {
            transform:
                translateY(-5px);

            box-shadow:
                0 17px 35px
                rgba(15,23,42,.09);
        }


        .highlight-strong {
            border-left:
                4px solid #06b6d4;
        }


        .highlight-priority {
            border-left:
                4px solid #f97316;
        }


        .highlight-label {
            color: #94a3b8;

            font-size: 8px;

            font-weight: 900;

            text-transform: uppercase;

            letter-spacing: 1px;
        }


        .highlight-name {
            color: #0f172a;

            font-size: 16px;

            font-weight: 950;

            margin-top: 5px;
        }


        .highlight-value {
            color: #2563eb;

            font-size: 10px;

            font-weight: 850;

            margin-top: 3px;
        }


        /* ==================================================
           RESPONSIVE
        ================================================== */

        @media (max-width: 800px) {

            .ats-hero-grid {
                grid-template-columns: 1fr;
            }

            .component-grid {
                grid-template-columns: 1fr;
            }

            .highlight-grid {
                grid-template-columns: 1fr;
            }

        }

        </style>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# OVERALL SCORE
# ============================================================

def display_overall_score(
    analysis: Dict[str, Any]
) -> None:

    _apply_styles()

    score = _safe_number(
        analysis.get(
            "ATS_score",
            analysis.get(
                "ats_score",
                0
            )
        )
    )

    score = _clamp(
        score,
        0,
        100
    )

    status, status_color, status_bg = (
        _get_score_style(score)
    )

    interpretation = str(
        analysis.get(
            "interpretation",
            ""
        )
        or ""
    ).strip()

    if not interpretation:

        interpretation = (
            "Your resume has been evaluated across "
            "multiple ATS performance categories. "
            "Review the breakdown below to identify "
            "your strongest and weakest areas."
        )

    st.markdown(
        """
        <div class="ats-title">
            Analysis Results
        </div>

        <div class="ats-subtitle">
            A complete view of your resume's ATS performance,
            scoring components, and improvement priorities.
        </div>
        """,
        unsafe_allow_html=True,
    )


    st.markdown(
        f"""
        <div class="ats-hero">

            <div class="ats-hero-grid">

                <div>

                    <div class="ats-ring">

                        <div class="ats-ring-inner">

                            <div class="ats-score-number">
                                {score:.0f}
                            </div>

                            <div class="ats-score-label">
                                OUT OF 100
                            </div>

                        </div>

                    </div>

                </div>


                <div>

                    <div class="ats-eyebrow">
                        Overall ATS Performance
                    </div>

                    <div class="ats-status">
                        {status}
                    </div>

                    <div class="ats-description">
                        {interpretation}
                    </div>

                    <div
                        class="ats-pill"
                        style="
                            color:{status_color};
                            background:{status_bg};
                        "
                    >
                        ATS SCORE {score:.0f}/100
                    </div>

                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# SCORE BREAKDOWN
# ============================================================

def display_score_breakdown(
    analysis: Dict[str, Any]
) -> None:

    component_scores = (
        analysis.get(
            "component_scores"
        )
        or {}
    )

    st.markdown(
        """
        <div class="breakdown-title">
            Score Breakdown
        </div>

        <div class="breakdown-subtitle">
            See how each scoring category contributes
            to your resume's ATS performance.
        </div>
        """,
        unsafe_allow_html=True,
    )


    component_data = []


    # --------------------------------------------------------
    # PREPARE DATA
    # --------------------------------------------------------

    for label, key, max_score in COMPONENTS:

        value = _safe_number(
            component_scores.get(
                key,
                0
            )
        )

        value = _clamp(
            value,
            0,
            float(max_score)
        )

        percentage = (
            value / max_score * 100
            if max_score
            else 0
        )

        percentage = _clamp(
            percentage,
            0,
            100
        )

        status, color, background = (
            _get_component_style(
                percentage
            )
        )

        component_data.append(
            {
                "label": label,
                "value": value,
                "max": max_score,
                "percentage": percentage,
                "status": status,
                "color": color,
                "background": background,
            }
        )


    # --------------------------------------------------------
    # CARDS
    # --------------------------------------------------------

    cards = """
    <div class="component-grid">
    """


    for item in component_data:

        if item["percentage"] >= 85:

            description = (
                "Excellent performance. "
                "Keep this area consistent."
            )

        elif item["percentage"] >= 70:

            description = (
                "Strong foundation with "
                "some room for refinement."
            )

        elif item["percentage"] >= 60:

            description = (
                "Reasonable foundation. "
                "Targeted improvements can help."
            )

        else:

            description = (
                "This is a priority area "
                "for improving ATS performance."
            )


        cards += f"""
        <div class="component-card">

            <div class="component-header">

                <div class="component-name">
                    {item["label"]}
                </div>

                <div class="component-weight">
                    WEIGHT {item["max"]}%
                </div>

            </div>


            <div
                class="component-badge"
                style="
                    color:{item["color"]};
                    background:{item["background"]};
                "
            >
                {item["status"]}
            </div>


            <div class="component-score-row">

                <div class="component-score">
                    {item["value"]:.0f}
                </div>

                <div class="component-max">
                    / {item["max"]}
                </div>

                <div class="component-percent">
                    {item["percentage"]:.0f}%
                </div>

            </div>


            <div class="progress-track">

                <div
                    class="progress-value"
                    style="
                        width:{item["percentage"]:.1f}%;
                    "
                ></div>

            </div>


            <div class="component-description">
                {description}
            </div>

        </div>
        """


    cards += """
    </div>
    """


    st.markdown(
        cards,
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # STRONGEST / PRIORITY
    # --------------------------------------------------------

    if component_data:

        strongest = max(
            component_data,
            key=lambda item: item["percentage"]
        )

        weakest = min(
            component_data,
            key=lambda item: item["percentage"]
        )


        st.markdown(
            f"""
            <div class="highlight-grid">

                <div
                    class="
                        highlight-card
                        highlight-strong
                    "
                >

                    <div class="highlight-label">
                        Strongest Area
                    </div>

                    <div class="highlight-name">
                        {strongest["label"]}
                    </div>

                    <div class="highlight-value">
                        {strongest["percentage"]:.0f}%
                        performance
                    </div>

                </div>


                <div
                    class="
                        highlight-card
                        highlight-priority
                    "
                >

                    <div class="highlight-label">
                        Priority To Improve
                    </div>

                    <div class="highlight-name">
                        {weakest["label"]}
                    </div>

                    <div class="highlight-value">
                        {weakest["percentage"]:.0f}%
                        performance
                    </div>

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )
