from flask import Blueprint, render_template, request, send_from_directory, current_app, redirect, url_for
from app.services import DownloaderService
from config import Config

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    archivos = DownloaderService.obtener_archivos()
    return render_template('index.html', lista_archivos=archivos)

@main_bp.route('/procesar', methods=['POST'])
def procesar():
    url = request.form.get('url')
    tipo = request.form.get('tipo')
    
    if not url:
        return redirect(url_for('main.home'))

    try:
        nombre_archivo = DownloaderService.descargar_contenido(url, tipo)
        
        if nombre_archivo:
            # genera una URL interna para descarga forzada
            link_descarga = url_for('main.download_file', filename=nombre_archivo)
            return render_template('result.html', 
                                   nombre_archivo=nombre_archivo, 
                                   link_descarga_directa=link_descarga)
        else:
            return render_template('result.html', error="Archivo no encontrado tras descarga.")
            
    except Exception as e:
        return render_template('result.html', error=str(e))

@main_bp.route('/ver/<path:filename>')
def view_file(filename):
    return send_from_directory(Config.DOWNLOAD_FOLDER, filename)

@main_bp.route('/bajar/<path:filename>')
def download_file(filename):
    return send_from_directory(Config.DOWNLOAD_FOLDER, filename, as_attachment=True)