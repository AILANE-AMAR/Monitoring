import sqlite3
import pygal

# Connexion à la base de données
connection = sqlite3.connect('/home/vboxuser/mini-projet/monitoring.db')
cursor = connection.cursor()

# Récupérer les données de la table 'disk'
cursor.execute('SELECT * FROM disk')
disk_data = cursor.fetchall()
#conversion vers GIGA
bytes_to_gb = 1024 * 1024 * 1024
# Récupérer les données de la table 'ram'
cursor.execute('SELECT * FROM ram')
ram_data = cursor.fetchall()

# Récupérer les données de la table 'users'
cursor.execute('SELECT * FROM users')
users_data = cursor.fetchall()

# Initialiser les listes pour les graphiques
dates = []  # Liste unique pour les dates
usage_disk = []
usage_ram = []
active_users = []

# Ajouter les données dans les listes respectives
for row in disk_data:
    dates.append(row[4])
    usage_disk.append(row[1]/ bytes_to_gb)

for row in ram_data:
    usage_ram.append(row[2]/ bytes_to_gb)

for row in users_data:
    active_users.append(row[1])
# Graphique pour l'utilisation du disque
disk_chart = pygal.Line(x_label_rotation=20)
disk_chart.title = 'Disk Usage Over Time'
disk_chart.x_labels = dates
disk_chart.add('Disk Usage (%)', usage_disk)
disk_chart.render_to_file('../parte_4/static/disk_usage_chart.svg')

# Graphique pour l'utilisation de la RAM
ram_chart = pygal.Line(x_label_rotation=20)
ram_chart.title = 'RAM Usage Over Time'
ram_chart.x_labels = dates
ram_chart.add('RAM Usage (%)', usage_ram)
ram_chart.render_to_file('../parte_4/static/ram_usage_chart.svg')

# Graphique pour les utilisateurs actifs
users_chart = pygal.Line(x_label_rotation=20)
users_chart.title = 'Active Users Over Time'
users_chart.x_labels = dates
users_chart.add('Active Users', active_users)
users_chart.render_to_file('../parte_4/static/active_users_chart.svg')

# Créer un graphique en ligne combiné
combined_chart = pygal.Line(x_label_rotation=20)
combined_chart.title = 'System Usage (Disk, RAM, Users) Over Time'

# Ajouter les séries de données
combined_chart.x_labels = dates
combined_chart.add('Disk Usage (%)', usage_disk)
combined_chart.add('RAM Usage (%)', usage_ram)
combined_chart.add('Active Users', active_users)

# Rendu du graphique combiné dans un fichier SVG
combined_chart.render_to_file('../parte_4/static/combined_usage_chart.svg')

# Fermer la connexion
connection.close()

