import sqlite3
import pymysql

conn = sqlite3.connect("Juego_datos.db")
conn=pymysql.connect(
		host="localhost",
		user="root",
		passwd="password",
		database="Juego_datos"
		)
#establece cursor
cursor = conn.cursor()

# Crear una tabla (si no existe)
cursor.execute('''CREATE TABLE IF NOT EXISTS JUGADOR(
id INTEGER PRIMARY KEY,
nombre TEXT,
Numer_partidas INT,
ganadas INT,
perdidas INT,
empatadas INT,
)''')
# Confirmar los cambios en la base de datos
conn.commit()
conn.close()