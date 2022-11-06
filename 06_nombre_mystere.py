import sys
import random

INSTRUCTION="""Trouve le nombre mystère en 5 coups !
Il est compris entre 0 et 50"""

essais = 5
nb_mystère = random.randrange(51)

print(INSTRUCTION)
while essais >0:
  guess= input("Devine le nombre: ")
  if guess.isdigit:
    guess= int(guess)
    if guess==nb_mystère:
      print('You winner !')
      sys.exit()
    elif guess < nb_mystère:
      essais -=1
      print(f"Le nombre mystère est plus grand que {guess}")
      print(f"Il reste {essais} essais")
    elif guess > nb_mystère:
      essais -=1
      print(f"Le nombre mystère est plus petit que {guess}")
      print(f"Il reste {essais} essais")
  else:
    print("please provide an integer !")

print(f"You loser, answer was : {nb_mystère}")