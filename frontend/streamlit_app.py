from typing import Any, Dict, List, Tuple

import streamlit as st

from frontend.components._helpers import get_score_color


# ============================================================
# BACKEND COMPONENT SCALE
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

def _safe_score(value: Any) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def _clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def _component_status(percent: float) -> Tuple[str, str, str]:
    """
    Returns:
        status, text_color, background_color
    """

    if percent >= 85:
        return (
            "Excellent",
            "#15803d",
            "#dcfce7",
        )

    if percent >= 70:
        return (
            "Strong",
            "#0369a1",
            "#e0f2fe",
        )

    if percent >= 60:
        return (
            "Moderate",
            "#a16207",
            "#fef3c7",
        )

    return (
        "Needs Work",
        "#c2410c",
        "#ffedd5",
    )


def _get_score_status(score: float) -> Tuple[str, str]:
    if score >= 90:
        return "Excellent ATS Match", "#15803d"

    if score >= 80:
        return "Strong ATS Match", "#0369a1"

    if score >= 70:
        return "Good ATS Match", "#0891b2"

    if score >= 60:
        return "Moderate ATS Match", "#a16207"

    return "Needs Improvement", "#c2410c"


def _get_component_insight(
    label: str,
    percent: float,
) -> str:

    if percent >= 85:
        return f"{label} is one of the strongest parts of your resume."

    if percent >= 70:
        return f"{label} is performing well with room for refinement."

    if percent >= 60:
        return f"{label} has a reasonable foundation but can be improved."

    return f"{label} should be prioritized for improvement."


def _apply_styles() -> None:

    st.markdown(
        """
        <style>

        /* ====================================================
           MAIN HEADER
        ==================================================== */

        .score-section-title {
            color: #07152f;
            font-size: 29px;
            font-weight: 950;
            letter-spacing: -0.035em;
            margin-top: 20px;
            margin-bottom: 4px;
        }

        .score-section-subtitle {
            color: #64748b;
            font-size: 12px;
            line-height: 1.6;
            margin-bottom: 18px;
        }


        /* ====================================================
           HERO
        ==================================================== */

        .ats-hero {
            position: relative;
            overflow: hidden;

            min-height: 300px;

            border-radius: 28px;

            padding: 30px;

            background:
                linear-gradient(
                    135deg,
                    #07152f 0%,
                    #0b2550 52%,
                    #123a6b 100%
                );

            box-shadow:
                0 24px 55px
                rgba(7, 21, 47, 0.20);

            border:
                1px solid
                rgba(255,255,255,0.08);

            margin-bottom: 25px;
        }


        .ats-hero::before {
            content: "";

            position: absolute;

            width: 270px;
            height: 270px;

            border-radius: 50%;

            right: -100px;
            top: -150px;

            border:
                1px solid
                rgba(34,211,238,0.18);

            box-shadow:
                0 0 0 45px
                rgba(34,211,238,0.025),
                0 0 0 90px
                rgba(236,72,153,0.018);
        }


        .ats-hero::after {
            content: "";

            position: absolute;

            width: 180px;
            height: 180px;

            border-radius: 50%;

            left: -100px;
            bottom: -110px;

            background:
                radial-gradient(
                    circle,
                    rgba(236,72,153,0.13),
                    transparent 68%
                );
        }


        .ats-hero-grid {
            position: relative;

            z-index: 2;

            display: grid;

            grid-template-columns:
                270px
                minmax(0, 1fr);

            gap: 42px;

            align-items: center;

            height: 100%;
        }


        /* ====================================================
           SCORE RING
           ==================================================== */

        .ats-score-ring {
            position: relative;

            width: 220px;
            height: 220px;

            border-radius: 50%;

            margin: auto;

            display: flex;

            align-items: center;
            justify-content: center;

            background:
                conic-gradient(
                    var(--score-color)
                    var(--score-percent),
                    rgba(255,255,255,0.09)
                    var(--score-percent)
                );

            box-shadow:
                0 0 0 1px
                rgba(255,255,255,0.08),
                0 18px 45px
                rgba(0,0,0,.20);
        }


        .ats-score-ring::before {
            content: "";

            position: absolute;

            inset: 10px;

            border-radius: 50%;

            background:
                linear-gradient(
                    145deg,
                    #0a1d3d,
                    #06142d
                );

            box-shadow:
                inset 0 0 30px
                rgba(0,0,0,.20);
        }


        .ats-score-content {
            position: relative;

            z-index: 2;

            text-align: center;
        }


        .ats-score-value {
            color: white;

            font-size: 58px;

            line-height: .95;

            font-weight: 950;

            letter-spacing: -0.06em;
        }


        .ats-score-outof {
            color: #94a3b8;

            font-size: 9px;

            font-weight: 800;

            letter-spacing: .15em;

            margin-top: 7px;
        }


        /* ====================================================
           HERO CONTENT
           ==================================================== */

        .hero-eyebrow {
            color: #67e8f9;

            font-size: 9px;

            font-weight: 950;

            letter-spacing: .14em;

            text-transform: uppercase;

            margin-bottom: 8px;
        }


        .hero-heading {
            color: white;

            font-size: 31px;

            font-weight: 950;

            line-height: 1.1;

            letter-spacing: -.035em;
        }


        .hero-heading span {
            color: #67e8f9;
        }


        .hero-description {
            color: #cbd5e1;

            font-size: 11px;

            line-height: 1.75;

            max-width: 560px;

            margin-top: 10px;
        }


        .hero-badge {
            display: inline-block;

            margin-top: 15px;

            padding:
                7px 12px;

            border-radius: 999px;

            font-size: 8px;

            font-weight: 950;

            letter-spacing: .05em;

            border: 1px solid
                rgba(255,255,255,.10);
        }


        /* ====================================================
           BREAKDOWN HEADER
           ==================================================== */

        .breakdown-heading {
            color: #07152f;

            font-size: 22px;

            font-weight: 950;

            letter-spacing: -.025em;

            margin-top: 8px;

            margin-bottom: 3px;
        }


        .breakdown-subheading {
            color: #64748b;

            font-size: 10px;

            margin-bottom: 15px;
        }


        /* ====================================================
           COMPONENT GRID
           ==================================================== */

        .component-grid {
            display: grid;

            grid-template-columns:
                repeat(
                    2,
                    minmax(0, 1fr)
                );

            gap: 15px;

            margin-bottom: 20px;
        }


        .component-card {
            position: relative;

            overflow: hidden;

            padding: 19px;

            border-radius: 20px;

            background:
                linear-gradient(
                    145deg,
                    #ffffff,
                    #f8fafc
                );

            border: 1px solid #e2e8f0;

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
                translateY(-7px)
                scale(1.012);

            box-shadow:
                0 20px 42px
                rgba(15,23,42,.11);

            border-color:
                #93c5fd;
        }


        .component-card::before {
            content: "";

            position: absolute;

            left: 0;
            top: 0;

            width: 100%;
            height: 3px;

            background:
                linear-gradient(
                    90deg,
                    #06b6d4,
                    #3b82f6,
                    #ec4899
                );
        }


        .component-top {
            display: flex;

            justify-content:
                space-between;

            align-items:
                center;

            gap: 10px;
        }


        .component-name {
            color: #0f172a;

            font-size: 13px;

            font-weight: 900;
        }


        .component-weight {
            color: #94a3b8;

            font-size: 8px;

            font-weight: 800;
        }


        .component-status {
            display: inline-block;

            padding:
                4px 8px;

            border-radius: 999px;

            font-size: 7px;

            font-weight: 950;

            margin-top: 12px;
        }


        .component-score-row {
            display: flex;

            align-items: baseline;

            gap: 5px;

            margin-top: 12px;
        }


        .component-score {
            color: #07152f;

            font-size: 26px;

            font-weight: 950;

            letter-spacing: -.04em;
        }


        .component-max {
            color: #94a3b8;

            font-size: 10px;

            font-weight: 750;
        }


        .component-percent {
            margin-left: auto;

            color: #475569;

            font-size: 11px;

            font-weight: 900;
        }


        /* ====================================================
           PROGRESS
           ==================================================== */

        .component-track {
            width: 100%;

            height: 8px;

            background: #e2e8f0;

            border-radius: 999px;

            overflow: hidden;

            margin-top: 11px;
        }


        .component-fill {
            height: 100%;

            border-radius: 999px;

            background:
                linear-gradient(
                    90deg,
                    #06b6d4,
                    #2563eb
                );

            box-shadow:
                0 2px 8px
                rgba(37,99,235,.22);
        }


        .component-insight {
            color: #64748b;

            font-size: 9px;

            line-height: 1.55;

            margin-top: 9px;
        }


        /* ====================================================
           HIGHLIGHTS
           ==================================================== */

        .highlight-grid {
            display: grid;

            grid-template-columns:
                repeat(
                    2,
                    minmax(0,1fr)
                );

            gap: 15px;

            margin-top: 5px;

            margin-bottom: 20px;
        }


        .highlight-card {
            position: relative;

            overflow: hidden;

            padding: 18px;

            border-radius: 20px;

            background: white;

            border: 1px solid #e2e8f0;

            box-shadow:
                0 8px 24px
                rgba(15,23,42,.05);

            transition:
                transform .22s ease,
                box-shadow .22s ease;
        }


        .highlight-card:hover {
            transform:
                translateY(-5px);

            box-shadow:
                0 17px 35px
                rgba(15,23,42,.09);
        }


        .highlight-card.strong {
            border-left:
                4px solid #06b6d4;
        }


        .highlight-card.priority {
            border-left:
                4px solid #f97316;
        }


        .highlight-label {
            color: #94a3b8;

            font-size: 8px;

            font-weight: 950;

            text-transform: uppercase;

            letter-spacing: .10em;
        }


        .highlight-name {
            color: #0f172a;

            font-size: 16px;

            font-weight: 950;

            margin-top: 5px;
        }


        .highlight-value {
            color: #0369a1;

            font-size: 10px;

            font-weight: 850;

            margin-top: 3px;
        }


        /* ====================================================
           RESPONSIVE
           ==================================================== */

        @media (max-width: 850px) {

            .ats-hero-grid {
                grid-template-columns: 1fr;
                gap: 22px;
            }

            .ats-score-ring {
                width: 185px;
                height: 185px;
            }

            .ats-score-value {
                font-size: 48px;
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
    analysis: Dict[str, Any],
) -> None:

    _apply_styles()

    score = _safe_score(
        analysis.get(
            "ATS_score",
            analysis.get(
                "ats_score",
                0,
            ),
        )
    )

    score = _clamp(score)

    interpretation = str(
        analysis.get(
            "interpretation",
            "",
        )
        or ""
    ).strip()

    status, status_color = _get_score_status(
        score
    )

    _, score_bg = get_score_color(
        score
    )

    if not interpretation:

        if score >= 90:
            interpretation = (
                "Your resume shows excellent ATS alignment "
                "and strong recruiter-ready signals."
            )

        elif score >= 80:
            interpretation = (
                "Your resume has a strong ATS foundation "
                "with a few areas worth refining."
            )

        elif score >= 70:
            interpretation = (
                "Your resume has a good foundation, "
                "but targeted improvements can increase "
                "its ATS performance."
            )

        elif score >= 60:
            interpretation = (
                "Your resume is partially aligned with ATS "
                "requirements and needs focused improvement."
            )

        else:
            interpretation = (
                "Several important areas need attention "
                "before the resume is fully ATS-ready."
            )

    st.html(
        """
        <div class="score-section-title">
            Analysis Results
        </div>

        <div class="score-section-subtitle">
            A complete view of your resume's ATS performance,
            scoring components, and improvement priorities.
        </div>
        """
    )

    st.html(
        f"""
        <div class="ats-hero">

            <div class="ats-hero-grid">

                <div>

                    <div
                        class="ats-score-ring"
                        style="
                            --score-percent:{score:.1f}%;
                            --score-color:{status_color};
                        "
                    >

                        <div class="ats-score-content">

                            <div class="ats-score-value">
                                {score:.0f}
                            </div>

                            <div class="ats-score-outof">
                                OUT OF 100
                            </div>

                        </div>

                    </div>

                </div>


                <div>

                    <div class="hero-eyebrow">
                        Overall Resume Performance
                    </div>

                    <div class="hero-heading">
                        <span>{status}</span>
                    </div>

                    <div class="hero-description">
                        {interpretation}
                    </div>

                    <div
                        class="hero-badge"
                        style="
                            color:{status_color};
                            background:{score_bg};
                        "
                    >
                        ATS SCORE: {score:.0f}/100
                    </div>

                </div>

            </div>

        </div>
        """
    )


# ============================================================
# SCORE BREAKDOWN
# ============================================================

def display_score_breakdown(
    analysis: Dict[str, Any],
) -> None:

    component_scores = (
        analysis.get(
            "component_scores"
        )
        or {}
    )

    st.html(
        """
        <div class="breakdown-heading">
            Score Breakdown
        </div>

        <div class="breakdown-subheading">
            See how each ATS scoring category contributes
            to your overall resume performance.
        </div>
        """
    )

    components_data: List[Dict[str, Any]] = []

    for label, key, max_score in COMPONENTS:

        raw_value = _safe_score(
            component_scores.get(
                key,
                0,
            )
        )

        value = _clamp(
            raw_value,
            0,
            float(max_score),
        )

        percentage = (
            value / max_score * 100
            if max_score
            else 0
        )

        percentage = _clamp(
            percentage
        )

        status, color, background = (
            _component_status(
                percentage
            )
        )

        components_data.append(
            {
                "label": label,
                "key": key,
                "value": value,
                "max": max_score,
                "percentage": percentage,
                "status": status,
                "color": color,
                "background": background,
            }
        )

    # --------------------------------------------------------
    # COMPONENT CARDS
    # --------------------------------------------------------

    cards_html = """
    <div class="component-grid">
    """

    for item in components_data:

        cards_html += f"""
        <div class="component-card">

            <div class="component-top">

                <div class="component-name">
                    {item["label"]}
                </div>

                <div class="component-weight">
                    WEIGHT {item["max"]}%
                </div>

            </div>


            <div
                class="component-status"
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


            <div class="component-track">

                <div
                    class="component-fill"
                    style="
                        width:{item["percentage"]:.1f}%;
                    "
                ></div>

            </div>


            <div class="component-insight">
                {_get_component_insight(
                    item["label"],
                    item["percentage"]
                )}
            </div>

        </div>
        """

    cards_html += """
    </div>
    """

    st.html(
        cards_html
    )

    # --------------------------------------------------------
    # STRONGEST / PRIORITY
    # --------------------------------------------------------

    if components_data:

        strongest = max(
            components_data,
            key=lambda x: x["percentage"],
        )

        weakest = min(
            components_data,
            key=lambda x: x["percentage"],
        )

        st.html(
            f"""
            <div class="highlight-grid">

                <div class="highlight-card strong">

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


                <div class="highlight-card priority">

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
            """
        )
