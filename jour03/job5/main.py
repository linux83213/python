                                                            # Fonction pour vérifier si un nombre est premier
def est_premier(n):
    if n < 2:                                                # Les nombres inférieurs à 2 ne sont pas premiers
        return False
    for i in range(2, int(n ** 0.5) + 1):                # Vérifie les diviseurs jusqu'à la racine carrée de n
        if n % i == 0:                                   # Si n est divisible par i, alors ce n'est pas un nombre premier
            return False
    return True

                                                            # Affichage des nombres premiers jusqu'à 1000


for i in range(2, 1001):
    if est_premier(i):
        print(i)
