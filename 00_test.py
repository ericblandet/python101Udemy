# importer
import random
from pprint import pprint

r1 = random.randint(0,10)
r2 = random.uniform(0,10)
r3 = random.randrange(0,101,10)
print(r1)
print(r2)
print(r3)

import os
chemin = "/Users/eric/code/python101Udemy"
dossier = os.path.join(chemin, "dossier","test")

# if not os.path.exists(dossier):
    # os.makedirs(dossier)

os.makedirs(dossier, exist_ok=True)
if os.path.exists(dossier):
  os.removedirs(dossier)

pprint(dir(os))

