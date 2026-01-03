import subprocess
import os
import glob
from datetime import datetime
from config import Config

class DownloaderService:
    @staticmethod
    def descargar_contenido(url, tipo):
        prefijo = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_template = f"{prefijo}_%(title)s.%(ext)s"
        
        # Comando Base 
        comando = [
            "yt-dlp", 
            "-P", Config.DOWNLOAD_FOLDER, 
            "--restrict-filenames",
            "--no-playlist" # Protección anti-bloqueo para no descargar playlist y que Google bloquee nuestra IP
        ]

        if tipo == 'audio':
            comando += [
                "-x", 
                "--audio-format", "mp3", 
                "--audio-quality", "128K", #esta calidad ya que la mayor calidad solo esta disponible en YTM premium
                "--force-overwrites", 
                "-o", output_template, 
                url
            ]
        else:
            comando += [
                "--merge-output-format", "mp4", 
                "--force-overwrites", 
                "-o", output_template, 
                url
            ]

        # Ejecutar y lanzar excepción si falla
        subprocess.run(comando, check=True)
        
        # Buscar el archivo descargado
        patron = os.path.join(Config.DOWNLOAD_FOLDER, f"{prefijo}_*")
        encontrados = glob.glob(patron)
        
        if encontrados:
            return os.path.basename(encontrados[0])
        return None

    @staticmethod
    def obtener_archivos():
        archivos = []
        try:
            rutas = glob.glob(os.path.join(Config.DOWNLOAD_FOLDER, "*"))
            rutas.sort(key=os.path.getmtime, reverse=True)
            
            for ruta in rutas:
                nombre = os.path.basename(ruta)
                if nombre.startswith("."): continue
                
                size_mb = os.path.getsize(ruta) / (1024 * 1024)
                size_str = f"{size_mb:.1f} MB" if size_mb >= 1 else f"{int(os.path.getsize(ruta)/1024)} KB"
                
                fecha_ts = os.path.getmtime(ruta)
                fecha_str = datetime.fromtimestamp(fecha_ts).strftime('%d/%m %H:%M')
                
                ext = os.path.splitext(nombre)[1].lower()
                icono = "🎵" if ext in ['.mp3', '.m4a'] else "🎬" if ext in ['.mp4', '.mkv', '.webm'] else "📄"
                
                archivos.append({
                    "nombre": nombre, "tamano": size_str, "fecha": fecha_str, "icono": icono
                })
        except Exception:
            pass # Si falla listar, devolvemos lista vacia
            
        return archivos