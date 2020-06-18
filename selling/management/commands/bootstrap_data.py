from django.core.management.base import BaseCommand, CommandError
from selling.models import ShoeType, ShoeColor

class Command(BaseCommand):
    help = 'Adds shoe type and color tables'

    def handle(self, *args, **options):
        styles = [
            'sneaker',
            'boot',
            'sandal',
            'dress',
            'other'
        ]

        colors = [
            'Red',
            'Orange',
            'Yellow',
            'Green',
            'Blue',
            'Indigo',
            'Violet',
            'White',
            'Black'
        ]

        for style in styles:
            ShoeType.objects.create(style=style)
        for color in colors:
            ShoeColor.objects.create(color=color)