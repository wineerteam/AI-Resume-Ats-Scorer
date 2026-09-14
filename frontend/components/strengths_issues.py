from typing import Any, Dict, List

import streamlit as st


# ============================================================
# HELPERS
# ============================================================

def _clean_items(items: Any) -> List[str]:
    if not isinstance(items, list):
        return []

    cleaned = []

    for item in items:
        if item is None:
            continue

        text = str(item).strip()

        if text and text not in cleaned:
            cleaned.append(text)

    return cleaned


# ============================================================
# STYLES
# ============================================================

def _apply_styles() -> None:

    st.markdown(
        """
        <style>

        .strengths-title {
            color: #0f172a;
            font-size: 27px;
            font-weight: 950;
            letter-spacing: -0.025em;
            margin-top: 22px;
            margin-bottom: 2px;
        }

        .strengths-subtitle {
            color: #64748b;
            font-size: 12px;
            line-height: 1.6;
            margin-bottom: 18px;
        }


        /* =====================================================
           STRENGTH GRID
           ===================================================== */

        .strength-grid {
            display: grid;
            grid-template-columns:
                repeat(2, minmax(0, 1fr));
            gap: 14px;
        }

        .strength-card {
            position: relative;
            overflow: hidden;

            min-height: 105px;
            padding: 18px;

            border-radius: 20px;

            background:
                linear-gradient(
                    145deg,
                    #ffffff,
                    #f8fafc
                );

            border: 1px solid #dbeafe;

            box-shadow:
                0 8px 24px
                rgba(15, 23, 42, 0.06);

            transition:
                transform 0.23s ease,
                box-shadow 0.23s ease,
                border-color 0.23s ease;
        }

        .strength-card:hover {
            transform:
                translateY(-6px)
                scale(1.01);

            box-shadow:
                0 18px 38px
                rgba(15, 23, 42, 0.11);

            border-color:
                #93c5fd;
        }

        .strength-card::before {
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

        .strength-number {
            display: inline-flex;

            align-items: center;
            justify-content: center;

            width: 29px;
            height: 29px;

            border-radius: 10px;

            background:
                linear-gradient(
                    135deg,
                    #e0f2fe,
                    #dbeafe
                );

            color: #0369a1;

            font-size: 10px;
            font-weight: 950;

            margin-bottom: 10px;
        }

        .strength-text {
            color: #1e293b;

            font-size: 12px;
            font-weight: 750;

            line-height: 1.65;

            padding-right: 5px;
        }


        /* =====================================================
           EMPTY STATE
           ===================================================== */

        .strength-empty {
            position: relative;
            overflow: hidden;

            padding: 36px 24px;

            border-radius: 22px;

            background:
                linear-gradient(
                    135deg,
                    #f8fafc,
                    #f0fdfa
                );

            border: 1px solid #a7f3d0;

            box-shadow:
                0 10px 28px
                rgba(15, 23, 42, 0.05);

            text-align: center;
        }

        .strength-empty::before {
            content: "";

            position: absolute;

            width: 180px;
            height: 180px;

            border-radius: 50%;

            border: 1px solid
                rgba(20, 184, 166, 0.10);

            top: -90px;
            left: -70px;
        }

        .strength-empty::after {
            content: "";

            position: absolute;

            width: 160px;
            height: 160px;

            border-radius: 50%;

            border: 1px solid
                rgba(59, 130, 246, 0.08);

            right: -70px;
            bottom: -90px;
        }

        .empty-title {
            position: relative;
            z-index: 2;

            color: #0f172a;

            font-size: 17px;
            font-weight: 900;

            margin-bottom: 7px;
        }

        .empty-text {
            position: relative;
            z-index: 2;

            color: #64748b;

            font-size: 11px;

            line-height: 1.7;

            max-width: 560px;

            margin:
                0 auto;
        }


        /* =====================================================
           INSIGHT
           ===================================================== */

        .strength-insight {
            margin-top: 18px;

            padding: 16px 18px;

            border-radius: 17px;

            background:
                linear-gradient(
                    135deg,
                    #eff6ff,
                    #ecfeff
                );

            border: 1px solid #bae6fd;
        }

        .insight-label {
            color: #0369a1;

            font-size: 8px;
            font-weight: 950;

            text-transform: uppercase;

            letter-spacing: .10em;

            margin-bottom: 4px;
        }

        .insight-text {
            color: #334155;

            font-size: 11px;

            line-height: 1.65;
        }


        /* =====================================================
           RESPONSIVE
           ===================================================== */

        @media (max-width: 700px) {

            .strength-grid {
                grid-template-columns: 1fr;
            }

        }

        </style>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# STRENGTHS
# ============================================================

def display_strengths(
    strengths: List[str],
) -> None:

    _apply_styles()

    strengths = _clean_items(strengths)

    # ========================================================
    # HEADER
    # ========================================================

    st.html(
        """
        <div class="strengths-title">
            Resume Strengths
        </div>

        <div class="strengths-subtitle">
            Strong signals identified in your resume.
        </div>
        """
    )

    # ========================================================
    # EMPTY STATE
    # ========================================================

    if not strengths:

        st.html(
            """
            <div class="strength-empty">

                <div class="empty-title">
                    Strengths Not Identified Yet
                </div>

                <div class="empty-text">
                    Continue improving your resume to build
                    stronger ATS and recruiter signals.
                </div>

            </div>
            """
        )

        return

    # ========================================================
    # STRENGTH CARDS
    # ========================================================

    cards_html = """
    <div class="strength-grid">
    """

    for index, item in enumerate(
        strengths,
        start=1,
    ):

        cards_html += f"""
        <div class="strength-card">

            <div class="strength-number">
                {index:02d}
            </div>

            <div class="strength-text">
                {item}
            </div>

        </div>
        """

    cards_html += """
    </div>
    """

    st.html(cards_html)

    # ========================================================
    # INSIGHT
    # ========================================================

    count = len(strengths)

    if count >= 5:
        insight = (
            "Your resume demonstrates multiple strong signals. "
            "Keep these strengths while improving weaker areas."
        )

    elif count >= 3:
        insight = (
            "Your resume has several positive signals. "
            "Strengthening the remaining gaps can make the "
            "profile more balanced."
        )

    else:
        insight = (
            "A few strengths were identified. Consider adding "
            "more measurable achievements, technical evidence, "
            "and relevant project impact where appropriate."
        )

    st.html(
        f"""
        <div class="strength-insight">

            <div class="insight-label">
                Resume Insight
            </div>

            <div class="insight-text">
                {insight}
            </div>

        </div>
        """
    )


# ============================================================
# CRITICAL ISSUES
# ============================================================

def display_critical_issues(
    analysis: Dict[str, Any],
) -> None:

    critical = _clean_items(
        analysis.get("critical_issues")
    )

    summary = _clean_items(
        analysis.get("issues_summary")
    )

    # Remove duplicates from additional issues
    critical_lower = {
        item.lower()
        for item in critical
    }

    extra = [
        item
        for item in summary
        if item.lower()
        not in critical_lower
    ]

    # ========================================================
    # HEADER
    # ========================================================

    st.markdown(
        """
        ### Critical Issues
        """,
    )

    st.caption(
        "Issues that should be reviewed first for better "
        "ATS performance."
    )

    # ========================================================
    # NO ISSUES
    # ========================================================

    if not critical and not extra:

        st.success(
            "No Critical Issues Found"
        )

        st.caption(
            "Your resume does not currently contain any "
            "urgent issues identified by the analysis."
        )

        return

    # ========================================================
    # SUMMARY METRICS
    # ========================================================

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Critical",
        len(critical),
    )

    c2.metric(
        "Additional",
        len(extra),
    )

    c3.metric(
        "Total Flags",
        len(critical) + len(extra),
    )

    # ========================================================
    # CRITICAL ITEMS
    # ========================================================

    if critical:

        st.warning(
            "Address these issues before focusing on "
            "lower-priority improvements."
        )

        critical_html = """
        <div class="strength-grid">
        """

        for index, item in enumerate(
            critical,
            start=1,
        ):

            critical_html += f"""
            <div class="strength-card">

                <div
                    class="strength-number"
                    style="
                        background:#fee2e2;
                        color:#b91c1c;
                    "
                >
                    {index:02d}
                </div>

                <div class="strength-text">
                    {item}
                </div>

            </div>
            """

        critical_html += "</div>"

        st.html(critical_html)

    # ========================================================
    # ADDITIONAL ISSUES
    # ========================================================

    if extra:

        with st.expander(
            f"Additional flagged items ({len(extra)})",
            expanded=False,
        ):

            for item in extra:

                st.markdown(
                    f"- {item}"
                )
