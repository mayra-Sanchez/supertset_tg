from superset.config import *

# Habilitar funciones de embedding
FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True,
}

# Habilitar CORS para Angular
ENABLE_CORS = True
CORS_OPTIONS = {
    'supports_credentials': True,
    'allow_headers': ['*'],
    'resources': ['*'],
    'origins': [
        'http://localhost:4200',  # Ajusta según el dominio/puerto de tu frontend
    ]
}

# Encabezados HTTP para permitir que se cargue en iframe desde Angular
HTTP_HEADERS = {
    'Content-Security-Policy': "frame-ancestors 'self' http://localhost:4200;",
    # No uses X-Frame-Options porque no tiene efecto en navegadores modernos
}
