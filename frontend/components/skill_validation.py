from typing import Any, Dict, List

import streamlit as st


# ============================================================
# CONFIG
# ============================================================

VALIDATION_LEVELS = {
    "excellent": {
        "min": 85,
        "label": "Excellent",
        "color": "#166534",
        "bg": "#dcfce7",
        "border": "#86efac",
    },
    "strong": {
        "min": 70,
        "label": "Strong",
        "color": "#0369a1",
        "bg": "#e0f2fe",
        "border": "#7dd3fc",
    },
    "moderate": {
        "min": 50,
        "label": "Moderate",
        "color": "#a16207",
        "bg": "#fef3c7",
        "border": "#fcd34d",
    },
    "weak": {
        "min": 0,
        "label": "Needs Improvement",
        "color": "#b91c1c",
        "bg": "#fee2e2",
        "border": "#fca5a5",
    },
}


# ============================================================
# HELPERS
# ============================================================

def _safe_number(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _clean_text(value: Any) -> str:
    if value is None:
        return ""

    return str(value).strip()


def _clean_projects(value: Any) -> List[str]:
    if not isinstance(value, list):
        return []

    projects = []

    for item in value:
        text = _clean_text(item)

        if text and text not in projects:
            projects.append(text)

    return projects


def _get_validation_level(pct: float) -> Dict[str, str]:
    if pct >= 85:
        return VALIDATION_LEVELS["excellent"]

    if pct >= 70:
        return VALIDATION_LEVELS["strong"]

    if pct >= 50:
        return VALIDATION_LEVELS["moderate"]

    return VALIDATION_LEVELS["weak"]


def _normalize_similarity(value: Any) -> float:
    if not isinstance(value, (int, float)):
        return 0.0

    value = float(value)

    if value <= 1:
        value *= 100

    return max(0.0, min(100.0, value))


def _get_evidence_level(similarity: Any) -> str:
    value = _normalize_similarity(similarity)

    if value >= 85:
        return "Strong Evidence"

    if value >= 65:
        return "Good Evidence"

    if value > 0:
        return "Limited Evidence"

    return "Resume Evidence"


def _get_evidence_color(similarity: Any) -> str:
    value = _normalize_similarity(similarity)

    if value >= 85:
        return "#166534"

    if value >= 65:
        return "#0369a1"

    if value > 0:
        return "#a16207"

    return "#64748b"


# ============================================================
# CSS
# ============================================================

def _apply_styles() -> None:

    st.markdown(
        """
        <style>

        /* ==================================================
           HEADER
        ================================================== */

        .skill-v5-title {
            font-size: 28px;
            font-weight: 900;
            color: #0f172a;
            letter-spacing: -0.02em;
            margin-top: 18px;
        }

        .skill-v5-subtitle {
            color: #64748b;
            font-size: 13px;
            line-height: 1.6;
            margin-top: 4px;
            margin-bottom: 20px;
        }


        /* ==================================================
           TOP DASHBOARD
        ================================================== */

        .skill-dashboard {
            display: grid;
            grid-template-columns: 0.95fr 1.5fr;
            gap: 15px;
            margin-bottom: 18px;
        }


        /* ==================================================
           SCORE RING
        ================================================== */

        .score-panel {
            min-height: 230px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            border-radius: 22px;
            background:
                linear-gradient(
                    145deg,
                    #0f172a,
                    #172554
                );
            box-shadow:
                0 14px 35px rgba(15,23,42,.18);
            position: relative;
            overflow: hidden;
        }

        .score-panel::before {
            content: "";
            position: absolute;
            width: 180px;
            height: 180px;
            border-radius: 50%;
            border: 1px solid rgba(255,255,255,.08);
            top: -70px;
            right: -50px;
        }

        .score-panel::after {
            content: "";
            position: absolute;
            width: 130px;
            height: 130px;
            border-radius: 50%;
            border: 1px solid rgba(34,211,238,.12);
            bottom: -65px;
            left: -35px;
        }

        .score-ring {
            width: 130px;
            height: 130px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            background:
                conic-gradient(
                    #22d3ee var(--pct),
                    rgba(255,255,255,.10) 0
                );
            box-shadow:
                0 0 35px rgba(34,211,238,.16);
        }

        .score-ring::before {
            content: "";
            position: absolute;
            width: 103px;
            height: 103px;
            border-radius: 50%;
            background: #0f172a;
        }

        .score-number {
            position: relative;
            z-index: 2;
            color: white;
            font-size: 30px;
            font-weight: 950;
        }

        .score-percent {
            position: absolute;
            margin-top: 48px;
            color: #94a3b8;
            font-size: 9px;
            z-index: 3;
        }

        .score-status {
            margin-top: 11px;
            color: #67e8f9;
            font-size: 13px;
            font-weight: 850;
            position: relative;
            z-index: 2;
        }

        .score-caption {
            color: #94a3b8;
            font-size: 10px;
            margin-top: 3px;
            position: relative;
            z-index: 2;
        }


        /* ==================================================
           SUMMARY PANEL
        ================================================== */

        .summary-panel {
            padding: 18px;
            border-radius: 22px;
            background:
                linear-gradient(
                    145deg,
                    #ffffff,
                    #f8fafc
                );
            border: 1px solid #e2e8f0;
            box-shadow:
                0 10px 28px rgba(15,23,42,.07);
        }

        .summary-heading {
            font-size: 16px;
            font-weight: 900;
            color: #0f172a;
            margin-bottom: 12px;
        }

        .summary-grid {
            display: grid;
            grid-template-columns:
                repeat(2, minmax(0, 1fr));
            gap: 10px;
        }

        .summary-item {
            padding: 13px;
            border-radius: 15px;
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            transition:
                transform .2s ease,
                box-shadow .2s ease;
        }

        .summary-item:hover {
            transform: translateY(-4px);
            box-shadow:
                0 9px 20px rgba(15,23,42,.08);
        }

        .summary-label {
            color: #64748b;
            font-size: 9px;
            text-transform: uppercase;
            letter-spacing: .07em;
            font-weight: 850;
        }

        .summary-value {
            color: #0f172a;
            font-size: 23px;
            font-weight: 900;
            margin-top: 3px;
        }

        .summary-small {
            color: #64748b;
            font-size: 9px;
            margin-top: 2px;
        }


        /* ==================================================
           INSIGHT
        ================================================== */

        .validation-insight {
            padding: 15px 17px;
            border-radius: 17px;
            margin: 15px 0 23px 0;
            background:
                linear-gradient(
                    135deg,
                    #eff6ff,
                    #ecfeff
                );
            border: 1px solid #bae6fd;
            box-shadow:
                0 6px 18px rgba(15,23,42,.05);
        }

        .insight-title {
            color: #075985;
            font-size: 13px;
            font-weight: 900;
        }

        .insight-text {
            color: #475569;
            font-size: 11px;
            line-height: 1.65;
            margin-top: 4px;
        }


        /* ==================================================
           SECTION
        ================================================== */

        .skill-section-title {
            font-size: 18px;
            color: #0f172a;
            font-weight: 900;
            margin-top: 20px;
        }

        .skill-section-subtitle {
            color: #64748b;
            font-size: 11px;
            margin-top: 3px;
            margin-bottom: 12px;
        }


        /* ==================================================
           VALIDATED SKILL GRID
        ================================================== */

        .validated-grid-v5 {
            display: grid;
            grid-template-columns:
                repeat(2, minmax(0, 1fr));
            gap: 12px;
            margin-bottom: 15px;
        }

        .validated-skill {
            position: relative;
            padding: 17px;
            border-radius: 18px;
            background:
                linear-gradient(
                    145deg,
                    #ffffff,
                    #f0fdf4
                );
            border: 1px solid #bbf7d0;
            box-shadow:
                0 7px 20px rgba(15,23,42,.055);
            transition:
                transform .23s ease,
                box-shadow .23s ease;
            overflow: hidden;
        }

        .validated-skill::before {
            content: "";
            position: absolute;
            left: 0;
            top: 0;
            bottom: 0;
            width: 4px;
            background: #22c55e;
        }

        .validated-skill:hover {
            transform:
                translateY(-5px)
                scale(1.01);
            box-shadow:
                0 16px 32px rgba(15,23,42,.11);
        }

        .validated-top {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 10px;
        }

        .validated-name {
            font-size: 15px;
            font-weight: 900;
            color: #0f172a;
        }

        .evidence-badge {
            padding: 5px 8px;
            border-radius: 999px;
            font-size: 8px;
            font-weight: 900;
            white-space: nowrap;
        }

        .similarity-text {
            color: #475569;
            font-size: 10px;
            margin-top: 8px;
            font-weight: 750;
        }

        .mini-track {
            height: 6px;
            background: #dcfce7;
            border-radius: 999px;
            margin-top: 6px;
            overflow: hidden;
        }

        .mini-fill {
            height: 100%;
            border-radius: 999px;
            background:
                linear-gradient(
                    90deg,
                    #22c55e,
                    #06b6d4
                );
        }

        .evidence-row {
            margin-top: 10px;
            color: #64748b;
            font-size: 10px;
            line-height: 1.5;
        }

        .evidence-label {
            color: #475569;
            font-weight: 800;
        }


        /* ==================================================
           UNVALIDATED
        ================================================== */

        .unvalidated-grid-v5 {
            display: grid;
            grid-template-columns:
                repeat(3, minmax(0, 1fr));
            gap: 10px;
            margin-top: 10px;
        }

        .unvalidated-skill {
            padding: 14px;
            border-radius: 16px;
            background:
                linear-gradient(
                    145deg,
                    #ffffff,
                    #fff7ed
                );
            border: 1px solid #fed7aa;
            box-shadow:
                0 6px 17px rgba(15,23,42,.05);
            transition:
                transform .2s ease,
                box-shadow .2s ease;
        }

        .unvalidated-skill:hover {
            transform:
                translateY(-4px);
            box-shadow:
                0 12px 25px rgba(15,23,42,.09);
        }

        .unvalidated-name-v5 {
            color: #9a3412;
            font-size: 12px;
            font-weight: 850;
        }

        .unvalidated-note-v5 {
            color: #78716c;
            font-size: 9px;
            line-height: 1.5;
            margin-top: 5px;
        }


        /* ==================================================
           PROJECT COVERAGE
        ================================================== */

        .project-grid {
            display: grid;
            grid-template-columns:
                repeat(3, minmax(0, 1fr));
            gap: 10px;
            margin-top: 10px;
        }

        .project-card {
            padding: 13px;
            border-radius: 15px;
            background: #ffffff;
            border: 1px solid #e2e8f0;
            box-shadow:
                0 5px 15px rgba(15,23,42,.045);
        }

        .project-name {
            color: #0f172a;
            font-size: 11px;
            font-weight: 850;
        }

        .project-count {
            color: #0369a1;
            font-size: 20px;
            font-weight: 900;
            margin-top: 3px;
        }

        .project-label {
            color: #64748b;
            font-size: 9px;
        }


        /* ==================================================
           EMPTY
        ================================================== */

        .skill-empty {
            padding: 25px;
            text-align: center;
            border-radius: 20px;
            background:
                linear-gradient(
                    135deg,
                    #f8fafc,
                    #eef6ff
                );
            border: 1px solid #bae6fd;
        }

        .skill-empty-title {
            color: #075985;
            font-size: 16px;
            font-weight: 900;
        }

        .skill-empty-text {
            color: #64748b;
            font-size: 11px;
            margin-top: 5px;
        }


        /* ==================================================
           RESPONSIVE
        ================================================== */

        @media (max-width: 850px) {

            .skill-dashboard {
                grid-template-columns: 1fr;
            }

            .unvalidated-grid-v5,
            .project-grid {
                grid-template-columns:
                    repeat(2, minmax(0, 1fr));
            }

        }

        @media (max-width: 650px) {

            .validated-grid-v5,
            .unvalidated-grid-v5,
            .project-grid {
                grid-template-columns: 1fr;
            }

            .summary-grid {
                grid-template-columns: 1fr;
            }

        }

        </style>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# MAIN FUNCTION
# ============================================================

def display_skill_validation(
    analysis: Dict[str, Any],
) -> None:

    _apply_styles()

    # --------------------------------------------------------
    # BACKEND DATA
    # --------------------------------------------------------

    details = (
        analysis.get(
            "skill_validation_details"
        ) or {}
    )

    validated = (
        details.get("validated") or []
    )

    unvalidated = (
        details.get("unvalidated") or []
    )

    total = details.get(
        "total",
        len(validated) + len(unvalidated),
    )

    total = int(
        _safe_number(total)
    )

    pct = _safe_number(
        details.get(
            "validation_pct",
            0.0,
        )
    )

    pct = max(
        0.0,
        min(100.0, pct),
    )

    validated_count = len(validated)
    unvalidated_count = len(unvalidated)

    # ========================================================
    # HEADER
    # ========================================================

    st.markdown(
        """
        <div class="skill-v5-title">
            Skill Validation
        </div>

        <div class="skill-v5-subtitle">
            Measure how strongly your listed skills are
            supported by projects and experience evidence.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ========================================================
    # EMPTY STATE
    # ========================================================

    if total == 0:

        st.markdown(
            """
            <div class="skill-empty">

                <div class="skill-empty-title">
                    No Skills Detected
                </div>

                <div class="skill-empty-text">
                    Add relevant technical and professional
                    skills to your resume for validation.
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        return

    status = _get_validation_level(pct)

    # ========================================================
    # TOP DASHBOARD
    # ========================================================

    st.markdown(
        f"""
        <div class="skill-dashboard">

            <div class="score-panel">

                <div
                    class="score-ring"
                    style="--pct:{pct:.1f}%"
                >

                    <div class="score-number">
                        {pct:.0f}
                    </div>

                    <div class="score-percent">
                        PERCENT
                    </div>

                </div>

                <div class="score-status">
                    {status["label"]} Validation
                </div>

                <div class="score-caption">
                    Skill evidence coverage
                </div>

            </div>


            <div class="summary-panel">

                <div class="summary-heading">
                    Validation Overview
                </div>

                <div class="summary-grid">

                    <div class="summary-item">

                        <div class="summary-label">
                            Total Skills
                        </div>

                        <div class="summary-value">
                            {total}
                        </div>

                        <div class="summary-small">
                            Skills detected
                        </div>

                    </div>


                    <div class="summary-item">

                        <div class="summary-label">
                            Validated
                        </div>

                        <div
                            class="summary-value"
                            style="color:#166534;"
                        >
                            {validated_count}
                        </div>

                        <div class="summary-small">
                            Evidence found
                        </div>

                    </div>


                    <div class="summary-item">

                        <div class="summary-label">
                            Need Evidence
                        </div>

                        <div
                            class="summary-value"
                            style="color:#c2410c;"
                        >
                            {unvalidated_count}
                        </div>

                        <div class="summary-small">
                            Skills to strengthen
                        </div>

                    </div>


                    <div class="summary-item">

                        <div class="summary-label">
                            Validation Rate
                        </div>

                        <div
                            class="summary-value"
                            style="color:{status["color"]};"
                        >
                            {pct:.0f}%
                        </div>

                        <div class="summary-small">
                            Overall coverage
                        </div>

                    </div>

                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    # ========================================================
    # INSIGHT
    # ========================================================

    if unvalidated_count == 0:

        insight_title = (
            "Strong Skill-to-Evidence Alignment"
        )

        insight_text = (
            "All detected skills have supporting evidence "
            "in the available resume data. This makes your "
            "skill section more credible to recruiters."
        )

    elif pct >= 70:

        insight_title = (
            "Good Validation with Room to Improve"
        )

        insight_text = (
            f"{validated_count} of {total} detected skills "
            "have supporting evidence. Strengthen the "
            "remaining skills with relevant projects or "
            "experience bullets where applicable."
        )

    else:

        insight_title = (
            "Your Biggest Opportunity: Add Evidence"
        )

        insight_text = (
            f"{unvalidated_count} of {total} skills lack "
            "clear supporting evidence. Connect these skills "
            "to projects, experience, achievements, or "
            "measurable work where applicable."
        )

    st.markdown(
        f"""
        <div class="validation-insight">

            <div class="insight-title">
                {insight_title}
            </div>

            <div class="insight-text">
                {insight_text}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    # ========================================================
    # VALIDATED SKILLS
    # ========================================================

    if validated:

        st.markdown(
            """
            <div class="skill-section-title">
                Validated Skills
            </div>

            <div class="skill-section-subtitle">
                Skills supported by project or experience evidence.
            </div>
            """,
            unsafe_allow_html=True,
        )

        cards = '<div class="validated-grid-v5">'

        project_skill_counts: Dict[str, int] = {}

        for entry in validated:

            if not isinstance(entry, dict):
                continue

            skill = _clean_text(
                entry.get(
                    "skill",
                    "Unknown Skill",
                )
            )

            if not skill:
                skill = "Unknown Skill"

            projects = _clean_projects(
                entry.get("projects")
            )

            similarity = _normalize_similarity(
                entry.get("similarity")
            )

            evidence_level = _get_evidence_level(
                entry.get("similarity")
            )

            evidence_color = _get_evidence_color(
                entry.get("similarity")
            )

            # ----------------------------------------------
            # Project coverage
            # ----------------------------------------------

            for project in projects:

                project_skill_counts[project] = (
                    project_skill_counts.get(
                        project,
                        0,
                    ) + 1
                )

            # ----------------------------------------------
            # Evidence text
            # ----------------------------------------------

            if projects:

                project_text = ", ".join(
                    projects[:3]
                )

                if len(projects) > 3:

                    project_text += (
                        f" +{len(projects) - 3} more"
                    )

            else:

                project_text = (
                    "Experience section"
                )

            cards += f"""
            <div class="validated-skill">

                <div class="validated-top">

                    <div class="validated-name">
                        {skill}
                    </div>

                    <div
                        class="evidence-badge"
                        style="
                            color:{evidence_color};
                            background:#ffffff;
                            border:1px solid
                                rgba(15,23,42,.08);
                        "
                    >
                        {evidence_level}
                    </div>

                </div>


                <div class="similarity-text">
                    Evidence Match
                    &nbsp;&nbsp;
                    {similarity:.0f}%
                </div>


                <div class="mini-track">

                    <div
                        class="mini-fill"
                        style="
                            width:{similarity:.0f}%;
                        "
                    ></div>

                </div>


                <div class="evidence-row">

                    <span class="evidence-label">
                        Demonstrated in:
                    </span>

                    {project_text}

                </div>

            </div>
            """

        cards += "</div>"

        st.markdown(
            cards,
            unsafe_allow_html=True,
        )

        # ====================================================
        # PROJECT COVERAGE
        # ====================================================

        # Rebuild project map safely
        project_skill_counts = {}

        for entry in validated:

            if not isinstance(entry, dict):
                continue

            projects = _clean_projects(
                entry.get("projects")
            )

            for project in projects:

                project_skill_counts[project] = (
                    project_skill_counts.get(
                        project,
                        0,
                    ) + 1
                )

        if project_skill_counts:

            st.markdown(
                """
                <div class="skill-section-title">
                    Project Coverage
                </div>

                <div class="skill-section-subtitle">
                    How many validated skills are demonstrated
                    by each project.
                </div>
                """,
                unsafe_allow_html=True,
            )

            sorted_projects = sorted(
                project_skill_counts.items(),
                key=lambda x: x[1],
                reverse=True,
            )

            project_html = '<div class="project-grid">'

            for project, count in sorted_projects[:6]:

                project_html += f"""
                <div class="project-card">

                    <div class="project-name">
                        {project}
                    </div>

                    <div class="project-count">
                        {count}
                    </div>

                    <div class="project-label">
                        validated skills demonstrated
                    </div>

                </div>
                """

            project_html += "</div>"

            st.markdown(
                project_html,
                unsafe_allow_html=True,
            )

    # ========================================================
    # UNVALIDATED SKILLS
    # ========================================================

    if unvalidated:

        st.markdown(
            """
            <div class="skill-section-title">
                Skills Needing Evidence
            </div>

            <div class="skill-section-subtitle">
                These skills are listed but are not clearly
                connected to supporting resume evidence.
            </div>
            """,
            unsafe_allow_html=True,
        )

        cards = '<div class="unvalidated-grid-v5">'

        for skill in unvalidated:

            skill_text = _clean_text(skill)

            if not skill_text:
                continue

            cards += f"""
            <div class="unvalidated-skill">

                <div class="unvalidated-name-v5">
                    {skill_text}
                </div>

                <div class="unvalidated-note-v5">
                    Connect this skill to a relevant project,
                    experience bullet, achievement, or
                    measurable outcome where applicable.
                </div>

            </div>
            """

        cards += "</div>"

        st.markdown(
            cards,
            unsafe_allow_html=True,
        )

    # ========================================================
    # FINAL RECOMMENDATION
    # ========================================================

    if unvalidated_count > 0:

        st.markdown(
            """
            <div class="validation-insight">

                <div class="insight-title">
                    Recommended Next Step
                </div>

                <div class="insight-text">
                    Review the skills needing evidence and
                    strengthen the most relevant ones first.
                    Evidence should come from genuine projects,
                    experience, achievements, or work you can
                    actually discuss in an interview.
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )
