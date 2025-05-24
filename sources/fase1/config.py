import os
from pathlib import Path

# Diretórios base
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
LOGS_DIR = BASE_DIR / "logs"

# Criar diretórios se não existirem
for directory in [DATA_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR, LOGS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# Configurações da API
API_CONFIG = {
    "title": "FarmTech - Fase 1",
    "description": "API para dados meteorológicos e cálculos agrícolas",
    "version": "1.0.0",
    "docs_url": "/docs",
    "redoc_url": "/redoc"
}

# Configurações de logging
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "stream": "ext://sys.stdout"
        },
        "file": {
            "class": "logging.FileHandler",
            "formatter": "default",
            "filename": str(LOGS_DIR / "weather.log")
        }
    },
    "root": {
        "level": "INFO",
        "handlers": ["console", "file"]
    }
}

# Configurações de culturas
CROP_CONFIG = {
    "soja": {
        "sementes_kg_ha": 80,
        "fertilizante_kg_ha": 300,
        "agua_litros_ha": 5000,
        "ciclo_dias": 120
    },
    "milho": {
        "sementes_kg_ha": 25,
        "fertilizante_kg_ha": 350,
        "agua_litros_ha": 6000,
        "ciclo_dias": 150
    },
    "trigo": {
        "sementes_kg_ha": 120,
        "fertilizante_kg_ha": 250,
        "agua_litros_ha": 4000,
        "ciclo_dias": 180
    }
}

# Configurações de API externa
WEATHER_API_CONFIG = {
    "base_url": "https://api.openweathermap.org/data/2.5",
    "units": "metric",
    "lang": "pt_br"
} 