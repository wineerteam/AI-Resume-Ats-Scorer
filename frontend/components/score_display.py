from typing import Any, Dict, List, Tuple

import streamlit as st

from frontend.components._helpers import get_score_color


# ============================================================
# COMPONENT CONFIG
# ============================================================

COMPONENTS: List[Tuple[str, str, int]] = [
    ("Formatting", "formatting", 20),
    ("Keywords & Skills", "keywords", 25),
    ("Content Quality", "content", 25),
    ("Skill Validation", "skill_validation", 15),
    ("ATS Compatibility", "ats_compatibility", 15),
]


# ============================================================
# HELPERS
# ============================================================

def _safe_float(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def _score_status(score: float) -> Dict[str, str]:
    if score >= 90:
        return {
            "label": "Excellent",
            "color": "#166534",
            "bg": "#dcfce7",
            "border": "#86efac",
        }

    if score >= 80:
        return {
            "label": "Strong",
            "color": "#0369a1",
            "bg": "#e0f2fe",
            "border": "#7dd3fc",
        }

    if score >= 70:
        return {
            "label": "Good",
            "color": "#0f766e",
            "bg": "#ccfbf1",
            "border": "#5eead4",
        }

    if score >= 60:
        return {
            "label": "Moderate",
            "color": "#a16207",
            "bg": "#fef3c7",
            "border": "#fcd34d",
        }

    return {
        "label": "Needs Work",
        "color": "#b91c1c",
        "bg": "#fee2e2",
        "border": "#fca5a5",
    }


def _priority_level(score: float) -> Dict[str, str]:
    if score < 60:
        return {
            "label": "HIGH PRIORITY",
            "color": "#b91c1c",
            "bg": "#fee2e2",
        }

    if score < 75:
        return {
            "label": "MEDIUM PRIORITY",
            "color": "#a16207",
            "bg": "#fef3c7",
        }

    return {
        "label": "LOW PRIORITY",
        "color": "#166534",
        "bg": "#dcfce7",
    }


def _component_tip(
    label: str,
    percentage: float,
) -> str:

    if percentage >= 85:
        return f"{label} is performing strongly."

    if percentage >= 70:
        return (
            f"{label} is in a good range with some "
            "room for refinement."
        )

    if percentage >= 60:
        return (
            f"{label} should be reviewed for targeted "
            "improvements."
        )

    return (
        f"{label} is a key improvement opportunity "
        "for your resume."
    )


def _apply_styles() -> None:

    st.markdown(
        """
        <style>

        /* =====================================================
           GLOBAL
        ===================================================== */

        .ats-v6-title {
            color: #0f172a;
            font-size: 30px;
            font-weight: 950;
            letter-spacing: -0.03em;
            margin-top: 18px;
        }

        .ats-v6-subtitle {
            color: #64748b;
            font-size: 13px;
            line-height: 1.6;
            margin-top: 4px;
            margin-bottom: 20px;
        }


        /* =====================================================
           HERO
        ===================================================== */

        .ats-hero {
            position: relative;
            overflow: hidden;
            border-radius: 26px;
            padding: 28px;
            background:
                linear-gradient(
                    135deg,
                    #07152f 0%,
                    #102a56 55%,
                    #075985 100%
                );
            box-shadow:
                0 20px 48px rgba(15,23,42,.20);
            margin-bottom: 22px;
        }

        .ats-hero::before {
            content: "";
            position: absolute;
            width: 260px;
            height: 260px;
            border-radius: 50%;
            border: 1px solid
                rgba(255,255,255,.08);
            right: -105px;
            top: -125px;
        }

        .ats-hero::after {
            content: "";
            position: absolute;
            width: 190px;
            height: 190px;
            border-radius: 50%;
            border: 1px solid
                rgba(34,211,238,.10);
            left: -100px;
            bottom: -120px;
        }

        .ats-hero-grid {
            position: relative;
            z-index: 2;
            display: grid;
            grid-template-columns:
                205px 1fr;
            gap: 28px;
            align-items: center;
        }


        /* =====================================================
           SCORE RING
        ===================================================== */

        .ats-score-ring {
            width: 180px;
            height: 180px;
            border-radius: 50%;
            margin: auto;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;

            background:
                conic-gradient(
                    #22d3ee var(--score),
                    rgba(255,255,255,.10) 0
                );

            box-shadow:
                0 0 45px
                rgba(34,211,238,.18);
        }

        .ats-score-ring::before {
            content: "";
            position: absolute;
            width: 141px;
            height: 141px;
            border-radius: 50%;
            background: #0a1a36;
        }

        .ats-score-value {
            position: relative;
            z-index: 2;
            color: white;
            font-size: 44px;
            font-weight: 950;
            line-height: 1;
        }

        .ats-score-outof {
            position: absolute;
            z-index: 3;
            color: #94a3b8;
            font-size: 9px;
            margin-top: 60px;
            letter-spacing: .08em;
            font-weight: 800;
        }


        /* =====================================================
           HERO CONTENT
        ===================================================== */

        .ats-eyebrow {
            color: #67e8f9;
            font-size: 9px;
            font-weight: 900;
            text-transform: uppercase;
            letter-spacing: .13em;
        }

        .ats-hero-heading {
            color: white;
            font-size: 28px;
            font-weight: 950;
            margin-top: 5px;
        }

        .ats-hero-text {
            color: #cbd5e1;
            font-size: 12px;
            line-height: 1.7;
            max-width: 680px;
            margin-top: 6px;
        }

        .ats-hero-badge {
            display: inline-block;
            padding: 7px 12px;
            margin-top: 14px;
            border-radius: 999px;
            color: #e0f2fe;
            background:
                rgba(255,255,255,.09);
            border: 1px solid
                rgba(255,255,255,.13);
            font-size: 9px;
            font-weight: 900;
        }


        /* =====================================================
           SCORE HEALTH
        ===================================================== */

        .health-title {
            color: #0f172a;
            font-size: 20px;
            font-weight: 900;
            margin-top: 18px;
        }

        .health-subtitle {
            color: #64748b;
            font-size: 11px;
            margin-top: 3px;
            margin-bottom: 13px;
        }

        .health-card {
            padding: 16px;
            border-radius: 18px;
            background: white;
            border: 1px solid #e2e8f0;
            box-shadow:
                0 7px 20px rgba(15,23,42,.055);
        }

        .health-scale {
            display: grid;
            grid-template-columns:
                repeat(5, 1fr);
            gap: 7px;
        }

        .health-item {
            text-align: center;
            padding: 10px 5px;
            border-radius: 13px;
            border: 1px solid #e2e8f0;
            background: #f8fafc;
        }

        .health-dot {
            width: 9px;
            height: 9px;
            border-radius: 50%;
            margin: 0 auto 6px auto;
        }

        .health-label {
            font-size: 9px;
            color: #334155;
            font-weight: 850;
        }

        .health-range {
            color: #94a3b8;
            font-size: 8px;
            margin-top: 2px;
        }


        /* =====================================================
           BREAKDOWN
        ===================================================== */

        .breakdown-title {
            color: #0f172a;
            font-size: 21px;
            font-weight: 900;
            margin-top: 25px;
        }

        .breakdown-subtitle {
            color: #64748b;
            font-size: 11px;
            margin-top: 3px;
            margin-bottom: 14px;
        }

        .component-grid-v6 {
            display: grid;
            grid-template-columns:
                repeat(2, minmax(0, 1fr));
            gap: 14px;
        }

        .component-card-v6 {
            position: relative;
            padding: 18px;
            border-radius: 20px;
            background:
                linear-gradient(
                    145deg,
                    #ffffff,
                    #f8fafc
                );
            border: 1px solid #e2e8f0;
            box-shadow:
                0 8px 22px rgba(15,23,42,.055);
            overflow: hidden;

            transition:
                transform .23s ease,
                box-shadow .23s ease,
                border-color .23s ease;
        }

        .component-card-v6:hover {
            transform:
                translateY(-6px)
                scale(1.01);
            box-shadow:
                0 18px 36px rgba(15,23,42,.11);
            border-color:
                rgba(14,165,233,.25);
        }

        .component-card-v6::before {
            content: "";
            position: absolute;
            left: 0;
            top: 0;
            bottom: 0;
            width: 4px;
            background:
                linear-gradient(
                    180deg,
                    #06b6d4,
                    #3b82f6
                );
        }

        .component-header-v6 {
            display: flex;
            justify-content: space-between;
            gap: 10px;
            align-items: flex-start;
        }

        .component-name-v6 {
            color: #0f172a;
            font-size: 14px;
            font-weight: 900;
        }

        .component-weight-v6 {
            color: #64748b;
            font-size: 9px;
            margin-top: 3px;
        }

        .component-status-v6 {
            padding: 5px 8px;
            border-radius: 999px;
            font-size: 8px;
            font-weight: 900;
            white-space: nowrap;
        }

        .component-number-row {
            display: flex;
            align-items: baseline;
            margin-top: 14px;
            gap: 5px;
        }

        .component-number-v6 {
            color: #0f172a;
            font-size: 27px;
            font-weight: 950;
        }

        .component-max-v6 {
            color: #94a3b8;
            font-size: 11px;
            font-weight: 750;
        }

        .component-percent-v6 {
            margin-left: auto;
            color: #0369a1;
            font-size: 13px;
            font-weight: 900;
        }

        .component-track-v6 {
            height: 9px;
            background: #e2e8f0;
            border-radius: 999px;
            overflow: hidden;
            margin-top: 8px;
        }

        .component-fill-v6 {
            height: 100%;
            border-radius: 999px;
            background:
                linear-gradient(
                    90deg,
                    #06b6d4,
                    #3b82f6
                );
        }

        .component-bottom-v6 {
            display: flex;
            justify-content: space-between;
            gap: 10px;
            margin-top: 10px;
        }

        .component-tip-v6 {
            color: #64748b;
            font-size: 9px;
            line-height: 1.5;
        }

        .component-contribution-v6 {
            color: #0f172a;
            font-size: 9px;
            font-weight: 850;
            white-space: nowrap;
        }


        /* =====================================================
           PRIORITY SECTION
        ===================================================== */

        .priority-title {
            color: #0f172a;
            font-size: 20px;
            font-weight: 900;
            margin-top: 25px;
        }

        .priority-subtitle {
            color: #64748b;
            font-size: 11px;
            margin-top: 3px;
            margin-bottom: 13px;
        }

        .priority-grid {
            display: grid;
            grid-template-columns:
                repeat(2, minmax(0, 1fr));
            gap: 13px;
        }

        .priority-card {
            padding: 17px;
            border-radius: 18px;
            background: white;
            border: 1px solid #e2e8f0;
            box-shadow:
                0 7px 20px rgba(15,23,42,.055);
            transition:
                transform .2s ease,
                box-shadow .2s ease;
        }

        .priority-card:hover {
            transform: translateY(-5px);
            box-shadow:
                0 15px 30px rgba(15,23,42,.09);
        }

        .priority-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 10px;
        }

        .priority-rank {
            color: #0369a1;
            font-size: 10px;
            font-weight: 950;
        }

        .priority-badge {
            padding: 5px 8px;
            border-radius: 999px;
            font-size: 8px;
            font-weight: 900;
        }

        .priority-name {
            color: #0f172a;
            font-size: 15px;
            font-weight: 900;
            margin-top: 9px;
        }

        .priority-score {
            color: #64748b;
            font-size: 10px;
            margin-top: 3px;
        }

        .priority-bar {
            height: 6px;
            background: #e2e8f0;
            border-radius: 999px;
            margin-top: 10px;
            overflow: hidden;
        }

        .priority-fill {
            height: 100%;
            border-radius: 999px;
            background:
                linear-gradient(
                    90deg,
                    #f97316,
                    #ef4444
                );
        }


        /* =====================================================
           RECRUITER READINESS
        ===================================================== */

        .readiness-card {
            margin-top: 22px;
            padding: 19px;
            border-radius: 20px;
            background:
                linear-gradient(
                    135deg,
                    #fff7ed,
                    #fff1f2
                );
            border: 1px solid #fed7aa;
            box-shadow:
                0 8px 22px rgba(15,23,42,.055);
        }

        .readiness-label {
            color: #9a3412;
            font-size: 9px;
            font-weight: 900;
            text-transform: uppercase;
            letter-spacing: .09em;
        }

        .readiness-title {
            color: #0f172a;
            font-size: 17px;
            font-weight: 900;
            margin-top: 4px;
        }

        .readiness-text {
            color: #57534e;
            font-size: 11px;
            line-height: 1.65;
            margin-top: 4px;
        }


        /* =====================================================
           RESPONSIVE
        ===================================================== */

        @media (max-width: 800px) {

            .ats-hero-grid {
                grid-template-columns: 1fr;
                text-align: center;
            }

            .ats-hero-text {
                margin-left: auto;
                margin-right: auto;
            }

            .health-scale {
                grid-template-columns:
                    repeat(3, 1fr);
            }

        }

        @media (max-width: 650px) {

            .component-grid-v6,
            .priority-grid {
                grid-template-columns: 1fr;
            }

            .health-scale {
                grid-template-columns:
                    repeat(2, 1fr);
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

    score = _safe_float(
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

    status = _score_status(score)

    # --------------------------------------------------------
    # Fallback interpretation
    # --------------------------------------------------------

    if not interpretation:

        if score >= 90:
            interpretation = (
                "Your resume demonstrates excellent overall "
                "ATS performance."
            )

        elif score >= 80:
            interpretation = (
                "Your resume has strong ATS performance "
                "with a solid overall structure."
            )

        elif score >= 70:
            interpretation = (
                "Your resume has a good ATS foundation, "
                "with some areas that can be refined."
            )

        elif score >= 60:
            interpretation = (
                "Your resume has a moderate ATS foundation "
                "and would benefit from targeted improvements."
            )

        else:
            interpretation = (
                "Your resume has several ATS improvement "
                "opportunities that should be addressed."
            )

    # ========================================================
    # HEADER
    # ========================================================

    st.markdown(
        """
        <div class="ats-v6-title">
            Analysis Results
        </div>

        <div class="ats-v6-subtitle">
            A complete view of your resume's ATS performance,
            scoring components, and improvement priorities.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ========================================================
    # HERO
    # ========================================================

    st.markdown(
        f"""
        <div class="ats-hero">

            <div class="ats-hero-grid">

                <div>

                    <div
                        class="ats-score-ring"
                        style="--score:{score:.1f}%"
                    >

                        <div class="ats-score-value">
                            {score:.0f}
                        </div>

                        <div class="ats-score-outof">
                            OUT OF 100
                        </div>

                    </div>

                </div>


                <div>

                    <div class="ats-eyebrow">
                        Overall ATS Performance
                    </div>

                    <div class="ats-hero-heading">
                        {status["label"]} ATS Match
                    </div>

                    <div class="ats-hero-text">
                        {interpretation}
                    </div>

                    <div class="ats-hero-badge">
                        ATS SCORE &nbsp; {score:.0f}/100
                    </div>

                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    # ========================================================
    # SCORE HEALTH
    # ========================================================

    health_levels = [
        ("Excellent", "90+", "#22c55e"),
        ("Strong", "80–89", "#06b6d4"),
        ("Good", "70–79", "#14b8a6"),
        ("Moderate", "60–69", "#f59e0b"),
        ("Needs Work", "<60", "#ef4444"),
    ]

    health_html = """
    <div class="health-title">
        ATS Score Health
    </div>

    <div class="health-subtitle">
        Understand where your current score sits on the
        overall ATS performance scale.
    </div>

    <div class="health-card">

        <div class="health-scale">
    """

    for label, score_range, color in health_levels:

        health_html += f"""
            <div class="health-item">

                <div
                    class="health-dot"
                    style="background:{color};"
                ></div>

                <div class="health-label">
                    {label}
                </div>

                <div class="health-range">
                    {score_range}
                </div>

            </div>
        """

    health_html += """
        </div>

    </div>
    """

    st.markdown(
        health_html,
        unsafe_allow_html=True,
    )


# ============================================================
# SCORE BREAKDOWN
# ============================================================

def display_score_breakdown(
    analysis: Dict[str, Any],
) -> None:

    _apply_styles()

    component_scores = (
        analysis.get(
            "component_scores"
        ) or {}
    )

    # ========================================================
    # PREPARE DATA
    # ========================================================

    data = []

    for label, key, max_score in COMPONENTS:

        value = _safe_float(
            component_scores.get(
                key,
                0,
            )
        )

        value = max(
            0.0,
            min(
                float(max_score),
                value,
            ),
        )

        percentage = (
            value / max_score * 100
            if max_score
            else 0
        )

        percentage = _clamp(
            percentage
        )

        status = _score_status(
            percentage
        )

        data.append(
            {
                "label": label,
                "key": key,
                "value": value,
                "max": max_score,
                "percentage": percentage,
                "status": status,
            }
        )

    # ========================================================
    # HEADER
    # ========================================================

    st.markdown(
        """
        <div class="breakdown-title">
            Score Breakdown
        </div>

        <div class="breakdown-subtitle">
            Each category is shown on its own backend-defined
            scoring scale while the percentage shows relative
            performance within that category.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ========================================================
    # COMPONENT CARDS
    # ========================================================

    cards = '<div class="component-grid-v6">'

    for item in data:

        status = item["status"]

        cards += f"""
        <div class="component-card-v6">

            <div class="component-header-v6">

                <div>

                    <div class="component-name-v6">
                        {item["label"]}
                    </div>

                    <div class="component-weight-v6">
                        Weight: {item["max"]}% of total score
                    </div>

                </div>

                <div
                    class="component-status-v6"
                    style="
                        color:{status["color"]};
                        background:{status["bg"]};
                        border:1px solid
                            {status["border"]};
                    "
                >
                    {status["label"]}
                </div>

            </div>


            <div class="component-number-row">

                <div class="component-number-v6">
                    {item["value"]:.0f}
                </div>

                <div class="component-max-v6">
                    / {item["max"]}
                </div>

                <div class="component-percent-v6">
                    {item["percentage"]:.0f}%
                </div>

            </div>


            <div class="component-track-v6">

                <div
                    class="component-fill-v6"
                    style="
                        width:{item["percentage"]:.0f}%;
                    "
                ></div>

            </div>


            <div class="component-bottom-v6">

                <div class="component-tip-v6">
                    {_component_tip(
                        item["label"],
                        item["percentage"],
                    )}
                </div>

                <div class="component-contribution-v6">
                    Contribution:
                    {item["value"]:.0f}
                </div>

            </div>

        </div>
        """

    cards += "</div>"

    st.markdown(
        cards,
        unsafe_allow_html=True,
    )

    # ========================================================
    # IMPROVEMENT PRIORITIES
    # ========================================================

    weakest_first = sorted(
        data,
        key=lambda item: item["percentage"],
    )

    priority_items = [
        item
        for item in weakest_first
        if item["percentage"] < 85
    ][:3]

    if priority_items:

        st.markdown(
            """
            <div class="priority-title">
                Improvement Priorities
            </div>

            <div class="priority-subtitle">
                Focus on the lowest-performing scoring
                categories first for the most targeted review.
            </div>
            """,
            unsafe_allow_html=True,
        )

        priority_html = '<div class="priority-grid">'

        for index, item in enumerate(
            priority_items,
            start=1,
        ):

            priority = _priority_level(
                item["percentage"]
            )

            priority_html += f"""
            <div class="priority-card">

                <div class="priority-top">

                    <div class="priority-rank">
                        PRIORITY {index}
                    </div>

                    <div
                        class="priority-badge"
                        style="
                            color:{priority["color"]};
                            background:{priority["bg"]};
                        "
                    >
                        {priority["label"]}
                    </div>

                </div>


                <div class="priority-name">
                    {item["label"]}
                </div>

                <div class="priority-score">
                    Current performance:
                    {item["percentage"]:.0f}%
                    &nbsp; ({item["value"]:.0f}/{item["max"]})
                </div>


                <div class="priority-bar">

                    <div
                        class="priority-fill"
                        style="
                            width:{item["percentage"]:.0f}%;
                        "
                    ></div>

                </div>

            </div>
            """

        priority_html += "</div>"

        st.markdown(
            priority_html,
            unsafe_allow_html=True,
        )

    # ========================================================
    # STRONGEST + PRIORITY AREA
    # ========================================================

    strongest = max(
        data,
        key=lambda item: item["percentage"],
    )

    weakest = min(
        data,
        key=lambda item: item["percentage"],
    )

    if weakest["percentage"] >= 85:

        readiness_title = (
            "Excellent Overall Foundation"
        )

        readiness_text = (
            "All scoring categories are performing strongly. "
            "Your next improvements should focus on fine-tuning "
            "rather than major structural changes."
        )

    elif weakest["percentage"] >= 70:

        readiness_title = (
            "Strong Foundation with Targeted Opportunities"
        )

        readiness_text = (
            f"{strongest['label']} is currently your strongest "
            f"area, while {weakest['label']} is the main area "
            "to review for further improvement."
        )

    else:

        readiness_title = (
            "Good Starting Point — Prioritize Weak Areas"
        )

        readiness_text = (
            f"{weakest['label']} currently has the largest "
            "improvement opportunity. Addressing the lowest "
            "scoring areas can make your resume more balanced."
        )

    # ========================================================
    # RECRUITER READINESS
    # ========================================================

    st.markdown(
        f"""
        <div class="readiness-card">

            <div class="readiness-label">
                Recruiter Readiness Insight
            </div>

            <div class="readiness-title">
                {readiness_title}
            </div>

            <div class="readiness-text">
                {readiness_text}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )
