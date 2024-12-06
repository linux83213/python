# Création de la liste L contenant au moins 5 entiers
L = [10, 20, 30, 40, 50]

# Afficher la deuxième valeur de la liste (index 1)
print(f"Deuxième valeur de la liste: {L[1]}")

# Fonction qui remplace L[3] par la somme des cases voisines L[2] et L[4]
def remplacer_par_somme_voisines():
    L[3] = L[2] + L[4]  # Remplacer L[3] par la somme de L[2] et L[4]
    print(f"Liste après remplacement: {L}")

# Appel de la fonction pour remplacer L[3] par la somme de L[2] et L[4]
remplacer_par_somme_voisines()

# Afficher la dernière valeur de la liste (index -1)
print(f"Dernière valeur de la liste: {L[-1]}")
