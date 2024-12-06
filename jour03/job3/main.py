# Parcours des nombres de 0 à 100
for i in range(101):
    # Si le nombre est 26, 37 ou 88, on passe à l'itération suivante
    if i in [26, 37, 88]:
        continue
    print(i)
    