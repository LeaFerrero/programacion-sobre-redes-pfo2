import sqlite3
from flask import Flask, request, jsonify, render_template_string
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
DB_NAME = 'database.db'

def init_db():
    """Crea la tabla de usuarios si no existe en la base de datos."""
    conexion = None
    try:
        conexion = sqlite3.connect(DB_NAME)
        cursor = conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT UNIQUE NOT NULL,
                contraseña TEXT NOT NULL
            )
        ''')
        conexion.commit()
    finally:
        if conexion:
            conexion.close()

# Inicializar la base de datos al iniciar el script
init_db()

@app.route('/registro', methods=['POST'])
def registro():
    datos = request.get_json()

    # Validar que se reciba el JSON correctamente
    if not datos or 'usuario' not in datos or 'contraseña' not in datos:
        return jsonify({'error': 'Faltan datos requeridos: usuario y contraseña'}), 400

    usuario = datos['usuario']
    contrasena_plana = datos['contraseña']

    # Hashear la contraseña usando werkzeug.security
    contrasena_hasheada = generate_password_hash(contrasena_plana)
    conexion = None

    try:
        conexion = sqlite3.connect(DB_NAME)
        cursor = conexion.cursor()

        # Insertar el nuevo usuario en SQLite
        cursor.execute(
            'INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)',
            (usuario, contrasena_hasheada)
        )
        conexion.commit()
        return jsonify({'mensaje': f'Usuario {usuario} registrado exitosamente'}), 201

    except sqlite3.IntegrityError:
        # Captura el error si el usuario ya existe (por la restricción UNIQUE)
        return jsonify({'error': 'El usuario ya existe'}), 409
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if conexion:
            conexion.close()

@app.route('/login', methods=['POST'])
def login():
    datos = request.get_json()

    # Validar que se envíen las credenciales
    if not datos or 'usuario' not in datos or 'contraseña' not in datos:
        return jsonify({'error': 'Faltan credenciales requeridas'}), 400

    usuario = datos['usuario']
    contrasena_plana = datos['contraseña']
    conexion = None

    try:
        conexion = sqlite3.connect(DB_NAME)
        cursor = conexion.cursor()

        # Consultar el hash almacenado para el usuario ingresado
        cursor.execute('SELECT contraseña FROM usuarios WHERE usuario = ?', (usuario,))
        resultado = cursor.fetchone()

        # Verificar existencia del usuario y validar el hash
        if resultado and check_password_hash(resultado[0], contrasena_plana):
            return jsonify({'mensaje': 'Inicio de sesión exitoso'}), 200
        else:
            return jsonify({'error': 'Credenciales inválidas'}), 401

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if conexion:
            conexion.close()

@app.route('/tareas', methods=['GET'])
def tareas():
    # HTML estático de bienvenida
    html_bienvenida = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Bienvenida - Gestor de Tareas</title>
    </head>
    <body>
        <h1>Bienvenido al Sistema de Gestión de Tareas</h1>
        <p>Has accedido correctamente a la plataforma.</p>
    </body>
    </html>
    """
    return render_template_string(html_bienvenida)


if __name__ == '__main__':
    app.run(debug=True)