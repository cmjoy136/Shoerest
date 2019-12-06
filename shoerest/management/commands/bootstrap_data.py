from django.core.management.base import BaseCommand, CommandError
from shoerest.quickstart.models import ShoeColor, ShoeType

class Command(BaseCommand):
    help = 'populate shoecolors and shoe type'

    def handle(self, *args, **options):
        ShoeColor.objects.create(color_name='Red')
        ShoeColor.objects.create(color_name='Orange')
        ShoeColor.objects.create(color_name='Yellow')
        ShoeColor.objects.create(color_name='Green')
        ShoeColor.objects.create(color_name='Blue')
        ShoeColor.objects.create(color_name='Indigo')
        ShoeColor.objects.create(color_name='Violet')
        ShoeColor.objects.create(color_name='White')
        ShoeColor.objects.create(color_name='Black')
        ShoeType.objects.create(style='Sneaker')
        ShoeType.objects.create(style='Boot')
        ShoeType.objects.create(style='Sandal')
        ShoeType.objects.create(style='Dress')
        ShoeType.objects.create(style='Other')
    