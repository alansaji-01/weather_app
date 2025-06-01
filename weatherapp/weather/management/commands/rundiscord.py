# weather/management/commands/rundiscord.py
from django.core.management.base import BaseCommand
from weather.discord_bot import run

class Command(BaseCommand):
    help = 'Run the Discord bot'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting Discord bot...'))
        run()
    