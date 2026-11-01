import random
import streamlit as st

st.title("Anomaly Checker")
st.write("Enter names and see the result (random, just for fun).")

names = [st.text_input(f"Enter name {i + 1}", key=f"name_{i}") for i in range(3)]

if st.button("Check"):
    for name in names:
        if name.strip():
            result = random.choice(["gay", "straight"])
            st.write(f"**{name}** is {result}.")
