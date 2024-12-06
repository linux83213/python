# Liste donnée
L = [8, 24, 48, 2, 16]

# Fonction qui compte les multiples de 3 dans la liste
def compter_multiples_de_3(liste):
    count = 0  # Variable pour compter les multiples de 3
    for nombre in liste:
        if nombre % 3 == 0:  # Vérifie si le nombre est un multiple de 3
            count += 1
    return count

# Appel de la fonction et affichage du résultat
resultat = compter_multiples_de_3(L)
print(f"Nombre de multiples de 3 dans la liste : {resultat}")
