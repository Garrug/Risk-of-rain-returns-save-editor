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

data = '"pickup_fireShield_got","challenge_unlock_arti_c2_completed","challenge_unlock_enforcer_skin_a_completed","challenge_unlock_artifact_kin_completed","challenge_unlock_hand_x2_completed","challenge_unlock_engi_v2_completed","stage_templeOfTheElders_visited","challenge_unlock_commando_z2_completed","challenge_unlock_mercenary_completed","challenge_unlock_mercenary_skin_s_completed","challenge_unlock_arti_skin_s_completed","pickup_warbanner_got","pickup_redWhip_got","survivor_commando_viewed","challenge_unlock_acrid_z2_completed","tutorial_seen","challenge_unlock_watch_completed","pickup_happiestMask_got","challenge_unlock_acrid_completed","challenge_unlock_engi_z2_completed","challenge_unlock_enforcer_completed","challenge_unlock_mercenary_c2_completed","challenge_unlock_sniper_z2_completed","trophy_record_stages_completed","challenge_unlock_drifter_c2_completed","challenge_unlock_artifact_cognation_completed","challenge_unlock_hand_completed","trophy_record_time_played","trophy_record_boss_kills","challenge_unlock_acrid_c2_completed","challenge_unlock_mercenary_v2_completed","survivor_sniper_viewed","challenge_unlock_commando_c2_completed","pickup_soldiersSyringe_got","survivor_robomando_viewed","trophy_record_max_multikill","challenge_unlock_bandit_z2_completed","challenge_unlock_arti_completed","pickup_carraraMarble_got","trophy_record_time_untouched","pickup_hopooFeather_got","challenge_unlock_artifact_honor_completed","pickup_smartShopper_got","survivor_pilot_viewed","challenge_unlock_artifact_origin_completed","survivor_huntress_viewed","pickup_timeKeepersSecret_got","challenge_unlock_drifter_x2_completed","challenge_unlock_arti_x2_completed","challenge_unlock_commando_skin_a_completed","trophy_record_max_item_stack","challenge_unlock_pilot_z2_completed","stage_desolateForest_visited","challenge_unlock_commando_x2_completed","challenge_unlock_sniper_completed","pickup_sproutingEgg_got","challenge_unlock_huntress_x2_completed","challenge_unlock_chef_skin_s_completed","challenge_unlock_chef_z2_completed","trophy_record_time_alive","challenge_unlock_chef_completed","challenge_unlock_bandit_completed","survivor_bandit_viewed","challenge_unlock_bandit_v2_completed","challenge_unlock_hand_v2_completed","challenge_unlock_miner_c2_completed","challenge_unlock_bandit_skin_s_completed","challenge_unlock_hand_skin_a_completed","survivor_engineer_viewed","pickup_mysteriousVial_got","pickup_beatingEmbryo_got","challenge_unlock_enforcer_v2_completed","stage_magmaBarracks_visited","pickup_headstompers_got","challenge_unlock_huntress_skin_s_completed","challenge_unlock_artifact_sacrifice_completed","challenge_unlock_drifter_skin_s_completed","trophy_record_total_gold","pickup_lifeSavings_got","trophy_record_items","survivor_miner_viewed","challenge_unlock_huntress_z2_completed","challenge_unlock_mercenary_x2_completed","challenge_unlock_loader_z2_completed","challenge_unlock_artifact_spite_completed","trophy_record_level","challenge_unlock_artifact_temporary_completed","challenge_unlock_bandit_c2_completed","challenge_unlock_hand_x3_completed","challenge_unlock_miner_x2_completed","challenge_unlock_chef_v2_completed","pickup_atgMissileMk1_got","challenge_unlock_gamemode_trials_completed","survivor_arti_viewed","pickup_rustyJetpack_got","challenge_unlock_gasolіne_completed","pickup_monsterTooth_got","monster_whorl_got","pickup_sawmerang_got","pickup_mortarTube_got","stage_skyMeadow_visited","challenge_unlock_arti_v2_completed","challenge_unlock_miner_completed","trophy_record_kills","challenge_unlock_artifact_spirit_completed","challenge_unlock_artifact_dissonance_completed","challenge_unlock_huntress_c2_completed","challenge_unlock_loader_v2_completed","challenge_unlock_miner_skin_a_completed","challenge_unlock_sniper_c2_completed","challenge_unlock_loader_skin_s_completed","trophy_record_max_damage","challenge_unlock_artifact_enigma_completed","survivor_acrid_viewed","pickup_hardlightAfterburner_got","trophy_record_total_purchases","pickup_oldBox_got","pickup_infusion_got","challenge_unlock_pilot_c2_completed","challenge_unlock_enforcer_x2_completed","trophy_record_damage_taken","challenge_unlock_loader_completed","challenge_unlock_drifter_completed","challenge_unlock_engi_c2_completed","challenge_unlock_drifter_v2_completed","challenge_unlock_chef_c2_completed","stage_sunkenTombs_visited","challenge_unlock_enforcer_skin_s_completed","challenge_unlock_engineer_completed","challenge_unlock_enforcer_z2_completed","survivor_enforcer_viewed","challenge_unlock_huntress_v2_completed","trophy_record_total_score","pickup_guardiansHeart_got","trophy_record_total_damage","pickup_frostRelic_got","challenge_unlock_pilot_skin_a_completed","trophy_record_shrine_win_max","pickup_thallium_got","trophy_record_shrine_loss_max","challenge_unlock_acrid_x2_completed","challenge_unlock_miner_z2_completed","trophy_record_max_drone_count","survivor_drifter_viewed","challenge_unlock_acrid_skin_s_completed","challenge_unlock_artifact_distortion_completed","challenge_unlock_pilot_completed","challenge_unlock_engi_x2_completed","challenge_unlock_sniper_x2_completed","pickup_ukulele_got","trophy_record_deaths","challenge_unlock_commando_skin_s_completed","challenge_unlock_artifact_command_completed","challenge_unlock_artifact_mountain_completed","mode_trials_viewed","survivor_chef_viewed","challenge_unlock_sniper_skin_a_completed","challenge_unlock_commando_v2_completed","pickup_bundleOfFireworks_got","challenge_unlock_pilot_v2_completed","challenge_unlock_loader_x2_completed","challenge_unlock_artifact_glass_completed",'

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
