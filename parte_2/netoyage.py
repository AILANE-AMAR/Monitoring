import sqlite3

conn = sqlite3.connect('/home/vboxuser/mini-projet/monitoring.db')
cursor = conn.cursor()

tables = ['ram', 'users', 'disk', 'alerts']

for table in tables:
    # Garde les 10 dernières lignes (les plus récents par id)
    cursor.execute(f'''
        DELETE FROM {table}
        WHERE id NOT IN (
            SELECT id FROM {table}
            ORDER BY id DESC
            LIMIT 10
        )
    ''')
    conn.commit()

conn.close()
print("✅ Nettoyage terminé. 10 dernières lignes conservées.")
