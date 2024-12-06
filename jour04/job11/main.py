# Définition de la fonction time_to_text
def time_to_text(minutes):
    # Vérification que le nombre de minutes est un entier positif
    if not isinstance(minutes, int) or minutes < 0:
        print("Veuillez entrer un nombre entier positif.")
        return

    # Calculer le nombre d'heures et de minutes
    heures = minutes // 60  # Nombre d'heures
    minutes_restantes = minutes % 60  # Nombre de minutes restantes

    # Afficher le résultat sous la forme "X heures et Y minutes"
    print(f"{heures} heures et {minutes_restantes} minutes")

# Appels de la fonction avec différents nombres de minutes
time_to_text(130)  # Affiche "2 heures et 10 minutes"
time_to_text(45)   # Affiche "0 heures et 45 minutes"
time_to_text(75)   # Affiche "1 heure et 15 minutes"
time_to_text(0)    # Affiche "0 heures et 0 minutes"
time_to_text(-30)  # Affiche "Veuillez entrer un nombre entier positif."
time_to_text(150)  # Affiche "2 heures et 30 minutes"
