import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import requests
import logging

# Load environment variables from .env
load_dotenv()

logging.basicConfig(level=logging.INFO)
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    logging.info(f"Discord bot ready: {bot.user.name}")

def get_weather(location):
    api_key = os.getenv("WEATHER_API_KEY")
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={
            "q": location,
            "appid": api_key,
            "units": "metric"
        }
    )
    if response.status_code != 200:
        error_msg = response.json().get('message', 'City not found or API error.')
        # Ensure error_msg is always a string and log its type for debugging
        logging.error(f"API error message: {error_msg} (type: {type(error_msg)})")
        raise Exception(str(error_msg))
    return response.json()

@bot.command(name='weather')
async def weather(ctx, *, location: str):
    try:
        data = get_weather(location)
        await ctx.send(
            f"**🌍 {data['name']}, {data['sys']['country']}**\n"
            f"```\n"
            f"🌡️ Temp: {data['main']['temp']}°C\n"
            f"💧 Humidity: {data['main']['humidity']}%\n"
            f"🌬️ Wind: {data['wind']['speed']} m/s\n"
            f"```"
        )
    except Exception as e:
        logging.error(f"Exception in weather command: {e} (type: {type(e)})")
        await ctx.send(f"⚠️ Error: {str(e)}")

def run():
    bot.run(os.getenv("DISCORD_BOT_TOKEN"))