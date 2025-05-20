"""ANI Module: quant.py — TOUARANGI"""

class QuantEngine:
    def __init__(self):
        self.module_weights = {
            'tone.py': 1.0,
            'ka_mahi.py': 1.1,
            'edge_signal.py': 1.2,
            'record.py': 0.8,
            'filter.py': 1.0
        }
        self.thresholds = {
            "record_only": 0.4,
            "bridge_check": 0.6,
            "strike_ready": 0.75
        }

    def compute_ncs(self, track_state):
        total_score = 0
        total_weight = 0

        for module, entries in track_state["module_data"].items():
            if not entries:
                continue
            latest = entries[-1]

            direction = latest["direction"]
            strength = latest["strength"]
            volatility = latest["volatility"]
            weight = self.module_weights.get(module, 1.0)

            if direction == "converging":
                dir_factor = 1
            elif direction == "disrupting":
                dir_factor = -1
            else:
                dir_factor = 0.3

            volatility_penalty = 1 - volatility
            score = dir_factor * strength * volatility_penalty * weight

            total_score += score
            total_weight += weight

        ncs_score = total_score / total_weight if total_weight else 0

        if ncs_score < self.thresholds["record_only"]:
            status = "record_only"
        elif ncs_score < self.thresholds["bridge_check"]:
            status = "bridge_check"
        else:
            status = "strike_ready"

        return {
            "ncs_score": round(ncs_score, 4),
            "convergence_shape": track_state["shape"],
            "status": status
        }