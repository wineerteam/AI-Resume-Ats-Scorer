from typing import Tuple, Dict, Any


# ============================================================
# SCORE UTILITIES
# ============================================================

def _safe_score(score: Any) -> float:
    """
    Safely convert score to a number between 0 and 100.
    Handles None, strings, invalid values, etc.
    """
    try:
        value = float(score)
    except (TypeError, ValueError):
        return 0.0

    return max(0.0, min(100.0, value))


def get_score_color(score: float) -> Tuple[str, str]:
    """
    Return (text_color, background_color) for a 0-100 score.
    """

    score = _safe_score(score)

    if score >= 90:
        return "#166534", "#dcfce7"       # Excellent

    if score >= 80:
        return "#15803d", "#ecfdf5"       # Strong

    if score >= 70:
        return "#0369a1", "#e0f2fe"       # Good

    if score >= 60:
        return "#b45309", "#fef3c7"       # Moderate

    return "#b91c1c", "#fee2e2"           # Needs work


# ============================================================
# SCORE STATUS
# ============================================================

def get_score_status(score: float) -> str:
    """
    Return a human-readable status for the ATS score.
    """

    score = _safe_score(score)

    if score >= 90:
        return "Excellent"

    if score >= 80:
        return "Strong"

    if score >= 70:
        return "Good"

    if score >= 60:
        return "Needs Improvement"

    return "Needs Work"


def get_score_label(score: float) -> str:
    """
    Return a recruiter-friendly ATS match label.
    """

    score = _safe_score(score)

    if score >= 90:
        return "Excellent ATS Match"

    if score >= 80:
        return "Strong ATS Match"

    if score >= 70:
        return "Good ATS Match"

    if score >= 60:
        return "Moderate ATS Match"

    return "Low ATS Match"


# ============================================================
# SCORE EMOJI
# ============================================================

def get_score_emoji(score: float) -> str:
    """
    Kept for backward compatibility.

    UI can remain emoji-free while old code importing this
    function continues to work.
    """

    return ""


# ============================================================
# SEVERITY UTILITIES
# ============================================================

def get_severity_style(
    severity: str,
) -> Tuple[str, str, str]:
    """
    Return:
        (indicator, text_color, background_color)

    Supports backend severity values:
        critical, high, medium, low, minor, info
    """

    level = str(severity or "").strip().lower()

    if level in ("critical", "high"):
        return (
            "CRITICAL",
            "#b91c1c",
            "#fee2e2",
        )

    if level == "medium":
        return (
            "MEDIUM",
            "#b45309",
            "#fef3c7",
        )

    if level in ("low", "minor"):
        return (
            "LOW",
            "#0369a1",
            "#e0f2fe",
        )

    return (
        "INFO",
        "#166534",
        "#dcfce7",
    )


def get_severity_priority(severity: str) -> int:
    """
    Higher number = higher severity.
    Useful for sorting feedback/issues.
    """

    level = str(severity or "").strip().lower()

    priorities = {
        "critical": 5,
        "high": 4,
        "medium": 3,
        "low": 2,
        "minor": 1,
        "info": 0,
    }

    return priorities.get(level, 0)


# ============================================================
# PROGRESS COLORS
# ============================================================

def get_score_progress_color(score: float) -> str:
    """
    Return a suitable color for progress bars, score rings,
    charts, and visual indicators.
    """

    score = _safe_score(score)

    if score >= 90:
        return "#16a34a"

    if score >= 80:
        return "#22c55e"

    if score >= 70:
        return "#06b6d4"

    if score >= 60:
        return "#f59e0b"

    return "#ef4444"


# ============================================================
# SCORE RANGE
# ============================================================

def get_score_range(score: float) -> Tuple[int, int]:
    """
    Return the score range/category boundaries.
    """

    score = _safe_score(score)

    if score >= 90:
        return 90, 100

    if score >= 80:
        return 80, 89

    if score >= 70:
        return 70, 79

    if score >= 60:
        return 60, 69

    return 0, 59


# ============================================================
# SCORE CATEGORY
# ============================================================

def get_score_category(score: float) -> str:
    """
    Short category name useful for cards, charts and filters.
    """

    score = _safe_score(score)

    if score >= 90:
        return "Excellent"

    if score >= 80:
        return "Strong"

    if score >= 70:
        return "Good"

    if score >= 60:
        return "Moderate"

    return "Low"


# ============================================================
# SCORE DETAILS
# ============================================================

def get_score_details(score: float) -> Dict[str, Any]:
    """
    Return all important visual/semantic information for
    a score in one dictionary.

    Useful for dashboard/history/scorer UI.
    """

    score = _safe_score(score)

    text_color, background_color = get_score_color(score)

    return {
        "score": score,
        "status": get_score_status(score),
        "label": get_score_label(score),
        "category": get_score_category(score),
        "range": get_score_range(score),
        "text_color": text_color,
        "background_color": background_color,
        "progress_color": get_score_progress_color(score),
    }


# ============================================================
# SCORE IMPROVEMENT
# ============================================================

def calculate_score_change(
    current_score: float,
    previous_score: float,
) -> float:
    """
    Calculate score improvement/difference.

    Example:
        current = 85
        previous = 72
        result = +13
    """

    current = _safe_score(current_score)
    previous = _safe_score(previous_score)

    return round(current - previous, 1)


def get_score_change_status(
    current_score: float,
    previous_score: float,
) -> str:
    """
    Return a meaningful status for score movement.
    """

    change = calculate_score_change(
        current_score,
        previous_score,
    )

    if change >= 10:
        return "Significant Improvement"

    if change > 0:
        return "Improved"

    if change == 0:
        return "No Change"

    if change <= -10:
        return "Significant Decline"

    return "Declined"


def get_score_change_details(
    current_score: float,
    previous_score: float,
) -> Dict[str, Any]:
    """
    Return complete score comparison information.
    """

    change = calculate_score_change(
        current_score,
        previous_score,
    )

    if change > 0:
        direction = "up"
    elif change < 0:
        direction = "down"
    else:
        direction = "same"

    return {
        "current": _safe_score(current_score),
        "previous": _safe_score(previous_score),
        "change": change,
        "direction": direction,
        "status": get_score_change_status(
            current_score,
            previous_score,
        ),
    }


# ============================================================
# SCORE QUALITY CHECK
# ============================================================

def is_strong_score(score: float) -> bool:
    """
    True when score is 80 or above.
    """

    return _safe_score(score) >= 80


def is_excellent_score(score: float) -> bool:
    """
    True when score is 90 or above.
    """

    return _safe_score(score) >= 90


def needs_improvement(score: float) -> bool:
    """
    True when score is below 70.
    """

    return _safe_score(score) < 70


# ============================================================
# SCORE MESSAGE
# ============================================================

def get_score_message(score: float) -> str:
    """
    Return a short actionable message for the user.
    """

    score = _safe_score(score)

    if score >= 90:
        return (
            "Your resume is highly ATS-friendly "
            "and well aligned with recruiter expectations."
        )

    if score >= 80:
        return (
            "Your resume has a strong ATS profile. "
            "A few targeted improvements can make it even better."
        )

    if score >= 70:
        return (
            "Your resume has a good foundation, "
            "but some areas can be optimized for ATS matching."
        )

    if score >= 60:
        return (
            "Your resume needs improvement in key ATS areas "
            "such as keywords, formatting, or content."
        )

    return (
        "Your resume needs significant optimization "
        "before applying to ATS-based jobs."
    )
