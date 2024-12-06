# Itérer de 1 à 100
for i in range(1, 101):
    # Vérifier si le nombre est multiple de 3 et 5
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # Vérifier si le nombre est multiple de 3
    elif i % 3 == 0:
        print("Fizz")
    # Vérifier si le nombre est multiple de 5
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)