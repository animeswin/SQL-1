import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clientes (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL,
        Idade INTEGER NOT NULL,
        Cidade TEXT NOT NULL
    )
''')

print("Tabela Clientes criada com sucesso!")

conn.commit()
conn.close()