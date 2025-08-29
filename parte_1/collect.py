import psutil
import sqlite3

# Connexion à la base de données
conn = sqlite3.connect('/home/vboxuser/mini-projet/monitoring.db')
cursor = conn.cursor()

# Créer la table 'ram' si elle n'existe pas déjà
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ram (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        total INTEGER,
        used INTEGER,
        free INTEGER
    )
''')
ram = psutil.virtual_memory()
total_ram = ram.total
used_ram = ram.used
free_ram = ram.free
cursor.execute('''
    INSERT INTO ram (total, used, free) 
    VALUES (?, ?, ?)
''', (total_ram, used_ram, free_ram))
conn.commit()
conn.close()
print(f"RAM UTILISÉE : {ram.percent}%")
