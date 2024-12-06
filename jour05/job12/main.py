# Fonction qui trie une liste en ordre croissant sans utiliser de fonctions système
def tri_bulle(liste):
    # On suppose que la liste a au moins un élément
    n = len(liste)  # Calculer la longueur de la liste (utilisation manuelle)
    
    # On parcourt la liste plusieurs fois
    for i in range(n):
        # À chaque itération, on parcourt la liste et on compare les éléments adjacents
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:  # Si l'élément courant est plus grand que le suivant
                # On échange les éléments
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    
    return liste

# Exemple d'utilisation
L = [7, 3, 9, 2, 5]
print(f"Liste avant tri : {L}")
L_triee = tri_bulle(L)
print(f"Liste après tri : {L_triee}")
