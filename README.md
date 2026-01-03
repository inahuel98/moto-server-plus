# MotoServer: DescargasWEB

> **Transforma tu viejo Android en un Servidor de Descargas y Streaming con Python.**

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask-green)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

## Descripción

**MotoServer** es una aplicación web diseñada para reutilizar teléfonos Android antiguos (e-waste) convirtiéndolos en servidores domésticos eficientes. Permite descargar contenido multimedia (video y audio) de plataformas como YouTube, TikTok y otros, gestionando los archivos en una galería local accesible desde cualquier dispositivo en la red Wi-Fi.

El proyecto implementa una arquitectura **MVC (Modelo-Vista-Controlador)** modular y escalable, optimizada para hardware limitado (ARM).

## Características Principales

* **Descarga Híbrida:** Procesa la descarga en el servidor y la envía automáticamente al dispositivo del usuario.
* **Protección Anti-Bot:** Integración con `yt-dlp` configurado para evitar bloqueos de IP y listas de reproducción accidentales.
* **Galería Integrada:** Interfaz web moderna (Modo Oscuro) para visualizar, reproducir y gestionar archivos descargados.
* **Conversión Inteligente:** Soporte para MP3 y MP4, optimizado para bajo consumo de CPU.
* **Diseño Responsivo:** Funciona perfecto en móviles y escritorio.

## Arquitectura del Proyecto

El código ha sido refactorizado siguiendo patrones de ingeniería de software para facilitar su mantenimiento:

```text
MotoServer/
├── app/
│   ├── __init__.py      # Application Factory
│   ├── routes.py        # Controladores (Endpoints)
│   ├── services.py      # Lógica de Negocio (yt-dlp wrapper)
│   └── templates/       # Vistas (Jinja2 + CSS herencia)
├── Nube_Web/            # Almacenamiento local
├── config.py            # Variables de entorno y configuración
├── run.py               # Punto de entrada
└── requirements.txt     # Dependencias
```

Es necesaria la descarga de Termux en el dispositivo
Luego ejecutar los siguientes comandos
```bash pkg update && pkg upgrade -y 
pkg install python ffmpeg nodejs git -y 

git clone https://github.com/inahuel98/MotoServer.git
cd MotoServer

pip install -r requirements.txt

### Iniciar el servidor:
python3 run.py

### Acceder desde el navegador: 
Abri tu navegador y entra a la IP de tu celular: http://192.168.1.XX:8080 //completa segun la direccion ip del dispositivo (en Termux escribe ifconfig y busca la direccion bajo wlan0)
