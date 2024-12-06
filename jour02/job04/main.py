N = int(input("Entrez un nombre entier N supérieur à zéro : "))

# Vérifier si l'utilisateur a saisi un nombre positif
if N > 0:
    # Afficher les tables de multiplication de 1 à N
    for i in range(1, N+1):
        print(f"Table de multiplication de {i} :")
        for j in range(1, 11):  # De 1 à 10 (pour la table de 1 à 10)
            print(f"{i} x {j} = {i*j}")
        print()  # Laisser une ligne vide entre chaque table
else:
    print("Veuillez entrer un nombre supérieur à zéro.")
