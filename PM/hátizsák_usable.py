# Hátizsák feladat dinamikus programozásos megoldása

# ÚTMUTATÓ
# 1. ADD MEG A SÚLYOKAT ÉS ÉRTÉKEKET
# 2. ADD MEG A MAX_WEIGHT-ET
# 3. ADD MEG A HIÁNYZÓ ÉRTÉKEK KOORDINÁTÁIT
# 4. FUTTASD A PROGRAMOT

# Súlyok és értékek
weights = [2,1,2,3,3]  # ADD MEG AZ ELSŐ SORT, VAN BENNE <= JEL
values = [2,6,2,7,7]   # ADD MEG A MÁSODIK SORT, ->MAX VAN BENNE

# A hátizsák maximális súlya (kapacitás)
max_weight = 10 #ADD MEG, HOGY AZ ELSŐ KÉPLET VÉGÉN MILYEN SZÁM ÁLL!!!

# A tételek száma
num_items = len(weights)

# DP tábla inicializálása
dp = [[0] * (max_weight + 1) for _ in range(num_items + 1)]

# A DP tábla kitöltése
for i in range(1, num_items + 1):
    for w in range(max_weight + 1):
        if weights[i - 1] <= w:
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
        else:
            dp[i][w] = dp[i - 1][w]

# Az eredmények megjelenítése
for row in dp:
    print(row)

# A maximális érték a dp[num_items][max_weight] helyen található
print("Maximum érték a hátizsákban:", dp[num_items][max_weight])

# ADD MEG A BETŰK KOORDINÁTÁIT - CSAK OLVASD LE AZ OSZLOPOK SORSZÁMÁT
# A táblázatban szereplő nagybetűs értékek:
A = dp[5][10]
B = dp[4][9]
C = dp[2][7]
D = dp[3][10]
E = dp[3][8]
F = dp[2][10]

print(f"A: {A}")
print(f"B: {B}")
print(f"C: {C}")
print(f"D: {D}")
print(f"E: {E}")
print(f"F: {F}")
