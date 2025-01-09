import numpy as np

# ÚTMUTATÓ
# 1. A táblát töltsd ki pontosan
# 2. Add meg a generálóelem koordinátáit, figyelj arra, hogy a sor és oszlopok sorszáma 0-tól számítódik
# tehát, ami a 2.sor 3. oszlopában van (1,2) koordinátát kap
# 3. menj le a hiányzó értékekhez, töltsd ki és itt is figyelj a helyes koordináták megadására

# Első szimplex tábla (adott értékek) - EZT ADD MEG
table1 = np.array([
    [1, -2, 3, 2, -3, 30],  # a6
    [1, 3, -1, 3, 1, 15],  # a7
    [3, -3, 3, -1, 3, 25],  # a8
    [-2, 1, -3, -3, -2, 0]  # z - c sor
], dtype=float)

# Generáló elem (pivot elem helye) - EZT ADD MEG
pivot_row = 2  # HA 3. SORBAN VAN -> 3-1 = 2-ŐT ADJ MEG
pivot_col = 2  # HA AZ 5. OSZLOPBAN VAN -> 5-1= 4-ET ADJ MEG
pivot_element = table1[pivot_row, pivot_col]

# Második szimplex tábla inicializálása
table2 = np.zeros_like(table1)

# Pivot sor normalizálása
table2[pivot_row, :] = table1[pivot_row, :] / pivot_element
table2[pivot_row, pivot_col] = 1 / pivot_element  # A generáló elem reciproka

# Frissítjük a többi sort
for i in range(len(table1)):
    if i != pivot_row:
        # Generáló oszlop frissítése
        table2[i, pivot_col] = table1[i, pivot_col] / (pivot_element * -1)
        # Egyéb értékek frissítése
        for j in range(len(table1[0])):
            if j != pivot_col:
                table2[i, j] = table1[i, j] - table1[i, pivot_col] * table2[pivot_row, j]

# Kiírjuk az eredményeket
print("Második szimplex tábla:")
print(np.round(table2, 5))

# Hiányzó értékek azonosítása; [sor-1, oszlop-1]
missing_values = {
    "A": table2[3, 3],  # A helyén lévő érték
    "B": table2[2, 0],  # B helyén lévő érték
    "C": table2[1, 3],  # C helyén lévő érték
    "D": table2[2, 4],  # D helyén lévő érték
    "E": table2[2, 3],  # E helyén lévő érték
    "F": table2[0, 0],  # F helyén lévő érték
    "G": table2[1, 5],  # G helyén lévő érték
    "H": table2[3, 2],  # H helyén lévő érték
    "I": table2[1, 2],  # I helyén lévő érték
    "J": table2[2, 5],  # J helyén lévő érték
    "K": table2[3, 1],  # K helyén lévő érték
    "L": table2[3, 4],  # L helyén lévő érték
}

print("\nHiányzó értékek:")
for key, value in missing_values.items():
    print(f"{key} = {np.round(value, 5)}")
