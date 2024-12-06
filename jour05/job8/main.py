# Liste donnée
L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

# Fonction qui calcule la somme des nombres pairs dans la liste
def somme_paires(liste):
    somme = 0  # Initialisation de la somme à 0
    for nombre in liste:
        if nombre % 2 == 0:  # Vérifie si le nombre est pair
            somme += nombre  # Ajoute le nombre à la somme
    return somme

# Appel de la fonction et affichage du résultat
resultat = somme_paires(L)
print(f"La somme des valeurs paires dans la liste est : {resultat}")
