def telecharger_json(url):
    # 1. Faire la requête HTTP
    # 2. En cas d'erreur réseau ou de JSON invalide : lever GbfsError
    # 3. Renvoyer le dict
    ...

def decouvrir_feeds(url_gbfs):
    # 1. Télécharger gbfs.json
    # 2. Renvoyer {nom_du_fichier: url} pour chaque feed
    ...

def telecharger_fichiers_statiques(url_gbfs, dossier):
    # 1. Récupérer les URLs avec decouvrir_feeds
    # 2. Créer le dossier s'il n'existe pas
    # 3. Pour chacun des 3 fichiers (system_information, station_information, vehicle_types) :
    #      - le télécharger
    #      - valider son contenu
    #      - l'écrire en .json (encoding="utf-8")
    # 4. Renvoyer le nombre de stations
    ...
