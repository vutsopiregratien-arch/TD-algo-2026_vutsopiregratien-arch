# Exercice 2 — Parcourir une liste avec enumerate()

entree = input("Entrez des éléments: ")
liste = entree.split()

for i, elem in enumerate(liste):
    print(f"Indice {i}: {elem}")
