import sqlite3

conn = sqlite3.connect('Usuarios.db')

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS USUARIOS(
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    NOME TEXT NOT NULL,
    EMAIL TEXT NOT NULL,
    USUARIO TEXT NOT NULL,
    SENHA TEXT NOT NULL
    );"""
)


print("Conectado ao banco de dados")