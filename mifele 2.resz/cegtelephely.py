import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree

# Eredeti költségmátrix
cost_matrix = np.array([
    [np.inf, 11,11,8,8,6,10],
    [11, np.inf, 10, 9, 11, 9, 7],
    [11, 10, np.inf, 8, 4, 9, 10],
    [8, 9, 8, np.inf, 8, 10, 9],
    [8, 11, 4, 8, np.inf, 13, 12],
    [6, 9, 9, 10, 13, np.inf, 12],
    [10, 7, 10, 9, 12, 12, np.inf]
])

# Minimális feszítőfa (MST) kiszámítása
mst_original = minimum_spanning_tree(cost_matrix)
original_cost = mst_original.sum()

# Költségmátrix frissítése az új árakkal
cost_matrix_updated = cost_matrix.copy()
cost_matrix_updated[1, 3] = 10  #szam -1 a szambol!!! csak [] -nél
cost_matrix_updated[3, 1] = 10  #uaz a szam csak fordítva
cost_matrix_updated[3, 4] = 10  #szam -1 a szambol!!! csak [] -nél
cost_matrix_updated[4, 3] = 10  #uaz a szam csak fordítva

# Minimális feszítőfa kiszámítása az új költségekkel
mst_updated = minimum_spanning_tree(cost_matrix_updated)
updated_cost = mst_updated.sum()

print(original_cost)
print(updated_cost)
