from typing import Any, Dict, List, Tuple

import streamlit as st


# ============================================================
# CONFIGURATION
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
        "background": "#fee2e2",
        "border": "#fca5a5",
        "impact": "Very High Impact",
    },
    "high": {
        "label": "HIGH",
        "color": "#c2410c",
        "background": "#ffedd5",
        "border": "#fdba74",
        "impact": "High Impact",
    },
    "medium": {
        "label": "MEDIUM",
        "color": "#a16207",
        "background": "#fef3c7",
        "border": "#fcd34d",
        "impact": "Medium Impact",
    },
    "low": {
        "label": "LOW",
        "color": "#0369a1",
        "background": "#e0f2fe",
        "border": "#7dd3fc",
        "impact": "Low Impact",
    },
}


# ============================================================
# HELPERS
# ============================================================

def _clean_text(value: Any) -> str:
    """Safely clean text values."""

    if value is None:
        return ""

    return str(value).strip()


def _normalize_severity(value: Any) -> str:
    """Normalize backend severity values."""

    level = _clean_text(value).lower()

    if level in SEVERITY_RANK:
        return level

    if level == "minor":
        return "low"

    return "medium"


def _detect_category(
    title: str,
    action: str,
) -> str:
    """
    Detect the ATS area related to an action item.

    This is only a UI categorization layer.
    """

    text = f"{title} {action}".lower()

    category_keywords = {
        "Keywords & Skills": [
            "keyword",
            "skill",
            "technology",
            "technical",
            "tool",
            "stack",
            "match",
            "jd",
            "job description",
        ],
        "Formatting": [
            "format",
            "font",
            "spacing",
            "layout",
            "margin",
            "heading",
            "section",
            "bullet",
            "template",
        ],
        "Content Quality": [
            "content",
            "achievement",
            "metric",
            "quantif",
            "impact",
            "experience",
            "bullet point",
            "description",
            "action verb",
        ],
        "ATS Compatibility": [
            "ats",
            "parse",
            "parsing",
            "compatib",
            "readable",
            "parser",
            "file",
            "pdf",
        ],
        "Skill Validation": [
            "validation",
            "proof",
            "project",
            "certification",
            "evidence",
            "demonstrat",
        ],
    }

    for category, keywords in category_keywords.items():
        if any(keyword in text for keyword in keywords):
            return category

    return "General"


def _get_priority_score(level: str) -> int:
    """Return numerical priority score."""

    values = {
        "critical": 100,
        "high": 80,
        "medium": 60,
        "low": 30,
    }

    return values.get(level, 30)


# ============================================================
# COLLECT ITEMS
# ============================================================

def _collect_action_items(
    analysis: Dict[str, Any],
) -> List[Dict[str, Any]]:
    """
    Collect, clean, categorize and prioritize action items.

    Returns dictionaries instead of raw tuples so the UI
    can display richer information.
    """

    items: List[Dict[str, Any]] = []
    seen = set()

    detailed_feedback = (
        analysis.get("detailed_feedback") or []
    )

    for issue in detailed_feedback:

        if not isinstance(issue, dict):
            continue

        severity = _normalize_severity(
            issue.get("severity_level")
        )

        title = _clean_text(
            issue.get("issue_title")
        )

        if not title:
            title = "Resume Improvement"

        actions = issue.get("action_items") or []

        for action in actions:

            action_text = _clean_text(action)

            if not action_text:
                continue

            unique_key = (
                severity,
                title.lower(),
                action_text.lower(),
            )

            if unique_key in seen:
                continue

            seen.add(unique_key)

            items.append(
                {
                    "severity": severity,
                    "title": title,
                    "action": action_text,
                    "category": _detect_category(
                        title,
                        action_text,
                    ),
                    "priority": _get_priority_score(
                        severity
                    ),
                }
            )

    # --------------------------------------------------------
    # Fallback suggestions
    # --------------------------------------------------------

    if not items:

        for suggestion in (
            analysis.get("suggestions") or []
        ):

            suggestion_text = _clean_text(
                suggestion
            )

            if not suggestion_text:
                continue

            unique_key = (
                "medium",
                "General",
                suggestion_text.lower(),
            )

            if unique_key in seen:
                continue

            seen.add(unique_key)

            items.append(
                {
                    "severity": "medium",
                    "title": "General Recommendation",
                    "action": suggestion_text,
                    "category": _detect_category(
                        "General",
                        suggestion_text,
                    ),
                    "priority": 60,
                }
            )

    # Highest priority first
    items.sort(
        key=lambda item: (
            SEVERITY_RANK.get(
                item["severity"],
                99,
            ),
            -item["priority"],
        )
    )

    return items


# ============================================================
# SUMMARY
# ============================================================

def _get_summary(
    items: List[Dict[str, Any]],
) -> Dict[str, int]:

    summary = {
        "critical": 0,
        "high": 0,
        "medium": 0,
        "low": 0,
    }

    for item in items:

        level = item["severity"]

        if level in summary:
            summary[level] += 1

    return summary


# ============================================================
# TOP RECOMMENDATIONS
# ============================================================

def _get_top_recommendations(
    items: List[Dict[str, Any]],
    limit: int = 3,
) -> List[Dict[str, Any]]:
    """Return highest-priority recommendations."""

    return items[:limit]


# ============================================================
# CSS
# ============================================================

def _apply_styles() -> None:

    st.markdown(
        """
        <style>

        /* ==================================================
           MAIN CONTAINER
        ================================================== */

        .improvement-wrapper {
            margin-top: 22px;
            margin-bottom: 28px;
        }

        .improvement-title {
            font-size: 25px;
            font-weight: 900;
            color: #0f172a;
            margin-bottom: 3px;
        }

        .improvement-subtitle {
            color: #64748b;
            font-size: 13px;
            margin-bottom: 20px;
        }


        /* ==================================================
           SUMMARY CARDS
        ================================================== */

        .improvement-summary {
            display: grid;
            grid-template-columns:
                repeat(4, minmax(0, 1fr));
            gap: 12px;
            margin-bottom: 22px;
        }

        .summary-card {
            padding: 16px;
            border-radius: 17px;
            background:
                linear-gradient(
                    145deg,
                    rgba(255,255,255,0.98),
                    rgba(248,250,252,0.96)
                );
            border:
                1px solid rgba(15,23,42,0.09);
            box-shadow:
                0 7px 20px rgba(15,23,42,0.06);
            transition:
                transform .23s ease,
                box-shadow .23s ease;
        }

        .summary-card:hover {
            transform:
                translateY(-4px)
                scale(1.015);
            box-shadow:
                0 14px 30px rgba(15,23,42,0.11);
        }

        .summary-label {
            font-size: 10px;
            font-weight: 850;
            text-transform: uppercase;
            letter-spacing: .08em;
            color: #64748b;
        }

        .summary-value {
            font-size: 25px;
            line-height: 1.1;
            font-weight: 900;
            color: #0f172a;
            margin-top: 5px;
        }


        /* ==================================================
           TOP RECOMMENDATIONS
        ================================================== */

        .top-section {
            padding: 20px;
            margin-bottom: 24px;
            border-radius: 20px;
            background:
                linear-gradient(
                    135deg,
                    #f8fafc,
                    #eef6ff
                );
            border:
                1px solid rgba(14,165,233,.16);
            box-shadow:
                0 9px 26px rgba(15,23,42,.07);
        }

        .top-heading {
            font-size: 17px;
            font-weight: 850;
            color: #0f172a;
            margin-bottom: 15px;
        }

        .top-item {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 12px;
            margin: 8px 0;
            border-radius: 13px;
            background: rgba(255,255,255,.80);
            border:
                1px solid rgba(15,23,42,.07);
            transition:
                transform .2s ease,
                box-shadow .2s ease;
        }

        .top-item:hover {
            transform: translateX(4px);
            box-shadow:
                0 7px 18px rgba(15,23,42,.08);
        }

        .top-number {
            min-width: 30px;
            height: 30px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 9px;
            background: #0f172a;
            color: #ffffff;
            font-size: 12px;
            font-weight: 900;
        }

        .top-content {
            flex: 1;
        }

        .top-title {
            font-size: 13px;
            font-weight: 800;
            color: #0f172a;
        }

        .top-action {
            font-size: 12px;
            color: #64748b;
            margin-top: 2px;
        }


        /* ==================================================
           SECTION HEADER
        ================================================== */

        .section-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin: 22px 0 12px 0;
        }

        .section-heading {
            font-size: 18px;
            font-weight: 850;
            color: #0f172a;
        }

        .section-count {
            font-size: 11px;
            font-weight: 800;
            color: #64748b;
            background: #f1f5f9;
            padding: 6px 10px;
            border-radius: 999px;
        }


        /* ==================================================
           ACTION CARD
        ================================================== */

        .action-card {
            position: relative;
            padding: 19px;
            margin: 11px 0;
            border-radius: 19px;
            background:
                linear-gradient(
                    145deg,
                    rgba(255,255,255,.99),
                    rgba(248,250,252,.96)
                );
            border:
                1px solid rgba(15,23,42,.09);
            box-shadow:
                0 7px 21px rgba(15,23,42,.065);
            transition:
                transform .25s ease,
                box-shadow .25s ease,
                border-color .25s ease;
            overflow: hidden;
        }

        .action-card::before {
            content: "";
            position: absolute;
            left: 0;
            top: 0;
            bottom: 0;
            width: 4px;
            background: #06b6d4;
        }

        .action-card:hover {
            transform:
                translateY(-5px)
                scale(1.008);
            box-shadow:
                0 16px 34px rgba(15,23,42,.12);
            border-color:
                rgba(14,165,233,.25);
        }

        .action-top {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 12px;
        }

        .action-left {
            flex: 1;
        }

        .action-title {
            color: #0f172a;
            font-size: 15px;
            font-weight: 850;
        }

        .action-category {
            display: inline-block;
            margin-top: 7px;
            padding: 4px 9px;
            border-radius: 999px;
            background: #eff6ff;
            color: #0369a1;
            font-size: 10px;
            font-weight: 800;
        }

        .severity-badge {
            padding: 6px 10px;
            border-radius: 999px;
            font-size: 10px;
            font-weight: 900;
            letter-spacing: .06em;
            white-space: nowrap;
        }

        .impact-text {
            margin-top: 13px;
            color: #475569;
            font-size: 11px;
            font-weight: 750;
        }

        .action-description {
            margin-top: 6px;
            color: #334155;
            font-size: 13px;
            line-height: 1.65;
        }


        /* ==================================================
           PROGRESS
        ================================================== */

        .progress-wrapper {
            margin-top: 8px;
            height: 7px;
            border-radius: 999px;
            background: #e2e8f0;
            overflow: hidden;
        }

        .progress-bar {
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
           RESPONSIVE
        ================================================== */

        @media (max-width: 850px) {

            .improvement-summary {
                grid-template-columns:
                    repeat(2, minmax(0, 1fr));
            }

        }

        @media (max-width: 550px) {

            .improvement-summary {
                grid-template-columns: 1fr;
            }

            .action-top {
                flex-direction: column;
            }

            .severity-badge {
                align-self: flex-start;
            }

            .action-card {
                padding: 15px;
            }

        }

        </style>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# DISPLAY
# ============================================================

def display_action_items(
    analysis: Dict[str, Any],
) -> None:
    """
    Display the ATS Improvement Center.

    Existing function signature preserved.
    """

    items = _collect_action_items(analysis)

    if not items:
        return

    _apply_styles()

    summary = _get_summary(items)

    # ========================================================
    # HEADER
    # ========================================================

    st.markdown(
        """
        <div class="improvement-wrapper">

            <div class="improvement-title">
                ATS Improvement Center
            </div>

            <div class="improvement-subtitle">
                Prioritized recommendations to improve your
                resume's ATS performance.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    # ========================================================
    # SUMMARY
    # ========================================================

    st.markdown(
        f"""
        <div class="improvement-summary">

            <div class="summary-card">
                <div class="summary-label">
                    Total Actions
                </div>
                <div class="summary-value">
                    {len(items)}
                </div>
            </div>

            <div class="summary-card">
                <div class="summary-label">
                    Critical
                </div>
                <div
                    class="summary-value"
                    style="color:#b91c1c;"
                >
                    {summary["critical"]}
                </div>
            </div>

            <div class="summary-card">
                <div class="summary-label">
                    High Priority
                </div>
                <div
                    class="summary-value"
                    style="color:#c2410c;"
                >
                    {summary["high"]}
                </div>
            </div>

            <div class="summary-card">
                <div class="summary-label">
                    Medium
                </div>
                <div
                    class="summary-value"
                    style="color:#a16207;"
                >
                    {summary["medium"]}
                </div>
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    # ========================================================
    # TOP 3
    # ========================================================

    top_items = _get_top_recommendations(items)

    if top_items:

        top_html = """
        <div class="top-section">

            <div class="top-heading">
                Top Recommendations
            </div>
        """

        for index, item in enumerate(
            top_items,
            start=1,
        ):

            top_html += f"""
            <div class="top-item">

                <div class="top-number">
                    {index}
                </div>

                <div class="top-content">

                    <div class="top-title">
                        {item["title"]}
                    </div>

                    <div class="top-action">
                        {item["action"]}
                    </div>

                </div>

            </div>
            """

        top_html += "</div>"

        st.markdown(
            top_html,
            unsafe_allow_html=True,
        )

    # ========================================================
    # ALL ACTIONS
    # ========================================================

    st.markdown(
        f"""
        <div class="section-header">

            <div class="section-heading">
                All Recommendations
            </div>

            <div class="section-count">
                {len(items)} actions
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    # ========================================================
    # CARDS
    # ========================================================

    for index, item in enumerate(
        items,
        start=1,
    ):

        level = item["severity"]

        meta = SEVERITY_META.get(
            level,
            SEVERITY_META["medium"],
        )

        # Priority percentage is only a visual indicator.
        priority = item["priority"]

        # Make sure the progress width remains valid.
        progress_width = max(
            20,
            min(100, priority),
        )

        card_html = f"""
        <div class="action-card">

            <div class="action-top">

                <div class="action-left">

                    <div class="action-title">
                        {index}. {item["title"]}
                    </div>

                    <div class="action-category">
                        {item["category"]}
                    </div>

                </div>

                <div
                    class="severity-badge"
                    style="
                        color:{meta["color"]};
                        background:{meta["background"]};
                        border:1px solid {meta["border"]};
                    "
                >
                    {meta["label"]}
                </div>

            </div>

            <div class="impact-text">
                {meta["impact"]}
            </div>

            <div class="action-description">
                {item["action"]}
            </div>

            <div class="progress-wrapper">
                <div
                    class="progress-bar"
                    style="width:{progress_width}%"
                ></div>
            </div>

        </div>
        """

        st.markdown(
            card_html,
            unsafe_allow_html=True,
        )
