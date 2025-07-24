# AI Investment Advisor for Africa

A clean, web-based AI assistant built with Streamlit to provide financial guidance for low income individuals, thus includes freelancer's, unemployed hustler's, and the general informal sector in Africa. Design to get them started on increasing their earnings and planning their long term future. Great for learners, advisors, and entrepreneurs.
It meets the SDG requirments of the project mainly SDG 1: No Poverty – Promotes financial resilience

SDG 8: Decent Work & Economic Growth – Supports income generation

SDG 10: Reduced Inequalities – Brings guidance to marginalized groups

SDG 17: Partnerships – Scalable tool for NGOs, financial institutions

---
## 🌍 Overview
An AI-powered financial advisor designed to assist beginner investors across African countries with localised, easy to-understand advice on saving, investing, and growing income.

This project is part of the **PLP Software Engineering Final Project** and uses **Streamlit** to build an interactive web app that includes:

- A **natural language chatbot**
- A **personalized investment recommendation tool**
- Support for **bulk advice via CSV uploads**
- Mobile friendly and deployable as a simple web app

---
##  Features
| Feature                        | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| 💬 AI Chatbot                 | Ask open-ended financial questions like: "Where can I invest with $100?"   |
| 📊 Personalized Advice         | Input income, expenses, savings, and get risk-based investment guidance     |
| 📁 CSV Upload                  | Upload user financial data and get bulk personalized advice                 |
| 🌐 Country-Aware Tips          | Gives custom tips for Kenya 🇰🇪, Nigeria 🇳🇬, SA 🇿🇦, Uganda 🇺🇬, Ghana 🇬🇭, Zimbabwe 🇿🇼 |
| 🧠 Rule-Based NLP              | Uses keyword detection & logic scoring (no heavy ML)                        |
| ☁️ Deployable App              | Designed to run on Streamlit Community Cloud or locally                     |

---
- **Chatbot Advisor** — Ask anything about saving or investing in various African countries, and get intelligent responses.
- **Personalised Advice** — Input personal finance details or upload multiple profiles via CSV to get tailored financial guidance.
- **📂 CSV Upload** — Bulk-process financial data and generate advice for multiple users.
- **📋 Financial Readiness Score** — Evaluates emergency fund, income/expenditure, and risk tolerance.
- **💾 Chat History** — Stores chat logs in `chat_history.csv` with timestamps.

---

##  How It Works

**Chatbot:**  
Uses **spaCy NLP** to extract money amounts and country mentions for contextual responses.

**Personalised Advice:**  
A rule based decision system guides saving, investing, and financial goal attainment.

**CSV Feature:**  
Upload a structured CSV to advice multiple users in one go.

---

##  Getting Started

1. Clone the repo:
    ```bash
    git clone https://github.com/SN5ON/ai-investment-advisor.git
    cd ai-investment-advisor
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    python -m spacy download en_core_web_sm
    ```
3. Run locally:
    ```bash
    streamlit run app.py
    ```

---

## 📂 CSV Format Example
an example of the csv format is in the repository
```csv
user_id,country,monthly_income,monthly_expenses,savings,risk_level,goal
1,Kenya,132,117,43,medium,educate children
2,Nigeria,120,90,50,low,save for emergencies
3,South Africa,200,150,150,medium,invest in stocks

https://plp-final-project-ai-advisor-bqeqxl25yykhtxe66xrvih.streamlit.app/