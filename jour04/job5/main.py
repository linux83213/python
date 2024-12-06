# Définition de la fonction calcule
def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Erreur : division par zéro"
    elif operator == "%":
        if num2 != 0:
            return num1 % num2
        else:
            return "Erreur : division par zéro"
    else:
        return "Opérateur non valide"

# Exemple d'appels de la fonction
resultat1 = calcule(10, "+", 5)  # Addition
resultat2 = calcule(10, "-", 3)  # Soustraction
resultat3 = calcule(10, "*", 4)  # Multiplication
resultat4 = calcule(10, "/", 2)  # Division
resultat5 = calcule(10, "%", 3)  # Modulo
resultat6 = calcule(10, "/", 0)  # Division par zéro

# Affichage des résultats
print(resultat1)  # 15
print(resultat2)  # 7
print(resultat3)  # 40
print(resultat4)  # 5.0
print(resultat5)  # 1
print(resultat6)  # Erreur : division par zéro
