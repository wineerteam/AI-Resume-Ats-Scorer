from typing import Any, Dict, Optional
from html import escape

import streamlit as st


# ============================================================
# HELPERS
# ============================================================

def _safe_number(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _clamp(
    value: float,
    minimum: float = 0.0,
    maximum: float = 100.0,
) -> float:
    return max(minimum, min(value, maximum))


def _similarity_to_percent(value: Any) -> float:
    value = _safe_number(value)

    if value <= 1:
        return _clamp(value * 100)

    return _clamp(value)


def _clean_list(values: Any) -> list:
    if not values:
        return []

    if not isinstance(values, (list, tuple)):
        values = [values]

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
# CSS
# ============================================================

def _apply_styles() -> None:
    st.markdown(
        """
<style>

/* =========================================================
   JD MAIN SECTION
   ========================================================= */

.jd-section {
    margin-top: 28px;
    margin-bottom: 20px;
}


/* =========================================================
   HEADER
   ========================================================= */

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
    padding: 0;
    color: #0b1735;
    font-size: 26px;
    line-height: 1.2;
    font-weight: 900;
    letter-spacing: -0.7px;
}

.jd-subtitle {
    margin: 0;
    color: #64748b;
    font-size: 12px;
    line-height: 1.5;
    font-weight: 600;
}

.jd-badge {
    padding: 8px 14px;
    border-radius: 999px;

    background:
        linear-gradient(
            135deg,
            #fff3a6 0%,
            #facc15 45%,
            #f59e0b 100%
        );

    color: #4a3500;

    border: 1px solid rgba(234, 179, 8, 0.45);

    font-size: 10px;
    font-weight: 900;
    letter-spacing: 0.6px;

    white-space: nowrap;

    box-shadow:
        0 6px 15px rgba(234, 179, 8, 0.16);
}


/* =========================================================
   SCORE GRID
   ========================================================= */

.jd-score-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 18px;
    margin-bottom: 18px;
}


/* =========================================================
   SCORE CARD
   ========================================================= */

.jd-score-card {
    position: relative;
    overflow: hidden;

    min-height: 205px;

    padding: 23px;

    border-radius: 21px;

    background:
        linear-gradient(
            145deg,
            #ffffff 0%,
            #fffdf5 55%,
            #fff8d8 100%
        );

    border:
        1px solid rgba(148, 163, 184, 0.20);

    box-shadow:
        0 12px 28px rgba(15, 23, 42, 0.08),
        0 4px 0 rgba(217, 160, 0, 0.10);

    transition:
        transform 0.28s cubic-bezier(.2,.8,.2,1),
        box-shadow 0.28s ease,
        border-color 0.28s ease;
}


/* 3D hover */

.jd-score-card:hover {
    transform:
        translateY(-7px)
        scale(1.018);

    border-color:
        rgba(236, 72, 153, 0.42);

    box-shadow:
        0 20px 40px rgba(15, 23, 42, 0.14),
        0 0 28px rgba(236, 72, 153, 0.10);
}


/* =========================================================
   MULTICOLOR TOP BORDER
   ========================================================= */

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


/* =========================================================
   SCORE LABEL
   ========================================================= */

.jd-score-label {
    margin-bottom: 9px;

    color: #64748b;

    font-size: 11px;
    font-weight: 900;

    text-transform: uppercase;
    letter-spacing: 1px;
}


/* =========================================================
   SCORE VALUE
   ========================================================= */

.jd-score-value {
    margin-bottom: 9px;

    color: #0b1735;

    font-size: 50px;
    line-height: 1;

    font-weight: 950;

    letter-spacing: -2.5px;
}

.jd-score-value span {
    color: #94a3b8;

    font-size: 21px;
    font-weight: 800;

    letter-spacing: 0;
}


/* =========================================================
   STATUS
   ========================================================= */

.jd-score-status {
    display: inline-block;

    margin-bottom: 16px;

    padding: 5px 11px;

    border-radius: 999px;

    background:
        linear-gradient(
            135deg,
            #fff8cf,
            #fef3c7
        );

    color: #a16207;

    border:
        1px solid rgba(234, 179, 8, 0.20);

    font-size: 10px;
    font-weight: 900;
}


/* =========================================================
   PROGRESS
   ========================================================= */

.jd-progress-track {
    width: 100%;
    height: 10px;

    overflow: hidden;

    border-radius: 999px;

    background: #eee9dc;

    box-shadow:
        inset 0 1px 3px rgba(15, 23, 42, 0.09);
}

.jd-progress-fill {
    height: 100%;

    border-radius: 999px;

    background:
        linear-gradient(
            90deg,
            #facc15 0%,
            #f59e0b 35%,
            #ec4899 70%,
            #ef4444 100%
        );

    box-shadow:
        0 0 12px rgba(236, 72, 153, 0.24);

    transition:
        width 0.7s ease;
}


/* =========================================================
   DESCRIPTION
   ========================================================= */

.jd-score-description {
    margin-top: 11px;

    color: #64748b;

    font-size: 10px;
    line-height: 1.55;
}


/* =========================================================
   KEYWORD CARDS
   ========================================================= */

.jd-keyword-card {
    position: relative;

    overflow: hidden;

    padding: 22px;

    border-radius: 20px;

    background:
        linear-gradient(
            145deg,
            #ffffff,
            #faf7ef
        );

    border:
        1px solid rgba(148, 163, 184, 0.20);

    box-shadow:
        0 10px 24px rgba(15, 23, 42, 0.07);

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease,
        border-color 0.25s ease;
}

.jd-keyword-card::before {
    content: "";

    position: absolute;

    left: 0;
    top: 0;

    width: 4px;
    height: 100%;

    background:
        linear-gradient(
            180deg,
            #facc15,
            #ec4899,
            #ef4444
        );
}

.jd-keyword-card:hover {
    transform:
        translateY(-5px)
        scale(1.01);

    border-color:
        rgba(236, 72, 153, 0.30);

    box-shadow:
        0 17px 32px rgba(15, 23, 42, 0.10);
}


/* =========================================================
   CARD TEXT
   ========================================================= */

.jd-card-heading {
    margin-bottom: 5px;

    color: #0b1735;

    font-size: 15px;
    font-weight: 900;
}

.jd-card-description {
    margin-bottom: 15px;

    color: #64748b;

    font-size: 10px;
    line-height: 1.5;
}


/* =========================================================
   CHIPS
   ========================================================= */

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
    font-weight: 800;

    transition:
        transform 0.18s ease,
        box-shadow 0.18s ease;
}

.jd-chip:hover {
    transform:
        translateY(-3px)
        scale(1.04);
}


/* Matched */

.jd-chip-matched {
    background:
        linear-gradient(
            135deg,
            #ecfdf5,
            #d1fae5
        );

    color: #047857;

    border:
        1px solid rgba(16, 185, 129, 0.22);

    box-shadow:
        0 4px 10px rgba(16, 185, 129, 0.08);
}


/* Missing */

.jd-chip-missing {
    background:
        linear-gradient(
            135deg,
            #fff1f2,
            #ffe4e6
        );

    color: #be123c;

    border:
        1px solid rgba(244, 63, 94, 0.22);

    box-shadow:
        0 4px 10px rgba(244, 63, 94, 0.08);
}


/* =========================================================
   BOTTOM GRID
   ========================================================= */

.jd-bottom-grid {
    display: grid;

    grid-template-columns: 1fr 1fr;

    gap: 18px;
}


/* =========================================================
   GAP CARD
   ========================================================= */

.jd-gap-card {
    position: relative;

    overflow: hidden;

    padding: 21px;

    border-radius: 19px;

    background: #ffffff;

    border:
        1px solid rgba(148, 163, 184, 0.18);

    box-shadow:
        0 9px 22px rgba(15, 23, 42, 0.06);

    transition:
        transform 0.24s ease,
        box-shadow 0.24s ease;
}

.jd-gap-card::before {
    content: "";

    position: absolute;

    left: 0;
    top: 0;

    width: 4px;
    height: 100%;

    background:
        linear-gradient(
            180deg,
            #facc15,
            #f97316,
            #ef4444
        );
}

.jd-gap-card:hover {
    transform:
        translateY(-5px);

    box-shadow:
        0 16px 31px rgba(15, 23, 42, 0.10);
}


/* =========================================================
   GAP ITEMS
   ========================================================= */

.jd-gap-item {
    display: flex;
    align-items: center;

    gap: 10px;

    padding: 10px 11px;

    margin-bottom: 8px;

    border-radius: 10px;

    background: #faf8f2;

    border:
        1px solid rgba(148, 163, 184, 0.12);

    color: #334155;

    font-size: 11px;
    font-weight: 650;

    transition:
        transform 0.18s ease,
        background 0.18s ease;
}

.jd-gap-item:hover {
    transform:
        translateX(5px);

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
        0 0 8px rgba(239, 68, 68, 0.25);
}


/* =========================================================
   EMPTY STATE
   ========================================================= */

.jd-empty {
    padding: 18px;

    border-radius: 11px;

    background:
        #f8fafc;

    border:
        1px dashed #cbd5e1;

    color: #64748b;

    font-size: 11px;

    text-align: center;
}


/* =========================================================
   RESPONSIVE
   ========================================================= */

@media (max-width: 900px) {

    .jd-score-grid,
    .jd-bottom-grid {
        grid-template-columns: 1fr;
    }

    .jd-header {
        align-items: flex-start;
        flex-direction: column;
    }

    .jd-badge {
        align-self: flex-start;
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
# MAIN FUNCTION
# ============================================================

def display_jd_comparison(
    jd_comparison: Optional[Dict[str, Any]]
) -> None:

    # Keep original functionality.
    if not jd_comparison:
        return

    _apply_styles()


    # ========================================================
    # BACKEND DATA
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
    # IMPORTANT:
    # HTML is rendered using st.html(), NOT st.markdown().
    # ========================================================

    st.html(
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
"""
    )


    # ========================================================
    # SCORE CARDS
    # ========================================================

    match_status = _match_status(match_pct)
    similarity_status = _similarity_status(semantic)


    st.html(
        f"""
<div class="jd-score-grid">

    <div class="jd-score-card">

        <div class="jd-score-label">
            Overall Job Match
        </div>

        <div class="jd-score-value">
            {match_pct:.0f}<span>%</span>
        </div>

        <div class="jd-score-status">
            {escape(match_status)}
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


    <div class="jd-score-card">

        <div class="jd-score-label">
            Semantic Similarity
        </div>

        <div class="jd-score-value">
            {semantic:.0f}<span>%</span>
        </div>

        <div class="jd-score-status">
            {escape(similarity_status)}
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
"""
    )


    # ========================================================
    # MATCHED KEYWORDS
    # ========================================================

    if matched:

        matched_chips = "".join(
            f"""
<span class="jd-chip jd-chip-matched">
    {escape(keyword)}
</span>
"""
            for keyword in matched[:15]
        )

    else:

        matched_chips = """
<div class="jd-empty">
    No matched keywords detected yet.
</div>
"""


    # ========================================================
    # MISSING KEYWORDS
    # ========================================================

    if missing:

        missing_chips = "".join(
            f"""
<span class="jd-chip jd-chip-missing">
    {escape(keyword)}
</span>
"""
            for keyword in missing[:15]
        )

    else:

        missing_chips = """
<div class="jd-empty">
    All key terms are currently covered.
</div>
"""


    # ========================================================
    # KEYWORD CARDS
    # ========================================================

    st.html(
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
"""
    )


    # ========================================================
    # SKILLS GAP
    # ========================================================

    if gap:

        gap_items = "".join(
            f"""
<div class="jd-gap-item">

    <span class="jd-gap-marker"></span>

    <span>{escape(skill)}</span>

</div>
"""
            for skill in gap[:12]
        )

    else:

        gap_items = """
<div class="jd-empty">
    No significant skills gap detected.
</div>
"""


    # ========================================================
    # ALIGNMENT SUMMARY
    # ========================================================

    summary_items = f"""
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
"""


    # ========================================================
    # FINAL CARDS
    # ========================================================

    st.html(
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
            Quick overview of your job-description alignment.
        </div>

        {summary_items}

    </div>

</div>
"""
    )
