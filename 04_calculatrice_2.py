
# Calculatrice v2

a = input("Entrez un premier nombre:")
b = input("Entrez un deuxième nombre:")


resultat =''

while not(a.isdigit() and b.isdigit()):
  print("Les données entrées ne sont pas valides")
  a = input("Entrez un premier nombre:")
  b = input("Entrez un deuxième nombre:")

print(f'Le résultat de l\'addition de {a} et de {b} est {int(a)+ int(b)}')