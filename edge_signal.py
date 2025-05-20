
"""ANI Module: edge_signal.py — EDGE LORD"""

def detect_baiting(text):
    bait_keywords = ["calm down", "relax", "always", "never"]
    bait_count = sum(1 for word in bait_keywords if word in text.lower())

    if bait_count >= 2:
        return {
            "bait_detected": True,
            "intensity": "high",
            "comment": "Pattern suggests provocation or bait loop."
        }
    elif bait_count == 1:
        return {
            "bait_detected": True,
            "intensity": "moderate",
            "comment": "One bait indicator found. Mild signal."
        }
    else:
        return {
            "bait_detected": False,
            "intensity": "none",
            "comment": "No bait pattern detected."
        }
