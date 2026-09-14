from typing import Any, Dict, List

import streamlit as st


# ============================================================
# CONFIG
# ============================================================

SEVERITY_RANK = {
    "critical": 0,
    "high": 1,
    "medium": 2,
    "low": 3,
}

SEVERITY_META = {
    "critical": {
        "label": "CRITICAL",
        "color": "#b91c1c",
        "bg": "#fee2e2",
        "border": "#fca5a5",
        "impact": "Very High ATS Impact",
    },
    "high": {
        "label": "HIGH",
        "color": "#c2410c",
        "bg": "#ffedd5",
        "border": "#fdba74",
        "impact": "High ATS Impact",
    },
    "medium": {
        "label": "MEDIUM",
        "color": "#a16207",
        "bg": "#fef3c7",
        "border": "#fcd34d",
        "impact": "Medium ATS Impact",
    },
    "low": {
        "label": "LOW",
        "color": "#0369a1",
        "bg": "#e0f2fe",
        "border": "#7dd3fc",
        "impact": "Low ATS Impact",
    },
}


# ============================================================
# HELPERS
# ============================================================

def _clean_items(value: Any) -> List[str]:
    """Clean and deduplicate text items."""

    if not value:
        return []

    result = []
    seen = set()

    for item in value:
        if item is None:
            continue

        text = str(item).strip()

        if not text:
            continue

        key = text.lower()

        if key in seen:
            continue

        seen.add(key)
        result.append(text)

    return result


def _normalize_severity(value: Any) -> str:
    """Normalize backend severity."""

    level = str(value or "medium").strip().lower()

    if level in SEVERITY_META:
        return level

    if level == "minor":
        return "low"

    return "medium"


def _detect_category(
    title: str,
    description: str,
) -> str:
    """Detect the resume area related to an issue."""

    text = (
        f"{title} {description}"
    ).lower()

    categories = {
        "Keywords & Skills": [
            "keyword",
            "skill",
            "technology",
            "technical",
            "tool",
            "stack",
            "job description",
            " jd ",
            "match",
        ],
        "Formatting": [
            "format",
            "font",
            "spacing",
            "layout",
            "margin",
            "heading",
            "bullet",
            "section",
            "template",
        ],
        "Content Quality": [
            "content",
            "achievement",
            "metric",
            "quantif",
            "impact",
            "experience",
            "action verb",
            "description",
        ],
        "ATS Compatibility": [
            "ats",
            "parser",
            "parsing",
            "compatib",
            "readable",
            "file",
            "pdf",
        ],
        "Skill Validation": [
            "validation",
            "project",
            "certification",
            "evidence",
            "proof",
            "demonstrat",
        ],
    }

    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in text:
                return category

    return "General"


def _get_impact(severity: str) -> int:
    """Convert severity to visual impact percentage."""

    return {
        "critical": 100,
        "high": 85,
        "medium": 65,
        "low": 35,
    }.get(severity, 50)


# ============================================================
# ISSUE COLLECTION
# ============================================================

def _collect_issues(
    analysis: Dict[str, Any],
) -> List[Dict[str, Any]]:
    """Collect detailed issues from analysis."""

    issues = []
    seen = set()

    for issue in (
        analysis.get("detailed_feedback") or []
    ):

        if not isinstance(issue, dict):
            continue

        severity = _normalize_severity(
            issue.get("severity_level")
        )

        title = str(
            issue.get("issue_title")
            or "Resume Improvement"
        ).strip()

        description = str(
            issue.get("description")
            or issue.get("issue_description")
            or ""
        ).strip()

        actions = _clean_items(
            issue.get("action_items") or []
        )

        key = (
            title.lower(),
            description.lower(),
            severity,
        )

        if key in seen:
            continue

        seen.add(key)

        issues.append(
            {
                "severity": severity,
                "title": title,
                "description": description,
                "actions": actions,
                "category": _detect_category(
                    title,
                    description,
                ),
                "impact": _get_impact(severity),
            }
        )

    # --------------------------------------------------------
    # If detailed feedback does not exist, use summaries
    # --------------------------------------------------------

    if not issues:

        for item in _clean_items(
            analysis.get("issues_summary") or []
        ):

            issues.append(
                {
                    "severity": "medium",
                    "title": item,
                    "description": "",
                    "actions": [],
                    "category": _detect_category(
                        item,
                        "",
                    ),
                    "impact": 65,
                }
            )

    issues.sort(
        key=lambda x: SEVERITY_RANK.get(
            x["severity"],
            99,
        )
    )

    return issues


# ============================================================
# CSS
# ============================================================

def _apply_styles() -> None:

    st.markdown(
        """
        <style>

        /* ==================================================
           GENERAL
        ================================================== */

        .ri-title {
            font-size: 26px;
            font-weight: 900;
            color: #0f172a;
            margin-top: 20px;
        }

        .ri-subtitle {
            color: #64748b;
            font-size: 13px;
            margin-top: 3px;
            margin-bottom: 22px;
        }


        /* ==================================================
           STRENGTH CARDS
        ================================================== */

        .strength-grid {
            display: grid;
            grid-template-columns:
                repeat(2, minmax(0, 1fr));
            gap: 12px;
            margin: 13px 0 25px 0;
        }

        .strength-card {
            position: relative;
            padding: 16px 18px;
            border-radius: 17px;
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
        }

        .strength-card::before {
            content: "";
            position: absolute;
            left: 0;
            top: 0;
            bottom: 0;
            width: 4px;
            background: #22c55e;
            border-radius: 17px 0 0 17px;
        }

        .strength-card:hover {
            transform:
                translateY(-5px)
                scale(1.01);
            box-shadow:
                0 15px 30px rgba(15,23,42,.10);
        }

        .strength-num {
            display: inline-flex;
            width: 28px;
            height: 28px;
            align-items: center;
            justify-content: center;
            border-radius: 8px;
            background: #dcfce7;
            color: #166534;
            font-size: 10px;
            font-weight: 900;
            margin-right: 9px;
        }

        .strength-text {
            color: #1e293b;
            font-size: 13px;
            font-weight: 650;
            line-height: 1.55;
        }


        /* ==================================================
           ISSUE OVERVIEW
        ================================================== */

        .overview-grid {
            display: grid;
            grid-template-columns:
                repeat(4, minmax(0, 1fr));
            gap: 10px;
            margin: 14px 0 22px 0;
        }

        .overview-card {
            padding: 14px;
            border-radius: 15px;
            background: #ffffff;
            border: 1px solid #e2e8f0;
            box-shadow:
                0 5px 15px rgba(15,23,42,.05);
            transition:
                transform .2s ease,
                box-shadow .2s ease;
        }

        .overview-card:hover {
            transform: translateY(-3px);
            box-shadow:
                0 11px 23px rgba(15,23,42,.09);
        }

        .overview-label {
            font-size: 9px;
            text-transform: uppercase;
            letter-spacing: .08em;
            font-weight: 850;
            color: #64748b;
        }

        .overview-value {
            font-size: 22px;
            font-weight: 900;
            margin-top: 3px;
        }


        /* ==================================================
           FIX FIRST
        ================================================== */

        .fix-section {
            padding: 20px;
            margin: 18px 0 25px 0;
            border-radius: 20px;
            background:
                linear-gradient(
                    135deg,
                    #f8fafc,
                    #eef6ff
                );
            border:
                1px solid rgba(14,165,233,.14);
            box-shadow:
                0 8px 24px rgba(15,23,42,.06);
        }

        .fix-title {
            color: #0f172a;
            font-size: 17px;
            font-weight: 900;
            margin-bottom: 13px;
        }

        .fix-card {
            display: flex;
            gap: 12px;
            align-items: flex-start;
            padding: 12px;
            margin: 8px 0;
            border-radius: 13px;
            background: rgba(255,255,255,.82);
            border: 1px solid rgba(15,23,42,.07);
            transition: transform .2s ease;
        }

        .fix-card:hover {
            transform: translateX(4px);
        }

        .fix-number {
            display: flex;
            min-width: 29px;
            height: 29px;
            align-items: center;
            justify-content: center;
            border-radius: 8px;
            background: #0f172a;
            color: white;
            font-size: 10px;
            font-weight: 900;
        }

        .fix-content {
            flex: 1;
        }

        .fix-heading {
            color: #0f172a;
            font-size: 13px;
            font-weight: 850;
        }

        .fix-meta {
            color: #64748b;
            font-size: 11px;
            margin-top: 3px;
        }


        /* ==================================================
           ISSUE CARD
        ================================================== */

        .issue-card {
            position: relative;
            padding: 18px;
            margin: 11px 0;
            border-radius: 18px;
            background:
                linear-gradient(
                    145deg,
                    #ffffff,
                    #f8fafc
                );
            border: 1px solid #e2e8f0;
            box-shadow:
                0 7px 21px rgba(15,23,42,.06);
            transition:
                transform .24s ease,
                box-shadow .24s ease,
                border-color .24s ease;
            overflow: hidden;
        }

        .issue-card:hover {
            transform:
                translateY(-5px)
                scale(1.008);
            box-shadow:
                0 16px 34px rgba(15,23,42,.11);
            border-color:
                rgba(14,165,233,.25);
        }

        .issue-card::before {
            content: "";
            position: absolute;
            left: 0;
            top: 0;
            bottom: 0;
            width: 4px;
            background: #ef4444;
        }

        .issue-top {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 12px;
        }

        .issue-title {
            color: #0f172a;
            font-size: 15px;
            font-weight: 850;
        }

        .category-pill {
            display: inline-block;
            margin-top: 7px;
            padding: 4px 9px;
            border-radius: 999px;
            background: #eff6ff;
            color: #0369a1;
            font-size: 9px;
            font-weight: 850;
        }

        .severity-pill {
            padding: 6px 10px;
            border-radius: 999px;
            font-size: 9px;
            font-weight: 900;
            letter-spacing: .06em;
            white-space: nowrap;
        }

        .issue-description {
            margin-top: 12px;
            color: #475569;
            font-size: 12px;
            line-height: 1.6;
        }

        .impact-label {
            margin-top: 13px;
            color: #64748b;
            font-size: 10px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: .06em;
        }

        .impact-track {
            height: 6px;
            margin-top: 5px;
            border-radius: 999px;
            background: #e2e8f0;
            overflow: hidden;
        }

        .impact-fill {
            height: 100%;
            border-radius: 999px;
            background:
                linear-gradient(
                    90deg,
                    #06b6d4,
                    #3b82f6
                );
        }


        /* ==================================================
           EMPTY STATE
        ================================================== */

        .empty-state {
            padding: 25px;
            text-align: center;
            border-radius: 18px;
            background:
                linear-gradient(
                    135deg,
                    #f8fafc,
                    #f0fdf4
                );
            border: 1px solid #bbf7d0;
            color: #475569;
        }

        .empty-title {
            color: #166534;
            font-size: 16px;
            font-weight: 850;
            margin-bottom: 5px;
        }

        .empty-text {
            font-size: 12px;
        }


        /* ==================================================
           RESPONSIVE
        ================================================== */

        @media (max-width: 800px) {

            .overview-grid {
                grid-template-columns:
                    repeat(2, minmax(0, 1fr));
            }

        }

        @media (max-width: 600px) {

            .strength-grid {
                grid-template-columns: 1fr;
            }

            .overview-grid {
                grid-template-columns: 1fr;
            }

            .issue-top {
                flex-direction: column;
            }

            .severity-pill {
                align-self: flex-start;
            }

        }

        </style>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# DISPLAY STRENGTHS
# ============================================================

def display_strengths(
    strengths: List[str],
) -> None:

    _apply_styles()

    strengths = _clean_items(strengths)

    st.markdown(
        """
        <div class="ri-title">
            Resume Strengths
        </div>

        <div class="ri-subtitle">
            Strong signals identified in your resume.
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not strengths:

        st.markdown(
            """
            <div class="empty-state">

                <div class="empty-title">
                    Strengths Not Identified Yet
                </div>

                <div class="empty-text">
                    Continue improving your resume to build
                    stronger ATS and recruiter signals.
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        return

    cards = '<div class="strength-grid">'

    for index, item in enumerate(
        strengths,
        start=1,
    ):

        cards += f"""
        <div class="strength-card">

            <span class="strength-num">
                {index:02d}
            </span>

            <span class="strength-text">
                {item}
            </span>

        </div>
        """

    cards += "</div>"

    st.markdown(
        cards,
        unsafe_allow_html=True,
    )


# ============================================================
# DISPLAY CRITICAL ISSUES
# ============================================================

def display_critical_issues(
    analysis: Dict[str, Any],
) -> None:

    _apply_styles()

    critical = _clean_items(
        analysis.get("critical_issues") or []
    )

    issues = _collect_issues(analysis)

    summary = _clean_items(
        analysis.get("issues_summary") or []
    )

    # --------------------------------------------------------
    # If absolutely no issues exist
    # --------------------------------------------------------

    if not critical and not issues and not summary:

        st.success(
            "No Critical Issues Found!"
        )

        st.markdown(
            """
            <div class="empty-state">

                <div class="empty-title">
                    Your Resume Looks Healthy
                </div>

                <div class="empty-text">
                    No urgent ATS issues were identified.
                    Focus on refining your resume further.
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        return

    # ========================================================
    # HEADER
    # ========================================================

    st.markdown(
        """
        <div class="ri-title">
            Resume Insights
        </div>

        <div class="ri-subtitle">
            Identify what needs attention and fix the
            highest-impact problems first.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ========================================================
    # ISSUE DISTRIBUTION
    # ========================================================

    counts = {
        "critical": 0,
        "high": 0,
        "medium": 0,
        "low": 0,
    }

    for issue in issues:

        level = issue["severity"]

        if level in counts:
            counts[level] += 1

    total = sum(counts.values())

    st.markdown(
        f"""
        <div class="overview-grid">

            <div class="overview-card">
                <div class="overview-label">
                    Critical
                </div>
                <div
                    class="overview-value"
                    style="color:#b91c1c;"
                >
                    {counts["critical"]}
                </div>
            </div>

            <div class="overview-card">
                <div class="overview-label">
                    High
                </div>
                <div
                    class="overview-value"
                    style="color:#c2410c;"
                >
                    {counts["high"]}
                </div>
            </div>

            <div class="overview-card">
                <div class="overview-label">
                    Medium
                </div>
                <div
                    class="overview-value"
                    style="color:#a16207;"
                >
                    {counts["medium"]}
                </div>
            </div>

            <div class="overview-card">
                <div class="overview-label">
                    Total Issues
                </div>
                <div class="overview-value">
                    {total}
                </div>
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    # ========================================================
    # FIX FIRST
    # ========================================================

    fix_items = []

    # Critical issues first
    for item in issues:

        if item["severity"] in (
            "critical",
            "high",
        ):
            fix_items.append(item)

    # If fewer than 3, fill with medium
    if len(fix_items) < 3:

        for item in issues:

            if item in fix_items:
                continue

            fix_items.append(item)

            if len(fix_items) >= 3:
                break

    fix_items = fix_items[:3]

    if fix_items:

        fix_html = """
        <div class="fix-section">

            <div class="fix-title">
                Fix First
            </div>
        """

        for index, item in enumerate(
            fix_items,
            start=1,
        ):

            meta = SEVERITY_META[
                item["severity"]
            ]

            fix_html += f"""
            <div class="fix-card">

                <div class="fix-number">
                    {index:02d}
                </div>

                <div class="fix-content">

                    <div class="fix-heading">
                        {item["title"]}
                    </div>

                    <div class="fix-meta">
                        {meta["impact"]}
                        &nbsp;&nbsp;|&nbsp;&nbsp;
                        {item["category"]}
                    </div>

                </div>

            </div>
            """

        fix_html += "</div>"

        st.markdown(
            fix_html,
            unsafe_allow_html=True,
        )

    # ========================================================
    # CRITICAL ISSUES FROM BACKEND
    # ========================================================

    if critical:

        st.markdown(
            """
            <div class="section-header">
                <div class="section-heading">
                    Critical Issues
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        for index, item in enumerate(
            critical,
            start=1,
        ):

            st.markdown(
                f"""
                <div class="issue-card">

                    <div class="issue-top">

                        <div>
                            <div class="issue-title">
                                {index:02d}. {item}
                            </div>

                            <span class="category-pill">
                                HIGH PRIORITY
                            </span>
                        </div>

                        <span
                            class="severity-pill"
                            style="
                                color:#b91c1c;
                                background:#fee2e2;
                                border:1px solid #fca5a5;
                            "
                        >
                            CRITICAL
                        </span>

                    </div>

                    <div class="impact-label">
                        ATS Impact
                    </div>

                    <div class="impact-track">
                        <div
                            class="impact-fill"
                            style="width:100%;"
                        ></div>
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

    # ========================================================
    # DETAILED ISSUES
    # ========================================================

    if issues:

        st.markdown(
            """
            <div class="section-header">
                <div class="section-heading">
                    Detailed Analysis
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        for index, issue in enumerate(
            issues,
            start=1,
        ):

            meta = SEVERITY_META[
                issue["severity"]
            ]

            description_html = ""

            if issue["description"]:

                description_html = f"""
                <div class="issue-description">
                    {issue["description"]}
                </div>
                """

            st.markdown(
                f"""
                <div class="issue-card">

                    <div class="issue-top">

                        <div>

                            <div class="issue-title">
                                {index:02d}. {issue["title"]}
                            </div>

                            <span class="category-pill">
                                {issue["category"]}
                            </span>

                        </div>

                        <span
                            class="severity-pill"
                            style="
                                color:{meta["color"]};
                                background:{meta["bg"]};
                                border:1px solid {meta["border"]};
                            "
                        >
                            {meta["label"]}
                        </span>

                    </div>

                    {description_html}

                    <div class="impact-label">
                        {meta["impact"]}
                    </div>

                    <div class="impact-track">
                        <div
                            class="impact-fill"
                            style="width:{issue["impact"]}%"
                        ></div>
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

            # ------------------------------------------------
            # Recommended actions
            # ------------------------------------------------

            if issue["actions"]:

                with st.expander(
                    "Recommended Actions",
                    expanded=False,
                ):

                    for action in issue["actions"]:

                        st.markdown(
                            f"- {action}"
                        )

    # ========================================================
    # FALLBACK SUMMARY
    # ========================================================

    if not issues and summary:

        st.markdown(
            """
            <div class="section-header">
                <div class="section-heading">
                    Flagged Items
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        for index, item in enumerate(
            summary,
            start=1,
        ):

            st.markdown(
                f"""
                <div class="issue-card">

                    <div class="issue-title">
                        {index:02d}. {item}
                    </div>

                    <span class="category-pill">
                        REVIEW
                    </span>

                </div>
                """,
                unsafe_allow_html=True,
            )
