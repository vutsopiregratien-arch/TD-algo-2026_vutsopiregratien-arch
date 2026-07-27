# Exercice 5 — Manipulation avancée avec finally
import math

try:
    x = float(input("Entrez un nombre : "))
    if x < 0:
        raise ValueError("Impossible de calculer la racine d'un nombre négatif.")
    racine = math.sqrt(x)
except ValueError as e:
    print(f"Erreur : {e}")
else:
    print(f"Racine carrée = {racine:.2f}")
finally:
    print("Fin du calcul.")
