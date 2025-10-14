# SPDX-License-Identifier: Apache-2.0
# (c) 2025 Brian Warren

from __future__ import annotations
from typing import Dict

# Default pillar weights (can be tuned)
DEFAULT_WEIGHTS = {
    "mission": 1.0,
    "humility": 2.0,
    "scaffolding": 1.0,
    "deeds": 1.0,
    "continuity": 1.5,
}

def drc_score(
    scores: Dict[str, float],
    weights: Dict[str, float] = DEFAULT_WEIGHTS,
) -> float:
    """
    Compute a weighted composite DRC score in [0,1].

    - scores: e.g., {"mission":0.93, "humility":0.90, ...}
    - weights: relative importance (defaults above)

    Any missing pillar gets weight 0 for this computation.
    """
    num = 0.0
    den = 0.0
    for k, w in weights.items():
        if k in scores and 0.0 <= scores[k] <= 1.0:
            num += w * scores[k]
            den += w
    return 0.0 if den == 0 else round(num / den, 4)
