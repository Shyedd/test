import difflib

def lire_data(filepath):
    """
    Lit le fichier data.txt contenant les phrases correctes.
    Retourne une liste de phrases.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return [ligne.strip() for ligne in file.readlines()]
    except FileNotFoundError:
        print(f"Erreur : Le fichier {filepath} est introuvable.")
        return []

def verifier_fautes(phrase_utilisateur, phrases_correctes):
    """
    Compare la phrase saisie par l'utilisateur avec les phrases correctes.
    Retourne les fautes détectées ou un message indiquant que la phrase est correcte.
    """
    correspondance = difflib.get_close_matches(phrase_utilisateur, phrases_correctes, n=1, cutoff=0.8)
    if correspondance:
        phrase_correcte = correspondance[0]
        if phrase_utilisateur == phrase_correcte:
            return "Correct : Aucun problème détecté."
        else:
            differents = list(difflib.ndiff([phrase_correcte], [phrase_utilisateur]))
            fautes = [ligne for ligne in differents if ligne.startswith('- ') or ligne.startswith('+ ')]
            return f"Fautes détectées : {'; '.join(fautes)}"
    else:
        return "Erreur : Aucune correspondance trouvée."

def main():
    """
    Point d'entrée principal du programme.
    """
    # Chemin du fichier contenant les phrases correctes
    chemin_data = 'data.txt'

    # Lire les phrases correctes depuis le fichier
    phrases_correctes = lire_data(chemin_data)
    if not phrases_correctes:
        return

    print("Bienvenue dans le vérificateur de fautes ! Tapez 'exit' pour quitter.")

    while True:
        # Demander une phrase à l'utilisateur
        phrase_utilisateur = input("Entrez une phrase à vérifier : ").strip()

        if phrase_utilisateur.lower() == 'exit':
            print("Au revoir !")
            break

        # Vérifier les fautes
        resultat = verifier_fautes(phrase_utilisateur, phrases_correctes)
        print(resultat)

if __name__ == "__main__":
    main()
