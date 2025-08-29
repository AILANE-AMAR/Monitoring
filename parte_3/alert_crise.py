import sqlite3
from mail import send_alert  # Importe la fonction pour envoyer l'alerte

# Définir les seuils
DISK_MAX = 90
RAM_MAX = 90

# Connexion à la base de données SQLite
conn = sqlite3.connect('/home/vboxuser/mini-projet/monitoring.db')
cursor = conn.cursor()

# Récupérer les dernières données d'utilisation du disque
cursor.execute('SELECT used_space, total_space FROM disk ORDER BY id DESC LIMIT 1')
disk_data = cursor.fetchone()

# Récupérer les dernières données d'utilisation de la RAM
cursor.execute('SELECT used, total FROM ram ORDER BY id DESC LIMIT 1')
ram_data = cursor.fetchone()

# Fermeture de la connexion à la base de données
conn.close()

# Vérifier l'utilisation du disque et envoyer l'alerte si nécessaire
if disk_data:
    used_space, total_space = disk_data
    disk_usage = (used_space / total_space) * 100  # Calcul du pourcentage d'utilisation
    if disk_usage > MAX:
        send_alert(
            subject="Alerte Disque",
            alert_type="Alerte : Utilisation du Disque",
            alert_message=f"Utilisation disque critique : {disk_usage:.2f}%"
        )

# Vérifier l'utilisation de la RAM et envoyer l'alerte si necessaire
if ram_data:
    used_ram, total_ram = ram_data
    ram_usage = (used_ram / total_ram) * 100  # Calcul du pourcentage d'utilisation
    if ram_usage > RAM_MAX:
        send_alert(
            subject="Alerte RAM",
            alert_type="Alerte : Utilisation de la RAM",
            alert_message=f"Utilisation RAM critique : {ram_usage:.2f}%"
        )

