import requests
import re
import sqlite3

# URL de la page CERT-FR
url = "https://www.cert.ssi.gouv.fr/"

# Récupérer le contenu HTML de la page
response = requests.get(url)
html_content = response.text

# Vérifier si le contenu HTML est bien récupéré
if not html_content:
    print("Erreur : la page n'a pas été chargée.")
    exit()

# Expression régulière mise à jour pour extraire les alertes
pattern = r'<div class="item cert-alert open">.*?<span class="item-date">(.*?)</span>.*?<div class="item-ref">.*?<a href="(.*?)">(.*?)</a>.*?</div>.*?<div class="item-title">.*?<a href=".*?">(.*?)</a>.*?</div>'

# Extraction des alertes
alerts = re.search(pattern, html_content, re.DOTALL)

if not alerts:
    print(" Aucune alerte trouvée.")
    exit()

date, lien, ref, titre = alerts.groups()
full_link = f"https://www.cert.ssi.gouv.fr{lien}"

alerte_deja_exportee = False
try:
    with open("export.txt", "r", encoding="utf-8") as f:
        contenu = f.read()
        if full_link in contenu:
            alerte_deja_exportee = True
except FileNotFoundError:
    pass  # Le fichier n'existe pas encore  aucune alerte stockée

if not alerte_deja_exportee:
    with sqlite3.connect('/home/vboxuser/mini-projet/monitoring.db') as conn:
        c = conn.cursor()

        c.execute("INSERT INTO alerts (alert_title, alert_link) VALUES (?, ?)", (titre.strip(), full_link))

        conn.commit()

# Affichage des alertes
print(f"{titre.strip()} - {full_link}")

# Création de la table si elle n'existe pas déjà
with sqlite3.connect("monitoring.db") as conn:
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY,
            alert_title TEXT,
            alert_link TEXT
        )
    ''')
    conn.commit()
