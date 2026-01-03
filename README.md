# MotoServer: DescargasWEB

> **Transforma tu viejo Android en un Servidor de Descargas y Streaming con Python.**


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
```
## Demo
## 📸 Galería del Proyecto

<table>
  <tr>
    <td width="50%">
      <h3 align="center">Pantalla de Inicio, Pega tu link </h3>
      <img src="https://private-user-images.githubusercontent.com/72147221/531668071-2514781b-9447-40ec-9f5b-d56a4682c338.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njc0ODI1MTYsIm5iZiI6MTc2NzQ4MjIxNiwicGF0aCI6Ii83MjE0NzIyMS81MzE2NjgwNzEtMjUxNDc4MWItOTQ0Ny00MGVjLTlmNWItZDU2YTQ2ODJjMzM4LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjAxMDMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwMTAzVDIzMTY1NlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWQ4OTRkMzZmN2Y5YWQ4MmY4YzU3NTA2NDRjYjdkYTI0N2Y5ODUxNThiNTE1NDM3MzUwOTM0ZDkzYjNiYWEwMjYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.H5svMWm20KoWcHofjm2UMZBwRwLaP1w3WllMU2YnuzA" width="100%">
    </td>
    <td width="50%">
      <h3 align="center">Espera la Descarga</h3>
      <img src="https://private-user-images.githubusercontent.com/72147221/531668070-70fe5211-12d1-4957-a13f-41461c45f908.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njc0ODI1MTYsIm5iZiI6MTc2NzQ4MjIxNiwicGF0aCI6Ii83MjE0NzIyMS81MzE2NjgwNzAtNzBmZTUyMTEtMTJkMS00OTU3LWExM2YtNDE0NjFjNDVmOTA4LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjAxMDMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwMTAzVDIzMTY1NlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWNkZGVjMjZhM2Q3MGU4ODM3Y2YwZWMxMDgwZjE1NWRkMTExNjlhZGE1ODBhYzVhMTE4NWEzMmQ5YzIxMDc4ZWQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.MCz5QfX1xIapHqbZ2ttdN-fkQ9J560CKuwpMU45YNYs" width="100%">
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3 align="center">Descarga exitosa</h3>
      <img src="https://private-user-images.githubusercontent.com/72147221/531668072-3e37f2e7-2565-40da-9660-57fed0a5a7e6.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njc0ODI1MTYsIm5iZiI6MTc2NzQ4MjIxNiwicGF0aCI6Ii83MjE0NzIyMS81MzE2NjgwNzItM2UzN2YyZTctMjU2NS00MGRhLTk2NjAtNTdmZWQwYTVhN2U2LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjAxMDMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwMTAzVDIzMTY1NlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWVlNTRkZDBiZThmYjQ2NWVhYjA2OGY0MDE4Y2QzMzUyMjUzMDJhMjBlMjQwNDU1MDNiNGJlMjcyNTAyYjU2OWMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.91INWTY0Ip5KetHyRRYIrnvp0zJXbGSsl2EPTCy0eEw" width="100%">
    </td>
    <td width="50%">
      <h3 align="center">Muestra de archivos descargados y alojados en el server</h3>
      <img src="https://private-user-images.githubusercontent.com/72147221/531668073-8815614d-731b-42f1-9fb5-805fd6ed9a9c.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njc0ODI1MTYsIm5iZiI6MTc2NzQ4MjIxNiwicGF0aCI6Ii83MjE0NzIyMS81MzE2NjgwNzMtODgxNTYxNGQtNzMxYi00MmYxLTlmYjUtODA1ZmQ2ZWQ5YTljLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjAxMDMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwMTAzVDIzMTY1NlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWU1Y2Q5OWI5ZTAxODAzOTYyNGMyMzI2YjQwZDlhYjcwMDBiZTQ0NzA3OTdiNWU0N2NjYWRkMzAyOGJmMjA4ZmEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.ou7dvgrD3fbZyh8RXzqHVabk9_w1JZWiA2p8bS5gIek" width="100%">
    </td>
  </tr>
</table>
