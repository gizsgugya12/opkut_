import numpy as np

# ÚTMUTATÓ
# numpy LEGYEN INSTALLÁLVA
# 1. A MÁTRIXOT TÖLTSD KI ÚGY, AHOGY A FELADAT ÍRJA
# 2. MENJ LE A #MÁSODIK ESET KOMMENTHEZ, ADD MEG A KÉT KOORDINÁTÁT ÉS A KÉT ÚJ ÖSSZEGET
# FUTTATÁS


# Eredeti költségmátrix - EZT ADD MEG

original_cost_matrix = np.array([
    [np.inf, 7, 10, 6, 9, 7, 10],
    [7, np.inf, 11, 12, 11, 13, 12],
    [10, 11, np.inf, 9, 10, 12, 6],
    [6, 12, 9, np.inf, 8, 11, 9],
    [9, 11, 10, 8, np.inf, 4, 6],
    [7, 13, 12, 11, 4, np.inf, 13],
    [10, 12, 6, 9, 6, 13, np.inf]
])


def calculate_mst_cost(cost_matrix):
    # Élek listájának előkészítése (költség, telephely1, telephely2)
    edges = []
    for i in range(len(cost_matrix)):
        for j in range(i + 1, len(cost_matrix)):
            if cost_matrix[i, j] != np.inf:
                edges.append((cost_matrix[i, j], i, j))

    # Kruskal-algoritmus alkalmazása
    edges.sort()  # Élek rendezése költség szerint növekvő sorrendben
    parent = list(range(len(cost_matrix)))  # Szülőcsúcsok inicializálása

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_y] = root_x

    mst_cost = 0
    mst_edges = []

    for edge in edges:
        cost, u, v = edge
        if find(u) != find(v):
            union(u, v)
            mst_cost += cost
            mst_edges.append((u, v))

    return mst_cost, mst_edges


# Első eset: eredeti költségmátrix
cost_matrix_1 = original_cost_matrix.copy()
mst_cost_1, mst_edges_1 = calculate_mst_cost(cost_matrix_1)

print(f"Az optimális hálózat költsége: {mst_cost_1} millió forint")
print("Az optimális hálózat élei:")
for u, v in mst_edges_1:
    print(f"Telephely {u + 1} ↔ Telephely {v + 1}")

# Második eset: módosult költségmátrix - EZEKET ADD MEG
modositott_arak = {
    (1, 5): 10,
    (5, 7): 8
}

cost_matrix_2 = original_cost_matrix.copy()
for (i, j), uj_ar in modositott_arak.items():
    cost_matrix_2[i - 1, j - 1] = uj_ar
    cost_matrix_2[j - 1, i - 1] = uj_ar  # Bidirectional

mst_cost_2, mst_edges_2 = calculate_mst_cost(cost_matrix_2)

print(f"Az új optimális hálózat költsége: {mst_cost_2} millió forint")
print("Az új optimális hálózat élei:")
for u, v in mst_edges_2:
    print(f"Telephely {u + 1} ↔ Telephely {v + 1}")
