# Fonction qui échange la première et la dernière valeur d'une liste
def echanger_premiere_dernier(liste):
    # Vérifier si la liste n'est pas vide
    if len(liste) > 0:
        # Échanger la première et la dernière valeur
        liste[0], liste[-1] = liste[-1], liste[0]
        print(f"Liste après échange: {liste}")
    else:
        print("La liste est vide, aucun échange possible.")

# Exemple d'appel avec une liste non vide
ma_liste = [1, 2, 3, 4, 5]
echanger_premiere_dernier(ma_liste)

# Exemple avec une liste contenant un seul élément
ma_liste_unique = [10]
echanger_premiere_dernier(ma_liste_unique)

# Exemple avec une liste vide
ma_liste_vide = []
echanger_premiere_dernier(ma_liste_vide)
