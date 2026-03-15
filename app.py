import streamlit as st
import google.generativeai as genai

# Use the SINGULAR name here
key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=key)

st.title("📚 IELTS Test Builder")
st.write("Testing with 1 API Key")

topic = st.text_input("Enter Topic (e.g. Science)")

if st.button("Generate"):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(f"Create an IELTS reading test about {topic}")
    st.markdown(response.text)
