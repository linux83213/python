# Liste donnée
L = [7, 11, 42, 39, 2]

# Fonction qui augmente chaque élément de la liste de 1
def augmenter_liste(liste):
    for i in range(len(liste)):
        liste[i] += 1  # Augmenter l'élément de 1
    return liste

# Appel de la fonction pour modifier la liste
L_modifiee = augmenter_liste(L)

# Affichage de la liste modifiée
print(f"Liste après augmentation de chaque élément : {L_modifiee}")
