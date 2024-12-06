# Demande à l'utilisateur d'entrer un nombre
nombre = int(input("Entrez un nombre entier : "))

# Vérification si le nombre est pair ou impair
if nombre % 2 == 0:
    print(f"Le nombre {nombre} est pair")
else:
    print(f"Le nombre {nombre} est impair")
