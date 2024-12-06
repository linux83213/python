# Définition de la fonction qui vérifie si un nombre est positif ou négatif
def check_sign(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("négatif")
    else:
        print("le nombre est zéro")  # Cas où le nombre est exactement 0

# Appels de la fonction avec différents paramètres
check_sign(5)    # Affiche "positif"
check_sign(-3)   # Affiche "négatif"
check_sign(0)    # Affiche "le nombre est zéro"
check_sign(10)   # Affiche "positif"
check_sign(-8)   # Affiche "négatif"
