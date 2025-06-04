import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables FIRST
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG') == 'True'

# API Configurations
WEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'weather.apps.WeatherConfig',
]

ROOT_URLCONF = 'weatherapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
    }
]

STATIC_URL = 'static/'