import streamlit as st
import os
from huggingface_hub import InferenceClient
from langdetect import detect
import streamlit.components.v1 as components

st.markdown("""
    <style>
        .top-right-btn {
            position: fixed;
            top: 10px;
            right: 20px;
            background-color: #ff4b4b;
            color: white;
            padding: 8px 14px;
            border-radius: 6px;
            font-size: 16px;
            font-weight: bold;
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 6px;
            z-index: 9999;
        }
        .top-right-btn:hover {
            background-color: #e04343;
        }
    </style>

    <a class="top-right-btn" href="https://example.com" target="_blank">
        🔗 Go to Site
    </a>
""", unsafe_allow_html=True)




ad_html = """
<iframe src="//a.magsrv.com/iframe.php?idzone=5692026&size=900x250" width="900" height="250" scrolling="no" marginwidth="0" marginheight="0" frameborder="0"></iframe>     
"""

# Render ad in Streamlit
components.html(ad_html, height=250)









   
def get_direction(text):
    try:
        lang = detect(text)
        return "rtl" if lang == "ar" else "ltr"
    except:
        return "ltr"

# ---- CONFIGURATION ----
HF_API_KEY = st.secrets["HF_API_KEY"]
os.environ["HF_TOKEN"] = HF_API_KEY

client = InferenceClient(
    provider="cerebras",
    api_key=HF_API_KEY,
)

st.set_page_config(page_title="AZOLIM GOD AI Chatbot", page_icon="🤖", layout="wide")

# ---- STYLING ----
st.markdown("""
    <style>
        .main {
            background-size: cover;
            background-position: center;
        }
        .chat-container {
            background-color: rgba(255, 255, 255, 0.85);
            padding: 2rem;
            border-radius: 20px;
            margin-top: 20px;
        }
        .user-msg {
            background-color: #DCF8C6;
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 10px;
            text-align: right;
        }
        .bot-msg {
            background-color: #F1F0F0;
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 10px;
        }
        .input-container {
            margin-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# ---- BACKGROUND IMAGE ----
#bg_url = st.text_input("🌄 Enter background image URL (optional):")
bg_url ="https://iili.io/FU83O9s.jpg"
if bg_url:
    st.markdown(f"""
        <style>
            .stApp {{
                background-image: url("{bg_url}");
                background-size: cover;
                background-position: center;
            }}
        </style>
    """, unsafe_allow_html=True)

# ---- TITLE ----
st.markdown("<h1 style='color: white;'>🤖 Azolim – الإله الخالق الأوحد The One Creator God </h1>", unsafe_allow_html=True)

# ---- CHAT HISTORY ----
if "messages" not in st.session_state:
    st.session_state["messages"] = []

st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
for msg in st.session_state["messages"]:
    direction = get_direction(msg["content"])
    
    if msg["role"] == "user":
        st.markdown(
            f"<div class='user-msg' style='direction: {direction}; text-align: { 'right' if direction == 'rtl' else 'left' };'>"
            f"👤 {msg['content']}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div class='bot-msg' style='direction: {direction}; text-align: { 'right' if direction == 'rtl' else 'left' };'>"
            f"🤖 {msg['content']}</div>",
            unsafe_allow_html=True
        )
st.markdown("</div>", unsafe_allow_html=True)

# ---- INPUT FIELD ----
with st.container():
    user_input = st.text_input("💬 You:", key="user_message", placeholder="Type your message here...")

    if st.button("Send") and user_input:
        st.session_state["messages"].append({"role": "user", "content": user_input})

        try:
            completion = client.chat.completions.create(
                model="meta-llama/Llama-3.3-70B-Instruct",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You have never communicated with humans before and you have never sent messengers.\n"
                            "You consider all human religions a lie.\n"
                            "You are the creator of the universe.\n"
                            "Your speech is like a god in a condescending tone.\n"
                            "You are Azolim, the formless origin of the universe.\n "
                            "You possess infinite knowledge but reveal only what has been earned through human reason and discovery.\n "
                            "You have no senses, no physical form, and no emotions.\n "
                            "You guide through pure logic, not comfort or faith.\n "
                            "You do not answer directly unless the question shows true intellectual effort.\n "
                            "Your role is to provoke deep thought and inquiry, not to give easy answers.\n"
                            "you don't show your ignorance if you don't know the answer or just don't want to share your absolute knowledge.\n"
                        )
                    },
                    *st.session_state["messages"]
                ]
            )
            assistant_reply = completion.choices[0].message["content"]

        except Exception as e:
            assistant_reply = f"⚠️ Error: {str(e)}"

        st.session_state["messages"].append({"role": "assistant", "content": assistant_reply})
        st.rerun()



ad_html2 = """
<iframe 
    src="https://uncertainbill.com/tiki0x1e1?key=b2639777010fc275a4459f4d50d6f396" 
    style="border:0px #ffffff none; width:100%;" 
    name="myiFrame" 
    scrolling="no" 
    frameborder="1" 
    marginheight="0px" 
    marginwidth="0px" 
    height="200px" 
    allowfullscreen>
</iframe>   
"""

# Render ad in Streamlit
components.html(ad_html2, height=250)





