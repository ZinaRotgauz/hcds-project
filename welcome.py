import streamlit as st

st.set_page_config(page_title="Welcome Page", layout="wide")

st.title("🧠 BrainUX")
st.markdown("Welcome to the Stroke Prediction Assistant. Choose an option to begin:")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    c1, c2 = st.columns(2)
    with c1:
        st.page_link("predict.py", label="➡️ Get Started with Prediction", icon="🚀")
    with c2:
        st.page_link("essentials.py", label="📘 Learn Essentials", icon="📖")
