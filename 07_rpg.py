import random
import sys

RULES= """
Règles du jeu
Le but de ce projet est de créer un jeu de rôle textuel dans le terminal.
Le jeu comporte deux joueurs : vous et un ennemi.
Vous commencez tous les deux avec 50 points de vie.
Votre personnage dispose de 3 potions qui vous permettent de récupérer des points de vie.
L'ennemi ne dispose d'aucune potion.
Chaque potion vous permet de récupérer un nombre aléatoire de points de vie, compris entre 15 et 50.
Votre attaque inflige à l'ennemi des dégâts aléatoires compris entre 5 et 10 points de vie.
L'attaque de l'ennemi vous inflige des dégâts aléatoires compris entre 5 et 15 points de vie.
Lorsque vous utilisez une potion, vous passez le prochain tour.
👉 Déroulé de la partie
Lorsque vous lancez le script, vous devez demander à l'utilisateur s'il souhaite attaquer ou utiliser une potion :
"Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? "
Cette phrase sera demandée à l'utilisateur au début de chaque tour.
?  Si l'utilisateur choisi la première option (1), vous infligez des points de dégât à l'ennemi.
Ces points seront compris entre 5 et 10 et déterminés aléatoirement par le programme.
?  Si l'utilisateur choisi la deuxième option (2), vous prenez une potion.
Les points de vie que la potion vous donne doivent être compris entre 15 et 50 et générés aléatoirement par le programme Python.
Vous devez vérifier que l'utilisateur dispose de suffisamment de potion et décrémenter le nombre de potions qu'il a dans son inventaire lorsqu'il en boit une. Si l'utilisateur n'a plus de potions, vous devez lui indiquer et lui proposer de nouveau de faire un choix (attaquer ou prendre une potion).
Quand le joueur prend une potion, il passe le prochain tour.
Une fois l'action du joueur exécutée, et si l'ennemi est encore vivant, il vous attaque. Si l'ennemi est mort, vous pouvez terminer le jeu et indiqué à l'utilisateur qu'il a gagné ?
L'attaque de l'ennemi inflige des dégâts au joueur compris entre 5 et 15, là encore déterminés aléatoirement par le script.
Si vous n'avez plus de points de vie, le jeu se termine et vous avez perdu la partie.
À la fin du tour, vous devez afficher le nombre de points de vie restants du joueur et de l'ennemi.
Toutes ces opérations se répètent tant que le joueur et l'ennemi sont en vie.
À chaque tour, vous attaquez en premier. Il ne peut donc pas y avoir de match nul. Si lorsque vous attaquez, votre attaque fait descendre les points de vie de l'ennemi en dessous (ou égal à) 0, vous gagnez la partie sans que l'ennemi n'ait le temps de vous attaquer en retour.
"""
TITLE="***RPG OF DA YEAR***"
SUBTITLE="Bienvenue dans ce jeu merveilleux !"
ACTION_LIST=["1","2"]

my_life= 50
enemy_life = 50
potions = 3
turn_start="""
Que voulez vous faire ?
1: Attaquer
2: Boire une potion
Votre Action : """


print("="*100)
print(TITLE)
print("-"*50)
print(SUBTITLE)
print("-"*50)
print(RULES)
print("="*100)

while True:
  print("\n***Début du tour***")
  print(f"""Il reste {enemy_life} point{"s" if enemy_life != 1 else ""} de vie à votre enemi.
Il vous reste {my_life} point{"s" if my_life != 1 else ""} de vie.
Il vous reste {potions} potion{"s" if potions != 1 else ""}""")
  action=input(turn_start)
  if action not in ACTION_LIST:
    print("L'action n'est pas valide")
    continue
  elif action == "1":
    my_attack =random.randrange(5,11)
    enemy_life -= my_attack
    print(f" ⚔️ Vous infligez {my_attack} points de dégât")
    if enemy_life <=0:
      print(" 🍾 You win")
      break
    print(f"Votre ennemi a {enemy_life} points de vie")
  elif action == "2":
    if potions == 0:
      print(" 🤷‍♂️ Vous cherchez dans votre sac, mais il ne vous reste plus de potion. Vous perdez ce tour")
    else: 
      potions -=1
      add_life =random.randrange(15,51)
      print(f" 🧪 Vous récupérez {add_life if my_life+add_life<=50 else 50-add_life} poins de vie")
      my_life = 50 if my_life+add_life >50 else my_life+add_life
  input("***Au tour de votre adversaire***")
  his_attack=random.randrange(5,16)
  my_life-=his_attack
  print(f" ⚔️ Votre enemi vous inflige {his_attack} points de dégats")
  if my_life < 0:
    print(f" 🪦 Sorry, you lose and your enemy still has {enemy_life} points de vie")
    print("Ciao !")
    break
  input("***Fin du tour***")  

sys.exit()
  
    




