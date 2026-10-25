
import streamlit as st
from chatbot import get_answer

st.set_page_config(
    page_title="RailBot | Railway AI Assistant",
    page_icon="🚆",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {
    background:
        radial-gradient(ellipse at 15% 0%, #172d55 0%, transparent 45%),
        radial-gradient(ellipse at 90% 80%, #24204c 0%, transparent 40%),
        #080e1b;
    color: #edf3ff;
    font-family: 'Inter', sans-serif;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1050px;
    padding-top: 2rem;
    padding-bottom: 7rem;
}

.hero {
    text-align: center;
    padding: 30px 20px 25px;
}

.logo {
    display: inline-block;
    background: linear-gradient(135deg, #163b70, #6c4bd3);
    border: 1px solid #648ce8;
    border-radius: 22px;
    padding: 15px 20px;
    font-size: 34px;
    box-shadow: 0 0 38px #315fd344;
    margin-bottom: 18px;
}

.hero h1 {
    font-size: clamp(32px, 5vw, 48px);
    font-weight: 800;
    letter-spacing: -1.5px;
    margin: 0;
    background: linear-gradient(90deg, #ffffff, #91c8ff, #c2a6ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero p {
    color: #a9b9d3;
    font-size: 15px;
    margin-top: 12px;
}

.status {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 15px;
    border: 1px solid #285d55;
    border-radius: 30px;
    color: #8cf0c4;
    background: #102c2b;
    font-size: 12px;
    font-weight: 600;
    margin-top: 10px;
}

.section-label {
    color: #a9bce0;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin: 25px 0 13px;
}

div[data-testid="stChatMessage"] {
    background: #111d30;
    border: 1px solid #273a56;
    border-radius: 18px;
    padding: 17px 20px;
    margin-bottom: 13px;
}

div[data-testid="stChatMessage"]:has(
    [data-testid="chatAvatarIcon-user"]
) {
    background: #172746;
    border-color: #36558c;
}

div[data-testid="stChatMessage"] p {
    color: #edf3ff;
    line-height: 1.75;
    font-size: 14px;
}


div[data-testid="stBottom"],
div[data-testid="stBottom"] > div {
    background: #080e1b !important;
}

div[data-testid="stChatInput"] {
    border: 1px solid #415d88 !important;
    border-radius: 17px !important;
    background: #111d30 !important;
    box-shadow: 0 8px 35px #00000055 !important;
}

div[data-testid="stChatInput"] textarea {
    color: #ffffff !important;
    background: transparent !important;
}

div[data-testid="stChatInput"] textarea::placeholder {
    color: #a9b9d3 !important;
}

div[data-testid="stChatInput"] button {
    background: linear-gradient(135deg, #397cf6, #8059e8) !important;
    border-radius: 11px !important;
}


div.stButton > button {
    min-height: 65px;
    width: 100%;
    text-align: left;
    white-space: normal;
    color: #e2ecff;
    background: #111d30;
    border: 1px solid #293e5e;
    border-radius: 15px;
    padding: 13px 16px;
    font-size: 13px;
    transition: all 0.2s ease;
}

div.stButton > button:hover {
    background: #1b2e4c;
    border-color: #6598f7;
    color: #ffffff;
    transform: translateY(-2px);
}

.footer {
    text-align: center;
    color: #7285a5;
    font-size: 12px;
    padding: 30px 0 10px;
}

div[data-testid="stAlert"] {
    background: #17243a;
    color: #dce8ff;
    border: 1px solid #30466a;
    border-radius: 14px;
}

#MainMenu, footer {
    visibility: hidden;
}

@media (max-width: 640px) {
    .block-container {
        padding: 1rem 1rem 6rem;
    }
    .hero {
        padding-top: 20px;
    }
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="hero">
    <div class="logo">🚆</div>
    <h1>RailBot AI</h1>
    <p>Your intelligent companion for railway track inspection</p>
    <div class="status">● SYSTEM ONLINE &nbsp;|&nbsp; FAQ ASSISTANT</div>
</div>
""", unsafe_allow_html=True)

# Suggested questions
st.markdown(
    '<div class="section-label">✦ Explore railway intelligence</div>',
    unsafe_allow_html=True
)

suggestions = [
    "🔍 How does the robot detect cracks?",
    "📡 Which sensors can the robot use?",
    "🛡️ Why is track inspection important?",
    "🤖 Can the robot work autonomously?"
]

if "messages" not in st.session_state:
    st.session_state.messages = []

if "pending_question" not in st.session_state:
    st.session_state.pending_question = ""

columns = st.columns(2)

for index, question in enumerate(suggestions):
    with columns[index % 2]:
        if st.button(question, key=f"suggestion_{index}"):
            st.session_state.pending_question = question.split(" ", 1)[1]
            st.rerun()

# Chat history
st.markdown(
    '<div class="section-label">✦ Conversation</div>',
    unsafe_allow_html=True
)

if not st.session_state.messages:
    st.info(
        "👋 Welcome aboard! Ask me anything about railway inspection "
        "robots, crack detection, sensors, or safety."
    )

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

typed_question = st.chat_input(
    "Ask RailBot anything about railway inspection..."
)

user_question = typed_question

if not user_question and st.session_state.pending_question:
    user_question = st.session_state.pending_question
    st.session_state.pending_question = ""

if user_question:
    st.session_state.messages.append({
        "role": "user",
        "content": user_question
    })

    answer = get_answer(user_question)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    st.rerun()

st.markdown("""
<div class="footer">
    RAILBOT AI · Railway Inspection FAQ Assistant<br>
    Built with Python & Streamlit · Designed to assist inspection teams
</div>
""", unsafe_allow_html=True)
