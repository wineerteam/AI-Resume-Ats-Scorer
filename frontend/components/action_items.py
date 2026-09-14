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
        "background": "#fee2e2",
        "border": "#fecaca",
    },
    "high": {
        "label": "HIGH",
        "color": "#c2410c",
        "background": "#ffedd5",
        "border": "#fed7aa",
    },
    "medium": {
        "label": "MEDIUM",
        "color": "#a16207",
        "background": "#fef3c7",
        "border": "#fde68a",
    },
    "low": {
        "label": "LOW",
        "color": "#0369a1",
        "background": "#e0f2fe",
        "border": "#bae6fd",
    },
}


# ============================================================
# HELPERS
# ============================================================

def _clean_text(value: Any) -> str:
    if value is None:
        return ""

    return str(value).strip()


def _normalize_severity(value: Any) -> str:
    level = _clean_text(value).lower()

    if level in ("critical", "urgent"):
        return "critical"

    if level in ("high", "important"):
        return "high"

    if level in ("medium", "moderate"):
        return "medium"

    return "low"


def _get_priority_score(level: str) -> int:
    return {
        "critical": 100,
        "high": 80,
        "medium": 60,
        "low": 30,
    }.get(level, 20)


def _collect_action_items(
    analysis: Dict[str, Any],
) -> List[Dict[str, Any]]:

    items = []
    seen = set()

    detailed_feedback = (
        analysis.get("detailed_feedback")
        or []
    )

    for issue in detailed_feedback:

        if not isinstance(issue, dict):
            continue

        severity = _normalize_severity(
            issue.get("severity_level")
        )

        title = _clean_text(
            issue.get(
                "issue_title",
                "Resume Improvement",
            )
        )

        actions = (
            issue.get("action_items")
            or []
        )

        for action in actions:

            action_text = _clean_text(action)

            if not action_text:
                continue

            unique_key = (
                f"{severity}|"
                f"{title.lower()}|"
                f"{action_text.lower()}"
            )

            if unique_key in seen:
                continue

            seen.add(unique_key)

            items.append(
                {
                    "severity": severity,
                    "title": title,
                    "action": action_text,
                    "priority": _get_priority_score(
                        severity
                    ),
                }
            )

    # --------------------------------------------------------
    # FALLBACK TO GENERAL SUGGESTIONS
    # --------------------------------------------------------

    if not items:

        suggestions = (
            analysis.get("suggestions")
            or []
        )

        for suggestion in suggestions:

            text = _clean_text(suggestion)

            if not text:
                continue

            unique_key = text.lower()

            if unique_key in seen:
                continue

            seen.add(unique_key)

            items.append(
                {
                    "severity": "medium",
                    "title": "General Recommendation",
                    "action": text,
                    "priority": 60,
                }
            )

    items.sort(
        key=lambda item: (
            -item["priority"],
            item["title"].lower(),
        )
    )

    return items


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

        .improvement-title {
            color: #0f172a;
            font-size: 27px;
            font-weight: 950;
            letter-spacing: -0.03em;
            margin-top: 24px;
            margin-bottom: 4px;
        }

        .improvement-subtitle {
            color: #64748b;
            font-size: 12px;
            line-height: 1.6;
            margin-bottom: 18px;
        }


        /* =====================================================
           SUMMARY
        ===================================================== */

        .summary-grid {
            display: grid;
            grid-template-columns:
                repeat(3, minmax(0, 1fr));
            gap: 12px;
            margin-bottom: 20px;
        }

        .summary-card {
            position: relative;
            overflow: hidden;

            padding: 18px;

            border-radius: 19px;

            background:
                linear-gradient(
                    145deg,
                    #ffffff,
                    #f8fafc
                );

            border: 1px solid #e2e8f0;

            box-shadow:
                0 8px 24px
                rgba(15, 23, 42, 0.055);

            transition:
                transform .22s ease,
                box-shadow .22s ease,
                border-color .22s ease;
        }

        .summary-card:hover {
            transform:
                translateY(-5px)
                scale(1.01);

            box-shadow:
                0 17px 34px
                rgba(15, 23, 42, .10);

            border-color: #93c5fd;
        }

        .summary-card::before {
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

        .summary-label {
            color: #64748b;

            font-size: 8px;
            font-weight: 900;

            text-transform: uppercase;

            letter-spacing: .10em;
        }

        .summary-value {
            color: #0f172a;

            font-size: 27px;
            font-weight: 950;

            margin-top: 4px;
        }

        .summary-description {
            color: #94a3b8;

            font-size: 9px;

            margin-top: 2px;
        }


        /* =====================================================
           PRIORITY PANEL
           ===================================================== */

        .priority-panel {
            position: relative;
            overflow: hidden;

            padding: 20px;

            border-radius: 22px;

            background:
                linear-gradient(
                    135deg,
                    #07152f,
                    #102a56
                );

            box-shadow:
                0 15px 34px
                rgba(15, 23, 42, .13);

            margin-bottom: 20px;
        }

        .priority-panel::after {
            content: "";

            position: absolute;

            width: 170px;
            height: 170px;

            border-radius: 50%;

            border: 1px solid
                rgba(34, 211, 238, .10);

            right: -70px;
            top: -90px;
        }

        .priority-label {
            position: relative;
            z-index: 2;

            color: #67e8f9;

            font-size: 8px;
            font-weight: 950;

            text-transform: uppercase;

            letter-spacing: .11em;
        }

        .priority-title {
            position: relative;
            z-index: 2;

            color: white;

            font-size: 18px;
            font-weight: 900;

            margin-top: 4px;
        }

        .priority-text {
            position: relative;
            z-index: 2;

            color: #cbd5e1;

            font-size: 10px;

            line-height: 1.6;

            margin-top: 3px;
        }


        /* =====================================================
           ACTION CARDS
           ===================================================== */

        .action-grid {
            display: grid;

            grid-template-columns:
                repeat(2, minmax(0, 1fr));

            gap: 14px;
        }

        .action-card {
            position: relative;
            overflow: hidden;

            padding: 18px;

            border-radius: 20px;

            background: white;

            border: 1px solid #e2e8f0;

            box-shadow:
                0 7px 22px
                rgba(15, 23, 42, .055);

            transition:
                transform .22s ease,
                box-shadow .22s ease,
                border-color .22s ease;
        }

        .action-card:hover {
            transform:
                translateY(-6px)
                scale(1.01);

            box-shadow:
                0 18px 38px
                rgba(15, 23, 42, .10);

            border-color: #93c5fd;
        }

        .action-number {
            display: inline-flex;

            align-items: center;
            justify-content: center;

            width: 30px;
            height: 30px;

            border-radius: 10px;

            background:
                linear-gradient(
                    135deg,
                    #e0f2fe,
                    #dbeafe
                );

            color: #0369a1;

            font-size: 9px;
            font-weight: 950;

            margin-bottom: 11px;
        }

        .action-top {
            display: flex;

            justify-content: space-between;
            align-items: flex-start;

            gap: 10px;
        }

        .action-source {
            color: #0f172a;

            font-size: 13px;
            font-weight: 900;

            line-height: 1.4;
        }

        .severity-badge {
            padding: 5px 8px;

            border-radius: 999px;

            font-size: 7px;
            font-weight: 950;

            white-space: nowrap;
        }

        .action-text {
            color: #475569;

            font-size: 10px;

            line-height: 1.7;

            margin-top: 10px;
        }

        .priority-row {
            display: flex;

            justify-content: space-between;

            color: #94a3b8;

            font-size: 8px;
            font-weight: 800;

            margin-top: 13px;
        }

        .priority-track {
            height: 5px;

            border-radius: 999px;

            background: #e2e8f0;

            overflow: hidden;

            margin-top: 5px;
        }

        .priority-fill {
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
           EMPTY STATE
           ===================================================== */

        .action-empty {
            padding: 35px 22px;

            text-align: center;

            border-radius: 20px;

            background:
                linear-gradient(
                    135deg,
                    #f0fdf4,
                    #ecfeff
                );

            border: 1px solid #a7f3d0;
        }

        .action-empty-title {
            color: #166534;

            font-size: 17px;
            font-weight: 900;
        }

        .action-empty-text {
            color: #64748b;

            font-size: 10px;

            margin-top: 5px;
        }


        /* =====================================================
           RESPONSIVE
           ===================================================== */

        @media (max-width: 800px) {

            .summary-grid {
                grid-template-columns: 1fr;
            }

            .action-grid {
                grid-template-columns: 1fr;
            }

        }

        </style>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# MAIN COMPONENT
# ============================================================

def display_action_items(
    analysis: Dict[str, Any],
) -> None:

    _apply_styles()

    items = _collect_action_items(
        analysis
    )

    # ========================================================
    # HEADER
    # ========================================================

    st.html(
        """
        <div class="improvement-title">
            ATS Improvement Center
        </div>

        <div class="improvement-subtitle">
            Prioritized recommendations to improve your
            resume's ATS performance.
        </div>
        """
    )

    # ========================================================
    # EMPTY STATE
    # ========================================================

    if not items:

        st.html(
            """
            <div class="action-empty">

                <div class="action-empty-title">
                    No Improvement Actions Found
                </div>

                <div class="action-empty-text">
                    Your analysis did not return any specific
                    action items.
                </div>

            </div>
            """
        )

        return

    # ========================================================
    # COUNTS
    # ========================================================

    total = len(items)

    critical_count = sum(
        1
        for item in items
        if item["severity"] == "critical"
    )

    high_count = sum(
        1
        for item in items
        if item["severity"] == "high"
    )

    # ========================================================
    # SUMMARY CARDS
    # ========================================================

    st.html(
        f"""
        <div class="summary-grid">

            <div class="summary-card">

                <div class="summary-label">
                    Total Actions
                </div>

                <div class="summary-value">
                    {total}
                </div>

                <div class="summary-description">
                    Recommended improvements
                </div>

            </div>


            <div class="summary-card">

                <div class="summary-label">
                    High Priority
                </div>

                <div class="summary-value">
                    {critical_count + high_count}
                </div>

                <div class="summary-description">
                    Should be reviewed first
                </div>

            </div>


            <div class="summary-card">

                <div class="summary-label">
                    Coverage
                </div>

                <div class="summary-value">
                    {min(total, 10) * 10}%
                </div>

                <div class="summary-description">
                    Action plan generated
                </div>

            </div>

        </div>
        """
    )

    # ========================================================
    # PRIORITY MESSAGE
    # ========================================================

    if critical_count:

        priority_title = (
            "Start With Critical Issues"
        )

        priority_text = (
            f"{critical_count} critical "
            f"recommendation"
            f"{'s' if critical_count != 1 else ''} "
            "should be addressed before lower-priority "
            "improvements."
        )

    elif high_count:

        priority_title = (
            "Focus On High-Priority Improvements"
        )

        priority_text = (
            f"{high_count} high-priority "
            f"recommendation"
            f"{'s' if high_count != 1 else ''} "
            "are the best place to start."
        )

    else:

        priority_title = (
            "Work Through The Action Plan"
        )

        priority_text = (
            "No critical issues were identified. "
            "Work through the recommendations from "
            "highest to lowest priority."
        )

    st.html(
        f"""
        <div class="priority-panel">

            <div class="priority-label">
                Recommended Order
            </div>

            <div class="priority-title">
                {priority_title}
            </div>

            <div class="priority-text">
                {priority_text}
            </div>

        </div>
        """
    )

    # ========================================================
    # ACTION SECTION
    # ========================================================

    st.html(
        """
        <div class="improvement-title"
             style="font-size:21px; margin-top:5px;">
            Recommended Actions
        </div>

        <div class="improvement-subtitle">
            Follow these actions in priority order.
        </div>
        """
    )

    # ========================================================
    # ACTION CARDS
    # ========================================================

    cards_html = """
    <div class="action-grid">
    """

    for index, item in enumerate(
        items,
        start=1,
    ):

        severity = item["severity"]

        meta = SEVERITY_META.get(
            severity,
            SEVERITY_META["low"],
        )

        priority = item["priority"]

        # Visual priority only.
        priority_width = min(
            100,
            max(25, priority),
        )

        cards_html += f"""
        <div class="action-card">

            <div class="action-number">
                {index:02d}
            </div>

            <div class="action-top">

                <div class="action-source">
                    {item["title"]}
                </div>

                <div
                    class="severity-badge"
                    style="
                        color:{meta["color"]};
                        background:{meta["background"]};
                        border:1px solid
                            {meta["border"]};
                    "
                >
                    {meta["label"]}
                </div>

            </div>

            <div class="action-text">
                {item["action"]}
            </div>

            <div class="priority-row">

                <span>
                    Priority
                </span>

                <span>
                    {priority}/100
                </span>

            </div>

            <div class="priority-track">

                <div
                    class="priority-fill"
                    style="
                        width:{priority_width}%;
                    "
                ></div>

            </div>

        </div>
        """

    cards_html += """
    </div>
    """

    st.html(cards_html)
