import os
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import requests
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import logging

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('fase1/logs/weather.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Carrega variáveis de ambiente
load_dotenv()

app = FastAPI(title="FarmTech - Fase 1", description="API para dados meteorológicos e cálculos agrícolas")

class WeatherService:
    def __init__(self):
        self.api_key = os.getenv('WEATHER_API_KEY')
        self.base_url = "https://api.openweathermap.org/data/2.5"
        
    async def get_weather_data(self, lat: float, lon: float):
        """Obtém dados meteorológicos para uma localização específica."""
        try:
            url = f"{self.base_url}/weather"
            params = {
                'lat': lat,
                'lon': lon,
                'appid': self.api_key,
                'units': 'metric'
            }
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Erro ao obter dados meteorológicos: {str(e)}")
            raise HTTPException(status_code=500, detail="Erro ao obter dados meteorológicos")

class AgriculturalCalculator:
    def calculate_planting_area(self, length: float, width: float) -> float:
        """Calcula a área de plantio em hectares."""
        try:
            area_m2 = length * width
            area_ha = area_m2 / 10000
            return round(area_ha, 2)
        except Exception as e:
            logger.error(f"Erro ao calcular área: {str(e)}")
            raise HTTPException(status_code=500, detail="Erro ao calcular área")

    def calculate_inputs(self, area_ha: float, crop_type: str) -> dict:
        """Calcula a quantidade de insumos necessários."""
        # Valores de exemplo - devem ser ajustados conforme necessidade
        inputs_per_ha = {
            'soja': {'sementes': 80, 'fertilizante': 300, 'agua': 5000},
            'milho': {'sementes': 25, 'fertilizante': 350, 'agua': 6000},
            'trigo': {'sementes': 120, 'fertilizante': 250, 'agua': 4000}
        }
        
        try:
            if crop_type not in inputs_per_ha:
                raise ValueError(f"Cultura {crop_type} não suportada")
                
            inputs = inputs_per_ha[crop_type]
            return {
                'sementes_kg': round(inputs['sementes'] * area_ha, 2),
                'fertilizante_kg': round(inputs['fertilizante'] * area_ha, 2),
                'agua_litros': round(inputs['agua'] * area_ha, 2)
            }
        except Exception as e:
            logger.error(f"Erro ao calcular insumos: {str(e)}")
            raise HTTPException(status_code=500, detail=str(e))

# Instâncias dos serviços
weather_service = WeatherService()
agri_calculator = AgriculturalCalculator()

@app.get("/")
async def root():
    """Endpoint raiz para verificação de status."""
    return {"status": "online", "service": "FarmTech Fase 1"}

@app.get("/weather/{lat}/{lon}")
async def get_weather(lat: float, lon: float):
    """Endpoint para obter dados meteorológicos."""
    return await weather_service.get_weather_data(lat, lon)

@app.get("/calculate/area/{length}/{width}")
async def calculate_area(length: float, width: float):
    """Endpoint para calcular área de plantio."""
    return {"area_ha": agri_calculator.calculate_planting_area(length, width)}

@app.get("/calculate/inputs/{area}/{crop_type}")
async def calculate_inputs(area: float, crop_type: str):
    """Endpoint para calcular insumos necessários."""
    return agri_calculator.calculate_inputs(area, crop_type.lower())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 