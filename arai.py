"""ANI Bot 3: Ārai — Guardian Against Synthetic Language"""

import statistics
import time

class AraiSignal:
    def __init__(self, module, fluency, volatility, structure_depth, contradiction_score):
        self.module = module
        self.fluency = fluency
        self.volatility = volatility
        self.structure_depth = structure_depth
        self.contradiction_score = contradiction_score
        self.timestamp = time.time()

class AraiScreen:
    def __init__(self):
        self.signals = []

    def input_text(self, source_text):
        # Replace these with real module outputs in the future
        tone_signal = AraiSignal("tone.py", fluency=0.9, volatility=0.2, structure_depth=0.6, contradiction_score=0.2)
        logic_signal = AraiSignal("logic.py", fluency=0.8, volatility=0.3, structure_depth=0.4, contradiction_score=0.5)
        ka_mahi_signal = AraiSignal("ka_mahi.py", fluency=0.85, volatility=0.25, structure_depth=0.5, contradiction_score=0.3)
        
        self.signals = [tone_signal, logic_signal, ka_mahi_signal]

    def detect_artificiality(self):
        if not self.signals:
            return "No input."

        fluencies = [s.fluency for s in self.signals]
        volatilities = [s.volatility for s in self.signals]
        structures = [s.structure_depth for s in self.signals]
        contradictions = [s.contradiction_score for s in self.signals]

        avg_fluency = statistics.mean(fluencies)
        avg_volatility = statistics.mean(volatilities)
        avg_structure = statistics.mean(structures)
        avg_contradiction = statistics.mean(contradictions)

        if avg_fluency > 0.85 and avg_volatility < 0.3 and avg_structure < 0.5 and avg_contradiction < 0.4:
            return {
                "status": "Likely Synthetic",
                "confidence": round((avg_fluency + (1 - avg_volatility) + (1 - avg_structure)) / 3, 2),
                "shape": "Fluency without relational volatility",
                "note": "Language may lack relational signature"
            }
        else:
            return {
                "status": "Likely Human",
                "confidence": round(1 - abs(avg_contradiction - avg_volatility), 2),
                "shape": "Natural emotional range",
                "note": "Volatility and structure reflect relational experience"
            }