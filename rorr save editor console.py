def lire_contenu_fichier(nom_fichier):
    try:
        with open(nom_fichier, 'r') as fichier:
            contenu = fichier.read()
        return contenu
    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'a pas été trouvé.")
        return None

# Exemple d'utilisation
nom_fichier = 'all flags.txt'
contenu_fichier = lire_contenu_fichier(nom_fichier)



def inserer_apres_mot_cle(fichier_source, fichier_destination, mot_cle, nouvelle_chaine):
    try:
        # Créer le fichier source s'il n'existe pas encore
        with open(fichier_source, 'a') as file:
            file.write("")  # Écrire une chaîne vide pour créer le fichier

        # Lire le contenu du fichier source
        with open(fichier_source, 'r') as file:
            contenu_source = file.read()

        # Trouver l'emplacement du mot-clé
        index_mot_cle = contenu_source.find(mot_cle)

        if index_mot_cle != -1:
            # Insérer la nouvelle chaîne après le mot-clé
            contenu_modifie = contenu_source[:index_mot_cle + len(mot_cle)] + nouvelle_chaine + contenu_source[index_mot_cle + len(mot_cle):]
            
            # Écrire le contenu modifié dans le fichier destination
            with open(fichier_destination, 'w') as file:
                file.write(contenu_modifie)
            print("Opération réussie : La nouvelle chaîne a été insérée après le mot-clé.")
        else:
            print("Mot-clé non trouvé dans le fichier source.")
    except FileNotFoundError:
        print(f"Le fichier {fichier_source} n'a pas pu être créé ou trouvé.")

# Exemple d'utilisation
fichier_source = 'source.json'
fichier_destination = 'save.json'
mot_cle = '"flags":['
nouvelle_chaine = contenu_fichier

inserer_apres_mot_cle(fichier_source, fichier_destination, mot_cle, nouvelle_chaine)