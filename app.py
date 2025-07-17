import streamlit as st

st.set_page_config(page_title="Event Registration", page_icon="🎊", layout="centered")

# Use session state to track form submission
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# Page 1: Registration Form
if not st.session_state.submitted:
    st.markdown("<h1 style='color:white;text-shadow:2px 2px 4px #000;'>🎊 EVENT REGISTRATION FORM 🎊</h1>", unsafe_allow_html=True)

    with st.form("reg_form"):
        first = st.text_input("First Name")
        middle = st.text_input("Middle Name")
        last = st.text_input("Last Name")
        gender = st.radio("Gender", ["Male", "Female", "Other"])
        email = st.text_input("Email")
        password = st.text_input("Password (5–10 chars)", type="password")
        birthday = st.date_input("Birthday")

        submitted = st.form_submit_button("Submit 🎉")
        if submitted:
            if first and middle and last and email and (5 <= len(password) <= 10):
                st.session_state.submitted = True
            else:
                st.error("⚠️ Please fill all fields correctly.")
else:
    # Page 2: Happy Birthday
    st.markdown(
        """
        <div style="text-align:center; margin-top:50px;">
            <h1 style="
                font-size:60px;
                color:#fff;
                text-shadow:2px 2px 8px #000;
                animation: zoom 2s infinite alternate;
            ">🎉🎂 Happy Birthday! 🎂🎉</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.balloons()
