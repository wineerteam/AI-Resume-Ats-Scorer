# ============================================================
# PREMIUM SIDEBAR NAVIGATION STYLE
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       SIDEBAR BASE
    ======================================================== */

    [data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #07152f 0%,
                #091d3d 48%,
                #07152f 100%
            );

        border-right:
            1px solid
            rgba(37, 99, 235, 0.25);

        box-shadow:
            10px 0 40px
            rgba(3, 15, 35, 0.18);
    }


    [data-testid="stSidebar"] > div:first-child {
        padding-top: 1.5rem;
    }


    /* ========================================================
       NAVIGATION TITLE
    ======================================================== */

    .nav-brand {
        position: relative;

        padding: 6px 10px 18px 10px;

        margin-bottom: 8px;
    }


    .nav-brand-title {
        font-size: 23px;

        font-weight: 950;

        letter-spacing: -0.8px;

        color: #ffffff;

        line-height: 1.1;
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

        -webkit-text-fill-color:
            transparent;

        background-clip: text;
    }


    .nav-brand-subtitle {
        color: #94a3b8;

        font-size: 9px;

        font-weight: 700;

        letter-spacing: 1.3px;

        margin-top: 6px;

        text-transform: uppercase;
    }


    /* ========================================================
       CONNECTION LINE
    ======================================================== */

    .nav-connection {
        position: absolute;

        left: 22px;

        top: 125px;

        width: 2px;

        height: 250px;

        background:
            linear-gradient(
                180deg,
                #06b6d4,
                #2563eb,
                #ec4899,
                #f97316,
                #facc15
            );

        opacity: 0.55;

        border-radius: 10px;

        box-shadow:
            0 0 10px
            rgba(6, 182, 212, 0.25);
    }


    /* ========================================================
       NAVIGATION LABEL
    ======================================================== */

    .nav-section-label {
        color: #64748b;

        font-size: 8px;

        font-weight: 900;

        letter-spacing: 2px;

        text-transform: uppercase;

        margin:
            8px 0
            10px 8px;
    }


    /* ========================================================
       SIDEBAR BUTTON BASE
    ======================================================== */

    [data-testid="stSidebar"] .stButton {
        margin-bottom: 9px;

        position: relative;

        z-index: 3;
    }


    [data-testid="stSidebar"] .stButton > button {

        position: relative;

        width: 100%;

        min-height: 49px;

        border-radius: 15px;

        border:
            1px solid
            rgba(148, 163, 184, 0.14);

        background:
            linear-gradient(
                135deg,
                rgba(255,255,255,0.065),
                rgba(255,255,255,0.025)
            );

        color: #cbd5e1;

        font-size: 12px;

        font-weight: 850;

        letter-spacing: 0.2px;

        text-align: left;

        padding:
            0 16px;

        box-shadow:
            0 7px 0
            rgba(3, 12, 30, 0.35),

            0 10px 25px
            rgba(0,0,0,0.12);

        transition:
            transform 0.22s cubic-bezier(.2,.8,.2,1),
            box-shadow 0.22s ease,
            border-color 0.22s ease,
            background 0.22s ease,
            color 0.22s ease;

        overflow: hidden;
    }


    /* ========================================================
       LEFT COLOR BAR
    ======================================================== */

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
                #ec4899
            );

        opacity: 0.7;

        transition:
            width 0.22s ease,
            opacity 0.22s ease;
    }


    /* ========================================================
       LIGHT SHINE EFFECT
    ======================================================== */

    [data-testid="stSidebar"] .stButton > button::after {

        content: "";

        position: absolute;

        width: 80px;

        height: 150%;

        left: -100px;

        top: -25%;

        transform:
            rotate(20deg);

        background:
            linear-gradient(
                90deg,
                transparent,
                rgba(255,255,255,0.18),
                transparent
            );

        transition:
            left 0.45s ease;
    }


    /* ========================================================
       HOVER = ZOOM + 3D LIFT
    ======================================================== */

    [data-testid="stSidebar"] .stButton > button:hover {

        transform:
            translateX(7px)
            translateY(-4px)
            scale(1.035);

        color: #ffffff;

        background:
            linear-gradient(
                135deg,
                rgba(6,182,212,0.18),
                rgba(37,99,235,0.20),
                rgba(236,72,153,0.14)
            );

        border-color:
            rgba(96,165,250,0.48);

        box-shadow:

            0 8px 0
            rgba(3, 12, 30, 0.42),

            0 16px 30px
            rgba(37,99,235,0.18),

            0 0 25px
            rgba(6,182,212,0.10);
    }


    [data-testid="stSidebar"] .stButton > button:hover::before {

        width: 7px;

        opacity: 1;
    }


    [data-testid="stSidebar"] .stButton > button:hover::after {

        left: 125%;
    }


    /* ========================================================
       CLICK / PRESS = 3D PUSH
    ======================================================== */

    [data-testid="stSidebar"] .stButton > button:active {

        transform:
            translateX(5px)
            translateY(3px)
            scale(0.985);

        box-shadow:
            0 2px 0
            rgba(3,12,30,0.5),

            0 5px 12px
            rgba(0,0,0,0.2);
    }


    /* ========================================================
       FOCUS
    ======================================================== */

    [data-testid="stSidebar"] .stButton > button:focus {

        outline: none;

        border-color:
            rgba(6,182,212,0.55);

        box-shadow:
            0 0 0 2px
            rgba(6,182,212,0.10),

            0 10px 25px
            rgba(37,99,235,0.15);
    }


    /* ========================================================
       NAVIGATION DIVIDER
    ======================================================== */

    .nav-divider {

        height: 1px;

        margin:
            18px 5px 17px 5px;

        background:
            linear-gradient(
                90deg,
                transparent,
                rgba(148,163,184,0.25),
                transparent
            );
    }


    /* ========================================================
       ACCOUNT AREA
    ======================================================== */

    .account-title {

        color: #ffffff;

        font-size: 13px;

        font-weight: 900;

        margin-bottom: 10px;
    }


    /* ========================================================
       MOBILE
    ======================================================== */

    @media (max-width: 768px) {

        [data-testid="stSidebar"] .stButton > button {

            min-height: 46px;

            font-size: 11px;
        }

        .nav-brand-title {
            font-size: 20px;
        }

    }

    </style>
    """,
    unsafe_allow_html=True
)
