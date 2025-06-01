# weather/telegram_bot.py
import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from django.conf import settings

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context):
    await update.message.reply_text(
        "🌤️ Weather Bot Help:\n"
        "Just send me a location name (e.g., 'London' or 'New York') "
        "and I'll give you current weather info!"
    )


async def handle_location(update: Update, context):
    location = update.message.text
    try:
        weather_info = get_weather_data(location)
        await update.message.reply_text(weather_info)
    except Exception as e:
        await update.message.reply_text(f"⚠️ Error: {str(e)}")

def get_weather_data(location: str) -> str:
    """Reusable weather fetch function"""
    import requests
    api_key = settings.WEATHER_API_KEY
    
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={location}"
        f"&appid={api_key}&units=metric"
    )
    data = response.json()
    
    if response.status_code != 200:
        raise Exception(data.get('message', 'Unknown error'))
    
    return (
        f"🌍 Location: {data['name']}, {data['sys']['country']}\n"
        f"🌡️ Temperature: {data['main']['temp']}°C\n"
        f"💧 Humidity: {data['main']['humidity']}%\n"
        f"🌬️ Wind: {data['wind']['speed']} m/s\n"
        f"☁️ Conditions: {data['weather'][0]['description'].capitalize()}"
    )

def main():
    application = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_location))
    
    application.run_polling()

if __name__ == "__main__":
    main()