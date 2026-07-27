# Exercice 3 — Inverser une chaîne

texte = input("Entrez une chaîne : ")
inverse = ""

for char in texte:
    inverse = char + inverse  # On ajoute chaque caractère devant

print(f"Chaîne inversée: {inverse}")
