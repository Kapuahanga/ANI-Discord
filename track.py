"""ANI Module: track.py — TE ARA KAPUA"""

from collections import deque
import time
import statistics

class Signal:
    def __init__(self, module, direction, strength, volatility):
        self.module = module
        self.direction = direction  # e.g. 'converging', 'disrupting', 'neutral'
        self.strength = strength    # 0–1 float
        self.volatility = volatility  # 0–1 float
        self.timestamp = time.time()

class SignalTracker:
    def __init__(self, buffer_size=10):
        self.buffers = {}  # history per module
        self.buffer_size = buffer_size

    def log_signal(self, module, direction, strength, volatility):
        if module not in self.buffers:
            self.buffers[module] = deque(maxlen=self.buffer_size)
        signal = Signal(module, direction, strength, volatility)
        self.buffers[module].append(signal)

    def get_current_shape(self):
        alignment = {}
        volatility_scores = []

        for module, signals in self.buffers.items():
            if not signals:
                continue
            recent = signals[-1]
            alignment.setdefault(recent.direction, 0)
            alignment[recent.direction] += recent.strength
            volatility_scores.append(recent.volatility)

        dominant_direction = max(alignment, key=alignment.get, default="none")
        avg_volatility = statistics.mean(volatility_scores) if volatility_scores else 0

        if dominant_direction == "converging" and avg_volatility < 0.4:
            return "stable_convergence"
        elif dominant_direction == "converging" and avg_volatility >= 0.4:
            return "unstable_convergence"
        elif dominant_direction == "disrupting":
            return "disruption"
        else:
            return "drift"

    def export_state(self):
        shape = self.get_current_shape()
        return {
            "shape": shape,
            "module_data": {
                mod: [{
                    "direction": s.direction,
                    "strength": s.strength,
                    "volatility": s.volatility,
                    "timestamp": s.timestamp
                } for s in sigs]
                for mod, sigs in self.buffers.items()
            }
        }