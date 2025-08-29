# Aplicación Web Python con Flask

Una aplicación web moderna desarrollada con Flask, Bootstrap y Docker, optimizada para despliegue en EasyPanel.

## 🚀 Características

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Contenedorización**: Docker
- **API RESTful**: Endpoints JSON
- **Interfaz Responsive**: Diseño adaptativo
- **Navegación SPA**: Single Page Application con sidebar

## 📁 Estructura del Proyecto

```
proyecto/
├── app.py              # Aplicación principal Flask
├── requirements.txt    # Dependencias Python
├── Dockerfile         # Configuración Docker
├── docker-compose.yml # Orquestación Docker
├── .dockerignore      # Archivos a ignorar en Docker
├── README.md          # Este archivo
└── templates/         # Plantillas HTML
    ├── index.html     # Página principal
    └── about.html     # Página de información
```

## 🛠️ Instalación Local

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar o descargar el proyecto**
   ```bash
   git clone <url-del-repositorio>
   cd python-flask-app
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   ```

3. **Activar entorno virtual**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

5. **Ejecutar la aplicación**
   ```bash
   python app.py
   ```

6. **Acceder a la aplicación**
   Abre tu navegador y ve a: `http://localhost:5000`

## 🐳 Despliegue con Docker

### Opción 1: Docker Compose (Recomendado)

1. **Construir y ejecutar**
   ```bash
   docker-compose up --build
   ```

2. **Ejecutar en segundo plano**
   ```bash
   docker-compose up -d --build
   ```

3. **Detener la aplicación**
   ```bash
   docker-compose down
   ```

### Opción 2: Docker Build

1. **Construir imagen**
   ```bash
   docker build -t python-flask-app .
   ```

2. **Ejecutar contenedor**
   ```bash
   docker run -p 5000:5000 python-flask-app
   ```

## 🌐 Despliegue en EasyPanel

### Paso 1: Preparar el Proyecto

1. **Comprimir archivos**
   - Selecciona todos los archivos del proyecto
   - Crea un archivo ZIP con la siguiente estructura:
   ```
   proyecto.zip
   ├── app.py
   ├── requirements.txt
   ├── Dockerfile
   ├── docker-compose.yml
   ├── .dockerignore
   └── templates/
       ├── index.html
       └── about.html
   ```

### Paso 2: Crear Contenedor en EasyPanel

1. **Acceder a EasyPanel**
   - Inicia sesión en tu panel de EasyPanel

2. **Crear nuevo contenedor**
   - Ve a la sección "Contenedores"
   - Haz clic en "Crear Contenedor"

3. **Configurar contenedor**
   - **Tipo**: Docker Compose
   - **Nombre**: `python-flask-app`
   - **Puerto**: `5000`
   - **Variables de entorno**:
     ```
     FLASK_ENV=production
     PORT=5000
     SECRET_KEY=tu-clave-secreta-aqui
     ```

### Paso 3: Subir Código

1. **Subir archivo ZIP**
   - En la configuración del contenedor, busca la opción para subir archivos
   - Sube el archivo `proyecto.zip` que creaste

2. **O usar Git (si está disponible)**
   - Si tu proyecto está en GitHub/GitLab, puedes usar la URL del repositorio
   - EasyPanel clonará automáticamente el código

### Paso 4: Iniciar Contenedor

1. **Revisar configuración**
   - Verifica que el puerto 5000 esté configurado
   - Confirma que las variables de entorno estén definidas

2. **Iniciar aplicación**
   - Haz clic en "Iniciar" o "Deploy"
   - Espera a que el contenedor se construya y ejecute

3. **Verificar funcionamiento**
   - Accede a la URL proporcionada por EasyPanel
   - Deberías ver la aplicación funcionando

## 🔧 Configuración

### Variables de Entorno

| Variable | Descripción | Valor por Defecto |
|----------|-------------|-------------------|
| `PORT` | Puerto de la aplicación | `5000` |
| `FLASK_ENV` | Entorno Flask | `production` |
| `SECRET_KEY` | Clave secreta para sesiones | `dev-key-change-in-production` |

### Endpoints de la API

| Método | Endpoint | Descripción | Respuesta |
|--------|----------|-------------|-----------|
| GET | `/` | Página principal | HTML |
| GET | `/api/status` | Estado de la API | JSON |
| GET | `/api/data` | Obtener datos | JSON |
| POST | `/api/data` | Enviar datos | JSON |
| GET | `/about` | Página de información | HTML |

## 🧪 Pruebas

### Probar API localmente

```bash
# Verificar estado de la API
curl http://localhost:5000/api/status

# Obtener datos
curl http://localhost:5000/api/data

# Enviar datos
curl -X POST http://localhost:5000/api/data \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","description":"Test description"}'
```

## 🔍 Solución de Problemas

### Problema: Contenedor no inicia
- **Solución**: Verifica que el puerto 5000 esté disponible
- **Solución**: Revisa los logs del contenedor en EasyPanel

### Problema: Error de dependencias
- **Solución**: Asegúrate de que `requirements.txt` esté incluido en el ZIP
- **Solución**: Verifica que el Dockerfile esté correcto

### Problema: Página no carga
- **Solución**: Verifica que la aplicación esté ejecutándose en el puerto correcto
- **Solución**: Revisa la configuración de red en EasyPanel

## 📝 Personalización

### Cambiar el diseño
- Edita los archivos en `templates/`
- Modifica los estilos CSS en las plantillas HTML
- Usa Bootstrap 5 para componentes adicionales

### Agregar nuevas rutas
- Edita `app.py` para agregar nuevas rutas
- Crea nuevas plantillas HTML en `templates/`

### Modificar la API
- Agrega nuevos endpoints en `app.py`
- Actualiza el frontend JavaScript para usar nuevos endpoints

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📞 Soporte

Si tienes problemas con el despliegue o necesitas ayuda:
- Revisa la documentación de EasyPanel
- Verifica los logs del contenedor
- Asegúrate de que todos los archivos estén incluidos en el ZIP 