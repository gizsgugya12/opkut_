import numpy as np
from scipy.optimize import linear_sum_assignment

def solve_assignment_problem(cost_matrix, restriction=None, forced_assignment=None):
    """
    Megoldja a hozzárendelési problémát különböző feltételekkel.

    Paraméterek:
    - cost_matrix: A költségmátrix (numpy array).
    - restriction: Tuple (row, col), amely kizár egy hozzárendelést (pl. (2, 3)).
    - forced_assignment: Tuple (row, col), amely kötelezővé teszi egy hozzárendelést (pl. (2, 3)).

    Visszatérési értékek:
    - optimal_cost: Az optimális hozzárendelés költsége.
    """
    large_value = 10**6  # Nagy szám a kizárásokhoz

    # Másolat a költségmátrixról
    modified_matrix = cost_matrix.copy()

    # Korlát (restriction)
    if restriction:
        row, col = restriction
        modified_matrix[row, col] = large_value

    # Kényszer (forced_assignment)
    if forced_assignment:
        row, col = forced_assignment
        forced_cost = cost_matrix[row, col]
        modified_matrix = np.delete(modified_matrix, row, axis=0)  # Sor törlése
        modified_matrix = np.delete(modified_matrix, col, axis=1)  # Oszlop törlése

        # Megoldás a maradék mátrixra
        row_ind, col_ind = linear_sum_assignment(modified_matrix)
        optimal_cost = forced_cost + modified_matrix[row_ind, col_ind].sum()
    else:
        # Megoldás korlátozás nélkül vagy csak kizárással
        row_ind, col_ind = linear_sum_assignment(modified_matrix)
        optimal_cost = modified_matrix[row_ind, col_ind].sum()

    return optimal_cost

# Példa: mátrix megadása
cost_matrix = np.array([
    [8,15,18,4,2],
    [6,10,8,9,20],
    [5,9,10,14,4],
    [2,21,8,21,21],
    [9,5,19,7,13]
])

# 1. Alaphelyzet
print("Alaphelyzet:", solve_assignment_problem(cost_matrix))

# 2. Korlát: 3. munkás nem végezheti a 4. munkát
print("Korlát:", solve_assignment_problem(cost_matrix, restriction=(0, 4))) #-1 a számból, mivel 0tól indexelunk :)

# 3. Kényszer: 3. munkás mindenképp a 4. munkát végzi
print("Kényszer:", solve_assignment_problem(cost_matrix, forced_assignment=(0, 4))) #-1 a számból, mivel 0tól indexelunk :)
