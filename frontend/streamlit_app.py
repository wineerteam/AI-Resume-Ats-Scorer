import streamlit as st
import sys
from pathlib import Path


# ============================================================
# REPO PATH
# ============================================================

sys.path.insert(
    0,
    str(Path(__file__).parent.parent)
)


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="ATS Resume Scorer",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# AUTH SESSION STATE
# ============================================================

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


# ============================================================
# GOOGLE OAUTH CALLBACK
# ============================================================

if (
    not st.session_state.access_token
    and "code" in st.query_params
):

    from frontend.services import supabase_client

    result = supabase_client.exchange_code_for_session(
        st.query_params["code"]
    )

    st.query_params.clear()

    if "error" in result:

        st.session_state.auth_error = (
            f"Google sign-in failed: {result['error']}"
        )

    else:

        st.session_state.access_token = result["access_token"]
        st.session_state.refresh_token = result["refresh_token"]
        st.session_state.user_id = result["user_id"]
        st.session_state.user_email = result["email"]

        st.rerun()


# ============================================================
# LOAD CUSTOM CSS
# ============================================================

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
# PREMIUM SIDEBAR / NAVIGATION STYLE
# ============================================================

st.markdown(
    """
<style>

/* ============================================================
   SIDEBAR
   ============================================================ */

[data-testid="stSidebar"] {

    background:
        linear-gradient(
            180deg,
            #f7f4ee 0%,
            #f3f0e9 50%,
            #eeeae2 100%
        ) !important;

    border-right:
        1px solid
        rgba(120, 100, 80, 0.16) !important;

    box-shadow:
        8px 0 30px
        rgba(60, 45, 30, 0.08) !important;
}


/* ============================================================
   SIDEBAR CONTENT
   ============================================================ */

[data-testid="stSidebar"] > div:first-child {

    padding-top: 0.55rem !important;

    padding-left: 0.65rem !important;

    padding-right: 0.65rem !important;
}


/* ============================================================
   NAVIGATION TITLE
   ============================================================ */

[data-testid="stSidebar"] h2 {

    margin-top: 5px !important;

    margin-bottom: 18px !important;

    padding-left: 4px !important;

    font-size: 24px !important;

    line-height: 1.1 !important;

    font-weight: 950 !important;

    letter-spacing: -0.8px !important;

    background:
        linear-gradient(
            90deg,
            #eab308 0%,
            #f59e0b 25%,
            #ec4899 62%,
            #ef4444 100%
        );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;

    background-clip: text;
}


/* ============================================================
   NAVIGATION BUTTON WRAPPER
   ============================================================ */

[data-testid="stSidebar"] .stButton {

    margin-bottom: 11px !important;

    position: relative !important;

    z-index: 2 !important;
}


/* ============================================================
   MAIN NAVIGATION BUTTON
   ============================================================ */

[data-testid="stSidebar"] .stButton > button {

    position: relative !important;

    width: 100% !important;

    min-height: 54px !important;

    border-radius: 16px !important;

    border:
        1px solid
        rgba(180, 130, 20, 0.28) !important;

    background:
        linear-gradient(
            135deg,
            #fff8c7 0%,
            #facc15 42%,
            #f8b90b 100%
        ) !important;

    color: #342b16 !important;

    font-size: 13px !important;

    font-weight: 850 !important;

    letter-spacing: 0.1px !important;

    text-align: left !important;

    padding-left: 20px !important;

    overflow: hidden !important;

    box-shadow:
        0 7px 0 #d69e00,
        0 11px 22px
        rgba(170, 125, 0, 0.18) !important;

    transform:
        translateY(0)
        scale(1) !important;

    transition:
        transform 0.24s cubic-bezier(.2,.8,.2,1),
        box-shadow 0.24s ease,
        background 0.24s ease,
        border-color 0.24s ease,
        color 0.24s ease !important;
}


/* ============================================================
   MULTICOLOR LEFT STRIPE
   ============================================================ */

[data-testid="stSidebar"] .stButton > button::before {

    content: "";

    position: absolute;

    left: 0;

    top: 0;

    width: 5px;

    height: 100%;

    border-radius:
        16px 0 0 16px;

    background:
        linear-gradient(
            180deg,
            #facc15 0%,
            #f59e0b 22%,
            #ec4899 55%,
            #ef4444 78%,
            #dc2626 100%
        );

    box-shadow:
        2px 0 8px
        rgba(236, 72, 153, 0.18);

    transition:
        width 0.24s ease,
        box-shadow 0.24s ease;
}


/* ============================================================
   MOVING SHINE
   ============================================================ */

[data-testid="stSidebar"] .stButton > button::after {

    content: "";

    position: absolute;

    top: -50%;

    left: -130px;

    width: 75px;

    height: 200%;

    transform:
        rotate(20deg);

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(255,255,255,0.70),
            transparent
        );

    transition:
        left 0.58s ease;
}


/* ============================================================
   HOVER
   ZOOM + 3D LIFT + GLOW
   ============================================================ */

[data-testid="stSidebar"] .stButton > button:hover {

    transform:
        translateX(8px)
        translateY(-5px)
        scale(1.045) !important;

    color: #241b05 !important;

    border-color:
        rgba(236, 72, 153, 0.58) !important;

    background:
        linear-gradient(
            110deg,
            #ffe76b 0%,
            #facc15 32%,
            #f59e0b 55%,
            #f472b6 78%,
            #ef4444 100%
        ) !important;

    box-shadow:

        0 9px 0 #c98f00,

        0 17px 32px
        rgba(234, 179, 8, 0.25),

        0 0 28px
        rgba(236, 72, 153, 0.20),

        0 0 45px
        rgba(239, 68, 68, 0.10) !important;
}


/* ============================================================
   HOVER LEFT STRIPE
   ============================================================ */

[data-testid="stSidebar"] .stButton > button:hover::before {

    width: 8px;

    box-shadow:
        0 0 12px
        rgba(236, 72, 153, 0.55),

        0 0 18px
        rgba(239, 68, 68, 0.35);
}


/* ============================================================
   HOVER SHINE
   ============================================================ */

[data-testid="stSidebar"] .stButton > button:hover::after {

    left: 135%;
}


/* ============================================================
   CLICK / PRESS EFFECT
   ============================================================ */

[data-testid="stSidebar"] .stButton > button:active {

    transform:
        translateX(6px)
        translateY(4px)
        scale(0.985) !important;

    box-shadow:
        0 2px 0 #b37e00,

        0 5px 12px
        rgba(100, 70, 0, 0.18) !important;
}


/* ============================================================
   FOCUS
   ============================================================ */

[data-testid="stSidebar"] .stButton > button:focus {

    outline: none !important;

    border-color:
        #ec4899 !important;

    box-shadow:

        0 0 0 3px
        rgba(236, 72, 153, 0.13),

        0 8px 0 #d69e00,

        0 12px 25px
        rgba(234, 179, 8, 0.18) !important;
}


/* ============================================================
   DIVIDER
   ============================================================ */

[data-testid="stSidebar"] hr {

    margin:
        20px 5px 18px 5px !important;

    border: none !important;

    height: 2px !important;

    background:
        linear-gradient(
            90deg,
            transparent,
            #facc15,
            #ec4899,
            #ef4444,
            transparent
        ) !important;

    opacity: 0.55;
}


/* ============================================================
   ACCOUNT HEADING
   ============================================================ */

[data-testid="stSidebar"] h3 {

    color: #24201a !important;

    font-size: 15px !important;

    font-weight: 900 !important;

    letter-spacing: -0.2px !important;

    margin-bottom: 8px !important;
}


/* ============================================================
   SIDEBAR NORMAL TEXT
   ============================================================ */

[data-testid="stSidebar"] p {

    color: #514a40 !important;
}


/* ============================================================
   CAPTION
   ============================================================ */

[data-testid="stSidebar"]
[data-testid="stCaptionContainer"] {

    color: #756d62 !important;

    font-size: 10px !important;
}


/* ============================================================
   EMAIL LINK
   ============================================================ */

[data-testid="stSidebar"] a {

    color: #b45309 !important;

    font-weight: 700;
}


/* ============================================================
   INPUT BOX
   ============================================================ */

[data-testid="stSidebar"] input {

    background:
        rgba(255,255,255,0.80) !important;

    color: #29231b !important;

    border:
        1px solid
        rgba(120, 90, 40, 0.22) !important;

    border-radius: 12px !important;

    transition:
        border-color 0.20s ease,
        box-shadow 0.20s ease,
        transform 0.20s ease !important;
}


[data-testid="stSidebar"] input:focus {

    border-color:
        #ec4899 !important;

    box-shadow:
        0 0 0 2px
        rgba(236,72,153,0.12) !important;

    transform:
        translateY(-1px);
}


/* ============================================================
   SIGN IN / SIGN UP TABS
   ============================================================ */

[data-testid="stSidebar"]
[data-baseweb="tab-list"] {

    gap: 3px;

    padding: 4px;

    border-radius: 12px;

    background:
        rgba(255,255,255,0.60);
}


[data-testid="stSidebar"]
[data-baseweb="tab"] {

    color: #6b6256 !important;

    font-size: 10px;

    font-weight: 850;
}


[data-testid="stSidebar"]
[aria-selected="true"] {

    color: #b45309 !important;
}


/* ============================================================
   FORM BUTTON
   ============================================================ */

[data-testid="stSidebar"]
.stFormSubmitButton > button {

    min-height: 44px !important;

    border-radius: 12px !important;

    border:
        1px solid
        rgba(234,179,8,0.35) !important;

    background:
        linear-gradient(
            135deg,
            #facc15,
            #f59e0b,
            #ec4899
        ) !important;

    color: #ffffff !important;

    font-weight: 850 !important;

    box-shadow:
        0 5px 0 #d97706,

        0 9px 18px
        rgba(234,179,8,0.16) !important;

    transition:
        transform 0.20s ease,
        box-shadow 0.20s ease !important;
}


[data-testid="stSidebar"]
.stFormSubmitButton > button:hover {

    transform:
        translateY(-3px)
        scale(1.025) !important;

    box-shadow:
        0 7px 0 #c2410c,

        0 14px 24px
        rgba(236,72,153,0.20) !important;
}


/* ============================================================
   GOOGLE BUTTON
   ============================================================ */

[data-testid="stSidebar"]
.stLinkButton > a {

    min-height: 45px !important;

    border-radius: 13px !important;

    background:
        #fffdf7 !important;

    border:
        1px solid
        rgba(120,90,40,0.20) !important;

    color: #342b16 !important;

    font-size: 11px !important;

    font-weight: 850 !important;

    box-shadow:
        0 5px 0
        rgba(160,120,30,0.15) !important;

    transition:
        transform 0.22s ease,
        box-shadow 0.22s ease,
        border-color 0.22s ease !important;
}


[data-testid="stSidebar"]
.stLinkButton > a:hover {

    transform:
        translateY(-3px)
        scale(1.025) !important;

    border-color:
        #ec4899 !important;

    box-shadow:
        0 8px 0
        rgba(190,120,20,0.18),

        0 15px 25px
        rgba(236,72,153,0.12) !important;
}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 768px) {

    [data-testid="stSidebar"]
    .stButton > button {

        min-height: 48px !important;

        font-size: 12px !important;
    }

    [data-testid="stSidebar"] h2 {

        font-size: 21px !important;
    }
}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# VIEW STATE
# ============================================================

if "current_view" not in st.session_state:

    st.session_state.current_view = "landing"


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

with st.sidebar:

    st.markdown("## Navigation")


    # ========================================================
    # HOME
    # ========================================================

    if st.button(
        "Home",
        use_container_width=True
    ):

        st.session_state.current_view = "landing"

        st.rerun()


    # ========================================================
    # ATS SCORER
    # ========================================================

    if st.button(
        "ATS Scorer",
        use_container_width=True
    ):

        st.session_state.current_view = "scorer"

        st.rerun()


    # ========================================================
    # HISTORY
    # ========================================================

    if st.button(
        "History",
        use_container_width=True
    ):

        st.session_state.current_view = "history"

        st.rerun()


    # ========================================================
    # RESOURCES
    # ========================================================

    if st.button(
        "Resources",
        use_container_width=True
    ):

        st.session_state.current_view = "resources"

        st.rerun()


    # ========================================================
    # DIVIDER
    # ========================================================

    st.markdown("---")


    # ========================================================
    # ACCOUNT
    # ========================================================

    st.markdown("### Account")


    from frontend.services import supabase_client


    # ========================================================
    # SIGNED IN
    # ========================================================

    if st.session_state.access_token:

        st.caption(
            f"Signed in as **{st.session_state.user_email}**"
        )


        if st.button(
            "Sign out",
            use_container_width=True
        ):

            supabase_client.sign_out()


            for key in (
                "access_token",
                "refresh_token",
                "user_id",
                "user_email"
            ):

                st.session_state[key] = None


            st.rerun()


    # ========================================================
    # SIGNED OUT
    # ========================================================

    else:

        # ----------------------------------------------------
        # AUTH ERROR
        # ----------------------------------------------------

        if st.session_state.auth_error:

            st.error(
                st.session_state.auth_error
            )

            st.session_state.auth_error = None


        # ----------------------------------------------------
        # AUTH INFO
        # ----------------------------------------------------

        if st.session_state.auth_info:

            st.info(
                st.session_state.auth_info
            )

            st.session_state.auth_info = None


        # ----------------------------------------------------
        # AUTH TABS
        # ----------------------------------------------------

        tab_in, tab_up = st.tabs(
            [
                "Sign in",
                "Sign up"
            ]
        )


        # ====================================================
        # SIGN IN
        # ====================================================

        with tab_in:

            with st.form(
                "signin_form",
                clear_on_submit=False
            ):

                email = st.text_input(
                    "Email",
                    key="signin_email"
                )

                password = st.text_input(
                    "Password",
                    type="password",
                    key="signin_pw"
                )

                submitted = st.form_submit_button(
                    "Sign in",
                    use_container_width=True
                )


            if submitted:

                result = (
                    supabase_client
                    .sign_in_with_password(
                        email,
                        password
                    )
                )


                if "error" in result:

                    st.session_state.auth_error = (
                        result["error"]
                    )

                else:

                    st.session_state.access_token = (
                        result["access_token"]
                    )

                    st.session_state.refresh_token = (
                        result["refresh_token"]
                    )

                    st.session_state.user_id = (
                        result["user_id"]
                    )

                    st.session_state.user_email = (
                        result["email"]
                    )


                st.rerun()


        # ====================================================
        # SIGN UP
        # ====================================================

        with tab_up:

            with st.form(
                "signup_form",
                clear_on_submit=False
            ):

                email_up = st.text_input(
                    "Email",
                    key="signup_email"
                )

                password_up = st.text_input(
                    "Password (min 6 chars)",
                    type="password",
                    key="signup_pw"
                )

                submitted_up = (
                    st.form_submit_button(
                        "Create account",
                        use_container_width=True
                    )
                )


            if submitted_up:

                result = (
                    supabase_client
                    .sign_up_with_password(
                        email_up,
                        password_up
                    )
                )


                if "error" in result:

                    st.session_state.auth_error = (
                        result["error"]
                    )


                elif result.get(
                    "pending_confirmation"
                ):

                    st.session_state.auth_info = (
                        f"Check your inbox — "
                        f"confirmation email sent to "
                        f"{result['email']}."
                    )


                else:

                    st.session_state.access_token = (
                        result["access_token"]
                    )

                    st.session_state.refresh_token = (
                        result["refresh_token"]
                    )

                    st.session_state.user_id = (
                        result["user_id"]
                    )

                    st.session_state.user_email = (
                        result["email"]
                    )


                st.rerun()


        # ====================================================
        # GOOGLE OAUTH
        # ====================================================

        st.markdown(
            """
            <div style="
                text-align:center;
                margin:10px 0;
                color:#8a8175;
                font-size:11px;
                font-weight:700;
                letter-spacing:1px;
            ">
                OR
            </div>
            """,
            unsafe_allow_html=True
        )


        oauth = (
            supabase_client
            .google_oauth_url()
        )


        if "error" in oauth:

            st.caption(
                f"Google sign-in unavailable: "
                f"{oauth['error']}"
            )

        else:

            st.link_button(
                "Continue with Google",
                url=oauth["url"],
                use_container_width=True
            )


# ============================================================
# MAIN CONTENT
# ============================================================

if st.session_state.current_view == "landing":

    from frontend.views import landing

    landing.render()


elif st.session_state.current_view == "scorer":

    from frontend.views import scorer

    scorer.render()


elif st.session_state.current_view == "history":

    from frontend.views import history

    history.render()


elif st.session_state.current_view == "resources":

    from frontend.views import resources

    resources.render()
