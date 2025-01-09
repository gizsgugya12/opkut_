from scipy.optimize import linprog



c = [-21, -12]  # gorfri profit, palacsinta profit -SZÁM!!!

A = [
    [70, 40],  # Liszt korlát palacsinta
    [60, 45],  # Tej korlát palacsinta
    [1, 0],
    [0, 1]
]
b = [6500, 6075, 90, 75]  #liszt, tej max, legfeljebb darab gofri, pali
bounds = [(0, None), (0, None)]

# Solve the problem
result_B = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')


A_C = [
    [70, 40],  # Liszt korlát gofri pali
    [60, 45],  # Tej korlát gofri pali
    [0, 1]
]
b_C = [6500 - 70 * 90, 6075 - 60 * 90, 75]  # rendelkezessreallasmax - gofrliszt * legfeljebbmennyidarabkeszit
                                            # rendelkezesreallasmin - gofritej * legfeljebb gofri, lefgeljebb pali

result_C = linprog([-12], A_ub=[[40], [45], [1]], b_ub=b_C, bounds=[(0, None)], method='highs')


c_T1 = [-22, -11]  # 1.terv gofri pali
result_T1 = linprog(c_T1, A_ub=A, b_ub=b, bounds=bounds, method='highs')


c_T2 = [-20, -13]  #2. terv gofri pali
result_T2 = linprog(c_T2, A_ub=A, b_ub=b, bounds=bounds, method='highs')


best_result = result_T1 if result_T1.fun < result_T2.fun else result_T2
g_best, p_best = best_result.x
used_liszt = 70 * g_best + 40 * p_best #gofri liszt , palacsinta liszt
used_tej = 60 * g_best + 45 * p_best #gofri tej, palacsinta tej
remaining_liszt = 6500 - used_liszt #liszt max
remaining_tej = 6075 - used_tej #tej max

print(result_B.fun*-1)
print(result_C.x[0])
print(-best_result.fun)
print(remaining_tej)
print(remaining_liszt)