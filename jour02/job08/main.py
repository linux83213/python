# Initialisation de la première valeur
precedent = 0

# Boucle pour effectuer 12 tours
for tour in range(1, 13):  # range(1, 13) génère des valeurs de 1 à 12
    print(f"Tour {tour}: {precedent + 2}")
    precedent += 2  # Mettre à jour la valeur du tour précédent en ajoutant 2