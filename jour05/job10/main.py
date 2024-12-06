# Liste donnée
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Fonction qui calcule le produit des valeurs dans l'intervalle [25, 90]
def produit_intervalle(liste, min_val, max_val):
    produit = 1  # Initialisation du produit à 1 (car c'est l'élément neutre de la multiplication)
    for nombre in liste:
        if min_val <= nombre <= max_val:  # Vérifie si le nombre est dans l'intervalle [25, 90]
            produit *= nombre  # Multiplie le produit par le nombre
    return produit

# Appel de la fonction avec l'intervalle [25, 90]
resultat = produit_intervalle(L, 25, 90)
print(f"Le produit des valeurs dans l'intervalle [25, 90] est : {resultat}")

