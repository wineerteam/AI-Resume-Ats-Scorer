from typing import Optional

import requests
import streamlit as st

from frontend.services import api_client
from frontend.components.dashboard import display_results_dashboard


# ============================================================
# PREMIUM SCORER PAGE STYLES
# ============================================================

def _apply_styles() -> None:
    st.markdown(
        """
        <style>

        /* ====================================================
           GLOBAL
        ==================================================== */

        .block-container {
            max-width: 1220px;
            padding-top: 1.5rem;
            padding-bottom: 3rem;
        }

        * {
            box-sizing: border-box;
        }

        /* ====================================================
           HERO
        ==================================================== */

        .scorer-hero {
            position: relative;
            overflow: hidden;

            padding: 42px 42px;

            margin-bottom: 28px;

            border-radius: 30px;

            background:
                radial-gradient(
                    circle at 90% 15%,
                    rgba(250, 204, 21, 0.24),
                    transparent 24%
                ),
                radial-gradient(
                    circle at 8% 90%,
                    rgba(236, 72, 153, 0.20),
                    transparent 27%
                ),
                radial-gradient(
                    circle at 65% 100%,
                    rgba(6, 182, 212, 0.18),
                    transparent 30%
                ),
                linear-gradient(
                    135deg,
                    #0f172a 0%,
                    #172554 35%,
                    #1d4ed8 72%,
                    #0891b2 100%
                );

            border: 1px solid rgba(255,255,255,0.12);

            box-shadow:
                0 25px 65px rgba(15,23,42,0.28),
                inset 0 1px 0 rgba(255,255,255,0.12);

            transition:
                transform 0.3s ease,
                box-shadow 0.3s ease;
        }

        .scorer-hero:hover {
            transform:
                translateY(-5px)
                scale(1.005);

            box-shadow:
                0 35px 80px rgba(15,23,42,0.34);
        }

        .scorer-hero::before {
            content: "";

            position: absolute;

            width: 230px;
            height: 230px;

            right: -100px;
            top: -110px;

            border-radius: 50%;

            background:
                rgba(250,204,21,0.10);

            border:
                1px solid rgba(250,204,21,0.12);
        }

        .scorer-hero::after {
            content: "";

            position: absolute;

            width: 190px;
            height: 190px;

            left: -95px;
            bottom: -110px;

            border-radius: 50%;

            background:
                rgba(236,72,153,0.10);

            border:
                1px solid rgba(236,72,153,0.12);
        }

        .hero-content {
            position: relative;
            z-index: 2;
        }

        .hero-badge {
            display: inline-block;

            padding: 8px 16px;

            margin-bottom: 17px;

            border-radius: 50px;

            background:
                rgba(250,204,21,0.12);

            border:
                1px solid rgba(250,204,21,0.42);

            color: #fef3c7;

            font-size: 11px;

            font-weight: 800;

            letter-spacing: 1.4px;

            box-shadow:
                0 8px 25px rgba(250,204,21,0.08);
        }

        .scorer-hero h1 {
            color: #ffffff;

            font-size: 3rem;

            font-weight: 850;

            letter-spacing: -1.2px;

            margin: 0 0 12px 0;

            line-height: 1.12;
        }

        .scorer-hero p {
            max-width: 760px;

            color: #dbeafe;

            font-size: 15px;

            line-height: 1.75;

            margin: 0;
        }

        .hero-highlight {
            color: #facc15;

            font-weight: 800;

            text-decoration:
                underline;

            text-decoration-color:
                rgba(250,204,21,0.75);

            text-decoration-thickness: 2px;

            text-underline-offset: 4px;
        }

        /* ====================================================
           SECTION HEADING
        ==================================================== */

        .section-heading {
            margin:
                30px 0 17px 0;
        }

        .section-heading h2 {
            color: #0f172a;

            font-size: 1.55rem;

            font-weight: 850;

            letter-spacing: -0.4px;

            margin: 0 0 5px 0;
        }

        .section-heading p {
            color: #64748b;

            font-size: 13px;

            line-height: 1.6;

            margin: 0;
        }

        .section-accent {
            width: 70px;

            height: 4px;

            margin-top: 10px;

            border-radius: 50px;

            background:
                linear-gradient(
                    90deg,
                    #2563eb,
                    #06b6d4,
                    #facc15
                );

            box-shadow:
                0 4px 15px rgba(37,99,235,0.20);
        }

        /* ====================================================
           MODE CARDS
        ==================================================== */

        .mode-card {
            position: relative;

            min-height: 150px;

            padding: 23px;

            border-radius: 21px;

            background:
                linear-gradient(
                    145deg,
                    #ffffff,
                    #f8fafc
                );

            border:
                1px solid #e2e8f0;

            box-shadow:
                0 9px 25px rgba(15,23,42,0.06);

            transition:
                transform 0.3s ease,
                box-shadow 0.3s ease,
                border-color 0.3s ease;
        }

        .mode-card:hover {
            transform:
                translateY(-9px)
                scale(1.015);

            border-color:
                #93c5fd;

            box-shadow:
                0 25px 55px rgba(15,23,42,0.14);
        }

        .mode-blue {
            border-top:
                4px solid #2563eb;
        }

        .mode-yellow {
            border-top:
                4px solid #facc15;
        }

        .mode-title {
            color: #0f172a;

            font-size: 17px;

            font-weight: 800;

            margin-bottom: 7px;
        }

        .mode-description {
            color: #64748b;

            font-size: 13px;

            line-height: 1.65;
        }

        .mode-tag {
            display: inline-block;

            margin-top: 11px;

            padding: 5px 10px;

            border-radius: 50px;

            font-size: 10px;

            font-weight: 800;

            letter-spacing: 0.4px;
        }

        .tag-blue {
            color: #1d4ed8;

            background:
                #dbeafe;
        }

        .tag-yellow {
            color: #b45309;

            background:
                #fef3c7;
        }

        /* ====================================================
           STREAMLIT RADIO
        ==================================================== */

        div[role="radiogroup"] {
            gap: 10px;

            margin-top: 10px;
        }

        div[role="radiogroup"] label {
            border:
                1px solid #dbe3ef;

            border-radius:
                14px;

            padding:
                9px 15px;

            background:
                #ffffff;

            transition:
                transform 0.22s ease,
                box-shadow 0.22s ease,
                border-color 0.22s ease;
        }

        div[role="radiogroup"] label:hover {
            transform:
                translateY(-3px);

            border-color:
                #60a5fa;

            box-shadow:
                0 9px 22px rgba(37,99,235,0.10);
        }

        /* ====================================================
           UPLOAD CONTAINER
        ==================================================== */

        .upload-card {
            position: relative;

            overflow: hidden;

            min-height: 170px;

            padding: 25px;

            border-radius: 23px;

            background:
                linear-gradient(
                    145deg,
                    #ffffff,
                    #f8fafc
                );

            border:
                1px solid #e2e8f0;

            box-shadow:
                0 10px 28px rgba(15,23,42,0.07);

            transition:
                transform 0.3s ease,
                box-shadow 0.3s ease,
                border-color 0.3s ease;
        }

        .upload-card:hover {
            transform:
                translateY(-8px)
                scale(1.01);

            border-color:
                #93c5fd;

            box-shadow:
                0 28px 58px rgba(15,23,42,0.15);
        }

        .upload-card::after {
            content: "";

            position: absolute;

            width: 130px;
            height: 130px;

            right: -70px;
            bottom: -70px;

            border-radius: 50%;

            opacity: 0.10;

            transition:
                transform 0.35s ease;
        }

        .upload-card:hover::after {
            transform:
                scale(1.6);
        }

        .upload-blue {
            border-top:
                4px solid #2563eb;
        }

        .upload-blue::after {
            background:
                #06b6d4;
        }

        .upload-yellow {
            border-top:
                4px solid #facc15;
        }

        .upload-yellow::after {
            background:
                #f97316;
        }

        .upload-title {
            position: relative;

            z-index: 2;

            color: #0f172a;

            font-size: 19px;

            font-weight: 850;

            margin-bottom: 7px;
        }

        .upload-description {
            position: relative;

            z-index: 2;

            color: #64748b;

            font-size: 13px;

            line-height: 1.65;

            margin-bottom: 5px;
        }

        .upload-format {
            position: relative;

            z-index: 2;

            color: #2563eb;

            font-size: 11px;

            font-weight: 750;

            letter-spacing: 0.3px;
        }

        /* ====================================================
           FILE UPLOADER
        ==================================================== */

        [data-testid="stFileUploader"] {
            margin-top: -8px;
        }

        [data-testid="stFileUploaderDropzone"] {
            border:
                1.5px dashed #93c5fd !important;

            border-radius:
                17px !important;

            background:
                linear-gradient(
                    135deg,
                    #eff6ff,
                    #f0fdfa
                ) !important;

            transition:
                transform 0.25s ease,
                border-color 0.25s ease,
                box-shadow 0.25s ease;
        }

        [data-testid="stFileUploaderDropzone"]:hover {
            transform:
                translateY(-3px);

            border-color:
                #2563eb !important;

            box-shadow:
                0 12px 28px rgba(37,99,235,0.10);
        }

        /* ====================================================
           FILE STATUS
        ==================================================== */

        .file-status {
            display: flex;

            align-items: center;

            gap: 12px;

            margin-top: 9px;

            padding: 11px 14px;

            border-radius: 13px;

            background:
                linear-gradient(
                    135deg,
                    #ecfdf5,
                    #f0fdf4
                );

            border:
                1px solid #bbf7d0;
        }

        .file-status-dot {
            width: 9px;
            height: 9px;

            border-radius: 50%;

            background:
                #22c55e;

            box-shadow:
                0 0 0 5px rgba(34,197,94,0.10);
        }

        .file-status-text {
            color: #166534;

            font-size: 12px;

            font-weight: 700;
        }

        /* ====================================================
           TEXT AREA
        ==================================================== */

        textarea {
            border-radius:
                16px !important;

            border:
                1px solid #cbd5e1 !important;

            background:
                #ffffff !important;

            color:
                #0f172a !important;

            transition:
                border-color 0.2s ease,
                box-shadow 0.2s ease;
        }

        textarea:focus {
            border-color:
                #2563eb !important;

            box-shadow:
                0 0 0 3px
                rgba(37,99,235,0.10) !important;
        }

        /* ====================================================
           INFO / SUCCESS / ERROR
        ==================================================== */

        [data-testid="stAlert"] {
            border-radius:
                15px !important;

            box-shadow:
                0 7px 20px
                rgba(15,23,42,0.05);
        }

        /* ====================================================
           ANALYZE AREA
        ==================================================== */

        .analyze-card {
            position: relative;

            overflow: hidden;

            padding: 28px;

            margin: 12px 0 20px 0;

            text-align: center;

            border-radius: 24px;

            background:
                radial-gradient(
                    circle at 90% 20%,
                    rgba(250,204,21,0.17),
                    transparent 24%
                ),
                linear-gradient(
                    135deg,
                    #eff6ff,
                    #f0fdfa
                );

            border:
                1px solid #bfdbfe;

            box-shadow:
                0 12px 32px rgba(37,99,235,0.08);
        }

        .analyze-card h3 {
            color:
                #0f172a;

            font-size:
                20px;

            font-weight:
                850;

            margin:
                0 0 6px 0;
        }

        .analyze-card p {
            color:
                #64748b;

            font-size:
                13px;

            margin:
                0;
        }

        .stButton > button {
            min-height:
                54px;

            border-radius:
                16px;

            font-weight:
                800;

            letter-spacing:
                0.1px;

            transition:
                transform 0.25s ease,
                box-shadow 0.25s ease;
        }

        .stButton > button:hover {
            transform:
                translateY(-4px)
                scale(1.01);

            box-shadow:
                0 16px 38px
                rgba(37,99,235,0.25);
        }

        /* ====================================================
           RESULT HEADER
        ==================================================== */

        .result-header {
            position: relative;

            overflow: hidden;

            margin:
                30px 0 20px 0;

            padding:
                27px 30px;

            border-radius:
                24px;

            background:
                radial-gradient(
                    circle at 92% 10%,
                    rgba(250,204,21,0.18),
                    transparent 25%
                ),
                linear-gradient(
                    135deg,
                    #0f172a,
                    #1e3a8a,
                    #2563eb
                );

            box-shadow:
                0 20px 45px
                rgba(15,23,42,0.20);
        }

        .result-header h2 {
            color:
                #ffffff;

            font-size:
                1.7rem;

            font-weight:
                850;

            margin:
                0 0 6px 0;
        }

        .result-header p {
            color:
                #dbeafe;

            font-size:
                13px;

            margin:
                0;
        }

        .result-header span {
            color:
                #facc15;

            font-weight:
                800;
        }

        /* ====================================================
           EXPORT
        ==================================================== */

        .export-header {
            margin:
                35px 0 15px 0;

            padding:
                20px 22px;

            border-radius:
                19px;

            background:
                linear-gradient(
                    135deg,
                    #ffffff,
                    #f8fafc
                );

            border:
                1px solid #e2e8f0;

            box-shadow:
                0 8px 24px
                rgba(15,23,42,0.06);
        }

        .export-header h3 {
            color:
                #0f172a;

            font-size:
                18px;

            font-weight:
                850;

            margin:
                0 0 5px 0;
        }

        .export-header p {
            color:
                #64748b;

            font-size:
                12px;

            margin:
                0;
        }

        /* ====================================================
           SIDEBAR
        ==================================================== */

        [data-testid="stSidebar"] {
            background:
                linear-gradient(
                    180deg,
                    #f8fafc,
                    #eef2ff
                );
        }

        [data-testid="stSidebar"] h2 {
            color:
                #0f172a;
        }

        /* ====================================================
           DIVIDERS
        ==================================================== */

        hr {
            border:
                none !important;

            height:
                1px !important;

            background:
                linear-gradient(
                    90deg,
                    transparent,
                    #cbd5e1,
                    transparent
                ) !important;

            margin:
                28px 0 !important;
        }

        /* ====================================================
           MOBILE
        ==================================================== */

        @media (max-width: 768px) {

            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }

            .scorer-hero {
                padding:
                    30px 22px;
            }

            .scorer-hero h1 {
                font-size:
                    2.2rem;
            }

            .scorer-hero p {
                font-size:
                    14px;
            }

            .upload-card {
                min-height:
                    auto;

                margin-bottom:
                    18px;
            }

            .mode-card {
                margin-bottom:
                    15px;
            }

            .section-heading h2 {
                font-size:
                    1.35rem;
            }

            .result-header {
                padding:
                    22px;
            }
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# JOB DESCRIPTION READER
# ============================================================

def _read_jd(jd_file, jd_text: str) -> str:
    """
    Turn whatever the user provided into a plain JD string.

    TXT files are decoded locally.
    PDF/DOCX are not sent through a parser here.
    """

    if jd_text:
        return jd_text.strip()

    if jd_file is None:
        return ""

    if jd_file.name.lower().endswith(".txt"):
        return jd_file.getvalue().decode(
            "utf-8",
            errors="ignore",
        )

    st.warning(
        "Job description files must be `.txt` for now — "
        "paste the JD text instead if you have a PDF or DOCX."
    )

    return ""


# ============================================================
# BACKEND ERROR
# ============================================================

def _show_backend_error(exc: Exception) -> None:
    """Translate requests exceptions into friendly messages."""

    if isinstance(exc, requests.ConnectionError):

        st.error(
            "Could not reach the backend. "
            "Is `uvicorn backend.main:app` running on port 8000?"
        )

    elif isinstance(exc, requests.Timeout):

        st.error(
            "The backend took too long to respond. "
            "Try a smaller resume or check the server logs."
        )

    elif (
        isinstance(exc, requests.HTTPError)
        and exc.response is not None
    ):

        try:

            detail = exc.response.json().get(
                "detail",
                exc.response.text,
            )

        except ValueError:

            detail = exc.response.text

        st.error(
            f"Backend returned "
            f"{exc.response.status_code}: {detail}"
        )

    else:

        st.error(
            f"Unexpected error: {exc}"
        )


# ============================================================
# SUMMARY
# ============================================================

def _summary_text(analysis: dict) -> str:

    score = analysis.get(
        "ATS_score",
        analysis.get("ats_score", 0),
    )

    lines = [
        f"ATS Score: {score:.0f}/100",
        "",
    ]

    if analysis.get("strengths"):

        lines.append("STRENGTHS:")

        lines.extend(
            f"  - {s}"
            for s in analysis["strengths"]
        )

        lines.append("")

    if analysis.get("critical_issues"):

        lines.append("CRITICAL ISSUES:")

        lines.extend(
            f"  - {s}"
            for s in analysis["critical_issues"]
        )

        lines.append("")

    if analysis.get("suggestions"):

        lines.append("SUGGESTIONS:")

        lines.extend(
            f"  - {s}"
            for s in analysis["suggestions"]
        )

    return "\n".join(lines)


# ============================================================
# UPLOAD AREA
# ============================================================

def _render_upload_area(analysis_mode: str):

    left, right = st.columns(
        2,
        gap="large",
    )

    # ========================================================
    # RESUME
    # ========================================================

    with left:

        st.html(
            """
            <div class="upload-card upload-blue">

                <div class="upload-title">
                    Resume Upload
                </div>

                <div class="upload-description">
                    Upload your resume to evaluate its
                    ATS compatibility, structure,
                    keywords and content quality.
                </div>

                <div class="upload-format">
                    PDF • DOC • DOCX • Maximum 5 MB
                </div>

            </div>
            """
        )

        resume_file = st.file_uploader(
            "Choose your resume file",
            type=[
                "pdf",
                "doc",
                "docx",
            ],
            help="Supported: PDF, DOC, DOCX (max 5 MB)",
            key="resume_upload",
        )

        if resume_file:

            st.html(
                f"""
                <div class="file-status">

                    <div class="file-status-dot"></div>

                    <div class="file-status-text">
                        {resume_file.name}
                        &nbsp; • &nbsp;
                        {resume_file.size / 1024:.1f} KB
                        &nbsp; • &nbsp;
                        Ready for analysis
                    </div>

                </div>
                """
            )

    # ========================================================
    # JOB DESCRIPTION
    # ========================================================

    jd_file: Optional[object] = None

    jd_text = ""

    with right:

        if analysis_mode == "Job Description Comparison":

            st.html(
                """
                <div class="upload-card upload-yellow">

                    <div class="upload-title">
                        Job Description
                    </div>

                    <div class="upload-description">
                        Compare your resume against a
                        specific job description to identify
                        relevant skills and missing keywords.
                    </div>

                    <div class="upload-format">
                        Paste text or upload TXT
                    </div>

                </div>
                """
            )

            jd_method = st.radio(
                "Input method:",
                [
                    "Paste Text",
                    "Upload .txt File",
                ],
                horizontal=True,
                key="jd_input_method",
            )

            if jd_method == "Upload .txt File":

                jd_file = st.file_uploader(
                    "Choose JD file (.txt only)",
                    type=["txt"],
                    key="jd_upload",
                )

                if jd_file:

                    st.success(
                        f"{jd_file.name} uploaded successfully."
                    )

            else:

                jd_text = st.text_area(
                    "Paste job description text:",
                    height=210,
                    placeholder=(
                        "Paste the complete job description here..."
                    ),
                    key="jd_text",
                )

                if jd_text:

                    st.success(
                        f"{len(jd_text)} characters ready for analysis."
                    )

        else:

            st.html(
                """
                <div class="upload-card upload-yellow">

                    <div class="upload-title">
                        Job Description
                    </div>

                    <div class="upload-description">
                        Target a specific role by switching
                        to Job Description Comparison mode.
                    </div>

                    <div class="upload-format">
                        Optional targeted analysis
                    </div>

                </div>
                """
            )

            st.info(
                "Switch to 'Job Description Comparison' "
                "mode to enable JD matching."
            )

    return (
        resume_file,
        jd_file,
        jd_text,
    )


# ============================================================
# EXPORT
# ============================================================

def _render_export_buttons(analysis: dict) -> None:

    st.html(
        """
        <div class="export-header">

            <h3>
                Export Your Results
            </h3>

            <p>
                Save your ATS analysis as a professional
                PDF report or lightweight text summary.
            </p>

        </div>
        """
    )

    c1, c2 = st.columns(
        2,
        gap="large",
    )

    # ========================================================
    # PDF
    # ========================================================

    with c1:

        if st.button(
            "Generate PDF Report",
            use_container_width=True,
            type="primary",
        ):

            try:

                with st.spinner(
                    "Generating PDF on backend..."
                ):

                    pdf_bytes = api_client.generate_pdf(
                        analysis,
                        access_token=st.session_state[
                            "access_token"
                        ],
                    )

                st.session_state[
                    "scorer_pdf_bytes"
                ] = pdf_bytes

            except requests.RequestException as exc:

                _show_backend_error(exc)

        if (
            "scorer_pdf_bytes"
            in st.session_state
        ):

            st.download_button(
                "Download PDF",
                data=st.session_state[
                    "scorer_pdf_bytes"
                ],
                file_name="ats_resume_report.pdf",
                mime="application/pdf",
                use_container_width=True,
                key="download_pdf_report",
            )

    # ========================================================
    # TXT
    # ========================================================

    with c2:

        st.download_button(
            "Download Summary (.txt)",
            data=_summary_text(analysis),
            file_name="ats_summary.txt",
            mime="text/plain",
            use_container_width=True,
            key="download_summary",
        )


# ============================================================
# MAIN RENDER
# ============================================================

def render() -> None:

    # ========================================================
    # APPLY GUI
    # ========================================================

    _apply_styles()

    # ========================================================
    # HERO
    # ========================================================

    st.html(
        """
        <div class="scorer-hero">

            <div class="hero-content">

                <div class="hero-badge">
                    AI-POWERED RESUME ANALYSIS
                </div>

                <h1>
                    ATS Resume Scorer
                </h1>

                <p>
                    Upload your resume and receive
                    <span class="hero-highlight">
                        intelligent ATS-focused feedback
                    </span>
                    designed to help you improve your
                    resume for modern hiring systems.
                </p>

            </div>

        </div>
        """
    )

    # ========================================================
    # SIDEBAR
    # ========================================================

    with st.sidebar:

        st.markdown("---")

        st.markdown(
            "## Analysis Options"
        )

        st.info(
            "**General ATS Score**: resume only — "
            "overall compatibility.\n\n"
            "**JD Comparison**: resume + job description — "
            "targeted match analysis."
        )

    # ========================================================
    # ANALYSIS MODE
    # ========================================================

    st.html(
        """
        <div class="section-heading">

            <h2>
                Choose Your Analysis
            </h2>

            <p>
                Select the type of evaluation you want
                to perform on your resume.
            </p>

            <div class="section-accent"></div>

        </div>
        """
    )

    mode1, mode2 = st.columns(
        2,
        gap="large",
    )

    with mode1:

        st.html(
            """
            <div class="mode-card mode-blue">

                <div class="mode-title">
                    General ATS Score
                </div>

                <div class="mode-description">
                    Evaluate your resume's overall ATS
                    compatibility without targeting
                    a specific job.
                </div>

                <span class="mode-tag tag-blue">
                    RESUME ONLY
                </span>

            </div>
            """
        )

    with mode2:

        st.html(
            """
            <div class="mode-card mode-yellow">

                <div class="mode-title">
                    Job Description Comparison
                </div>

                <div class="mode-description">
                    Compare your resume against a specific
                    job description for targeted matching.
                </div>

                <span class="mode-tag tag-yellow">
                    RESUME + JD
                </span>

            </div>
            """
        )

    analysis_mode = st.radio(
        "Analysis mode:",
        [
            "General ATS Score",
            "Job Description Comparison",
        ],
        horizontal=True,
        label_visibility="collapsed",
    )

    st.markdown("---")

    # ========================================================
    # UPLOAD
    # ========================================================

    st.html(
        """
        <div class="section-heading">

            <h2>
                Upload Your Documents
            </h2>

            <p>
                Add your resume and, if required,
                the target job description.
            </p>

            <div class="section-accent"></div>

        </div>
        """
    )

    (
        resume_file,
        jd_file,
        jd_text,
    ) = _render_upload_area(
        analysis_mode
    )

    st.markdown("---")

    # ========================================================
    # NO RESUME
    # ========================================================

    if not resume_file:

        st.info(
            "Upload your resume to begin."
        )

        if st.session_state.get(
            "scorer_analysis"
        ):

            st.html(
                """
                <div class="result-header">

                    <h2>
                        Previous Analysis
                    </h2>

                    <p>
                        Your previously generated
                        <span>ATS results</span>
                        are displayed below.
                    </p>

                </div>
                """
            )

            display_results_dashboard(
                st.session_state[
                    "scorer_analysis"
                ]
            )

        return

    # ========================================================
    # ACCESS TOKEN
    # ========================================================

    access_token = st.session_state.get(
        "access_token"
    )

    if not access_token:

        access_token = "mock_token"

        st.info(
            "Running in Guest/Bypass Mode. "
            "Authentication is bypassed, and your analysis "
            "will not be saved to your account history."
        )

    # ========================================================
    # ANALYZE
    # ========================================================

    st.html(
        """
        <div class="analyze-card">

            <h3>
                Ready to Analyze
            </h3>

            <p>
                Start the AI-powered evaluation of your resume.
            </p>

        </div>
        """
    )

    _, mid, _ = st.columns(
        [1, 2, 1]
    )

    with mid:

        analyze = st.button(
            "Analyze Resume",
            use_container_width=True,
            type="primary",
        )

    # ========================================================
    # NOT CLICKED
    # ========================================================

    if not analyze:

        if st.session_state.get(
            "scorer_analysis"
        ):

            st.html(
                """
                <div class="result-header">

                    <h2>
                        Analysis Results
                    </h2>

                    <p>
                        Your latest
                        <span>ATS analysis</span>
                        is displayed below.
                    </p>

                </div>
                """
            )

            display_results_dashboard(
                st.session_state[
                    "scorer_analysis"
                ]
            )

            _render_export_buttons(
                st.session_state[
                    "scorer_analysis"
                ]
            )

        return

    # ========================================================
    # FRESH ANALYSIS
    # ========================================================

    st.session_state.pop(
        "scorer_pdf_bytes",
        None,
    )

    st.session_state.pop(
        "scorer_analysis",
        None,
    )

    # ========================================================
    # JOB DESCRIPTION
    # ========================================================

    job_description = (
        _read_jd(
            jd_file,
            jd_text,
        )
        if analysis_mode
        == "Job Description Comparison"
        else ""
    )

    # ========================================================
    # BACKEND ANALYSIS
    # ========================================================

    try:

        with st.spinner(
            "Analyzing your resume... "
            "This can take 10–30 seconds."
        ):

            # =================================================
            # ORIGINAL BACKEND LOGIC
            # =================================================

            analysis = api_client.analyze_resume(
                resume_file=resume_file,
                access_token=access_token,
                job_description=job_description,
            )

    except requests.RequestException as exc:

        _show_backend_error(exc)

        return

    # ========================================================
    # SAVE RESULT
    # ========================================================

    st.session_state[
        "scorer_analysis"
    ] = analysis

    st.success(
        "Analysis complete!"
    )

    # ========================================================
    # RESULT
    # ========================================================

    st.html(
        """
        <div class="result-header">

            <h2>
                Analysis Complete
            </h2>

            <p>
                Your resume has been evaluated across
                <span>multiple ATS dimensions</span>.
            </p>

        </div>
        """
    )

    display_results_dashboard(
        analysis
    )

    # ========================================================
    # EXPORT
    # ========================================================

    _render_export_buttons(
        analysis
    )
