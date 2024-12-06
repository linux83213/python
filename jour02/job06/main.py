# Demander à l'utilisateur de saisir un nombre entier N
N = int(input("Entrez un nombre entier N : "))

# Initialiser un compteur pour les premières multiplications
compteur = 1

# Afficher les premiers résultats de la multiplication de N par 7
while compteur <= 10:  # Affiche les 10 premières multiplications
    print(f"{N} x {compteur} = {N * compteur}")
    compteur += 1  # Incrémenter le compteur