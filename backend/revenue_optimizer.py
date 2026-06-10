import sys
import os
import numpy as np

# ==========================
# ADD REVPY TO PATH
# ==========================

sys.path.append(
    os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "revpy_core"
    )
)

from revpy.optimizers import calc_EMSRb

# ==========================
# SAMPLE AIRLINE DATA
# ==========================

fares = np.array([
    12000,  # Business
    8000,   # Premium
    5000,   # Economy
    3000    # Saver
])

demands = np.array([
    40,
    60,
    120,
    180
])

sigmas = np.array([
    5,
    10,
    20,
    30
])

# ==========================
# EMSRb OPTIMIZATION
# ==========================

protection_levels = calc_EMSRb(
    fares,
    demands,
    sigmas
)

# ==========================
# OUTPUT
# ==========================

print("\n===== EMSRb Revenue Optimization =====\n")

for i, level in enumerate(protection_levels):
    print(
        f"Protection Level {i+1}: "
        f"{round(level, 2)} seats"
    )

print("\nOptimization Complete.")