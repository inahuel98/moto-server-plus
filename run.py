from app import create_app
from config import Config
import os

app = create_app()

if __name__ == '__main__':
    # chequeo la existencia de la carpeta
    if not os.path.exists(Config.DOWNLOAD_FOLDER):
        os.makedirs(Config.DOWNLOAD_FOLDER)
        
    # arranco el servidor en el puerto 8080
    app.run(host='0.0.0.0', port=8080, threaded=True)