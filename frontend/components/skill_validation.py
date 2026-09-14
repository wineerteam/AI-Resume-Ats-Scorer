from typing import Any, Dict, List

import streamlit as st


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


def _normalize_similarity(value: Any) -> float:
    """
    Backend may return similarity as:
        0.82
    or:
        82
    """

    similarity = _safe_number(value, 0.0)

    if similarity <= 1:
        similarity *= 100

    return max(
        0.0,
        min(100.0, similarity),
    )


def _get_evidence_level(
    projects: List[str],
    similarity: float,
) -> str:

    if len(projects) >= 2 or similarity >= 80:
        return "STRONG EVIDENCE"

    if len(projects) >= 1 or similarity >= 60:
        return "MODERATE EVIDENCE"

    return "LIMITED EVIDENCE"


def _get_evidence_meta(
    level: str,
) -> Dict[str, str]:

    if level == "STRONG EVIDENCE":
        return {
            "color": "#166534",
            "background": "#dcfce7",
            "border": "#86efac",
        }

    if level == "MODERATE EVIDENCE":
        return {
            "color": "#0369a1",
            "background": "#e0f2fe",
            "border": "#7dd3fc",
        }

    return {
        "color": "#b45309",
        "background": "#fef3c7",
        "border": "#fcd34d",
    }


# ============================================================
# STYLES
# ============================================================

def _apply_styles() -> None:

    st.markdown(
        """
        <style>

        /* =====================================================
           HEADER
        ===================================================== */

        .skill-title {
            color: #0f172a;
            font-size: 28px;
            font-weight: 950;
            letter-spacing: -0.03em;
            margin-top: 22px;
            margin-bottom: 3px;
        }

        .skill-subtitle {
            color: #64748b;
            font-size: 12px;
            line-height: 1.6;
            margin-bottom: 18px;
        }


        /* =====================================================
           TOP DASHBOARD
        ===================================================== */

        .skill-dashboard {
            display: grid;
            grid-template-columns: 230px 1fr;
            gap: 18px;
            align-items: stretch;
        }


        /* =====================================================
           SCORE PANEL
        ===================================================== */

        .score-panel {
            position: relative;
            overflow: hidden;

            min-height: 230px;

            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;

            border-radius: 23px;

            background:
                linear-gradient(
                    145deg,
                    #07152f,
                    #102a56,
                    #075985
                );

            box-shadow:
                0 18px 40px
                rgba(15,23,42,.16);
        }

        .score-panel::before {
            content: "";

            position: absolute;

            width: 180px;
            height: 180px;

            border-radius: 50%;

            border: 1px solid
                rgba(255,255,255,.08);

            top: -95px;
            right: -75px;
        }

        .score-panel::after {
            content: "";

            position: absolute;

            width: 140px;
            height: 140px;

            border-radius: 50%;

            border: 1px solid
                rgba(34,211,238,.08);

            bottom: -80px;
            left: -70px;
        }


        /* =====================================================
           SCORE RING
        ===================================================== */

        .score-ring {
            position: relative;

            width: 142px;
            height: 142px;

            border-radius: 50%;

            display: flex;
            align-items: center;
            justify-content: center;

            background:
                conic-gradient(
                    #22d3ee var(--pct),
                    rgba(255,255,255,.10) 0
                );

            box-shadow:
                0 0 35px
                rgba(34,211,238,.16);
        }

        .score-ring::before {
            content: "";

            position: absolute;

            width: 112px;
            height: 112px;

            border-radius: 50%;

            background: #0a1a36;
        }

        .score-number {
            position: relative;
            z-index: 2;

            color: white;

            font-size: 35px;
            font-weight: 950;

            line-height: 1;
        }

        .score-percent {
            position: absolute;

            z-index: 3;

            color: #94a3b8;

            font-size: 8px;
            font-weight: 850;

            margin-top: 52px;

            letter-spacing: .08em;
        }


        .score-label {
            position: relative;
            z-index: 2;

            color: #67e8f9;

            font-size: 8px;
            font-weight: 900;

            text-transform: uppercase;

            letter-spacing: .11em;

            margin-top: 12px;
        }


        /* =====================================================
           VALIDATION SUMMARY
        ===================================================== */

        .validation-summary {
            padding: 21px;

            border-radius: 23px;

            background:
                linear-gradient(
                    145deg,
                    #ffffff,
                    #f8fafc
                );

            border: 1px solid #e2e8f0;

            box-shadow:
                0 10px 28px
                rgba(15,23,42,.06);
        }

        .summary-eyebrow {
            color: #0369a1;

            font-size: 8px;
            font-weight: 950;

            text-transform: uppercase;
            letter-spacing: .11em;
        }

        .summary-heading {
            color: #0f172a;

            font-size: 20px;
            font-weight: 950;

            margin-top: 5px;
        }

        .summary-text {
            color: #64748b;

            font-size: 11px;

            line-height: 1.65;

            margin-top: 5px;
        }


        /* =====================================================
           STATS
        ===================================================== */

        .stat-grid {
            display: grid;

            grid-template-columns:
                repeat(3, minmax(0, 1fr));

            gap: 10px;

            margin-top: 17px;
        }

        .stat-card {
            padding: 13px;

            border-radius: 15px;

            background: #f8fafc;

            border: 1px solid #e2e8f0;
        }

        .stat-value {
            color: #0f172a;

            font-size: 22px;
            font-weight: 950;
        }

        .stat-label {
            color: #64748b;

            font-size: 8px;
            font-weight: 800;

            margin-top: 2px;
        }


        /* =====================================================
           VALIDATION BAR
        ===================================================== */

        .validation-bar-label {
            display: flex;

            justify-content: space-between;

            margin-top: 16px;

            color: #334155;

            font-size: 9px;
            font-weight: 850;
        }

        .validation-track {
            height: 9px;

            border-radius: 999px;

            background: #e2e8f0;

            overflow: hidden;

            margin-top: 6px;
        }

        .validation-fill {
            height: 100%;

            border-radius: 999px;

            background:
                linear-gradient(
                    90deg,
                    #06b6d4,
                    #3b82f6
                );
        }


        /* =====================================================
           INSIGHT
        ===================================================== */

        .validation-insight {
            margin-top: 15px;

            padding: 12px 14px;

            border-radius: 14px;

            background:
                linear-gradient(
                    135deg,
                    #eff6ff,
                    #ecfeff
                );

            border: 1px solid #bae6fd;
        }

        .validation-insight-title {
            color: #0369a1;

            font-size: 8px;
            font-weight: 950;

            text-transform: uppercase;

            letter-spacing: .09em;
        }

        .validation-insight-text {
            color: #475569;

            font-size: 10px;

            line-height: 1.55;

            margin-top: 3px;
        }


        /* =====================================================
           SECTION
        ===================================================== */

        .section-title {
            color: #0f172a;

            font-size: 21px;
            font-weight: 950;

            margin-top: 27px;
            margin-bottom: 3px;
        }

        .section-subtitle {
            color: #64748b;

            font-size: 11px;

            margin-bottom: 13px;
        }


        /* =====================================================
           SKILL CARDS
        ===================================================== */

        .skill-grid {
            display: grid;

            grid-template-columns:
                repeat(2, minmax(0, 1fr));

            gap: 13px;
        }

        .skill-card {
            position: relative;
            overflow: hidden;

            padding: 17px;

            border-radius: 19px;

            background: white;

            border: 1px solid #e2e8f0;

            box-shadow:
                0 7px 21px
                rgba(15,23,42,.055);

            transition:
                transform .22s ease,
                box-shadow .22s ease,
                border-color .22s ease;
        }

        .skill-card:hover {
            transform:
                translateY(-5px)
                scale(1.01);

            box-shadow:
                0 17px 34px
                rgba(15,23,42,.10);

            border-color: #93c5fd;
        }

        .skill-card::before {
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

        .skill-top {
            display: flex;

            justify-content: space-between;

            align-items: flex-start;

            gap: 10px;
        }

        .skill-name {
            color: #0f172a;

            font-size: 14px;
            font-weight: 900;
        }

        .evidence-badge {
            padding: 5px 8px;

            border-radius: 999px;

            font-size: 7px;
            font-weight: 950;

            white-space: nowrap;
        }


        /* =====================================================
           SIMILARITY
        ===================================================== */

        .similarity-row {
            display: flex;

            align-items: baseline;

            gap: 5px;

            margin-top: 13px;
        }

        .similarity-number {
            color: #0369a1;

            font-size: 24px;
            font-weight: 950;
        }

        .similarity-label {
            color: #94a3b8;

            font-size: 9px;
            font-weight: 800;
        }

        .mini-track {
            height: 6px;

            border-radius: 999px;

            background: #e2e8f0;

            overflow: hidden;

            margin-top: 6px;
        }

        .mini-fill {
            height: 100%;

            border-radius: 999px;

            background:
                linear-gradient(
                    90deg,
                    #14b8a6,
                    #06b6d4
                );
        }


        /* =====================================================
           PROJECT EVIDENCE
        ===================================================== */

        .evidence-label {
            color: #64748b;

            font-size: 8px;
            font-weight: 850;

            text-transform: uppercase;

            letter-spacing: .07em;

            margin-top: 12px;
        }

        .project-list {
            color: #334155;

            font-size: 10px;

            line-height: 1.6;

            margin-top: 3px;
        }


        /* =====================================================
           UNVALIDATED
        ===================================================== */

        .unvalidated-card {
            position: relative;

            padding: 15px 17px;

            border-radius: 17px;

            background:
                linear-gradient(
                    135deg,
                    #fff7ed,
                    #fff1f2
                );

            border: 1px solid #fed7aa;

            box-shadow:
                0 7px 20px
                rgba(15,23,42,.045);

            transition:
                transform .2s ease,
                box-shadow .2s ease;
        }

        .unvalidated-card:hover {
            transform: translateY(-4px);

            box-shadow:
                0 14px 28px
                rgba(15,23,42,.08);
        }

        .unvalidated-name {
            color: #7c2d12;

            font-size: 13px;
            font-weight: 900;
        }

        .unvalidated-text {
            color: #78716c;

            font-size: 9px;

            line-height: 1.5;

            margin-top: 3px;
        }


        /* =====================================================
           RECOMMENDATION
        ===================================================== */

        .recommendation-card {
            margin-top: 20px;

            padding: 18px;

            border-radius: 20px;

            background:
                linear-gradient(
                    135deg,
                    #07152f,
                    #102a56
                );

            box-shadow:
                0 12px 30px
                rgba(15,23,42,.12);
        }

        .recommendation-label {
            color: #67e8f9;

            font-size: 8px;
            font-weight: 950;

            text-transform: uppercase;

            letter-spacing: .10em;
        }

        .recommendation-title {
            color: white;

            font-size: 16px;
            font-weight: 900;

            margin-top: 4px;
        }

        .recommendation-text {
            color: #cbd5e1;

            font-size: 10px;

            line-height: 1.65;

            margin-top: 4px;
        }


        /* =====================================================
           RESPONSIVE
        ===================================================== */

        @media (max-width: 800px) {

            .skill-dashboard {
                grid-template-columns: 1fr;
            }

            .skill-grid {
                grid-template-columns: 1fr;
            }

        }

        @media (max-width: 550px) {

            .stat-grid {
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

    details = (
        analysis.get(
            "skill_validation_details"
        ) or {}
    )

    validated = (
        details.get("validated")
        or []
    )

    unvalidated = (
        details.get("unvalidated")
        or []
    )

    total = _safe_number(
        details.get(
            "total",
            len(validated) + len(unvalidated),
        )
    )

    pct = _safe_number(
        details.get(
            "validation_pct",
            0,
        )
    )

    pct = max(
        0.0,
        min(100.0, pct),
    )

    # ========================================================
    # HEADER
    # ========================================================

    st.html(
        """
        <div class="skill-title">
            Skill Validation
        </div>

        <div class="skill-subtitle">
            Measure how strongly your listed skills are
            supported by projects and experience evidence.
        </div>
        """
    )

    # ========================================================
    # SUMMARY TEXT
    # ========================================================

    validated_count = len(validated)
    unvalidated_count = len(unvalidated)

    if pct >= 80:

        summary_heading = (
            "Strong Skill Evidence"
        )

        summary_text = (
            "Most of your listed skills are supported by "
            "projects or experience evidence."
        )

    elif pct >= 60:

        summary_heading = (
            "Good Skill Coverage"
        )

        summary_text = (
            "A solid portion of your skills have supporting "
            "evidence, but some skills could be demonstrated "
            "more clearly."
        )

    elif pct > 0:

        summary_heading = (
            "Evidence Coverage Needs Improvement"
        )

        summary_text = (
            "Several listed skills need stronger connections "
            "to projects or experience evidence."
        )

    else:

        summary_heading = (
            "Limited Skill Evidence"
        )

        summary_text = (
            "The analysis found limited evidence connecting "
            "your listed skills to projects or experience."
        )

    # ========================================================
    # TOP DASHBOARD
    # ========================================================

    st.html(
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

                <div class="score-label">
                    Skill Validation Score
                </div>

            </div>


            <div class="validation-summary">

                <div class="summary-eyebrow">
                    Evidence Analysis
                </div>

                <div class="summary-heading">
                    {summary_heading}
                </div>

                <div class="summary-text">
                    {summary_text}
                </div>


                <div class="stat-grid">

                    <div class="stat-card">

                        <div class="stat-value">
                            {int(total)}
                        </div>

                        <div class="stat-label">
                            TOTAL SKILLS
                        </div>

                    </div>


                    <div class="stat-card">

                        <div class="stat-value">
                            {validated_count}
                        </div>

                        <div class="stat-label">
                            VALIDATED
                        </div>

                    </div>


                    <div class="stat-card">

                        <div class="stat-value">
                            {unvalidated_count}
                        </div>

                        <div class="stat-label">
                            NEED EVIDENCE
                        </div>

                    </div>

                </div>


                <div class="validation-bar-label">

                    <span>
                        Evidence Coverage
                    </span>

                    <span>
                        {pct:.0f}%
                    </span>

                </div>

                <div class="validation-track">

                    <div
                        class="validation-fill"
                        style="width:{pct:.0f}%"
                    ></div>

                </div>

            </div>

        </div>
        """
    )

    # ========================================================
    # INSIGHT
    # ========================================================

    if pct >= 80:

        insight = (
            "Your skills are well supported by evidence. "
            "Maintain this connection between skills and "
            "real project or experience outcomes."
        )

    elif pct >= 60:

        insight = (
            "Your evidence coverage is reasonably strong. "
            "Adding proof for the remaining skills can "
            "make your profile more credible."
        )

    elif total > 0:

        insight = (
            "Try connecting listed skills to specific "
            "projects, experience bullets, or measurable "
            "outcomes wherever the skill was actually used."
        )

    else:

        insight = (
            "No sufficient skill evidence was detected. "
            "Review your resume's skills, projects, and "
            "experience sections."
        )

    st.html(
        f"""
        <div class="validation-insight">

            <div class="validation-insight-title">
                Validation Insight
            </div>

            <div class="validation-insight-text">
                {insight}
            </div>

        </div>
        """
    )

    # ========================================================
    # VALIDATED SKILLS
    # ========================================================

    if validated:

        st.html(
            """
            <div class="section-title">
                Validated Skills
            </div>

            <div class="section-subtitle">
                Skills supported by evidence found in your
                projects or experience.
            </div>
            """
        )

        cards_html = """
        <div class="skill-grid">
        """

        for entry in validated:

            if not isinstance(entry, dict):
                continue

            skill = _clean_text(
                entry.get(
                    "skill",
                    "Unnamed Skill",
                )
            )

            projects = _clean_projects(
                entry.get(
                    "projects",
                    [],
                )
            )

            similarity = _normalize_similarity(
                entry.get(
                    "similarity",
                    0,
                )
            )

            evidence_level = _get_evidence_level(
                projects,
                similarity,
            )

            meta = _get_evidence_meta(
                evidence_level
            )

            if projects:

                project_text = ", ".join(
                    projects[:3]
                )

                if len(projects) > 3:
                    project_text += (
                        f" + {len(projects) - 3} more"
                    )

            else:

                project_text = (
                    "Experience evidence detected"
                )

            cards_html += f"""
            <div class="skill-card">

                <div class="skill-top">

                    <div class="skill-name">
                        {skill}
                    </div>

                    <div
                        class="evidence-badge"
                        style="
                            color:{meta["color"]};
                            background:{meta["background"]};
                            border:1px solid
                                {meta["border"]};
                        "
                    >
                        {evidence_level}
                    </div>

                </div>


                <div class="similarity-row">

                    <div class="similarity-number">
                        {similarity:.0f}%
                    </div>

                    <div class="similarity-label">
                        EVIDENCE MATCH
                    </div>

                </div>


                <div class="mini-track">

                    <div
                        class="mini-fill"
                        style="
                            width:{similarity:.0f}%;
                        "
                    ></div>

                </div>


                <div class="evidence-label">
                    Demonstrated In
                </div>

                <div class="project-list">
                    {project_text}
                </div>

            </div>
            """

        cards_html += """
        </div>
        """

        st.html(cards_html)

    # ========================================================
    # UNVALIDATED SKILLS
    # ========================================================

    if unvalidated:

        st.html(
            """
            <div class="section-title">
                Skills Needing Evidence
            </div>

            <div class="section-subtitle">
                These skills are listed but were not clearly
                connected to project or experience evidence.
            </div>
            """
        )

        cards_html = """
        <div class="skill-grid">
        """

        for skill in unvalidated:

            skill_text = _clean_text(
                skill
            )

            if not skill_text:
                continue

            cards_html += f"""
            <div class="unvalidated-card">

                <div class="unvalidated-name">
                    {skill_text}
                </div>

                <div class="unvalidated-text">
                    Consider demonstrating this skill through
                    a relevant project, experience bullet,
                    achievement, or measurable result.
                </div>

            </div>
            """

        cards_html += """
        </div>
        """

        st.html(cards_html)

    # ========================================================
    # NO SKILLS
    # ========================================================

    if total == 0:

        st.html(
            """
            <div class="recommendation-card">

                <div class="recommendation-label">
                    Skill Analysis
                </div>

                <div class="recommendation-title">
                    No Skills Detected
                </div>

                <div class="recommendation-text">
                    No skills were available for validation.
                    Review the Skills, Projects, and Experience
                    sections of your resume.
                </div>

            </div>
            """
        )

        return

    # ========================================================
    # FINAL RECOMMENDATION
    # ========================================================

    if unvalidated_count > 0:

        recommendation_title = (
            "Strengthen Your Skill Evidence"
        )

        recommendation_text = (
            f"{unvalidated_count} listed skill"
            f"{'s' if unvalidated_count != 1 else ''} "
            "could use stronger evidence. Connect them to "
            "relevant projects or experience where the skill "
            "was genuinely used."
        )

    else:

        recommendation_title = (
            "Excellent Skill Evidence Coverage"
        )

        recommendation_text = (
            "Your listed skills have supporting evidence. "
            "Keep the skill-to-project connection clear and "
            "specific throughout your resume."
        )

    st.html(
        f"""
        <div class="recommendation-card">

            <div class="recommendation-label">
                Recommended Next Step
            </div>

            <div class="recommendation-title">
                {recommendation_title}
            </div>

            <div class="recommendation-text">
                {recommendation_text}
            </div>

        </div>
        """
    )
