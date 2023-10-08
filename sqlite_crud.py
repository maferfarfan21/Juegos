import sqlite3



def crear_tabla():
    conn = sqlite3.connect('mi_base_de_datos.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY,nombre TEXT NOT NULL,email TEXT NOT NULL)''')
    conn.commit()
    conn.close()
def crear_usuario():
    nombre = input("Nombre del usuario: ")
    email = input("Correo electrónico del usuario: ")
    conn = sqlite3.connect('mi_base_de_datos.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (nombre, email) VALUES (?, ?)', (nombre, email))
    conn.commit()
    conn.close()
    print(f"Usuario {nombre} creado con éxito.")
def obtener_usuarios():
    conn = sqlite3.connect('mi_base_de_datos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios
def mostrar_usuarios():
    usuarios = obtener_usuarios()
    if usuarios:
        print("Lista de usuarios:")
    for usuario in usuarios:
        print(usuario)
    else:
        print("No hay usuarios registrados.")
def actualizar_usuario():
    id_usuario = int(input("ID del usuario a actualizar: "))
    nuevo_nombre = input("Nuevo nombre del usuario: ")
    nuevo_email = input("Nuevo correo electrónico del usuario: ")
    conn = sqlite3.connect('mi_base_de_datos.db')

cursor = conn.cursor()
cursor.execute('UPDATE usuarios SET nombre=?, email=? WHERE id=?', (nuevo_nombre, nuevo_email, id_usuario))
conn.commit()
conn.close()

print(f"Usuario con ID {id_usuario} actualizado con éxito.")
def eliminar_usuario():
    id_usuario = int(input("ID del usuario a eliminar: "))
conn = sqlite3.connect('mi_base_de_datos.db')
cursor = conn.cursor()
cursor.execute('DELETE FROM usuarios WHERE id=?', (id_usuario,))
conn.commit()
conn.close()
print(f"Usuario con ID {id_usuario} eliminado con éxito.")
if __name__ == "__main__":
    crear_tabla()
while True:
    print("\nMenú de Operaciones:")
    print("1. Crear Usuario")
    print("2. Mostrar Usuarios")
    print("3. Actualizar Usuario")
    print("4. Eliminar Usuario")
    print("5. Salir")
    opcion = input("Selecciona una opción (1/2/3/4/5): ")
if opcion == "1":
    crear_usuario()
    elif opcion == "2":
    mostrar_usuarios()
    elif opcion == "3":
    actualizar_usuario()
    elif opcion == "4":
    eliminar_usuario()
    elif opcion == "5":
    print("¡Hasta luego!")
    break
    else:
    print("Opción no válida. Por favor, selecciona una opción válida.")