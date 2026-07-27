# Exercice 1 — Nettoyer un texte utilisateur

texte = input("Entrez un texte: ")

# Nettoyage
texte_nettoye = texte.strip().lower().replace(".", "!")
print(f"Texte nettoyé: {texte_nettoye}")
