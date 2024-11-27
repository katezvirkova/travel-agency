from django.core.management.base import BaseCommand
from travel_bot.bot import *

class Command(BaseCommand):
    help = 'Run the Telegram bot'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting Telegram bot...')
        main()
