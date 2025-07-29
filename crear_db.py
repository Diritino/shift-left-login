import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Crear tabla de usuarios
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# Insertar un usuario válido
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", "admin123"))

conn.commit()
conn.close()

print("Base de datos creada con usuario 'admin' y contraseña 'admin123'")
