# Liste donnée
L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

# Fonction pour supprimer les doublons
def supprimer_doublons(liste):
    unique_list = []  # Liste vide pour stocker les éléments uniques
    for element in liste:
        if element not in unique_list:  # Vérifie si l'élément n'est pas déjà dans la nouvelle liste
            unique_list.append(element)  # Ajoute l'élément si c'est un élément unique
    return unique_list

# Appel de la fonction et affichage du résultat
L_sans_doublons = supprimer_doublons(L)
print(f"Liste sans doublons : {L_sans_doublons}")
