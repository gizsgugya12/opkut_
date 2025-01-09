import numpy as np
from scipy.optimize import linear_sum_assignment

# !!ÚTMUTATÓ!!
# A numpy ÉS scipy LEGYEN LETÖLTVE, HA NINCS ->TERMINAL pip install ...
# 1. KÖLTSÉGMÁTRIXOT PONTOSAN TÖLTSD KI
# 2. MENJ LE A MAIN-BE ÉS ÍRD BE A MUNKÁS ÉS MUNKA SORSZÁMÁT
# 3. NÉZD MEG, HOGY A "B" ÉS "C" FELADATBAN UGYANAZOK A SORSZÁMOK VANNAK-E
# 4. HA NEM, KÉZZEL ÍRD BE A FÜGGVÉNYBE A SORSZÁMOKAT

# Költségmátrix definiálása - EZT ADD MEG
cost_matrix = np.array([
    [22, 2, 11, 22, 16],
    [5, 18, 13, 10, 20],
    [21, 4, 22, 8, 5],
    [19, 4, 22, 4, 7],
    [7, 20, 22, 6, 14]
])


def optimalis_hozzarendeles(cost_matrix):
    """
    Alap optimális hozzárendelés meghatározása.
    """
    row_indices, col_indices = linear_sum_assignment(cost_matrix)
    optimal_cost = cost_matrix[row_indices, col_indices].sum()
    print("Az optimális hozzárendelés:")
    for i, j in zip(row_indices, col_indices):
        print(f"Munkás {i + 1} → Munka {j + 1}")
    print(f"Az optimális hozzárendelés költsége: {optimal_cost}")
    return optimal_cost


def korlatozott_hozzarendeles(cost_matrix, munkas_sorszama, munka_sorszama):
    """
    Korlátozott hozzárendelés meghatározása, ha egy munkás nem végezhet el egy adott munkát.
    """
    x = munkas_sorszama - 1
    y = munka_sorszama - 1
    cost_matrix[x, y] = 1e9  # Nagyon nagy szám, hogy kizárjuk ezt a hozzárendelést
    return optimalis_hozzarendeles(cost_matrix)


def kenyszeritett_hozzarendeles(cost_matrix, munkas_sorszama, munka_sorszama):
    """
    Kényszerített hozzárendelés meghatározása, ha egy munkás mindenképpen el kell végezze az adott munkát.
    """
    x = munkas_sorszama - 1
    y = munka_sorszama - 1
    biztos_szam = cost_matrix[x, y]
    cost_matrix[x, :] = 1e9  # Nagyon nagy szám, az egész sort nagy számra állítjuk be
    cost_matrix[x, y] = biztos_szam  # Az egy munkás-munka párost beállítjuk kicsire
    return optimalis_hozzarendeles(cost_matrix)


# Fő program
if __name__ == "__main__":
    munkas_sorsz = 4  ## EZT ADD MEG
    munka_sorsz = 2  ## EZT ADD MEG
    print("Alap eset:")
    optimalis_hozzarendeles(cost_matrix.copy())

    print(f"\nKorlátozott eset - {munkas_sorsz}. munkás nem végezheti az {munka_sorsz}. munkát:")
    korlatozott_hozzarendeles(cost_matrix.copy(), munkas_sorsz, munka_sorsz)

    print(f"\nKényszerített eset - {munkas_sorsz}. munkás mindenképpen a {munka_sorsz}. munkát végzi:")
    kenyszeritett_hozzarendeles(cost_matrix.copy(), munkas_sorsz, munka_sorsz)
