# Définition de la fonction moyenne
def moyenne(note1, note2, note3):
    return (note1 + note2 + note3) / 3

# Demander à l'utilisateur de saisir trois notes
note1 = float(input("Saisissez la première note : "))
note2 = float(input("Saisissez la deuxième note : "))
note3 = float(input("Saisissez la troisième note : "))

# Calcul de la moyenne
moyenne_etudiant = moyenne(note1, note2, note3)

# Affichage du message en fonction de la moyenne
if 15 <= moyenne_etudiant <= 20:
    print("Très bon élève")
elif 11 <= moyenne_etudiant < 15:
    print("Bon élève")
elif 8 <= moyenne_etudiant < 11:
    print("Élève moyen")
elif 0 <= moyenne_etudiant < 8:
    print("Élève devant faire des efforts")
else:
    print("La moyenne doit être entre 0 et 20")
