from superset.config import *

FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True,
    "DASHBOARD_NATIVE_FILTERS": True,         # 🔥 Esta línea habilita filtros nativos
    "DASHBOARD_NATIVE_FILTERS_SET": True,     # 🔥 Esta línea permite usar presets de filtros
    "ENABLE_EXPLORE_DRAG_AND_DROP": True,     # (Opcional, mejora el editor de charts)
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
}
