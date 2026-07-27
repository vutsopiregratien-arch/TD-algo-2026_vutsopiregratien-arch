# Exercice 3 — Extraire un mot sur deux

phrase = input("Entrez une phrase: ")
mots = phrase.split()

un_sur_deux = mots[::2]
print(f"Mots un sur deux: {un_sur_deux}")
