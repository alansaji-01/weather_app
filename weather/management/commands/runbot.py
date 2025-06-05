# weather/management/commands/runbot.py
from django.core.management.base import BaseCommand
from weather.telegram_bot import main

class Command(BaseCommand):
    help = 'Run the Telegram bot'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting Telegram bot...'))
        main()

        