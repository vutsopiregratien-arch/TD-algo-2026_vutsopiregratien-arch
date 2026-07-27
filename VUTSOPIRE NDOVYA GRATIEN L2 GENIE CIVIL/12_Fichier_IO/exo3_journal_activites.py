# Exercice 3 — Journal d'activités

activite = input("Entrez vos activités du jour : ")

with open("journal.txt", "a", encoding="utf-8") as f:
    f.write(activite + "\n")

print("Activité ajoutée dans 'journal.txt'.")
