
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="BLOSSOMS | Festival Arena",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------- COLOURFUL LIGHT THEME --------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=DM+Sans:wght@400;500;600;700;800&display=swap');

* {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 5% 5%, #fbdcff 0%, transparent 25%),
        radial-gradient(circle at 95% 15%, #d9eaff 0%, transparent 27%),
        radial-gradient(circle at 50% 100%, #fff0d5 0%, transparent 30%),
        #fffaff;
    color: #35244f;
}

.block-container {
    max-width: 1500px;
    padding-top: 1.2rem;
    padding-bottom: 2rem;
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#f2dfff,#ffe1ec,#fff0d9);
}

h1,h2,h3 {
    color: #38264f !important;
    font-family: 'Outfit', sans-serif !important;
    font-weight: 800 !important;
}

p {
    color: #82738f;
}

/* BRAND */

.brand {
    font-family: 'Outfit';
    font-size: 27px;
    font-weight: 900;
    letter-spacing: 1px;
    background: linear-gradient(100deg,#873ee5,#e64ca6,#ff8b52);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.brand-sub {
    font-size: 9px;
    letter-spacing: 3px;
    color: #a18cac;
    font-weight: 800;
}

/* HERO */

.hero {
    position: relative;
    overflow: hidden;
    padding: 34px;
    border-radius: 25px;
    background: linear-gradient(115deg,#8246e9,#bd51ce,#ed62a6,#ff956a);
    background-size: 250% 250%;
    animation: moveGradient 9s ease infinite;
    box-shadow: 0 15px 40px rgba(156,75,200,.22);
    margin-bottom: 19px;
}

@keyframes moveGradient {
    0% {background-position:0% 50%;}
    50% {background-position:100% 50%;}
    100% {background-position:0% 50%;}
}

.hero:after {
    content:"✦";
    position:absolute;
    right:7%;
    top:-80px;
    font-size:240px;
    color:rgba(255,255,255,.17);
}

.hero:before {
    content:"✧";
    position:absolute;
    right:33%;
    bottom:-100px;
    font-size:190px;
    color:rgba(255,255,255,.14);
}

.hero-label {
    color:#ffe8ff;
    font-size:10px;
    font-weight:900;
    letter-spacing:3px;
}

.hero-title {
    font-family:'Outfit';
    font-size:43px;
    font-weight:900;
    line-height:1.05;
    color:white;
    margin-top:12px;
}

.hero-description {
    color:#fff0fa;
    font-size:13px;
    margin-top:12px;
}

.hero-tag {
    display:inline-block;
    background:rgba(255,255,255,.2);
    border:1px solid rgba(255,255,255,.45);
    border-radius:30px;
    padding:7px 13px;
    color:white;
    font-size:10px;
    font-weight:800;
    margin:15px 5px 0 0;
}

/* LIVE STATUS */

.live-tag {
    display:inline-block;
    padding:7px 13px;
    border-radius:30px;
    background:#e5fff1;
    color:#149b66;
    border:1px solid #a7edcc;
    font-size:10px;
    font-weight:900;
}

/* STATS */

.stat-card {
    padding:19px;
    border-radius:20px;
    background:linear-gradient(145deg,#ffffff,#f9f1ff);
    border:1px solid #eadcf5;
    box-shadow:0 8px 22px rgba(111,72,144,.08);
    min-height:135px;
    transition:.25s;
}

.stat-card:hover {
    transform:translateY(-5px);
    box-shadow:0 14px 30px rgba(111,72,144,.16);
}

.stat-icon {
    font-size:28px;
}

.stat-label {
    color:#9987a8;
    font-size:10px;
    font-weight:900;
    letter-spacing:1px;
    margin-top:10px;
}

.stat-value {
    font-family:'Outfit';
    font-size:29px;
    font-weight:900;
    color:#442b62;
    margin-top:3px;
}

/* PANELS */

.panel {
    background:rgba(255,255,255,.92);
    border:1px solid #ebdef3;
    border-radius:20px;
    padding:19px;
    margin-bottom:15px;
    box-shadow:0 8px 25px rgba(92,57,119,.065);
}

.panel-title {
    color:#422b60;
    font-family:'Outfit';
    font-size:18px;
    font-weight:900;
}

.panel-subtitle {
    color:#ac8fbd;
    font-size:10px;
    letter-spacing:2px;
    font-weight:900;
    margin-bottom:12px;
}

/* PODIUM */

.podium-area {
    background:
        radial-gradient(circle at 50% 20%,#ffe6f4,transparent 50%),
        linear-gradient(140deg,#f6eaff,#e8f2ff,#fff0e4);
    border:1px solid #e8d9f5;
    border-radius:22px;
    padding:22px 13px 12px;
    margin:18px 0;
    overflow:hidden;
}

.podium-title {
    color:#53346f;
    font-family:'Outfit';
    font-size:20px;
    font-weight:900;
}

.podium-sub {
    color:#9b84ae;
    font-size:10px;
    letter-spacing:2px;
}

.podium {
    display:flex;
    flex-direction:column;
    justify-content:flex-end;
    align-items:center;
    text-align:center;
    height:240px;
}

.trophy {
    font-size:49px;
    filter:drop-shadow(0 6px 8px rgba(172,122,50,.2));
    margin-bottom:8px;
}

.winner-name {
    color:#4c3562;
    font-size:11px;
    font-weight:900;
    max-width:130px;
    overflow-wrap:anywhere;
    margin-bottom:5px;
}

.winner-points {
    color:#a26b26;
    font-size:12px;
    font-weight:900;
    margin-bottom:8px;
}

.podium-block {
    width:100%;
    display:flex;
    justify-content:center;
    align-items:center;
    border-radius:12px 12px 0 0;
    font-family:'Outfit';
    font-size:35px;
    font-weight:900;
    color:white;
    text-shadow:0 2px 5px rgba(0,0,0,.15);
}

.gold {
    height:115px;
    background:linear-gradient(145deg,#ffe06a,#ff9d39);
    box-shadow:0 0 25px #ffc85b70;
}

.silver {
    height:75px;
    background:linear-gradient(145deg,#c8d9f6,#819fe0);
}

.bronze {
    height:55px;
    background:linear-gradient(145deg,#ffc49c,#df835e);
}

/* LEADERBOARD */

.score-row {
    background:linear-gradient(100deg,#f2eaff,#fceaf5);
    border:1px solid #e9d9f4;
    border-radius:13px;
    padding:13px;
    margin-bottom:9px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    gap:8px;
    transition:.2s;
}

.score-row:nth-child(even) {
    background:linear-gradient(100deg,#e8f3ff,#eff5ff);
}

.score-row:hover {
    transform:translateX(4px);
}

.rank-name {
    color:#49315f;
    font-size:12px;
    font-weight:900;
}

.rank-detail {
    color:#9a88a9;
    font-size:10px;
    margin-top:4px;
}

.rank-points {
    color:#8c4cc7;
    font-family:'Outfit';
    font-size:16px;
    font-weight:900;
    white-space:nowrap;
}

/* EVENTS */

.event-box {
    background:linear-gradient(145deg,#fff,#faf3ff);
    border:1px solid #eadcf5;
    border-radius:19px;
    padding:18px;
    margin-bottom:13px;
    min-height:160px;
    box-shadow:0 7px 20px rgba(104,70,130,.07);
    transition:.25s;
}

.event-box:hover {
    transform:translateY(-5px);
    box-shadow:0 14px 26px rgba(104,70,130,.13);
}

.event-icon {
    font-size:32px;
}

.event-name {
    color:#4a3065;
    font-family:'Outfit';
    font-size:17px;
    font-weight:900;
    margin-top:9px;
}

.event-info {
    color:#9c8ba8;
    font-size:10px;
    margin-top:5px;
}

.event-score {
    color:#a34dca;
    font-size:11px;
    font-weight:900;
    margin-top:12px;
}

/* RIGHT SIDE */

.right-card {
    background:linear-gradient(135deg,#fff,#f5efff);
    border:1px solid #e8ddf2;
    border-radius:15px;
    padding:14px;
    margin-bottom:11px;
    box-shadow:0 5px 15px rgba(100,70,130,.06);
    transition:.2s;
}

.right-card:hover {
    transform:translateY(-3px);
}

.right-title {
    color:#50366c;
    font-size:12px;
    font-weight:900;
}

.right-description {
    color:#9789a4;
    font-size:10px;
    margin-top:4px;
}

/* BUTTONS */

.stButton > button,
.stFormSubmitButton > button {
    background:linear-gradient(100deg,#9550e9,#d44ebc,#ff876d);
    color:white;
    border:none;
    border-radius:11px;
    font-weight:900;
    min-height:43px;
    transition:.2s;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    transform:translateY(-2px);
    color:white;
    border:none;
    box-shadow:0 7px 18px #b25cd45c;
}

/* FORMS */

div[data-testid="stForm"] {
    background:white;
    border:1px solid #eadcf3;
    border-radius:19px;
    padding:22px;
    box-shadow:0 8px 25px rgba(100,70,130,.06);
}

.stSelectbox label,
.stTextInput label,
.stNumberInput label {
    color:#634c79 !important;
    font-weight:800;
}

div[data-baseweb="select"] > div {
    background:#faf6ff;
    border-color:#e4d6ef;
}

input,textarea {
    background:#faf6ff !important;
    color:#49345e !important;
}

/* METRICS */

[data-testid="stMetric"] {
    background:linear-gradient(145deg,#ffffff,#f6efff);
    border:1px solid #e9dcf3;
    border-radius:15px;
    padding:14px;
}

[data-testid="stMetricLabel"] {
    color:#927fa4;
}

[data-testid="stMetricValue"] {
    color:#51336e;
}

/* NAVIGATION */

.stRadio > div {
    background:linear-gradient(90deg,#f2e5ff,#ffe7f2,#fff0df);
    border:1px solid #e9d7f1;
    border-radius:14px;
    padding:9px;
}

.stRadio label {
    color:#654a7d !important;
    font-weight:800 !important;
}

/* DATA */

[data-testid="stDataFrame"] {
    border:1px solid #e8ddef;
    border-radius:13px;
    overflow:hidden;
}

hr {
    border-color:#eadff0;
}

/* FOOTER */

.footer {
    background:linear-gradient(100deg,#f0e2ff,#ffe3f0,#fff0d8);
    border:1px solid #ead9ef;
    border-radius:18px;
    padding:23px;
    text-align:center;
    margin-top:25px;
}

.footer-title {
    font-family:'Outfit';
    color:#9453c6;
    font-size:20px;
    font-weight:900;
}

.footer-text {
    color:#a28ba9;
    font-size:10px;
    letter-spacing:2px;
    margin-top:7px;
}

</style>
""", unsafe_allow_html=True)


# -------------------- SAMPLE DATA --------------------

SAMPLE_EVENTS = [
    {"event":"Battle of Bands","category":"Blossoms","type":"Music"},
    {"event":"Street Dance","category":"Blossoms","type":"Dance"},
    {"event":"Theatre Relay","category":"Blossoms","type":"Drama"},
    {"event":"Campus Canvas","category":"Blossoms","type":"Fine Arts"},
    {"event":"Quiz League","category":"Inter-Collegiate","type":"Literary"},
    {"event":"Code Sprint","category":"Inter-Collegiate","type":"Technology"},
    {"event":"Futsal 5-a-side","category":"Inter-Collegiate","type":"Sports"},
    {"event":"Pitch Perfect","category":"Inter-Collegiate","type":"Business"},
    {"event":"Photography Hunt","category":"Blossoms","type":"Photography"},
    {"event":"Fashion Fusion","category":"Blossoms","type":"Fashion"},
    {"event":"Battle of Brains","category":"Inter-Collegiate","type":"Literary"},
    {"event":"Acoustic Nights","category":"Blossoms","type":"Music"}
]

SAMPLE_SCORES = [
    ["Battle of Bands","CHRIST University","The Echoes",1,90,"Winner"],
    ["Battle of Bands","St Joseph's University","Frequency",2,78,"Runner-up"],
    ["Street Dance","CHRIST University","Pulse Crew",1,88,"Winner"],
    ["Street Dance","Mount Carmel College","MCC Motion",2,82,"Runner-up"],
    ["Quiz League","St Joseph's University","Brainwave",1,95,"Winner"],
    ["Quiz League","CHRIST University","The Think Tank",2,84,"Runner-up"],
    ["Code Sprint","PES University","ByteForce",1,92,"Winner"],
    ["Code Sprint","CHRIST University","Null Pointers",2,80,"Runner-up"],
    ["Futsal 5-a-side","Jain University","Jain Strikers",1,90,"Winner"],
    ["Futsal 5-a-side","PES University","PES United",2,76,"Runner-up"]
]

ICONS = {
    "Music":"🎵",
    "Dance":"💃",
    "Drama":"🎭",
    "Fine Arts":"🎨",
    "Literary":"📚",
    "Technology":"💻",
    "Sports":"⚽",
    "Business":"💼",
    "Photography":"📸",
    "Fashion":"👗",
    "Other":"✨"
}


# -------------------- SESSION STATE --------------------

if "events" not in st.session_state:
    st.session_state.events = pd.DataFrame(SAMPLE_EVENTS)

if "scores" not in st.session_state:
    st.session_state.scores = pd.DataFrame(
        SAMPLE_SCORES,
        columns=[
            "Event","College","Team / Participant",
            "Position","Points","Result"
        ]
    )

events = st.session_state.events
scores = st.session_state.scores


# -------------------- HEADER --------------------

header1,header2 = st.columns([1.4,1])

with header1:
    st.markdown("""
    <div style="display:flex;align-items:center;gap:12px;">
        <div style="font-size:38px;">🌸</div>
        <div>
            <div class="brand">BLOSSOMS FESTIVALVERSE</div>
            <div class="brand-sub">THE ULTIMATE CAMPUS CELEBRATION</div>
        </div>
    </div>
    """,unsafe_allow_html=True)

with header2:
    st.markdown("""
    <div style="text-align:right;padding:10px;">
        <span class="live-tag">● FESTIVAL LIVE</span>
        <span style="color:#a78db8;font-size:10px;margin-left:8px;">
            2026 EDITION
        </span>
    </div>
    """,unsafe_allow_html=True)

st.write("")

page = st.radio(
    "Navigation",
    [
        "🏠 Home",
        "🏆 Leaderboard",
        "✍️ Score Entry",
        "🎪 Events",
        "📊 Analytics"
    ],
    horizontal=True,
    label_visibility="collapsed"
)

st.divider()


# -------------------- CALCULATIONS --------------------

if not scores.empty:
    college_table = (
        scores.groupby("College",as_index=False)["Points"]
        .sum()
        .sort_values("Points",ascending=False)
        .reset_index(drop=True)
    )

    college_table["Rank"] = range(1,len(college_table)+1)
    total_points = int(scores["Points"].sum())
    leader = college_table.iloc[0]["College"]

else:
    college_table = pd.DataFrame(
        columns=["College","Points","Rank"]
    )
    total_points = 0
    leader = "No leader"


# -------------------- RIGHT PANEL --------------------

def right_panel():

    st.markdown("""
    <div class="panel">
        <div style="display:flex;align-items:center;gap:12px;">
            <div style="font-size:34px;">👑</div>
            <div>
                <div style="font-weight:900;color:#49305f;">
                    Festival Control
                </div>
                <div style="font-size:10px;color:#a28dae;">
                    ADMIN DASHBOARD
                </div>
            </div>
        </div>
    </div>
    """,unsafe_allow_html=True)

    items = [
        ("📊","Festival Insights","Explore college performance."),
        ("⚡","Score Control","Update competition results."),
        ("🎯","Event Creator","Add new competitions."),
        ("🏆","Champions Arena","Discover festival leaders."),
        ("📥","Data Export","Download your records.")
    ]

    for icon,title,desc in items:
        st.markdown(f"""
        <div class="right-card">
            <div style="display:flex;gap:12px;align-items:center;">
                <div style="font-size:24px;">{icon}</div>
                <div>
                    <div class="right-title">{title}</div>
                    <div class="right-description">{desc}</div>
                </div>
            </div>
        </div>
        """,unsafe_allow_html=True)

    st.markdown(f"""
    <div class="panel">
        <div class="panel-subtitle">FESTIVAL SNAPSHOT</div>
        <div style="color:#57366f;font-size:14px;font-weight:900;">
            {len(events)} EVENTS
        </div>
        <div style="color:#a18cae;font-size:11px;">
            {scores['College'].nunique() if not scores.empty else 0} Colleges participating
        </div>
        <div style="font-family:Outfit;font-size:25px;color:#ad59c9;font-weight:900;margin-top:10px;">
            {total_points:,} PTS
        </div>
    </div>
    """,unsafe_allow_html=True)


# -------------------- HOME --------------------

if page == "🏠 Home":

    left,right = st.columns([2.1,0.9])

    with left:

        st.markdown("""
        <div class="hero">
            <div class="hero-label">CHRIST UNIVERSITY PRESENTS</div>
            <div class="hero-title">
                BLOSSOMS<br>
                FESTIVALVERSE ✦
            </div>
            <div class="hero-description">
                Where talent meets the spotlight.
                One stage. Multiple colleges. Infinite possibilities.
            </div>
            <span class="hero-tag">🏆 LIVE LEADERBOARD</span>
            <span class="hero-tag">🎪 EVENT ARENA</span>
            <span class="hero-tag">📊 SMART ANALYTICS</span>
        </div>
        """,unsafe_allow_html=True)

        a,b,c = st.columns(3)

        stats = [
            (a,"🎪","TOTAL EVENTS",len(events)),
            (b,"🏫","COLLEGES",scores["College"].nunique() if not scores.empty else 0),
            (c,"⚡","TOTAL POINTS",total_points)
        ]

        for col,icon,label,value in stats:
            with col:
                st.markdown(f"""
                <div class="stat-card">
                    <div class="stat-icon">{icon}</div>
                    <div class="stat-label">{label}</div>
                    <div class="stat-value">{value:,}</div>
                </div>
                """,unsafe_allow_html=True)

        st.markdown("""
        <div class="podium-area">
            <div class="podium-title">🏆 THE CHAMPIONS PODIUM</div>
            <div class="podium-sub">THE RACE FOR THE FESTIVAL CROWN</div>
        """,unsafe_allow_html=True)

        if college_table.empty:
            st.info("Enter scores to reveal your champions.")
        else:

            first = college_table.iloc[0]
            second = college_table.iloc[1] if len(college_table)>1 else None
            third = college_table.iloc[2] if len(college_table)>2 else None

            p1,p2,p3 = st.columns([1,1.15,1])

            with p1:
                if second is not None:
                    st.markdown(f"""
                    <div class="podium">
                        <div class="trophy">🥈</div>
                        <div class="winner-name">{second['College']}</div>
                        <div class="winner-points">{int(second['Points'])} PTS</div>
                        <div class="podium-block silver">2</div>
                    </div>
                    """,unsafe_allow_html=True)

            with p2:
                st.markdown(f"""
                <div class="podium">
                    <div class="trophy">🏆</div>
                    <div class="winner-name">{first['College']}</div>
                    <div class="winner-points">{int(first['Points'])} PTS</div>
                    <div class="podium-block gold">1</div>
                </div>
                """,unsafe_allow_html=True)

            with p3:
                if third is not None:
                    st.markdown(f"""
                    <div class="podium">
                        <div class="trophy">🥉</div>
                        <div class="winner-name">{third['College']}</div>
                        <div class="winner-points">{int(third['Points'])} PTS</div>
                        <div class="podium-block bronze">3</div>
                    </div>
                    """,unsafe_allow_html=True)

        st.markdown("</div>",unsafe_allow_html=True)

        st.markdown("""
        <div class="panel">
            <div class="panel-title">✨ LIVE COLLEGE LEADERBOARD</div>
        """,unsafe_allow_html=True)

        if not college_table.empty:

            medals = ["🥇","🥈","🥉"]

            for i,row in college_table.iterrows():
                medal = medals[i] if i<3 else "🏅"

                st.markdown(f"""
                <div class="score-row">
                    <div style="display:flex;align-items:center;gap:12px;">
                        <div style="font-size:23px;">{medal}</div>
                        <div>
                            <div class="rank-name">{row['College']}</div>
                            <div class="rank-detail">
                                RANK #{i+1} • FESTIVAL COMPETITOR
                            </div>
                        </div>
                    </div>
                    <div class="rank-points">
                        {int(row['Points']):,} PTS
                    </div>
                </div>
                """,unsafe_allow_html=True)

        st.markdown("</div>",unsafe_allow_html=True)

    with right:
        right_panel()


# -------------------- LEADERBOARD --------------------

elif page == "🏆 Leaderboard":

    left,right = st.columns([2.1,0.9])

    with left:

        st.markdown("""
        <div class="hero">
            <div class="hero-label">THE ULTIMATE COMPETITION</div>
            <div class="hero-title">🏆 CHAMPIONS ARENA</div>
            <div class="hero-description">
                Every point counts. Who will take the crown?
            </div>
        </div>
        """,unsafe_allow_html=True)

        if not college_table.empty:

            medals = ["🥇","🥈","🥉"]
            cols = st.columns(3)

            for i in range(min(3,len(college_table))):
                row = college_table.iloc[i]

                with cols[i]:
                    st.markdown(f"""
                    <div class="panel" style="text-align:center;">
                        <div style="font-size:38px;">{medals[i]}</div>
                        <div style="font-size:12px;color:#55356e;font-weight:900;">
                            {row['College']}
                        </div>
                        <div style="font-size:28px;color:#a257c9;font-weight:900;">
                            {int(row['Points'])}
                        </div>
                        <div class="rank-detail">TOTAL POINTS</div>
                    </div>
                    """,unsafe_allow_html=True)

            st.markdown("### 📋 Complete Rankings")

            result = college_table.copy()
            result["Medal"] = result["Rank"].apply(
                lambda x: medals[int(x)-1] if x<=3 else "🏅"
            )

            st.dataframe(
                result[["Medal","Rank","College","Points"]],
                use_container_width=True,
                hide_index=True
            )

            st.markdown("### 📊 College Comparison")

            st.bar_chart(
                college_table.set_index("College")[["Points"]],
                color="#b36be5"
            )

        else:
            st.info("No scores available.")

    with right:
        right_panel()


# -------------------- SCORE ENTRY --------------------

elif page == "✍️ Score Entry":

    left,right = st.columns([2.1,0.9])

    with left:

        st.markdown("""
        <div class="hero">
            <div class="hero-label">EVENT OPERATIONS</div>
            <div class="hero-title">⚡ SCORE CONTROL ROOM</div>
            <div class="hero-description">
                Enter results. Award points. Update the leaderboard.
            </div>
        </div>
        """,unsafe_allow_html=True)

        if not events.empty:

            with st.form("score_form",clear_on_submit=True):

                st.markdown("### 🎯 Enter Competition Results")

                event = st.selectbox(
                    "Select Event",
                    events["event"].tolist()
                )

                college = st.text_input(
                    "College Name",
                    placeholder="CHRIST University"
                )

                team = st.text_input(
                    "Team / Participant",
                    placeholder="The Echoes"
                )

                a,b,c = st.columns(3)

                with a:
                    position = st.selectbox("Position",[1,2,3,4,5])

                with b:
                    points = st.number_input(
                        "Points",
                        min_value=0,
                        max_value=1000,
                        value=10
                    )

                with c:
                    result = st.selectbox(
                        "Result",
                        ["Winner","Runner-up","Third place","Participant"]
                    )

                submit = st.form_submit_button(
                    "🚀 PUBLISH RESULT",
                    use_container_width=True
                )

                if submit:

                    if not college.strip() or not team.strip():
                        st.error("Please enter college and participant details.")
                    else:

                        new = pd.DataFrame([{
                            "Event":event,
                            "College":college.strip(),
                            "Team / Participant":team.strip(),
                            "Position":position,
                            "Points":int(points),
                            "Result":result
                        }])

                        st.session_state.scores = pd.concat(
                            [st.session_state.scores,new],
                            ignore_index=True
                        )

                        st.success("🎉 RESULT PUBLISHED SUCCESSFULLY!")
                        st.balloons()
                        st.rerun()

        else:
            st.warning("Create an event first.")

        st.markdown("### 📑 Score Register")

        if not st.session_state.scores.empty:

            st.dataframe(
                st.session_state.scores,
                use_container_width=True,
                hide_index=True
            )

            csv = st.session_state.scores.to_csv(index=False).encode("utf-8")

            st.download_button(
                "⬇️ DOWNLOAD SCORES",
                csv,
                "festival_scores.csv",
                "text/csv"
            )

    with right:
        right_panel()


# -------------------- EVENTS --------------------

elif page == "🎪 Events":

    left,right = st.columns([2.1,0.9])

    with left:

        st.markdown("""
        <div class="hero">
            <div class="hero-label">DISCOVER THE COMPETITIONS</div>
            <div class="hero-title">🎪 EVENT UNIVERSE</div>
            <div class="hero-description">
                Music, dance, art, sports, technology and creativity.
            </div>
        </div>
        """,unsafe_allow_html=True)

        with st.form("event_form",clear_on_submit=True):

            st.markdown("### ✨ Create a New Event")

            event_name = st.text_input(
                "Event Name",
                placeholder="Battle of the Brains"
            )

            a,b = st.columns(2)

            with a:
                category = st.selectbox(
                    "Festival",
                    ["Blossoms","Inter-Collegiate"]
                )

            with b:
                event_type = st.selectbox(
                    "Category",
                    list(ICONS.keys())
                )

            add = st.form_submit_button(
                "＋ CREATE FESTIVAL EVENT",
                use_container_width=True
            )

            if add:

                existing = st.session_state.events["event"].str.lower().tolist()

                if not event_name.strip():
                    st.error("Enter an event name.")

                elif event_name.strip().lower() in existing:
                    st.warning("This event already exists.")

                else:

                    new = pd.DataFrame([{
                        "event":event_name.strip(),
                        "category":category,
                        "type":event_type
                    }])

                    st.session_state.events = pd.concat(
                        [st.session_state.events,new],
                        ignore_index=True
                    )

                    st.success("🌸 EVENT CREATED SUCCESSFULLY!")
                    st.rerun()

        st.markdown("### 🎟️ Registered Competitions")

        cols = st.columns(2)

        for i,row in events.iterrows():

            with cols[i%2]:

                points = scores.loc[
                    scores["Event"]==row["event"],"Points"
                ].sum()

                st.markdown(f"""
                <div class="event-box">
                    <div class="event-icon">{ICONS.get(row['type'],'✨')}</div>
                    <div class="event-name">{row['event']}</div>
                    <div class="event-info">
                        {row['category']} • {row['type']}
                    </div>
                    <div class="event-score">
                        ⚡ {int(points)} POINTS AWARDED
                    </div>
                </div>
                """,unsafe_allow_html=True)

    with right:
        right_panel()


# -------------------- ANALYTICS --------------------

elif page == "📊 Analytics":

    left,right = st.columns([2.1,0.9])

    with left:

        st.markdown("""
        <div class="hero">
            <div class="hero-label">DATA INTELLIGENCE</div>
            <div class="hero-title">📊 ANALYTICS STUDIO</div>
            <div class="hero-description">
                Discover the numbers behind every victory.
            </div>
        </div>
        """,unsafe_allow_html=True)

        if scores.empty:

            st.info("Enter scores to unlock analytics.")

        else:

            a,b = st.columns(2)

            with a:
                chosen_event = st.selectbox(
                    "Filter Event",
                    ["All Events"]+sorted(scores["Event"].unique().tolist())
                )

            with b:
                chosen_category = st.selectbox(
                    "Filter Festival",
                    ["All Festivals"]+sorted(events["category"].unique().tolist())
                )

            filtered = scores.copy()

            if chosen_event != "All Events":
                filtered = filtered[
                    filtered["Event"]==chosen_event
                ]

            if chosen_category != "All Festivals":

                allowed = events.loc[
                    events["category"]==chosen_category,"event"
                ].tolist()

                filtered = filtered[
                    filtered["Event"].isin(allowed)
                ]

            if filtered.empty:

                st.warning("No records found for the selected filters.")

            else:

                a,b,c = st.columns(3)

                a.metric("📋 ENTRIES",len(filtered))
                b.metric("🏫 COLLEGES",filtered["College"].nunique())
                c.metric("⚡ POINTS",int(filtered["Points"].sum()))

                st.divider()

                st.markdown("### 🏫 College Performance")

                college_data = (
                    filtered.groupby("College")["Points"]
                    .sum()
                    .sort_values(ascending=False)
                )

                st.bar_chart(college_data,color="#a66ae5")

                st.markdown("### 🎪 Event Performance")

                event_data = (
                    filtered.groupby("Event")["Points"]
                    .sum()
                    .sort_values(ascending=False)
                )

                st.bar_chart(event_data,color="#f17cae")

                st.markdown("### 🏅 Position Distribution")

                position_data = (
                    filtered["Position"]
                    .value_counts()
                    .sort_index()
                )

                position_data.index = [
                    "Position "+str(i) for i in position_data.index
                ]

                st.bar_chart(position_data,color="#51bda9")

                st.markdown("### 📑 Detailed Results")

                st.dataframe(
                    filtered,
                    use_container_width=True,
                    hide_index=True
                )

                csv = filtered.to_csv(index=False).encode("utf-8")

                st.download_button(
                    "⬇️ DOWNLOAD ANALYTICS REPORT",
                    csv,
                    "festival_analytics.csv",
                    "text/csv"
                )

    with right:
        right_panel()


# -------------------- FOOTER --------------------

st.markdown("""
<div class="footer">
    <div style="font-size:30px;">🌸 🎭 🎵 🏆 ✨</div>
    <div class="footer-title">BLOSSOMS FESTIVALVERSE</div>
    <div class="footer-text">
        CELEBRATE TALENT • CONNECT CAMPUSES • CREATE MEMORIES
    </div>
    <div style="color:#b09bb7;font-size:10px;margin-top:12px;">
        STREAMLIT FESTIVAL MANAGEMENT DASHBOARD • STUDENT PROJECT
    </div>
</div>
""",unsafe_allow_html=True)
