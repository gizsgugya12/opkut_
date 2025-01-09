import pulp

# ÚTMUTATÓ
# PIP INSTALL PULP A TERMINÁLBAN
# 1. SUPPLY ÉS DEMAND MEGADÁSA
# 2. MÁTRIX KITÖLTÉSE
# FUTTATÁS


# A probléma definiálása
prob = pulp.LpProblem("Transportation_Problem", pulp.LpMinimize)

# Kapacitás és kereslet
supply = [11, 1, 4, 8]  ## ADD MEG A supp. OSZLOP ADATAIT
demand = [4, 1, 2, 2, 4, 6, 2, 3]  ## ADD MEG A dem. SOR ADATAIT

# Költségmátrix - TÖLTSD KI A MÁTRIXT ÚGY, HOGY A SUPP. OSZLOPOT ÉS A DEM. SOR KIHAGYOD
costs = [
    [5, 6, 8, 6, 6, 8, 6, 10],
    [5, 5, 8, 8, 8, 7, 7, 6],
    [8, 8, 6, 7, 5, 7, 10, 9],
    [8, 9, 7, 10, 8, 9, 7, 8]
]

# Változók
routes = [(i, j) for i in range(len(supply)) for j in range(len(demand))]
vars = pulp.LpVariable.dicts("Route", (range(len(supply)), range(len(demand))), lowBound=0, cat='Continuous')

# Célfüggvény
prob += pulp.lpSum([vars[i][j] * costs[i][j] for (i, j) in routes])

# Korlátozások
# Kapacitás korlátozások
for i in range(len(supply)):
    prob += pulp.lpSum([vars[i][j] for j in range(len(demand))]) <= supply[i]

# Kereslet korlátozások
for j in range(len(demand)):
    prob += pulp.lpSum([vars[i][j] for i in range(len(supply))]) >= demand[j]

# A probléma megoldása
prob.solve()

# Eredmények kiírása
print("Az optimális szállítási költség:", pulp.value(prob.objective))
# for v in prob.variables():
#   print(v.name, "=", v.varValue)
