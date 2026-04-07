import streamlit as st
import time

st.set_page_config(page_title="🎉 Totally Serious Birthday App 😌", layout="centered")

# 🎨 Fun CSS
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #a18cd1, #fbc2eb);
}
.title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    color: #222;
}
.msg {
    text-align: center;
    font-size: 22px;
    margin-top: 20px;
}
.stButton>button {
    background-color: black;
    color: white;
    font-size: 20px;
    border-radius: 10px;
    padding: 10px 25px;
    transition: 0.3s;
}
.stButton>button:hover {
    background-color: #ff4b4b;
    transform: scale(1.1);
}
</style>
""", unsafe_allow_html=True)

# 😂 Dramatic Title
title = "🎂 BREAKING NEWS 🎂"
title_placeholder = st.empty()

for i in range(len(title)+1):
    title_placeholder.markdown(f"<div class='title'>{title[:i]}</div>", unsafe_allow_html=True)
    time.sleep(0.05)

# 😏 Funny Messages
messages = [
    "Important News!,Konjam kelunga 😌",  
"Inniku oruthi young nu nenaikirah 😏 ",
"Aana body already aunty😂 mode la irukku😂😂"
]

msg_placeholder = st.empty()

for msg in messages:
    for i in range(len(msg)+1):
        msg_placeholder.markdown(f"<div class='msg'>{msg[:i]}</div>", unsafe_allow_html=True)
        time.sleep(0.02)
    time.sleep(0.6)

st.balloons()

# 🎁 Suspicious Button
if "clicked" not in st.session_state:
    st.session_state.clicked = False

st.write("")

if st.button("👉 Do NOT Click This Button 👀"):
    st.session_state.clicked = True

# 😈 After clicking
if st.session_state.clicked:

    st.warning("😳 Oh no... you clicked it...")

    fake_loading = st.empty()

    for i in range(0, 101, 10):
        fake_loading.progress(i)
        time.sleep(0.2)

    st.error("🚨 SYSTEM OVERLOAD: TOO MUCH CLOWNESS🤡 DETECTED 🚨")
    time.sleep(1)

    st.success("🎉 Okay fine... Pirandha Naal Nalvaazhthukal!!! 🎉")
    st.snow()

    st.markdown("<h3 style='text-align:center;'>🎬 Proof that you're getting older 😏</h3>", unsafe_allow_html=True)

    # 🎬 Replace with your video
    st.video("https://drive.google.com/file/d/17zRgvUk5hiYa37gpO-LyRN3aG_fJdhyN/view?usp=sharing")
    
    st.markdown("""
    <h2 style='text-align:center;'>
   https://drive.google.com/file/d/17zRgvUk5hiYa37gpO-LyRN3aG_fJdhyN/view?usp=sharing
    </h2>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h2 style='text-align:center;'>
    Another year older... but not wiser 😂💖
    </h2>
    """, unsafe_allow_html=True)