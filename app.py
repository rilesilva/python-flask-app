from flask import Flask, render_template, jsonify, request
import os
from datetime import datetime

app = Flask(__name__)

# Configuración básica
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/api/status')
def api_status():
    """Endpoint de estado de la API"""
    return jsonify({
        'status': 'success',
        'message': 'API funcionando correctamente',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

@app.route('/api/data', methods=['GET', 'POST'])
def api_data():
    """Endpoint para manejar datos"""
    if request.method == 'GET':
        return jsonify({
            'items': [
                {'id': 1, 'name': 'Elemento 1', 'description': 'Descripción del elemento 1'},
                {'id': 2, 'name': 'Elemento 2', 'description': 'Descripción del elemento 2'},
                {'id': 3, 'name': 'Elemento 3', 'description': 'Descripción del elemento 3'}
            ]
        })
    elif request.method == 'POST':
        data = request.get_json()
        return jsonify({
            'status': 'success',
            'message': 'Datos recibidos correctamente',
            'received_data': data
        })

@app.route('/about')
def about():
    """Página de información"""
    return render_template('about.html')

if __name__ == '__main__':
    # Obtener puerto del entorno o usar 5000 por defecto
    port = int(os.environ.get('PORT', 5000))
    # Ejecutar en modo debug solo en desarrollo
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    app.run(host='0.0.0.0', port=port, debug=debug) 