import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets[API_KEY])
models= genai.list_models()

model= genai.GenerativeModel("gemini-2.5-flash")

st.title("AI cover letter generator")

st.subheader("Experimenting with this Chatbot")

st.write("Hello, how may i help you?")

jobtitle = st.text_input("Enter the job title")

resume_summary = st.text_input("enter the resume summary")




if st.button("Generate cover letter"):
    if jobtitle and resume_summary:
        prompt = f"Write A Cover Letter for {jobtitle} using these resume points: {resume_summary}"
        response = model.generate_content(prompt)
        st.write(response.text)
else:
    st.warning("Please provide both job title and resume summary.")
