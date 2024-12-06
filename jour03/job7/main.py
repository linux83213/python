# Définition de la chaîne
alphabet = "abcdefghijklmnopqrstuvwxyz" * 10

# Initialisation de la variable qui garde le nombre de caractères à afficher
index = 0
n = 1  # La première ligne aura 1 caractère

# Tant qu'il y a assez de caractères dans la chaîne
while index + n <= len(alphabet):
    # Affichage de la sous-chaîne
    print(alphabet[index:index + n])
    # Mise à jour de l'index et du nombre de caractères pour la ligne suivante
    index += n
    n += 1