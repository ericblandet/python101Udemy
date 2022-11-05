from pprint import pprint

#List comprehension
print("Exercice 1 : List comprehension")
nombres_1 = [1,21,5,44,76874,38]
resultat_1=[i for i in nombres_1 if i%2==0]
pprint (resultat_1)

nombres_2=range(-10,10)
resultat_2 = [i for i in nombres_2 if i >=0]
pprint (resultat_2)

nombres_3=range(5)
resultat_3 = [i*2 for i in nombres_3]
pprint (resultat_3)

nombres_4=range(10)
resultat_4 = [i if i%2==0 else -i for i in nombres_4]
pprint (resultat_4)

#-----------------------------------------------------#

print("-----------------------")
print("Exercice 2 : basic loop")
for i in range(10):
  print(f"Utilisateur {i+1}")