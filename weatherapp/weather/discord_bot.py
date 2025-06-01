import os
import discord
from discord.ext import commands
from django.conf import settings
import requests
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('discord_bot')

# Set up bot with intents
intents = discord.Intents.default()
intents.message_content = True  # Required to read message content

bot = commands.Bot(
    command_prefix='!',
    intents=intents,
    help_command=None  # Disable default help command
)

@bot.event
async def on_ready():
    logger.info(f'✅ Bot ready: {bot.user.name} (ID: {bot.user.id})')
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="!weather [city]"
        )
    )

@bot.command(name='weather')
async def weather_command(ctx, *, location: str = None):
    """Get weather for a specific location"""
    if not location:
        await ctx.send("🌤️ **Please specify a location!**\nExample: `!weather london`")
        return
    
    try:
        weather_info = get_weather_data(location)
        await ctx.send(weather_info)
    except Exception as e:
        logger.error(f"Weather command error: {str(e)}")
        await ctx.send(f"⚠️ Couldn't get weather for {location}. Please try again later.")

@bot.event
async def on_message(message):
    # Ignore messages from bots
    if message.author.bot:
        return
    
    # Handle direct mentions (e.g., @WeatherBot)
    if bot.user.mentioned_in(message):
        response = (
            "🌤️ **Weather Bot Help**\n"
            "Use `!weather [location]` to get weather info\n"
            "Example: `!weather tokyo`"
        )
        await message.channel.send(response)
    
    # Process commands
    await bot.process_commands(message)

def get_weather_data(location: str) -> str:
    """Fetch weather data from OpenWeatherMap API"""
    api_key = settings.WEATHER_API_KEY
    
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={
            'q': location,
            'appid': api_key,
            'units': 'metric'
        },
        timeout=10
    )
    
    if response.status_code != 200:
        error_msg = response.json().get('message', 'Unknown API error')
        raise Exception(f"Weather API error: {error_msg}")
    
    data = response.json()
    
    return (
        f"**🌍 {data['name']}, {data['sys']['country']}**\n"
        f"```\n"
        f"🌡️ Temperature: {data['main']['temp']}°C\n"
        f"💧 Humidity: {data['main']['humidity']}%\n"
        f"🌬️ Wind: {data['wind']['speed']} m/s\n"
        f"☁️ Conditions: {data['weather'][0]['description'].capitalize()}\n"
        f"```"
    )

def run():
    try:
        logger.info("Starting Discord bot...")
        bot.run(settings.DISCORD_BOT_TOKEN)
    except Exception as e:
        logger.critical(f"Bot crashed: {str(e)}")
        raise

if __name__ == "__main__":
    run()