import mysql.connector
from mysql.connector import Error

# Configuración de la conexión a MySQL
config = {
'user': 'root',
'password': 'Mafer159159',
'host': 'localhost',
}
try:
    connection = mysql.connector.connect(**config)

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS reviews2;")
        cursor.execute("USE reviews2;")

        # Crear la tabla usuarios
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            correo VARCHAR(100) UNIQUE NOT NULL,
            contraseña VARCHAR(100) NOT NULL
            );""")
            # Crear la tabla posts
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS posts (
            id INT AUTO_INCREMENT PRIMARY KEY,
            titulo VARCHAR(255) NOT NULL,
            contenido TEXT NOT NULL,
            usuario_id INT,
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
            );""")
        print("Base de datos y tablas creadas con éxito!")

except Error as e:
    print("ERROR", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexión a MySQL cerrada")

