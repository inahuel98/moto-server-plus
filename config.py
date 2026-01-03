import os

class Config:
    # Ruta absoluta a la carpeta de descargas
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DOWNLOAD_FOLDER = os.path.join(BASE_DIR, 'Nube_Web')
    
    # Configuración de Flask
    SECRET_KEY = 'moto_server_secret_key' # Necesario para seguridad básica 