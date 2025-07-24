import pandas as pd

def load_sample_users():
    data = {
        "user_id": [1, 2, 3, 4, 5],
        "country": ["Kenya", "South Africa", "South Africa", "South Africa", "Nigeria"],
        "monthly_income": [132, 136, 132, 244, 117],
        "monthly_expenses": [117, 75, 123, 196, 110],
        "savings": [43, 81, 27, 58, 42],
        "risk_level": ["medium", "low", "low", "medium", "low"],
        "goal": [
            "educate children",
            "buy land",
            "save for emergencies",
            "buy land",
            "save for emergencies"
        ]
    }
    return pd.DataFrame(data)
