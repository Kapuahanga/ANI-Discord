
"""ANI Module: ka_mahi.py — SARC BOT"""

def detect_sarcasm(text):
    # Mocked tone dissonance checker
    if "yeah right" in text.lower() or "totally" in text.lower():
        return {
            "sarcasm_level": "high",
            "tone_match": False,
            "comment": "Tone mismatch detected. Possible sarcasm."
        }
    return {
        "sarcasm_level": "low",
        "tone_match": True,
        "comment": "Tone appears aligned."
    }
