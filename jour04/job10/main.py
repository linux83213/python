# Définition de la fonction qui vérifie si un nombre est pair ou impair
def check_pair_impair(nombre):
    # Vérifier si le nombre est un entier positif
    if not isinstance(nombre, int) or nombre < 0:
        print("Veuillez entrer un nombre entier positif.")
        return  # Retourne sans rien faire si le nombre n'est pas valide

    # Vérifier si le nombre est pair ou impair
    if nombre % 2 == 0:
        print(f"{nombre} est pair.")
    else:
        print(f"{nombre} est impair.")

# Appels de la fonction avec différentes valeurs
check_pair_impair(4)     # Affiche "4 est pair."
check_pair_impair(7)     # Affiche "7 est impair."
check_pair_impair(-5)    # Affiche "Veuillez entrer un nombre entier positif."
check_pair_impair(10.5)  # Affiche "Veuillez entrer un nombre entier positif."
check_pair_impair(0)     # Affiche "0 est pair."
