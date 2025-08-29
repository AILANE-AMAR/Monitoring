import sqlite3
import requests
import re

# Récupérer la page des alertes CERT
url = "http://www.cert.ssi.gouv.fr/"
response = requests.get(url)

# Utiliser une expression régulière pour extraire tous les titres des alertes
# Cette expression va chercher toutes les balises <h3> contenant un titre d'alerte
alert_titles = re.findall(r'<h3.*?>(.*?)</h3>', response.text)

# Si des alertes ont été trouvées, on continue
if alert_titles:
    # Connexion à la base de données SQLite
    conn = sqlite3.connect('/home/amar/mini-projet/monitoring.db')
    cursor = conn.cursor()

    # Ajouter chaque alerte à la base de données
    for alert in alert_titles:
        alert = alert.strip()  # Enlever les espaces superflus autour de l'alerte
        # On vérifie si l'alerte existe déjà dans la base de données
        cursor.execute("SELECT alert_title FROM alerts WHERE alert_title = ?", (alert,))
        if not cursor.fetchone():  # Si l'alerte n'existe pas
            cursor.execute("INSERT INTO alerts (alert_title) VALUES (?)", (alert,))
            print(f"Alerte ajoutée : {alert}")
        else:
            print(f"Alerte déjà présente : {alert}")

    # Commit des changements et fermeture de la connexion
    conn.commit()
    conn.close()
else:
    print("Aucune alerte CERT trouvée.")
