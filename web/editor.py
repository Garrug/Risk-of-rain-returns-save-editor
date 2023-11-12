from flask import Flask, render_template, request
from flask import send_from_directory
import os

app = Flask(__name__)

def lire_contenu_fichier(nom_fichier):
    try:
        with open(nom_fichier, 'r') as fichier:
            contenu = fichier.read()
        return contenu
    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'a pas été trouvé.")
        return None

def inserer_apres_mot_cle(fichier_source, fichier_destination, mot_cle, nouvelle_chaine):
    try:
        with open(fichier_source, 'a') as file:
            file.write("")  # Écrire une chaîne vide pour créer le fichier

        with open(fichier_source, 'r') as file:
            contenu_source = file.read()

        index_mot_cle = contenu_source.find(mot_cle)

        if index_mot_cle != -1:
            contenu_modifie = contenu_source[:index_mot_cle + len(mot_cle)] + nouvelle_chaine + contenu_source[index_mot_cle + len(mot_cle):]

            with open(fichier_destination, 'w') as file:
                file.write(contenu_modifie)
            print("Opération réussie : Le contenu du fichier a été inséré après le mot-clé.")
        else:
            print("Mot-clé non trouvé dans le fichier source.")
    except FileNotFoundError:
        print(f"Le fichier {fichier_source} n'a pas pu être créé ou trouvé.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return render_template('index.html', error="Aucun fichier sélectionné.")
    
    file = request.files['file']

    if file.filename == '':
        return render_template('index.html', error="Aucun fichier sélectionné.")

    fichier_source = os.path.join('uploads', file.filename)
    file.save(fichier_source)

    dossier_destination = request.form.get('dossier_destination')
    if not os.path.exists(dossier_destination):
        os.makedirs(dossier_destination)

    mot_cle = '"flags":['

    contenu_fichier = lire_contenu_fichier(fichier_source)

    if contenu_fichier is not None:
        fichier_destination = os.path.join(dossier_destination, 'save.json')
        nouvelle_chaine = '"challenge_unlock_engineer_completed","challenge_unlock_enforcer_completed","challenge_unlock_bandit_completed","challenge_unlock_hand_completed","challenge_unlock_miner_completed","challenge_unlock_sniper_completed","challenge_unlock_acrid_completed","challenge_unlock_mercenary_completed","challenge_unlock_loader_completed","challenge_unlock_chef_completed","challenge_unlock_pilot_completed","challenge_unlock_drifter_completed","challenge_unlock_arti_completed","challenge_unlock_engi_x2_completed","challenge_unlock_engi_c2_completed","challenge_unlock_engi_v2_completed","challenge_unlock_enforcer_z2_completed","challenge_unlock_enforcer_x2_completed","challenge_unlock_enforcer_v2_completed","challenge_unlock_bandit_z2_completed","challenge_unlock_bandit_c2_completed","challenge_unlock_bandit_v2_completed","challenge_unlock_hand_x2_completed","challenge_unlock_hand_x3_completed","challenge_unlock_hand_v2_completed","challenge_unlock_miner_z2_completed","challenge_unlock_miner_x2_completed","challenge_unlock_miner_c2_completed","challenge_unlock_sniper_z2_completed","challenge_unlock_sniper_x2_completed","challenge_unlock_sniper_c2_completed","challenge_unlock_acrid_z2_completed","challenge_unlock_acrid_x2_completed","challenge_unlock_acrid_c2_completed","challenge_unlock_mercenary_x2_completed","challenge_unlock_mercenary_c2_completed","challenge_unlock_mercenary_v2_completed","challenge_unlock_loader_z2_completed","challenge_unlock_loader_x2_completed","challenge_unlock_loader_v2_completed","challenge_unlock_chef_z2_completed","challenge_unlock_chef_c2_completed","challenge_unlock_chef_v2_completed","challenge_unlock_pilot_z2_completed","challenge_unlock_pilot_c2_completed","challenge_unlock_pilot_v2_completed","challenge_unlock_drifter_x2_completed","challenge_unlock_drifter_c2_completed","challenge_unlock_drifter_v2_completed","challenge_unlock_arti_x2_completed","challenge_unlock_arti_c2_completed","challenge_unlock_arti_v2_completed","challenge_unlock_commando_skin_a_completed","challenge_unlock_enforcer_skin_a_completed","challenge_unlock_hand_skin_a_completed","challenge_unlock_miner_skin_a_completed","challenge_unlock_sniper_skin_a_completed","challenge_unlock_pilot_skin_a_completed","challenge_unlock_huntress_skin_s_completed","challenge_unlock_commando_skin_s_completed","challenge_unlock_enforcer_skin_s_completed","challenge_unlock_bandit_skin_s_completed","challenge_unlock_acrid_skin_s_completed","challenge_unlock_mercenary_skin_s_completed","challenge_unlock_loader_skin_s_completed","challenge_unlock_chef_skin_s_completed","challenge_unlock_arti_skin_s_completed","challenge_unlock_drifter_skin_s_completed","challenge_unlock_artifact_honor_completed","challenge_unlock_artifact_kin_completed","challenge_unlock_artifact_distortion_completed","challenge_unlock_artifact_spite_completed","challenge_unlock_artifact_glass_completed","challenge_unlock_artifact_enigma_completed","challenge_unlock_artifact_sacrifice_completed","challenge_unlock_artifact_command_completed","challenge_unlock_artifact_spirit_completed","challenge_unlock_artifact_origin_completed","challenge_unlock_artifact_mountain_completed","challenge_unlock_artifact_dissonance_completed","challenge_unlock_artifact_temporary_completed","challenge_unlock_artifact_cognation_completed",'


        inserer_apres_mot_cle(fichier_source, fichier_destination, mot_cle, nouvelle_chaine)

        return render_template('index.html', success="Opération réussie : Le contenu du fichier a été inséré après le mot-clé.")
    else:
        return render_template('index.html', error="Erreur lors de la lecture du fichier.")

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)