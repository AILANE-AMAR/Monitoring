import sqlite3

conn = sqlite3.connect('/home/vboxuser/mini-projet/monitoring.db')
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS processes')
# Recréer les tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ram (
        id INTEGER PRIMARY KEY,
        total INTEGER,
        used INTEGER,
        free INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        NBR INTEGER
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS disk (
        id INTEGER PRIMARY KEY,
        total_space INTEGER,
        used_space INTEGER,
        free_space INTEGER
     )
''')
cursor.execute('''
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY,
            alert_title TEXT,
            alert_link TEXT
        )
''')


conn.commit()
conn.close()

print("✅ Toutes les tables ont été supprimées et recréées.")
