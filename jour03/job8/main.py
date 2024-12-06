# Demande des longueurs des trois côtés du triangle
a = float(input("Entrez la longueur du côté a : "))
b = float(input("Entrez la longueur du côté b : "))
c = float(input("Entrez la longueur du côté c : "))

# Vérification de l'inégalité triangulaire
if a + b > c and a + c > b and b + c > a:
    print("Les longueurs peuvent former un triangle.")
    
    # Vérification si le triangle est rectangle (théorème de Pythagore)
    sides = sorted([a, b, c])  # Tri des côtés pour identifier le plus grand côté
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print("Le triangle est rectangle.")
    
    # Vérification si le triangle est équilatéral
    if a == b == c:
        print("Le triangle est équilatéral.")
    
    # Vérification si le triangle est isocèle
    elif a == b or a == c or b == c:
        print("Le triangle est isocèle.")
    
    # Sinon, c'est un triangle quelconque
    else:
        print("Le triangle est quelconque.")
    
else:
    print("Les longueurs ne peuvent pas former un triangle.")