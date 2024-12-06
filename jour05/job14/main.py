# Fonction qui retourne les mots plus longs que la taille spécifiée
def my_long_word(n, phrase):
    # Initialisation d'une liste vide pour stocker les mots longs
    words = []
    word = ""
    
    # Parcours de chaque caractère de la phrase pour découper les mots
    for char in phrase:
        if char == ' ':  # Un espace indique la fin d'un mot
            if len(word) > n:  # Si le mot a plus de n caractères
                words.append(word)  # Ajouter le mot à la liste des mots longs
            word = ""  # Réinitialiser le mot pour le prochain
        else:
            word += char  # Ajouter le caractère au mot en cours
    
    # Ajouter le dernier mot après la boucle (en cas où il n'est pas suivi d'un espace)
    if len(word) > n:
        words.append(word)
    
    # Retourner les mots longs trouvés
    return " ".join(words)

# Exemple d'utilisation
phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
resultat = my_long_word(3, phrase)
print(resultat)
