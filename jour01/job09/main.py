nom_produit = "puff"
prix_produit = 19.99
quantité_produit = 299

print (nom_produit)
print (prix_produit)

print (f"la quantité est : {quantité_produit}")

print (f"la nouvelle quantité est : {quantité_produit + 5}")

quantité_souhaitée= int (input("entrer la quantité souhaitée:"))

print(f"merci d'avoir choisi la quantitée : {quantité_souhaitée}")

print (f"la nouvelle quantité est de : {quantité_produit - quantité_souhaitée}")

augmentation = round(prix_produit * 10/100)

print(f"augmentation de 10% sur les puffs : {prix_produit + augmentation}")


