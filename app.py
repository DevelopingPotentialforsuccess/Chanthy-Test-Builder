import streamlit as st
import google.generativeai as genai
import random

# 1. Get the list of 10 keys from secrets
keys_list = st.secrets["GEMINI_API_KEYS"]

# 2. Pick a random key for this specific request
selected_key = random.choice(keys_list)
genai.configure(api_key=selected_key)

st.title("📚 IELTS Test Builder (Turbo Mode)")
st.write(f"Using a rotating pool of {len(keys_list)} keys")

topic = st.text_input("Enter Topic")
test_type = st.selectbox("Test Type", ["Reading", "Listening", "Writing", "Speaking"])

if st.button("Generate Now"):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(f"Create an IELTS {test_type} test about {topic}")
    st.markdown(response.text)
