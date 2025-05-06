import numpy as np
from scipy.optimize import fsolve

# Given values
Pc = 4.17e6  # Chamber pressure in Pascals
gamma = 1.37
epsilon = 10  # Expansion ratio (Ae/At)

# Area-Mach number function for isentropic flow
def area_mach_relation(M, gamma, epsilon):
    term1 = (2 / (gamma + 1)) * (1 + ((gamma - 1) / 2) * M**2)
    term2 = (term1) ** ((gamma + 1) / (2 * (gamma - 1)))
    return (1 / M) * term2 - epsilon

# Solve for exit Mach number (Me)
Me_initial_guess = 3.0
Me_solution = fsolve(area_mach_relation, Me_initial_guess, args=(gamma, epsilon))[0]

# Calculate Pe/Pc using isentropic pressure ratio
Pe_Pc = (1 + (gamma - 1)/2 * Me_solution**2) ** (-gamma / (gamma - 1))

# Calculate Pe
Pe = Pe_Pc * Pc  # in Pascals
Pe_kPa = Pe / 1000  # Convert to kPa

print(f"Exit Mach number (Me): {Me_solution:.3f}")
print(f"Nozzle exit pressure (Pe): {Pe_kPa:.2f} kPa")
