import streamlit as st
from openai import OpenAI

# ---- STREAMLIT PAGE CONFIG ----
st.set_page_config(page_title="⚡ Sparx AI", page_icon="⚡", layout="centered")

st.title("⚡ Sparx AI")
st.write("Your personal AI assistant powered by GPT-4.")

# ---- OPENAI CLIENT ----
# Works both locally (via .streamlit/secrets.toml) or on Streamlit Cloud
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ---- USER INPUT ----
user_input = st.text_input("You:", "")

# ---- CHAT FUNCTION ----
def chat_with_sparx(message: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are Sparx AI, a friendly, witty, and helpful AI assistant."},
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message.content

# ---- SEND BUTTON ----
if st.button("Send") and user_input:
    reply = chat_with_sparx(user_input)
    st.markdown(f"**Sparx AI:** {reply}")
