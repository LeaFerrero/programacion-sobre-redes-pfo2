# PFO 2: Sistema de Gestión de Tareas con API y Base de Datos

**Autor:** Leandro Raúl Ferrero

Este repositorio contiene el código fuente de la PFO 2 de programación sobre redes. El proyecto implementa una arquitectura cliente-servidor en Python. El servidor es una API REST construida con Flask que maneja la persistencia de datos mediante SQLite y asegura las credenciales utilizando la librería `werkzeug.security`. El cliente es un script de consola que permite interactuar con los endpoints HTTP de registro, login y visualización de recursos.

## Instrucciones de Ejecución

### 1. Requisitos Previos
* Python 3.x instalado en el sistema.
* Entorno virtual de Python (`venv`).

### 2. Instalación
Clonar el repositorio y configurar el entorno virtual:

    git clone [https://github.com/LeaFerrero/programacion-sobre-redes-pfo2.git](https://github.com/LeaFerrero/programacion-sobre-redes-pfo2.git)
    cd programacion-sobre-redes-pfo2
    python -m venv .venv
    source .venv/Scripts/activate
    pip install Flask requests

### 3. Ejecución del Servidor
Con el entorno virtual activado, iniciar la API Flask:

    python servidor.py

El servidor se ejecutará en http://127.0.0.1:5000 y generará automáticamente el archivo database.db en el directorio actual.

### 4. Ejecución del Cliente
Abrir una segunda terminal, activar nuevamente el entorno virtual y ejecutar el cliente interactivo:

    source .venv/Scripts/activate
    python cliente.py

Utilizar el menú numérico para registrar usuarios, iniciar sesión o consultar la ruta de tareas.

---

## Capturas de Pantalla de Pruebas Exitosas

**1. Registro de un nuevo usuario (POST /registro)**
![Captura Registro](capturas/registro.png)

**2. Inicio de sesión exitoso (POST /login)**
![Captura Login](capturas/login.png)

**3. Petición GET al endpoint /tareas**
![Captura Tareas](capturas/tareas.png)

**4. Registro de Logs**
![Captura Logs del Servidor](capturas/logs_servidor.png)
---

## Respuestas Conceptuales

### ¿Por qué hashear contraseñas?
Hashear contraseñas es un requisito de seguridad estricto para evitar el almacenamiento de credenciales en texto plano. El hashing aplica un algoritmo criptográfico unidireccional que transforma la contraseña original en una cadena de longitud fija. Si un atacante logra vulnerar el archivo de la base de datos, únicamente obtendrá los hashes, imposibilitando la lectura de las contraseñas reales. Para el proceso de autenticación, el sistema simplemente hashea la contraseña ingresada en el inicio de sesión y compara el resultado con el hash almacenado, validando la identidad sin necesidad de conocer el texto original.

### Ventajas de usar SQLite en este proyecto
SQLite es un motor de base de datos relacional transaccional, autónomo y sin servidor. Para este proyecto específico, sus principales ventajas son:

* **Ausencia de configuración:** No requiere instalar servicios externos, configurar puertos ni establecer credenciales de administrador en el sistema operativo.
* **Portabilidad:** Toda la base de datos y sus tablas residen en un único archivo físico local (`database.db`). Esto facilita la entrega académica, ya que el evaluador puede clonar el repositorio, ejecutar el script y la base de datos se generará automáticamente con el esquema correcto.
* **Integración nativa:** Al utilizar Python, el módulo `sqlite3` pertenece a la biblioteca estándar, eliminando la necesidad de instalar dependencias pesadas o conectores externos (drivers) adicionales para manejar la persistencia de datos.