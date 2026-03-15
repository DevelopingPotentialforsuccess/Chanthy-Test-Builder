import streamlit as st
import google.generativeai as genai

# This gets your key safely from the settings
key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=key)

st.title("📚 IELTS Test Builder")
st.write("Free AI Test Generator")

# User input
topic = st.text_input("Enter Topic (e.g. Technology, Education)")
test_type = st.selectbox("Test Type", ["Reading", "Listening", "Writing", "Speaking"])

if st.button("Generate Now"):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(f"Create an IELTS {test_type} test about {topic}")
    st.markdown(response.text)
