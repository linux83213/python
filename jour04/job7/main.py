# Définition de la fonction qui prend un langage et affiche un message approprié
def check_developer(langage):
    if langage == "JavaScript":
        print("tu es un développeur web")
    elif langage == "python":
        print("tu es un développeur IA")
    elif langage == "java":
        print("tu es un développeur logiciel")
    elif langage == "reactjs":
        print("tu es un développeur mobile")
    else:
        print("un jour, je serai le meilleur développeur...")

# Appels de la fonction avec différents langages
check_developer("JavaScript")  # Affiche "tu es un développeur web"
check_developer("python")      # Affiche "tu es un développeur IA"
check_developer("java")        # Affiche "tu es un développeur logiciel"
check_developer("reactjs")     # Affiche "tu es un développeur mobile"
check_developer("ruby")        # Affiche "un jour, je serai le meilleur développeur..."
