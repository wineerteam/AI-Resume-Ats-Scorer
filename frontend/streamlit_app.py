import streamlit as st
import sys
from pathlib import Path


# ------------------------------------------------------------
# REPO ROOT
# ------------------------------------------------------------

sys.path.insert(
    0,
    str(Path(__file__).parent.parent)
)


# ------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------

st.set_page_config(
    page_title="ATS Resume Scorer",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ------------------------------------------------------------
# YOUR AUTH SESSION STATE
# ------------------------------------------------------------

for key, default in [
    ("access_token", None),
    ("refresh_token", None),
    ("user_id", None),
    ("user_email", None),
    ("auth_error", None),
    ("auth_info", None),
]:
    if key not in st.session_state:
        st.session_state[key] = default


# ------------------------------------------------------------
# YOUR GOOGLE OAUTH CODE
# ------------------------------------------------------------

# ... your existing OAuth code ...


# ------------------------------------------------------------
# LOAD CUSTOM CSS
# ------------------------------------------------------------

def load_css():

    try:

        css_path = (
            Path(__file__).parent
            / "assets"
            / "styles.css"
        )

        with open(
            css_path,
            "r",
            encoding="utf-8"
        ) as f:

            return f"<style>{f.read()}</style>"

    except FileNotFoundError:

        return ""


st.markdown(
    load_css(),
    unsafe_allow_html=True
)


# ============================================================
# PREMIUM NAVIGATION CSS
# ============================================================

st.markdown(
    """
    <style>

    [data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #07152f 0%,
                #091d3d 50%,
                #07152f 100%
            );

        border-right:
            1px solid
            rgba(37,99,235,.25);

        box-shadow:
            10px 0 40px
            rgba(3,15,35,.18);
    }


    [data-testid="stSidebar"] .stButton {
        margin-bottom: 10px;
    }


    [data-testid="stSidebar"] .stButton > button {

        min-height: 50px;

        border-radius: 15px;

        border:
            1px solid
            rgba(148,163,184,.15);

        background:
            linear-gradient(
                135deg,
                rgba(255,255,255,.07),
                rgba(255,255,255,.025)
            );

        color: #cbd5e1;

        font-size: 12px;

        font-weight: 850;

        text-align: left;

        padding: 0 16px;

        box-shadow:
            0 7px 0
            rgba(3,12,30,.35),

            0 10px 25px
            rgba(0,0,0,.12);

        transition:
            all .22s cubic-bezier(.2,.8,.2,1);

        position: relative;

        overflow: hidden;
    }


    /* LEFT MULTICOLOR BAR */

    [data-testid="stSidebar"] .stButton > button::before {

        content: "";

        position: absolute;

        left: 0;
        top: 0;

        width: 4px;
        height: 100%;

        border-radius:
            15px 0 0 15px;

        background:
            linear-gradient(
                180deg,
                #06b6d4,
                #2563eb,
                #ec4899,
                #f97316,
                #facc15
            );

        transition:
            width .22s ease;
    }


    /* SHINE */

    [data-testid="stSidebar"] .stButton > button::after {

        content: "";

        position: absolute;

        width: 90px;
        height: 160%;

        left: -120px;
        top: -30%;

        transform:
            rotate(20deg);

        background:
            linear-gradient(
                90deg,
                transparent,
                rgba(255,255,255,.20),
                transparent
            );

        transition:
            left .45s ease;
    }


    /* HOVER */

    [data-testid="stSidebar"] .stButton > button:hover {

        transform:
            translateX(7px)
            translateY(-4px)
            scale(1.035);

        color: #ffffff;

        background:
            linear-gradient(
                135deg,
                rgba(6,182,212,.18),
                rgba(37,99,235,.20),
                rgba(236,72,153,.14)
            );

        border-color:
            rgba(96,165,250,.48);

        box-shadow:

            0 8px 0
            rgba(3,12,30,.42),

            0 16px 30px
            rgba(37,99,235,.18),

            0 0 25px
            rgba(6,182,212,.10);
    }


    [data-testid="stSidebar"] .stButton > button:hover::before {

        width: 7px;
    }


    [data-testid="stSidebar"] .stButton > button:hover::after {

        left: 130%;
    }


    /* CLICK */

    [data-testid="stSidebar"] .stButton > button:active {

        transform:
            translateX(5px)
            translateY(3px)
            scale(.985);

        box-shadow:
            0 2px 0
            rgba(3,12,30,.5),

            0 5px 12px
            rgba(0,0,0,.2);
    }


    /* BRAND */

    .nav-brand {
        padding:
            8px 10px 20px 10px;

        margin-bottom: 8px;
    }


    .nav-brand-title {

        font-size: 23px;

        font-weight: 950;

        color: #ffffff;

        letter-spacing: -1px;
    }


    .nav-brand-title span {

        background:
            linear-gradient(
                90deg,
                #06b6d4,
                #2563eb,
                #ec4899,
                #facc15
            );

        -webkit-background-clip: text;

        -webkit-text-fill-color: transparent;

        background-clip: text;
    }


    .nav-brand-subtitle {

        color: #94a3b8;

        font-size: 8px;

        font-weight: 800;

        letter-spacing: 1.5px;

        margin-top: 6px;

        text-transform: uppercase;
    }


    .nav-section-label {

        color: #64748b;

        font-size: 8px;

        font-weight: 900;

        letter-spacing: 2px;

        text-transform: uppercase;

        margin:
            5px 0 10px 8px;
    }


    .nav-divider {

        height: 1px;

        margin:
            18px 5px;

        background:
            linear-gradient(
                90deg,
                transparent,
                rgba(148,163,184,.28),
                transparent
            );
    }


    .account-title {

        color: #ffffff;

        font-size: 13px;

        font-weight: 900;

        margin-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)
