import streamlit as st
import pandas as pd
from advisor_logic import get_advice, personalised_advice
from data_simulation import load_sample_users
import spacy
import subprocess
import importlib.util

# --- Ensure spaCy model is available ---
model_name = "en_core_web_sm"
if importlib.util.find_spec(model_name) is None:
    subprocess.run(["python", "-m", "spacy", "download", model_name])

nlp = spacy.load(model_name)

# --- Streamlit Config ---
st.set_page_config(page_title="Africa Investment Advisor", page_icon="💸")

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Chatbot", "Personalised Advice", "Upload User CSV"])

# --- Helper Function: Display Chat Messages ---
def display_chat(chat_history):
    for speaker, message in chat_history:
        with st.chat_message("user" if speaker == "🧑 You" else "assistant"):
            st.markdown(f"**{speaker}**: {message}")

# --- Page: Chatbot ---
if page == "Chatbot":
    st.title("💬 AI Investment Advisor for Africa - Chatbot")
    st.markdown("Ask about saving, investing, or growing income in your country.")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("💬 Your question", placeholder="E.g., If I have $300000, where should I invest in Kenya?")

    if user_input:
        response = get_advice(user_input)
        st.session_state.chat_history.append(("🧑 You", user_input))
        st.session_state.chat_history.append(("🤖 Advisor", response))

    display_chat(st.session_state.chat_history)

# --- Page: Personalised Advice ---
elif page == "Personalised Advice":
    st.title("📊 Personalised Investment Advice")
    st.markdown("Enter your financial details below to get personalised advice.")

    col1, col2 = st.columns(2)
    with col1:
        income = st.number_input("Monthly Income ($)", min_value=0)
        expenses = st.number_input("Monthly Expenses ($)", min_value=0)
        savings = st.number_input("Current Savings ($)", min_value=0)
    with col2:
        risk_level = st.selectbox("Risk Level", options=["low", "medium", "high"])
        goal = st.text_input("Investment Goal (e.g., buy land, educate children)")

    if st.button("Get Personalised Advice"):
        if income > 0 and expenses > 0:
            advice = personalised_advice(income, expenses, savings, risk_level, goal)
            st.markdown(advice)
        else:
            st.warning("Please enter valid income and expenses.")

# --- Page: Upload CSV ---
elif page == "Upload User CSV":
    st.title("📁 Upload User Data")
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
            st.write("Preview of uploaded data:")
            st.dataframe(df.head())

            st.markdown("Generating personalised advice for each user:")

            for idx, row in df.iterrows():
                st.markdown(f"**User {int(row['user_id'])} ({row.get('country', 'N/A')}):**")
                advice = personalised_advice(
                    income=row.get('monthly_income', 0),
                    expenses=row.get('monthly_expenses', 0),
                    savings=row.get('savings', 0),
                    risk_level=row.get('risk_level', 'low'),
                    goal=row.get('goal', 'N/A')
                )
                st.markdown(advice)
                st.markdown("---")

        except Exception as e:
            st.error(f"Error reading the file: {e}")

# --- Sidebar Footer ---
st.sidebar.markdown("---")
st.sidebar.markdown("💡 **Tip:** Use the Chatbot for quick advice or Personalized Advice for tailored guidance.")
