from django.core.management.base import BaseCommand
from website.models import SURVEY_LINKS

class Command(BaseCommand):
    help = 'Check all survey links in the database'

    def handle(self, *args, **options):
        self.stdout.write('Checking SURVEY_LINKS database...')
        
        all_objects = SURVEY_LINKS.objects.all()
        self.stdout.write(f'Total objects: {all_objects.count()}')
        
        if all_objects.count() == 0:
            self.stdout.write(self.style.WARNING('No survey links found in database!'))
            return
        
        self.stdout.write('\nAll survey links:')
        for obj in all_objects:
            self.stdout.write(f'  - ID: {obj.id}, Name: "{obj.name}", Category: "{obj.category}", Link: "{obj.link}"')
        
        categories = set([obj.category for obj in all_objects])
        self.stdout.write(f'\nAll categories: {categories}')
        
        # Test stichting category specifically
        stichting_objects = SURVEY_LINKS.objects.filter(category='stichting')
        self.stdout.write(f'\nObjects with category "stichting": {stichting_objects.count()}')
        
        # Test case-insensitive
        stichting_iexact = SURVEY_LINKS.objects.filter(category__iexact='stichting')
        self.stdout.write(f'Objects with category__iexact="stichting": {stichting_iexact.count()}')
        
        # Test partial match
        stichting_icontains = SURVEY_LINKS.objects.filter(category__icontains='stichting')
        self.stdout.write(f'Objects with category__icontains="stichting": {stichting_icontains.count()}') 