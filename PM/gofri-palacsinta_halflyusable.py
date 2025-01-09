from scipy.optimize import linprog

#Minuszok maradnak köcsögdió

# Terv 0: (ide kerülnek az eredeti árak)
c = [-21, -12]  # Tehát ide írod az árakat ( elŐSZÖR GOFRI AZTÁN PALACSINTA mínusz marad)

# Terv 1: Amit a feladat szövege ír ott a terveknek az ára
c1 = [-22, -11]  # Tehát ide írod az árakat ( elŐSZÖR GOFRI AZTÁN PALACSINTA mínusz marad)

# Amit a feladat szövege ír ott a terveknek az ára
c2 = [-20, -13] #Tehát ide írod az árakat ( elŐSZÖR GOFRI AZTÁN PALACSINTA mínusz marad)


A = [
    [70, 40],  # Liszt korlátozása -> Behugyozod, hogy a gofrihoz és a palacsintához a liszt az mennyi
    [60, 45],  # Tej korlátozása -> Behugyozod, hogy a gofrihoz és a palacsintához a tej az mennyi
    [-1, 0],   # Gofri maximális darabszám
    [0, -1],   # Palacsinta maximális darabszám
]

# Korlátok -> (tej max, liszt max, max gofri, max pala)
b = [6500, 6075, 90, 75]

# Változók nem negatívak
x_bounds = (0, None)
y_bounds = (0, None)

# 1. kérdés: Legnagyobb profit az eredeti árakkal
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# 2. kérdés: Ha palacsinta ENNYI, akkor hány gofrik férnek bele a maximális korlátozásokba?
palacsinta_adott = 90  # Behugyozod a feladat szerint a g=számot


result1 = linprog(c1, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')


result2 = linprog(c2, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')


if result.success and result1.success and result2.success:

    gofri_darab = result.x[0]
    palacsinta_darab = result.x[1]
    profit = -result.fun


    print(f"Optimális termelési terv (eredeti árak):")
    print(f"Gofrik száma: {int(gofri_darab)}")
    print(f"Palacsinták száma: {int(palacsinta_darab)}")
    print(f"Maximális profit: {int(profit)} peták")
    print()


    if palacsinta_adott >= palacsinta_darab:

        gofri_max_liszt = (6500 - 40 * palacsinta_adott) / 70 #(Liszt max - pala liszt max * palacsinta_adott) / gofri liszt max

        gofri_max_tej = (6875 - 45 * palacsinta_adott) / 60 #(Tej max - pala tej max * palacsinta_adott) / gofri tej max

        gofri_max = min(gofri_max_liszt, gofri_max_tej, 90)  #Behugyozod a gofri maxot
        print(f"Ha palacsinta = {palacsinta_adott}, akkor a gofri darabszám: {int(gofri_max)}")
    else:
        print(f"A megadott palacsinta darabszám ({palacsinta_adott}) nem lehet nagyobb, mint a maximális ({float(palacsinta_darab)}).")

    #
    gofri_darab1 = result1.x[0]
    palacsinta_darab1 = result1.x[1]
    profit1 = -result1.fun


    gofri_darab2 = result2.x[0]
    palacsinta_darab2 = result2.x[1]
    profit2 = -result2.fun



    print(f"\nTerv 1 (Gofri: 8 peták, Palacsinta: 3 peták):")
    print(f"Gofrik száma: {int(gofri_darab1)}")
    print(f"Palacsinták száma: {int(palacsinta_darab1)}")
    print(f"Maximális profit: {int(profit1)} peták")

    print(f"\nTerv 2 (Gofri: 7 peták, Palacsinta: 4 peták):")
    print(f"Gofrik száma: {int(gofri_darab2)}")
    print(f"Palacsinták száma: {int(palacsinta_darab2)}")
    print(f"Maximális profit: {int(profit2)} peták")

    # A jobbik terv választása
    if profit1 > profit2 and profit1 > profit:
        print(f"\nA jobb terv a Terv 1, a maximális profit: {int(profit1)} peták")
    elif profit2 > profit:
        print(f"\nA jobb terv a Terv 2, a maximális profit: {int(profit2)} peták")
    else:
        print(f"\nA jobb terv az eredeti terv, a maximális profit: {int(profit)} peták")
else:
    print("Nincs megoldás.")