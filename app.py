import streamlit as st

pages = [
        st.Page("welcome.py", title="🏠 Welcome Page"),
        st.Page("essentials.py", title="📘 Learn Essentials"),
        st.Page("predict.py", title="🔎 Stroke Prediction"),
]

pg = st.navigation(pages)
pg.run()