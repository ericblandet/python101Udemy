from pprint import pprint

mdp = input("Entrez un mot de passe (min 8 caractères) : ")
mdp_trop_court = "votre mot de passe est trop court."
mdp_int = "Votre mot de passe ne contient que des nombres."
mdp_ok = "Votre mot de passe est ok."

# pas d'input : mdp_trop_court en maj
# input trop courte : mdp_trop_court en avec 1 maj
# si que nombre : votre mot de passe ne contient que des nombres
# Sinon: inscription terminée


if len(mdp) == 0:
  to_print=mdp_trop_court.upper()
elif len(mdp) < 8:
  to_print=mdp_trop_court.capitalize()
elif mdp.isdigit():
  to_print=mdp_int
else:
  to_print=mdp_ok

print(to_print)
  