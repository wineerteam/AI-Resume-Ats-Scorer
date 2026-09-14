import streamlit as st
import sys
from pathlib import Path


# ============================================================
# REPO PATH
# ============================================================

# Put the repo root on sys.path so frontend imports work
# regardless of the directory Streamlit was launched from.

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

    # Clear OAuth code after processing
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
# PREMIUM NAVIGATION STYLE
# ============================================================

st.markdown(
    """
<style>

/* =========================================================
   SIDEBAR BASE
   ========================================================= */

[data-testid="stSidebar"] {

    background:
        linear-gradient(
            180deg,
            #07152f 0%,
            #0a1f42 45%,
            #07152f 100%
        ) !important;

    border-right:
        1px solid
        rgba(37, 99, 235, 0.30);

    box-shadow:
        10px 0 35px
        rgba(2, 12, 30, 0.25);
}


/* =========================================================
   SIDEBAR CONTENT
   ========================================================= */

[data-testid="stSidebar"] > div:first-child {

    padding-top: 1.2rem;
}


/* =========================================================
   NAVIGATION HEADING
   ========================================================= */

[data-testid="stSidebar"] h2 {

    font-size: 21px !important;

    font-weight: 900 !important;

    letter-spacing: -0.5px;

    margin-bottom: 20px !important;

    background:
        linear-gradient(
            90deg,
            #06b6d4 0%,
            #2563eb 35%,
            #ec4899 70%,
            #facc15 100%
        );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;

    background-clip: text;
}


/* =========================================================
   NAVIGATION BUTTON WRAPPER
   ========================================================= */

[data-testid="stSidebar"] .stButton {

    margin-bottom: 11px;

    position: relative;
}


/* =========================================================
   MAIN NAV BUTTON
   ========================================================= */

[data-testid="stSidebar"] .stButton > button {

    position: relative;

    min-height: 52px;

    border-radius: 15px;

    border:
        1px solid
        rgba(148, 163, 184, 0.16);

    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,0.075),
            rgba(255,255,255,0.025)
        );

    color: #cbd5e1;

    font-size: 13px;

    font-weight: 850;

    letter-spacing: 0.2px;

    text-align: left;

    padding-left: 18px;

    overflow: hidden;

    box-shadow:
        0 7px 0
        rgba(2, 12, 30, 0.42),

        0 10px 22px
        rgba(0, 0, 0, 0.12);

    transition:
        transform 0.23s cubic-bezier(.2,.8,.2,1),
        background 0.23s ease,
        border-color 0.23s ease,
        box-shadow 0.23s ease,
        color 0.23s ease;
}


/* =========================================================
   MULTICOLOR LEFT EDGE
   ========================================================= */

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

    opacity: 0.85;

    transition:
        width 0.23s ease,
        opacity 0.23s ease;
}


/* =========================================================
   SHINE EFFECT
   ========================================================= */

[data-testid="stSidebar"] .stButton > button::after {

    content: "";

    position: absolute;

    top: -35%;

    left: -140px;

    width: 80px;

    height: 170%;

    transform: rotate(20deg);

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(255,255,255,0.24),
            transparent
        );

    transition:
        left 0.55s ease;
}


/* =========================================================
   HOVER = 3D + ZOOM + LIFT
   ========================================================= */

[data-testid="stSidebar"] .stButton > button:hover {

    transform:
        translateX(8px)
        translateY(-4px)
        scale(1.035);

    color: #ffffff;

    border-color:
        rgba(96, 165, 250, 0.55);

    background:
        linear-gradient(
            135deg,
            rgba(6,182,212,0.18),
            rgba(37,99,235,0.22),
            rgba(236,72,153,0.16)
        );

    box-shadow:

        0 8px 0
        rgba(2,12,30,0.48),

        0 17px 30px
        rgba(37,99,235,0.20),

        0 0 28px
        rgba(6,182,212,0.13);
}


/* =========================================================
   HOVER LEFT BAR
   ========================================================= */

[data-testid="stSidebar"] .stButton > button:hover::before {

    width: 7px;

    opacity: 1;
}


/* =========================================================
   HOVER SHINE
   ========================================================= */

[data-testid="stSidebar"] .stButton > button:hover::after {

    left: 135%;
}


/* =========================================================
   CLICK / PRESS EFFECT
   ========================================================= */

[data-testid="stSidebar"] .stButton > button:active {

    transform:
        translateX(6px)
        translateY(4px)
        scale(0.985);

    box-shadow:

        0 2px 0
        rgba(2,12,30,0.55),

        0 5px 12px
        rgba(0,0,0,0.25);
}


/* =========================================================
   FOCUS
   ========================================================= */

[data-testid="stSidebar"] .stButton > button:focus {

    outline: none;

    border-color:
        rgba(6,182,212,0.55);

    box-shadow:

        0 0 0 2px
        rgba(6,182,212,0.10),

        0 12px 28px
        rgba(37,99,235,0.16);
}


/* =========================================================
   HORIZONTAL DIVIDER
   ========================================================= */

[data-testid="stSidebar"] hr {

    margin:
        20px 4px;

    border: none;

    height: 1px;

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(148,163,184,0.30),
            transparent
        );
}


/* =========================================================
   ACCOUNT HEADING
   ========================================================= */

[data-testid="stSidebar"] h3 {

    color: #ffffff !important;

    font-size: 14px !important;

    font-weight: 850 !important;

    letter-spacing: 0.3px;
}


/* =========================================================
   SIDEBAR TEXT
   ========================================================= */

[data-testid="stSidebar"] p {

    color: #cbd5e1;
}


/* =========================================================
   CAPTION
   ========================================================= */

[data-testid="stSidebar"] [data-testid="stCaptionContainer"] {

    color: #94a3b8;

    font-size: 10px;
}


/* =========================================================
   INPUT FIELDS
   ========================================================= */

[data-testid="stSidebar"] input {

    background:
        rgba(255,255,255,0.045) !important;

    color: #ffffff !important;

    border:
        1px solid
        rgba(148,163,184,0.18) !important;

    border-radius: 11px !important;

    transition:
        border-color 0.2s ease,
        box-shadow 0.2s ease;
}


[data-testid="stSidebar"] input:focus {

    border-color:
        #06b6d4 !important;

    box-shadow:
        0 0 0 1px
        rgba(6,182,212,0.20) !important;
}


/* =========================================================
   SIGN IN / SIGN UP TABS
   ========================================================= */

[data-testid="stSidebar"] [data-baseweb="tab-list"] {

    gap: 3px;

    padding: 3px;

    border-radius: 11px;

    background:
        rgba(255,255,255,0.035);
}


[data-testid="stSidebar"] [data-baseweb="tab"] {

    color: #94a3b8;

    font-size: 10px;

    font-weight: 800;
}


[data-testid="stSidebar"] [aria-selected="true"] {

    color: #ffffff !important;
}


/* =========================================================
   FORM BUTTON
   ========================================================= */

[data-testid="stSidebar"] .stFormSubmitButton > button {

    border-radius: 12px;

    min-height: 43px;

    font-weight: 850;

    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease;
}


[data-testid="stSidebar"] .stFormSubmitButton > button:hover {

    transform:
        translateY(-2px);

    box-shadow:
        0 10px 22px
        rgba(37,99,235,0.22);
}


/* =========================================================
   GOOGLE BUTTON
   ========================================================= */

[data-testid="stSidebar"] .stLinkButton > a {

    min-height: 44px;

    border-radius: 12px;

    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,0.075),
            rgba(255,255,255,0.025)
        );

    border:
        1px solid
        rgba(148,163,184,0.18);

    color: #ffffff;

    font-size: 11px;

    font-weight: 850;

    transition:
        transform 0.22s ease,
        box-shadow 0.22s ease,
        border-color 0.22s ease;
}


[data-testid="stSidebar"] .stLinkButton > a:hover {

    transform:
        translateY(-3px)
        scale(1.02);

    border-color:
        rgba(236,72,153,0.42);

    box-shadow:
        0 12px 25px
        rgba(37,99,235,0.16);
}


/* =========================================================
   RESPONSIVE
   ========================================================= */

@media (max-width: 768px) {

    [data-testid="stSidebar"] .stButton > button {

        min-height: 47px;

        font-size: 11px;
    }

    [data-testid="stSidebar"] h2 {

        font-size: 19px !important;
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
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## Navigation")


    if st.button(
        "Home",
        use_container_width=True
    ):

        st.session_state.current_view = "landing"

        st.rerun()


    if st.button(
        "ATS Scorer",
        use_container_width=True
    ):

        st.session_state.current_view = "scorer"

        st.rerun()


    if st.button(
        "History",
        use_container_width=True
    ):

        st.session_state.current_view = "history"

        st.rerun()


    if st.button(
        "Resources",
        use_container_width=True
    ):

        st.session_state.current_view = "resources"

        st.rerun()


    st.markdown("---")


    st.markdown("### Account")


    # --------------------------------------------------------
    # SUPABASE CLIENT
    # --------------------------------------------------------

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
                "user_email",
            ):

                st.session_state[key] = None


            st.rerun()


    # ========================================================
    # SIGNED OUT
    # ========================================================

    else:

        if st.session_state.auth_error:

            st.error(
                st.session_state.auth_error
            )

            st.session_state.auth_error = None


        if st.session_state.auth_info:

            st.info(
                st.session_state.auth_info
            )

            st.session_state.auth_info = None


        tab_in, tab_up = st.tabs(
            [
                "Sign in",
                "Sign up"
            ]
        )


        # ----------------------------------------------------
        # SIGN IN
        # ----------------------------------------------------

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


        # ----------------------------------------------------
        # SIGN UP
        # ----------------------------------------------------

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


        # ----------------------------------------------------
        # GOOGLE LOGIN
        # ----------------------------------------------------

        st.markdown(
            """
            <div style="
                text-align:center;
                margin:10px 0;
                color:#94a3b8;
                font-size:12px;
            ">
                or
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
