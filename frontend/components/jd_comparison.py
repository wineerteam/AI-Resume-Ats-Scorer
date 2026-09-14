from typing import Any, Dict, Optional

import streamlit as st


# ============================================================
# HELPERS
# ============================================================

def _safe_number(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _clamp(value: float, minimum: float = 0.0, maximum: float = 100.0) -> float:
    return max(minimum, min(value, maximum))


def _similarity_to_percent(value: Any) -> float:
    """
    Backend semantic_similarity is normally 0-1.
    Also safely handles 0-100 values.
    """
    value = _safe_number(value)

    if value <= 1:
        return _clamp(value * 100)

    return _clamp(value)


def _clean_list(values: Any) -> list:
    if not values:
        return []

    if not isinstance(values, (list, tuple)):
        return [str(values)]

    result = []

    for item in values:
        text = str(item).strip()

        if text:
            result.append(text)

    return result


def _match_status(score: float) -> str:
    if score >= 85:
        return "Excellent Match"

    if score >= 70:
        return "Strong Match"

    if score >= 55:
        return "Moderate Match"

    return "Needs Improvement"


def _similarity_status(score: float) -> str:
    if score >= 85:
        return "Very Strong"

    if score >= 70:
        return "Strong"

    if score >= 55:
        return "Moderate"

    return "Low"


# ============================================================
# PREMIUM STYLES
# ============================================================

def _apply_styles() -> None:

    st.markdown(
        """
<style>

/* ============================================================
   MAIN SECTION
   ============================================================ */

.jd-section {

    margin-top: 28px;
    margin-bottom: 24px;
}


/* ============================================================
   HEADER
   ============================================================ */

.jd-header {

    display: flex;
    align-items: center;
    justify-content: space-between;

    gap: 18px;

    margin-bottom: 20px;
}


.jd-title-wrap {

    display: flex;
    flex-direction: column;
    gap: 5px;
}


.jd-title {

    margin: 0;

    font-size: 25px;

    font-weight: 900;

    letter-spacing: -0.6px;

    color: #0b1735;
}


.jd-subtitle {

    margin: 0;

    font-size: 12px;

    color: #64748b;

    font-weight: 550;
}


.jd-badge {

    padding: 7px 13px;

    border-radius: 999px;

    background:
        linear-gradient(
            135deg,
            #fff4b8,
            #facc15
        );

    color: #493700;

    border:
        1px solid
        rgba(234,179,8,0.45);

    font-size: 10px;

    font-weight: 900;

    letter-spacing: 0.5px;

    white-space: nowrap;

    box-shadow:
        0 4px 12px
        rgba(234,179,8,0.15);
}


/* ============================================================
   TOP SCORE GRID
   ============================================================ */

.jd-score-grid {

    display: grid;

    grid-template-columns:
        1fr 1fr;

    gap: 18px;

    margin-bottom: 20px;
}


/* ============================================================
   SCORE CARD
   ============================================================ */

.jd-score-card {

    position: relative;

    overflow: hidden;

    min-height: 205px;

    padding: 22px;

    border-radius: 20px;

    border:
        1px solid
        rgba(148,163,184,0.20);

    background:
        linear-gradient(
            145deg,
            #ffffff 0%,
            #fffdf5 55%,
            #fff8d9 100%
        );

    box-shadow:
        0 10px 24px
        rgba(15,23,42,0.08),

        0 4px 0
        rgba(180,140,0,0.10);

    transition:
        transform 0.25s cubic-bezier(.2,.8,.2,1),
        box-shadow 0.25s ease,
        border-color 0.25s ease;
}


.jd-score-card:hover {

    transform:
        translateY(-6px)
        scale(1.015);

    border-color:
        rgba(236,72,153,0.35);

    box-shadow:
        0 16px 34px
        rgba(15,23,42,0.13),

        0 0 28px
        rgba(236,72,153,0.08);
}


/* ============================================================
   SCORE CARD TOP ACCENT
   ============================================================ */

.jd-score-card::before {

    content: "";

    position: absolute;

    top: 0;

    left: 0;

    width: 100%;

    height: 5px;

    background:
        linear-gradient(
            90deg,
            #facc15,
            #f59e0b,
            #ec4899,
            #ef4444
        );
}


/* ============================================================
   SCORE LABEL
   ============================================================ */

.jd-score-label {

    font-size: 11px;

    font-weight: 850;

    text-transform: uppercase;

    letter-spacing: 1px;

    color: #6b7280;

    margin-bottom: 9px;
}


/* ============================================================
   SCORE VALUE
   ============================================================ */

.jd-score-value {

    font-size: 48px;

    line-height: 1;

    font-weight: 950;

    letter-spacing: -2px;

    color: #0b1735;

    margin-bottom: 8px;
}


.jd-score-value span {

    font-size: 21px;

    color: #94a3b8;

    font-weight: 750;

    letter-spacing: 0;
}


/* ============================================================
   SCORE STATUS
   ============================================================ */

.jd-score-status {

    display: inline-block;

    padding: 5px 10px;

    border-radius: 999px;

    background:
        rgba(250,204,21,0.18);

    color: #a16207;

    font-size: 10px;

    font-weight: 850;

    margin-bottom: 16px;
}


/* ============================================================
   PROGRESS TRACK
   ============================================================ */

.jd-progress-track {

    width: 100%;

    height: 10px;

    border-radius: 999px;

    overflow: hidden;

    background:
        #eee9dc;

    box-shadow:
        inset 0 1px 3px
        rgba(15,23,42,0.08);
}


.jd-progress-fill {

    height: 100%;

    border-radius: 999px;

    background:
        linear-gradient(
            90deg,
            #facc15,
            #f59e0b,
            #ec4899,
            #ef4444
        );

    box-shadow:
        0 0 10px
        rgba(236,72,153,0.20);

    transition:
        width 0.6s ease;
}


/* ============================================================
   SCORE DESCRIPTION
   ============================================================ */

.jd-score-description {

    margin-top: 11px;

    color: #64748b;

    font-size: 10px;

    line-height: 1.5;
}


/* ============================================================
   KEYWORD AREA
   ============================================================ */

.jd-keyword-card {

    position: relative;

    padding: 22px;

    border-radius: 20px;

    background:
        linear-gradient(
            145deg,
            #ffffff,
            #faf7ef
        );

    border:
        1px solid
        rgba(148,163,184,0.20);

    box-shadow:
        0 9px 22px
        rgba(15,23,42,0.07);

    transition:
        transform 0.24s ease,
        box-shadow 0.24s ease;
}


.jd-keyword-card:hover {

    transform:
        translateY(-4px);

    box-shadow:
        0 15px 30px
        rgba(15,23,42,0.10);
}


/* ============================================================
   CARD HEADING
   ============================================================ */

.jd-card-heading {

    font-size: 14px;

    font-weight: 900;

    color: #0b1735;

    margin-bottom: 5px;
}


.jd-card-description {

    font-size: 10px;

    color: #64748b;

    margin-bottom: 15px;
}


/* ============================================================
   KEYWORD CHIPS
   ============================================================ */

.jd-chip-wrap {

    display: flex;

    flex-wrap: wrap;

    gap: 8px;
}


.jd-chip {

    display: inline-flex;

    align-items: center;

    padding: 7px 10px;

    border-radius: 9px;

    font-size: 10px;

    font-weight: 750;

    transition:
        transform 0.18s ease,
        box-shadow 0.18s ease;
}


.jd-chip:hover {

    transform:
        translateY(-2px)
        scale(1.03);
}


.jd-chip-matched {

    background:
        linear-gradient(
            135deg,
            #ecfdf5,
            #d1fae5
        );

    color: #047857;

    border:
        1px solid
        rgba(16,185,129,0.22);

    box-shadow:
        0 4px 10px
        rgba(16,185,129,0.08);
}


.jd-chip-missing {

    background:
        linear-gradient(
            135deg,
            #fff1f2,
            #ffe4e6
        );

    color: #be123c;

    border:
        1px solid
        rgba(244,63,94,0.22);

    box-shadow:
        0 4px 10px
        rgba(244,63,94,0.08);
}


/* ============================================================
   LOWER GRID
   ============================================================ */

.jd-bottom-grid {

    display: grid;

    grid-template-columns:
        1fr 1fr;

    gap: 18px;
}


/* ============================================================
   GAP CARD
   ============================================================ */

.jd-gap-card {

    padding: 20px;

    border-radius: 18px;

    border:
        1px solid
        rgba(148,163,184,0.18);

    background:
        #ffffff;

    box-shadow:
        0 8px 20px
        rgba(15,23,42,0.06);

    transition:
        transform 0.22s ease,
        box-shadow 0.22s ease;
}


.jd-gap-card:hover {

    transform:
        translateY(-4px);

    box-shadow:
        0 14px 28px
        rgba(15,23,42,0.10);
}


/* ============================================================
   GAP ITEM
   ============================================================ */

.jd-gap-item {

    display: flex;

    align-items: center;

    gap: 10px;

    padding: 10px 11px;

    margin-bottom: 8px;

    border-radius: 10px;

    background:
        #faf8f2;

    border:
        1px solid
        rgba(148,163,184,0.12);

    color: #334155;

    font-size: 11px;

    font-weight: 650;

    transition:
        transform 0.18s ease,
        background 0.18s ease;
}


.jd-gap-item:hover {

    transform:
        translateX(4px);

    background:
        #fff7d6;
}


.jd-gap-marker {

    width: 8px;

    height: 8px;

    flex-shrink: 0;

    border-radius: 50%;

    background:
        linear-gradient(
            135deg,
            #f97316,
            #ef4444
        );

    box-shadow:
        0 0 8px
        rgba(239,68,68,0.22);
}


/* ============================================================
   EMPTY STATE
   ============================================================ */

.jd-empty {

    padding: 20px;

    border-radius: 12px;

    background:
        #f8fafc;

    border:
        1px dashed
        #cbd5e1;

    color: #64748b;

    font-size: 11px;

    text-align: center;
}


/* ============================================================
   RESPONSIVE
   ============================================================ */

@media (max-width: 900px) {

    .jd-score-grid,
    .jd-bottom-grid {

        grid-template-columns: 1fr;
    }

    .jd-header {

        align-items: flex-start;

        flex-direction: column;
    }
}


@media (max-width: 600px) {

    .jd-score-card,
    .jd-keyword-card,
    .jd-gap-card {

        padding: 17px;
    }

    .jd-score-value {

        font-size: 40px;
    }

    .jd-title {

        font-size: 21px;
    }
}

</style>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# MAIN COMPONENT
# ============================================================

def display_jd_comparison(
    jd_comparison: Optional[Dict[str, Any]]
) -> None:

    # Keep existing behavior:
    # caller decides whether section should render.

    if not jd_comparison:
        return


    _apply_styles()


    # ========================================================
    # READ BACKEND DATA
    # ========================================================

    match_pct = _clamp(
        _safe_number(
            jd_comparison.get(
                "match_percentage",
                0
            )
        )
    )


    semantic = _similarity_to_percent(
        jd_comparison.get(
            "semantic_similarity",
            0
        )
    )


    matched = _clean_list(
        jd_comparison.get(
            "matched_keywords",
            []
        )
    )


    missing = _clean_list(
        jd_comparison.get(
            "missing_keywords",
            []
        )
    )


    gap = _clean_list(
        jd_comparison.get(
            "skills_gap",
            []
        )
    )


    # ========================================================
    # HEADER
    # ========================================================

    st.markdown(
        """
<div class="jd-section">

    <div class="jd-header">

        <div class="jd-title-wrap">

            <h3 class="jd-title">
                Job Description Match
            </h3>

            <p class="jd-subtitle">
                Compare your resume against the target job requirements.
            </p>

        </div>

        <div class="jd-badge">
            RESUME VS JOB
        </div>

    </div>

</div>
        """,
        unsafe_allow_html=True,
    )


    # ========================================================
    # TOP SCORE CARDS
    # ========================================================

    match_status = _match_status(match_pct)

    similarity_status = _similarity_status(
        semantic
    )


    st.markdown(
        f"""
<div class="jd-score-grid">

    <!-- MATCH PERCENTAGE -->

    <div class="jd-score-card">

        <div class="jd-score-label">
            Overall Job Match
        </div>

        <div class="jd-score-value">
            {match_pct:.0f}<span>%</span>
        </div>

        <div class="jd-score-status">
            {match_status}
        </div>

        <div class="jd-progress-track">

            <div
                class="jd-progress-fill"
                style="width:{match_pct:.1f}%;">
            </div>

        </div>

        <div class="jd-score-description">
            Measures how closely your resume aligns
            with the job description requirements.
        </div>

    </div>


    <!-- SEMANTIC SIMILARITY -->

    <div class="jd-score-card">

        <div class="jd-score-label">
            Semantic Similarity
        </div>

        <div class="jd-score-value">
            {semantic:.0f}<span>%</span>
        </div>

        <div class="jd-score-status">
            {similarity_status}
        </div>

        <div class="jd-progress-track">

            <div
                class="jd-progress-fill"
                style="width:{semantic:.1f}%;">
            </div>

        </div>

        <div class="jd-score-description">
            Indicates how closely the meaning and context
            of your resume match the target role.
        </div>

    </div>

</div>
        """,
        unsafe_allow_html=True,
    )


    # ========================================================
    # MATCHED KEYWORDS
    # ========================================================

    matched_chips = ""


    if matched:

        for keyword in matched[:15]:

            matched_chips += (
                f'<span class="jd-chip jd-chip-matched">'
                f'{keyword}'
                f'</span>'
            )

    else:

        matched_chips = (
            '<div class="jd-empty">'
            'No matched keywords detected yet.'
            '</div>'
        )


    # ========================================================
    # MISSING KEYWORDS
    # ========================================================

    missing_chips = ""


    if missing:

        for keyword in missing[:15]:

            missing_chips += (
                f'<span class="jd-chip jd-chip-missing">'
                f'{keyword}'
                f'</span>'
            )

    else:

        missing_chips = (
            '<div class="jd-empty">'
            'All key terms are currently covered.'
            '</div>'
        )


    # ========================================================
    # KEYWORD GRID
    # ========================================================

    st.markdown(
        f"""
<div class="jd-score-grid">

    <div class="jd-keyword-card">

        <div class="jd-card-heading">
            Matched Keywords
        </div>

        <div class="jd-card-description">
            Terms from the job description already
            represented in your resume.
        </div>

        <div class="jd-chip-wrap">
            {matched_chips}
        </div>

    </div>


    <div class="jd-keyword-card">

        <div class="jd-card-heading">
            Missing Keywords
        </div>

        <div class="jd-card-description">
            Important terms that may need stronger
            representation in your resume.
        </div>

        <div class="jd-chip-wrap">
            {missing_chips}
        </div>

    </div>

</div>
        """,
        unsafe_allow_html=True,
    )


    # ========================================================
    # SKILLS GAP
    # ========================================================

    if gap:

        gap_items = ""

        for skill in gap[:12]:

            gap_items += f"""
<div class="jd-gap-item">

    <span class="jd-gap-marker"></span>

    <span>{skill}</span>

</div>
"""


    else:

        gap_items = """
<div class="jd-empty">
    No significant skills gap detected.
</div>
"""


    # ========================================================
    # FINAL SKILLS GAP CARD
    # ========================================================

    st.markdown(
        f"""
<div class="jd-bottom-grid">

    <div class="jd-gap-card">

        <div class="jd-card-heading">
            Skills Gap
        </div>

        <div class="jd-card-description">
            Skills that may require stronger evidence
            or better alignment with the target role.
        </div>

        {gap_items}

    </div>


    <div class="jd-gap-card">

        <div class="jd-card-heading">
            Alignment Summary
        </div>

        <div class="jd-card-description">
            Quick interpretation of your job-description alignment.
        </div>

        <div class="jd-gap-item">

            <span class="jd-gap-marker"></span>

            <span>
                Job match:
                <strong>{match_pct:.0f}%</strong>
            </span>

        </div>


        <div class="jd-gap-item">

            <span class="jd-gap-marker"></span>

            <span>
                Semantic similarity:
                <strong>{semantic:.0f}%</strong>
            </span>

        </div>


        <div class="jd-gap-item">

            <span class="jd-gap-marker"></span>

            <span>
                Matched keywords:
                <strong>{len(matched)}</strong>
            </span>

        </div>


        <div class="jd-gap-item">

            <span class="jd-gap-marker"></span>

            <span>
                Missing keywords:
                <strong>{len(missing)}</strong>
            </span>

        </div>

    </div>

</div>
        """,
        unsafe_allow_html=True,
    )
