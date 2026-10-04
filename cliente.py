import requests

BASE_URL = 'http://127.0.0.1:5000'

def registrar_usuario():
    usuario = input("Ingrese nuevo usuario: ")
    contrasena = input("Ingrese contraseña: ")

    try:
        respuesta = requests.post(f"{BASE_URL}/registro", json={
            "usuario": usuario,
            "contraseña": contrasena
        })
        print(f"Estado HTTP: {respuesta.status_code}")
        print(f"Respuesta: {respuesta.json()}\n")
    except requests.exceptions.ConnectionError:
        print("Error: No se pudo conectar al servidor. Verificá que Flask esté en ejecución.\n")

def iniciar_sesion():
    usuario = input("Ingrese usuario: ")
    contrasena = input("Ingrese contraseña: ")

    try:
        respuesta = requests.post(f"{BASE_URL}/login", json={
            "usuario": usuario,
            "contraseña": contrasena
        })
        print(f"Estado HTTP: {respuesta.status_code}")
        print(f"Respuesta: {respuesta.json()}\n")
    except requests.exceptions.ConnectionError:
        print("Error: No se pudo conectar al servidor. Verificá que Flask esté en ejecución.\n")

def ver_tareas():
    try:
        respuesta = requests.get(f"{BASE_URL}/tareas")
        print(f"Estado HTTP: {respuesta.status_code}")
        print(f"Contenido HTML:\n{respuesta.text}\n")
    except requests.exceptions.ConnectionError:
        print("Error: No se pudo conectar al servidor. Verificá que Flask esté en ejecución.\n")

def menu():
    while True:
        print("--- MENÚ DEL CLIENTE ---")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Ver tareas (HTML)")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            iniciar_sesion()
        elif opcion == '3':
            ver_tareas()
        elif opcion == '4':
            break
        else:
            print("Opción inválida.\n")

if __name__ == '__main__':
    menu()