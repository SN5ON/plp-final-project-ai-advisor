import spacy

# Load spaCy English model (already pre-installed via setup.sh)
nlp = spacy.load("en_core_web_sm")

def extract_money(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "MONEY":
            amount_str = ''.join(ch for ch in ent.text if ch.isdigit())
            if amount_str.isdigit():
                return int(amount_str)
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
    doc = nlp(user_input.lower())
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
