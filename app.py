import streamlit as st
from refine import refine_prompt

st.title("Prompt Refiner")

user_input = st.text_area("Enter text to refine:")

if st.button("Refine"):
    refined = refine_prompt(user_input)
    st.text_area("Refined text:", refined, height=150)
