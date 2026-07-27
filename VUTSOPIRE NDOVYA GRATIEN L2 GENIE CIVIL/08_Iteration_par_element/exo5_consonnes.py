# Exercice 5 — Parcourir une chaîne de caractères (afficher consonnes)

texte = input("Entrez un texte : ")
voyelles = "aeiouyAEIOUY"

print("Consonnes : ", end="")
for char in texte:
    if char.isalpha() and char not in voyelles:
        print(char, end="")
print()
