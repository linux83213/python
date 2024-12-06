#montant_investie = 10000 # Montant initiale de l'investissement 
#taux_rendement = 0.8 # Taux de rendement annuel 
# Fonction pour calculer le gain annuel en fonction du taux de rendement 
#print (montant_investie)
#print (taux_rendement)
#print (f"le gain annuel est de : {montant_investie * taux_rendement}")
#montant_ajouté = int (input("l'investisseur augmente son capital de " ) )
#print (f"le taux de rendemant augmente de 2% : {taux_rendement + 2}")
#augmentation = 2.8 
#print (f"les gains annuels  sont de  : {montant_ajouté * augmentation }")
#baisse_investissement = (montant_ajouté * 10 )
#print (baisse_investissement)
 
montant_investie = 10000  #montant initiale de l'investissment 
taux_rendement = 5   #taux de rendement annuel 

print (montant_investie)
print (taux_rendement)

#fonction pour calculer la gain annuel en fonction de taux de rendement 

gain_annuel = (montant_investie * taux_rendement/ 100)
 
#affichage du gain initial 
print (f"gain_annuel:{gain_annuel: .2f}€")

#augmentation du capital de 5000€ et augmentation du taux de rendement de 2%
montant_investie += 5000 
taux_rendement += 2

# calcul du gain après augmentation 
gain_augmenté = montant_investie * taux_rendement / 100
print (f"gain après l'augmentation : {gain_augmenté : .2f}€")

#baisse de 10% sur l'investissment et diminution de 2% sur le taux de rendement 
montant_investie -= montant_investie * 0.10
taux_rendement -= 1

#calcul du gain après retrait 
gain_final = montant_investie * taux_rendement /100
print (f"les gains après la baisse de l'investissment sont de :{gain_final:.2f}€")
