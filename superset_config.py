from superset.config import *

FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True,
    "DASHBOARD_NATIVE_FILTERS": True,
    "DASHBOARD_NATIVE_FILTERS_SET": True,
    "ENABLE_EXPLORE_DRAG_AND_DROP": True,
}

# === Habilitar CORS para Angular ===
ENABLE_CORS = True
CORS_OPTIONS = {
    'supports_credentials': True,
    'allow_headers': ['*'],
    'resources': ['*'],
    'origins': [
        'http://localhost:4200',
        'https://rpe-topaz.vercel.app',   # dominio de producción
    ]
}

# === Permitir iframes desde ambos orígenes ===
HTTP_HEADERS = {
    'Content-Security-Policy': "frame-ancestors 'self' http://localhost:4200 https://rpe-topaz.vercel.app;",
}
