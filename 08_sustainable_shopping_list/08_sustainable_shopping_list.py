import sys
import json
import os

CUR_DIR= os.path.dirname(__file__)
path = os.path.join(CUR_DIR, "shopping_list.json")

if os.path.exists(path):
  with open(path, "r") as f:
    shopping_list= json.load(f)
else :
  shopping_list=[]

instruction="---------------------\n1:Ajouter un élément\n2:Retirer un élément\n3:Afficher la liste\n4:Vider la liste\n5:Quitter\nQuel est ton choix: "
choice=input(instruction)

while choice != "5":
  if not (choice.isdigit()) or int(choice) > 5:
    print("Please provide a number between 1 and 5")
    choice=input(instruction)
  elif int(choice) == 1:
    to_add = input("Quel élément ajouter?")
    shopping_list.append(to_add)
    print(shopping_list)
    print(f"L'élément {to_add} a été ajouté")
    choice=input(instruction)
  elif int(choice) == 2:
    to_remove=input("Quel élément retirer?")
    if to_remove not in shopping_list:
      choice=input(instruction)
    else:
      index = shopping_list.index(to_remove)
      shopping_list.pop(index)
      print(f"L'élément {to_remove} a été retiré")
      choice=input(instruction)
  elif int(choice) == 3:
    if len(shopping_list) ==0:
      print("nothing to display")
    for i in shopping_list:
      print(f"{shopping_list.index(i)+1} : {i}")
    choice=input(instruction)
  elif int(choice) == 4:
    shopping_list.clear()
    print("La liste a été vidée")
    choice=input(instruction)
  elif int(choice) == 5:
    break
  else :
    print("something went wrong !")
    choice=input(instruction)

print("ciao !")
with open(path,"w") as f:
  json.dump(shopping_list, f, indent=4, ensure_ascii=False)
sys.exit()