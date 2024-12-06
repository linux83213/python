# Définition de la fonction qui prend deux paramètres : type et saison
def afficher_produit(type, saison):
    if type == "fruits":
        if saison == "hiver":
            print("orange, mandarine et kiwi")
        elif saison == "été":
            print("Poire, fraise, cassis")
        else:
            print("Saison non reconnue pour les fruits")
    elif type == "légume":
        if saison == "hiver":
            print("carotte, topinambour, endive")
        elif saison == "été":
            print("artichaut, aubergine, navet")
        else:
            print("Saison non reconnue pour les légumes")
    else:
        print("Type non reconnu. Veuillez entrer 'fruits' ou 'légume'.")

# Appels de la fonction avec différents paramètres
afficher_produit("fruits", "hiver")  # Affiche "orange, mandarine et kiwi"
afficher_produit("fruits", "été")    # Affiche "Poire, fraise, cassis"
afficher_produit("légume", "hiver")  # Affiche "carotte, topinambour, endive"
afficher_produit("légume", "été")    # Affiche "artichaut, aubergine, navet"
