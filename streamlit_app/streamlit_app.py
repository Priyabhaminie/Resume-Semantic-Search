import streamlit as st
import requests

st.title("Resume Semantic Search")

query = st.text_input("Enter your search query")
if st.button("Search"):
    response = requests.post("http://localhost:8000/search", json={"query_text": query})
    results = response.json()
    for result in results:
        st.write(result['payload']['resume_text'])
