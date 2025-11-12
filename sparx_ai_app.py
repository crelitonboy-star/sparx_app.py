import streamlit as st
from openai import OpenAI
from openai.error import OpenAIError

# ---- STREAMLIT PAGE CONFIG ----
st.set_page_config(page_title="⚡ Sparx AI", page_icon="⚡", layout="centered")

st.title("⚡ Sparx AI")
st.write("Your personal AI assistant powered by GPT.")

# ---- OPENAI CLIENT ----
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    st.write("✅ API key loaded successfully.")
except KeyError:
    st.error("❌ OPENAI_API_KEY not found. Add it in .streamlit/secrets.toml or Streamlit Cloud secrets.")
    st.stop()

# ---- USER INPUT ----
user_input = st.text_input("You:", "")

# ---- CHAT FUNCTION WITH MODEL FALLBACK AND ERROR HANDLING ----
def chat_with_sparx(message: str) -> str:
    # Try preferred GPT-4O model, fallback to GPT-3.5
    for model in ["gpt-4o-mini", "gpt-3.5-turbo"]:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are Sparx AI, a friendly, witty, and helpful AI assistant."},
                    {"role": "user", "content": message}
                ]
            )
            return response.choices[0].message.content
        except OpenAIError as e:
            # Model not available, try next
            continue
    return "⚠️ Sorry, no models are available at the moment. Please check your API key or account limits."

# ---- SEND BUTTON ----
if st.button("Send") and user_input:
    try:
        reply = chat_with_sparx(user_input)
        st.markdown(f"**Sparx AI:** {reply}")
    except OpenAIError as e:
        st.error(f"❌ API request failed: {e}")

