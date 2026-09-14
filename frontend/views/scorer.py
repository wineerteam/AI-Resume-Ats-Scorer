from typing import Optional

import requests
import streamlit as st

from frontend.services import api_client
from frontend.components.dashboard import display_results_dashboard


# ============================================================
# PAGE STYLING
# ============================================================

def _apply_styles() -> None:
    st.markdown(
        """
        <style>

        /* ====================================================
           GLOBAL
        ==================================================== */

        .block-container {
            max-width: 1200px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }


        /* ====================================================
           MAIN TITLE
        ==================================================== */

        .scorer-hero {
            position: relative;
            overflow: hidden;

            padding: 30px 35px;
            margin-bottom: 25px;

            border-radius: 25px;

            background:
                radial-gradient(
                    circle at 90% 15%,
                    rgba(250, 204, 21, 0.20),
                    transparent 25%
                ),
                radial-gradient(
                    circle at 10% 90%,
                    rgba(236, 72, 153, 0.15),
                    transparent 25%
                ),
                linear-gradient(
                    135deg,
                    #0f172a,
                    #1e3a8a 50%,
                    #2563eb
                );

            border: 1px solid rgba(255,255,255,0.12);

            box-shadow:
                0 20px 50px rgba(15,23,42,0.25);

            transition:
                transform 0.3s ease,
                box-shadow 0.3s ease;
        }


        .scorer-hero:hover {
            transform: translateY(-5px);
            box-shadow:
                0 30px 65px rgba(15,23,42,0.32);
        }


        .scorer-hero h1 {
            color: white;

            font-size: 2.5rem;

            font-weight: 850;

            margin: 0 0 8px 0;
        }


        .scorer-hero p {
            color: #dbeafe;

            font-size: 15px;

            line-height: 1.7;

            margin: 0;
        }


        .hero-highlight {
            color: #facc15;

            font-weight: 800;
        }


        /* ====================================================
           SECTION TITLE
        ==================================================== */

        .section-title {
            margin: 25px 0 15px 0;
        }


        .section-title h2 {
            color: #0f172a;

            font-size: 1.55rem;

            font-weight: 800;

            margin: 0 0 5px 0;
        }


        .section-title p {
            color: #64748b;

            font-size: 13px;

            margin: 0;
        }


        .section-accent {
            width: 65px;

            height: 4px;

            margin-top: 9px;

            border-radius: 20px;

            background:
                linear-gradient(
                    90deg,
                    #2563eb,
                    #06b6d4,
                    #facc15
                );
        }


        /* ====================================================
           ANALYSIS MODE
        ==================================================== */

        div[role="radiogroup"] {
            gap: 12px;
        }


        div[role="radiogroup"] label {
            border: 1px solid #dbe3ef;

            border-radius: 15px;

            padding: 10px 16px;

            background: #ffffff;

            transition:
                transform 0.25s ease,
                box-shadow 0.25s ease,
                border-color 0.25s ease;
        }


        div[role="radiogroup"] label:hover {
            transform: translateY(-3px);

            border-color: #60a5fa;

            box-shadow:
                0 10px 25px rgba(37,99,235,0.12);
        }


        /* ====================================================
           UPLOAD AREA
        ==================================================== */

        .upload-card {
            min-height: 210px;

            padding: 25px;

            border-radius: 22px;

            background:
                linear-gradient(
                    145deg,
                    #ffffff,
                    #f8fafc
                );

            border: 1px solid #e2e8f0;

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

            border-color: #93c5fd;

            box-shadow:
                0 25px 55px rgba(15,23,42,0.15);
        }


        .upload-title {
            color: #0f172a;

            font-size: 19px;

            font-weight: 800;

            margin-bottom: 5px;
        }


        .upload-subtitle {
            color: #64748b;

            font-size: 13px;

            margin-bottom: 15px;
        }


        .upload-accent-blue {
            border-top: 4px solid #2563eb;
        }


        .upload-accent-yellow {
            border-top: 4px solid #facc15;
        }


        /* ====================================================
           STREAMLIT FILE UPLOADER
        ==================================================== */

        [data-testid="stFileUploader"] {
            border-radius: 16px;
        }


        [data-testid="stFileUploaderDropzone"] {
            border: 1.5px dashed #93c5fd !important;

            border-radius: 16px !important;

            background:
                linear-gradient(
                    135deg,
                    #eff6ff,
                    #f0fdfa
                ) !important;

            transition:
                transform 0.25s ease,
                border-color 0.25s ease,
                background 0.25s ease;
        }


        [data-testid="stFileUploaderDropzone"]:hover {
            transform: translateY(-3px);

            border-color: #2563eb !important;

            background:
                linear-gradient(
                    135deg,
                    #dbeafe,
                    #cffafe
                ) !important;
        }


        /* ====================================================
           TEXT AREA
        ==================================================== */

        textarea {
            border-radius: 15px !important;

            border: 1px solid #cbd5e1 !important;

            background: #ffffff !important;

            color: #0f172a !important;

            transition:
                border-color 0.2s ease,
                box-shadow 0.2s ease;
        }


        textarea:focus {
            border-color: #2563eb !important;

            box-shadow:
                0 0 0 3px rgba(37,99,235,0.10) !important;
        }


        /* ====================================================
           BUTTONS
        ==================================================== */

        .stButton > button {
            min-height: 52px;

            border-radius: 15px;

            font-weight: 750;

            transition:
                transform 0.25s ease,
                box-shadow 0.25s ease;
        }


        .stButton > button:hover {
            transform:
                translateY(-4px)
                scale(1.01);

            box-shadow:
                0 15px 35px rgba(37,99,235,0.25);
        }


        .analyze-wrapper {
            padding: 10px 0 5px 0;
        }


        /* ====================================================
           INFO / WARNING / SUCCESS BOXES
        ==================================================== */

        [data-testid="stAlert"] {
            border-radius: 15px !important;

            border-left-width: 4px !important;

            box-shadow:
                0 7px 20px rgba(15,23,42,0.05);
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
            color: #0f172a;
        }


        /* ====================================================
           EXPORT SECTION
        ==================================================== */

        .export-card {
            padding: 23px;

            margin-top: 25px;

            border-radius: 21px;

            background:
                linear-gradient(
                    145deg,
                    #ffffff,
                    #f8fafc
                );

            border: 1px solid #e2e8f0;

            box-shadow:
                0 10px 25px rgba(15,23,42,0.06);
        }


        .export-card h3 {
            color: #0f172a;

            font-size: 18px;

            font-weight: 800;

            margin: 0 0 5px 0;
        }


        .export-card p {
            color: #64748b;

            font-size: 13px;

            margin: 0;
        }


        /* ====================================================
           RESULT HEADER
        ==================================================== */

        .result-header {
            position: relative;

            overflow: hidden;

            margin-top: 25px;

            padding: 25px;

            border-radius: 22px;

            background:
                linear-gradient(
                    135deg,
                    #0f172a,
                    #1e3a8a,
                    #2563eb
                );

            box-shadow:
                0 18px 42px rgba(15,23,42,0.20);
        }


        .result-header h2 {
            color: #ffffff;

            font-size: 1.6rem;

            font-weight: 800;

            margin: 0;
        }


        .result-header p {
            color: #dbeafe;

            font-size: 13px;

            margin: 6px 0 0 0;
        }


        .result-header span {
            color: #facc15;

            font-weight: 800;
        }


        /* ====================================================
           MOBILE
        ==================================================== */

        @media (max-width: 768px) {

            .scorer-hero {
                padding: 25px 20px;
            }

            .scorer-hero h1 {
                font-size: 2rem;
            }

            .upload-card {
                margin-bottom: 18px;
            }

            .section-title h2 {
                font-size: 1.35rem;
            }
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# JD READER
# ============================================================

def _read_jd(jd_file, jd_text: str) -> str:
    """
    Turn whatever the user provided into a plain JD string for the backend.

    For .txt files we decode in-process.
    For PDF/DOCX, ask the user to paste text instead.
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
    """Translate a requests exception into a friendly Streamlit error."""

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

    elif isinstance(exc, requests.HTTPError) and exc.response is not None:

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
# SUMMARY TEXT
# ============================================================

def _summary_text(analysis: dict) -> str:
    """Tiny client-side text summary for the Download button."""

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
    """Two-column upload widgets. Returns (resume_file, jd_file, jd_text)."""

    left, right = st.columns(2)

    # --------------------------------------------------------
    # RESUME
    # --------------------------------------------------------

    with left:

        st.html(
            """
            <div class="upload-card upload-accent-blue">

                <div class="upload-title">
                    Resume Upload
                </div>

                <div class="upload-subtitle">
                    Upload your resume for ATS analysis.
                    Supported formats: PDF, DOC, DOCX.
                </div>

            </div>
            """
        )

        resume_file = st.file_uploader(
            "Choose your resume file",
            type=["pdf", "doc", "docx"],
            help="Supported: PDF, DOC, DOCX (max 5 MB)",
            key="resume_upload",
        )

        if resume_file:

            st.success(
                f"{resume_file.name} "
                f"({resume_file.size / 1024:.1f} KB)"
            )

    # --------------------------------------------------------
    # JOB DESCRIPTION
    # --------------------------------------------------------

    jd_file: Optional[object] = None
    jd_text = ""

    with right:

        if analysis_mode == "Job Description Comparison":

            st.html(
                """
                <div class="upload-card upload-accent-yellow">

                    <div class="upload-title">
                        Job Description
                    </div>

                    <div class="upload-subtitle">
                        Add the job description to compare
                        your resume against the target role.
                    </div>

                </div>
                """
            )

            jd_method = st.radio(
                "Input method:",
                ["Paste Text", "Upload .txt File"],
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
                        f"{jd_file.name}"
                    )

            else:

                jd_text = st.text_area(
                    "Paste job description text:",
                    height=200,
                    placeholder=(
                        "Paste the complete job description here..."
                    ),
                    key="jd_text",
                )

                if jd_text:

                    st.success(
                        f"{len(jd_text)} characters"
                    )

        else:

            st.html(
                """
                <div class="upload-card upload-accent-yellow">

                    <div class="upload-title">
                        Job Description
                    </div>

                    <div class="upload-subtitle">
                        Optional JD matching is currently disabled.
                        Switch to Job Description Comparison
                        to enable targeted analysis.
                    </div>

                </div>
                """
            )

            st.info(
                "Switch to 'Job Description Comparison' "
                "mode to enable JD matching."
            )

    return resume_file, jd_file, jd_text


# ============================================================
# EXPORT BUTTONS
# ============================================================

def _render_export_buttons(analysis: dict) -> None:

    st.html(
        """
        <div class="export-card">

            <h3>
                Export Results
            </h3>

            <p>
                Save your ATS analysis for later reference.
            </p>

        </div>
        """
    )

    c1, c2 = st.columns(2)

    # --------------------------------------------------------
    # PDF
    # --------------------------------------------------------

    with c1:

        # Existing backend logic preserved.
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

        if "scorer_pdf_bytes" in st.session_state:

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

    # --------------------------------------------------------
    # TXT SUMMARY
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # APPLY GUI
    # --------------------------------------------------------

    _apply_styles()

    # --------------------------------------------------------
    # HERO
    # --------------------------------------------------------

    st.html(
        """
        <div class="scorer-hero">

            <h1>
                ATS Resume Scorer
            </h1>

            <p>
                Upload your resume and get a
                <span class="hero-highlight">
                    comprehensive ATS analysis
                </span>
                with actionable feedback.
            </p>

        </div>
        """
    )

    # --------------------------------------------------------
    # SIDEBAR
    # --------------------------------------------------------

    with st.sidebar:

        st.markdown("---")

        st.markdown("## Analysis Options")

        st.info(
            "**General ATS Score**: resume only — "
            "overall compatibility.\n\n"
            "**JD Comparison**: resume + job description — "
            "targeted match analysis."
        )

    st.markdown("---")

    # --------------------------------------------------------
    # ANALYSIS MODE
    # --------------------------------------------------------

    st.html(
        """
        <div class="section-title">

            <h2>
                Select Analysis Mode
            </h2>

            <p>
                Choose how you want your resume to be evaluated.
            </p>

            <div class="section-accent"></div>

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

    # --------------------------------------------------------
    # UPLOAD AREA
    # --------------------------------------------------------

    st.html(
        """
        <div class="section-title">

            <h2>
                Upload Your Documents
            </h2>

            <p>
                Provide your resume and optionally a job description.
            </p>

            <div class="section-accent"></div>

        </div>
        """
    )

    resume_file, jd_file, jd_text = _render_upload_area(
        analysis_mode
    )

    st.markdown("---")

    # --------------------------------------------------------
    # NO RESUME
    # --------------------------------------------------------

    if not resume_file:

        st.info(
            "Upload your resume to begin."
        )

        # Existing logic preserved.
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
                        are shown below.
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

    # --------------------------------------------------------
    # ACCESS TOKEN
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # ANALYZE BUTTON
    # --------------------------------------------------------

    st.html(
        """
        <div class="section-title">

            <h2>
                Ready to Analyze
            </h2>

            <p>
                Start the AI-powered resume evaluation.
            </p>

        </div>
        """
    )

    _, mid, _ = st.columns([1, 2, 1])

    with mid:

        analyze = st.button(
            "Analyze Resume",
            use_container_width=True,
            type="primary",
        )

    # --------------------------------------------------------
    # BUTTON NOT CLICKED
    # --------------------------------------------------------

    if not analyze:

        # Existing logic preserved.
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

    # --------------------------------------------------------
    # FRESH ANALYSIS
    # --------------------------------------------------------

    st.session_state.pop(
        "scorer_pdf_bytes",
        None,
    )

    st.session_state.pop(
        "scorer_analysis",
        None,
    )

    # --------------------------------------------------------
    # JOB DESCRIPTION
    # --------------------------------------------------------

    job_description = (
        _read_jd(
            jd_file,
            jd_text,
        )
        if analysis_mode == "Job Description Comparison"
        else ""
    )

    # --------------------------------------------------------
    # BACKEND ANALYSIS
    # --------------------------------------------------------

    try:

        with st.spinner(
            "Analyzing your resume... "
            "This can take 10–30 seconds."
        ):

            # =================================================
            # EXISTING API LOGIC — PRESERVED
            # =================================================

            analysis = api_client.analyze_resume(
                resume_file=resume_file,
                access_token=access_token,
                job_description=job_description,
            )

    except requests.RequestException as exc:

        _show_backend_error(exc)

        return

    # --------------------------------------------------------
    # STORE RESULT
    # --------------------------------------------------------

    st.session_state[
        "scorer_analysis"
    ] = analysis

    st.success(
        "Analysis complete!"
    )

    # --------------------------------------------------------
    # RESULT
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # EXPORT
    # --------------------------------------------------------

    _render_export_buttons(
        analysis
    )
