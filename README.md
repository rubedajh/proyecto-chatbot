README — Proyecto Chatbot con Python, JSON y Docker

🧠 Descripción del proyecto

Este proyecto consiste en un chatbot sencillo desarrollado en Python que utiliza un archivo JSON como base de datos de respuestas.

El objetivo es demostrar:

• 	Desarrollo de una aplicación en Python

• 	Uso de un archivo JSON para almacenar información

• 	Contenerización mediante Docker

• 	Ejecución con Docker Compose

• 	Control de versiones con Git y GitHub (ramas, commits y Pull Requests)

El proyecto forma parte del módulo de Optativa – Proyecto Final.



📂 Estructura del proyecto

proyecto-chatbot/

├─ app.py

├─ base\_datos.json

├─ requirements.txt

├─ Dockerfile

├─ docker-compose.yml

└─ README.md

✔ app.py

Código principal del chatbot en Python.

✔ base\_datos.json

Archivo JSON con las respuestas del bot.

✔ requirements.txt

Dependencias necesarias para ejecutar la aplicación.

✔ Dockerfile

Define la imagen Docker del proyecto.

✔ docker-compose.yml

Permite ejecutar el contenedor de forma sencilla.



🐍 Código de la aplicación (Python)

El archivo app.py carga el JSON y responde según el mensaje del usuario.



Es un chatbot básico que sirve como demostración funcional.



🗂 Base de datos JSON

Ejemplo del contenido:

{

&#x20; "hola": "Hola, ¿cómo estás?",

&#x20; "adios": "¡Hasta luego!",

&#x20; "default": "No entiendo tu mensaje, pero estoy aprendiendo."

}



Docker

✔ Construir la imagen

En la terminal de Visual Studio Code:

docker build -t chatbot .



✔ Ejecutar con Docker Compose

docker compose up



🧪 Requisitos previos

Para ejecutar el proyecto se necesita:

\- Python 3

\- Docker Desktop

\- Visual Studio Code

\- Git instalado



🌿 Control de versiones (Git y GitHub)

El repositorio incluye:

✔ Ramas creadas

\- main

\- feature/app (u otras ramas según el desarrollo)

✔ Commits documentados

Cada cambio se ha registrado con mensajes claros.

✔ Pull Request

Se ha creado un Pull Request desde la rama de desarrollo hacia main y se ha fusionado correctamente.



📌 Pasos realizados en Git

\- Inicialización del repositorio:

git init





\- Primer commit:

git add .

git commit -m "Versión inicial del proyecto"





\- Conexión con GitHub:

git remote add origin https://github.com/usuario/proyecto-chatbot.git

git branch -M main

git push -u origin main





\- Creación de rama:

git checkout -b feature/app





\- Subida de la rama:

git push -u origin feature/app





\- Creación y fusión del Pull Request en GitHub.



🎯 Conclusión

Este proyecto demuestra el uso combinado de:

\- Python

\- JSON

\- Docker

\- Docker Compose

\- Git

\- GitHub

Cumpliendo todos los entregables solicitados en el enunciado.

