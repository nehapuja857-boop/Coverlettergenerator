import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY]")
model= genai.GenerativeModel("gemini-2.5-flash")
st.title("Email Summarizer")
body= st.text_area("Write the proper email")

if st.button("generate the email"):
    if body:
        prompt= f"Summarize this email into 3-5 bullet points: {body}"
        response= model.generate_content(prompt)
        st.write(response.text)
    else:
        st.warning("provide the proper email")
    

