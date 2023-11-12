import tkinter as tk
from tkinter import filedialog

def lire_contenu_fichier(nom_fichier):
    try:
        with open(nom_fichier, 'r') as fichier:
            contenu = fichier.read()
        return contenu
    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'a pas été trouvé.")
        return None

data = lire_contenu_fichier("all flags.txt")

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


def choisir_fichier_source():
    fichier_source = filedialog.askopenfilename(title="Choisir le fichier source", filetypes=[("Fichiers JSON", "*.json")])
    entry_source.delete(0, tk.END)
    entry_source.insert(0, fichier_source)

def choisir_dossier_destination():
    dossier_destination = filedialog.askdirectory(title="Choisir le dossier de destination")
    entry_destination.delete(0, tk.END)
    entry_destination.insert(0, dossier_destination)

def executer_programme():
    fichier_source = entry_source.get()
    dossier_destination = entry_destination.get()
    mot_cle = '"flags":['
    
    contenu_fichier = lire_contenu_fichier(fichier_source)

    if contenu_fichier is not None:
        fichier_destination = f"{dossier_destination}/save.json"
        nouvelle_chaine = data

        inserer_apres_mot_cle(fichier_source, fichier_destination, mot_cle, nouvelle_chaine)

# Création de l'interface graphique
fenetre = tk.Tk()
fenetre.title("Risk of rain returns save editor")

# Widgets
label_source = tk.Label(fenetre, text="Save file:")
entry_source = tk.Entry(fenetre, width=40)
button_choisir_source = tk.Button(fenetre, text="Choose", command=choisir_fichier_source)

label_destination = tk.Label(fenetre, text="Output:")
entry_destination = tk.Entry(fenetre, width=40)
button_choisir_destination = tk.Button(fenetre, text="Choose", command=choisir_dossier_destination)


button_executer = tk.Button(fenetre, text="Execute", command=executer_programme)

# Placement des widgets
label_source.grid(row=0, column=0, padx=5, pady=5)
entry_source.grid(row=0, column=1, padx=5, pady=5)
button_choisir_source.grid(row=0, column=2, padx=5, pady=5)

label_destination.grid(row=1, column=0, padx=5, pady=5)
entry_destination.grid(row=1, column=1, padx=5, pady=5)
button_choisir_destination.grid(row=1, column=2, padx=5, pady=5)

button_executer.grid(row=3, column=0, columnspan=3, pady=10)

# Lancement de la boucle principale
fenetre.mainloop()
