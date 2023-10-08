from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask import app_ctx_stack

app = Flask(__name__)
# Configuración de la conexión a la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Mafer159159'
app.config['MYSQL_DB'] = 'reviews4'
mysql = MySQL(app)


# Aquí irán las rutas
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    cursor.close()
    return jsonify(usuarios)

@app.route('/usuarios/<id>', methods=['GET'])
def obtener_usuario(id):
    cursor = mysql.connection.cursor()
    cursor.execute(f'SELECT * FROM usuarios WHERE id = {id}')
    usuario = cursor.fetchone()
    cursor.close()
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404

@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Datos no válidos'}), 400
    nombre = data.get('nombre')
    correo = data.get('correo')
    contraseña = data.get('contraseña')# Deberías hashear la contraseña antes de almacenarla
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO usuarios (nombre, correo, contraseña) VALUES (%s, %s, %s)', (nombre,
    correo, contraseña))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'mensaje': 'Usuario creado'}), 201

@app.route('/usuarios/<id>', methods=['PUT'])
def actualizar_usuario(id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Datos no válidos'}), 400
    nombre = data.get('nombre')
    correo = data.get('correo')
    contraseña = data.get('contraseña') # Deberías hashear la contraseña antes de almacenarla
    cursor = mysql.connection.cursor()
    cursor.execute('UPDATE usuarios SET nombre = %s, correo = %s, contraseña = %s WHERE id = %s',
    (nombre, correo, contraseña, id))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'mensaje': 'Usuario actualizado'}), 200



# ...
if __name__ == '__main__':
    app.run(debug=True)

