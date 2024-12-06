# Fonction pour arrondir un nombre à l'entier le plus proche
def arrondir(nombre):
    # On récupère la partie entière et la partie décimale
    entier = int(nombre)
    decimale = nombre - entier
    if decimale >= 0.5:  # Si la partie décimale est >= 0.5, on arrondit vers le haut
        return entier + 1
    else:  # Sinon, on arrondit vers le bas
        return entier

# Fonction pour trier la liste manuellement (tri à bulle)
def trier_liste(liste):
    n = 0
    while True:
        echangé = False
        for i in range(len(liste) - 1 - n):
            if liste[i] > liste[i + 1]:
                # Échanger les éléments si nécessaire
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
                echangé = True
        if not echangé:
            break
        n += 1
    return liste

# Liste initiale
L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Arrondir chaque élément de la liste
L_arrondie = [arrondir(x) for x in L]

# Trier la liste après arrondi
L_triee = trier_liste(L_arrondie)

# Affichage du résultat
print(f"Liste arrondie et triée : {L_triee}")
