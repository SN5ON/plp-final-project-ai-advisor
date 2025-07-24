import re

# Extract amount from text manually (no spaCy)
def extract_money(text):
    matches = re.findall(r"\$\s?\d+(?:,\d{3})*(?:\.\d+)?|\d{3,}", text)
    if matches:
        amount_str = matches[0].replace("$", "").replace(",", "")
        try:
            return int(float(amount_str))
        except ValueError:
            return None
    return None

def extract_countries(text):
    countries = []
    country_keywords = {
        "kenya": "🇰🇪",
        "south africa": "🇿🇦",
        "nigeria": "🇳🇬",
        "zimbabwe": "🇿🇼",
        "uganda": "🇺🇬",
        "ghana": "🇬🇭",
        "usa": "🇺🇸",
    }
    text_lower = text.lower()
    for country, emoji in country_keywords.items():
        if country in text_lower:
            countries.append((country.title(), emoji))
    return countries

def get_advice(user_input):
    responses = []
    amount = extract_money(user_input)
    countries = extract_countries(user_input)

    if amount:
        if amount < 100:
            responses.append("📉 With less than $100, start by saving and using mobile investment platforms.")
        elif amount < 1000:
            responses.append("💰 Consider mutual funds, local ETFs, or fractional shares.")
        elif amount < 100000:
            responses.append("📈 Diversify: stocks, government bonds, maybe small real estate investment.")
        else:
            responses.append("🚀 With this capital, consult a licensed advisor for custom asset allocation (stocks, land, business, crypto, etc.).")

    for country, emoji in countries:
        if country.lower() == "kenya":
            responses.append(f"{emoji} Use AIB DigiTrader, Faida, or M-Akiba (via M-Pesa) for investing in Kenya.")
        elif country.lower() == "south africa":
            responses.append(f"{emoji} Use EasyEquities or Satrix from as little as R5 in South Africa.")
        elif country.lower() == "nigeria":
            responses.append(f"{emoji} Try Bamboo, Risevest, or Trove with ₦1000+ for stock access in Nigeria.")
        elif country.lower() == "zimbabwe":
            responses.append(f"{emoji} Try C-Trade to access ZSE with small capital in Zimbabwe.")
        elif country.lower() == "uganda":
            responses.append(f"{emoji} Try Crested Capital for Uganda Securities Exchange.")
        elif country.lower() == "ghana":
            responses.append(f"{emoji} Use EDC or Databank to start investing in Ghana.")
        elif country.lower() == "usa":
            responses.append(f"{emoji} Use EasyEquities, Bamboo, or Risevest for global ETFs like S&P 500.")

    if not responses:
        responses.append("🤖 I'm here to help with beginner investing across Africa. Ask about savings, stocks, or local options.")

    return "\n\n".join(responses)

def personalised_advice(income, expenses, savings, risk_level, goal):
    advice = []
    emergency_fund = expenses * 3

    advice.append(f"Your monthly income is ${income}, and expenses are ${expenses}.")
    advice.append(f"Recommended emergency fund: at least ${emergency_fund} (3 months of expenses).")

    if savings < emergency_fund:
        advice.append(f"💡 Build your emergency fund first. You currently have ${savings} saved.")
    else:
        advice.append(f"✅ You have sufficient emergency savings. You can start investing toward your goal: '{goal}'.")

        if risk_level == "low":
            advice.append("📉 Recommended: low-risk investments like treasury bonds, fixed deposits, or mutual funds.")
        elif risk_level == "medium":
            advice.append("📈 Consider a balanced portfolio with a mix of bonds and stocks, or local ETFs.")
        else:
            advice.append("🚀 You might explore higher-risk investments such as stocks or selected cryptocurrencies cautiously.")

    return "\n".join(advice)
