from django.core.management.base import BaseCommand
import csv
from sunbursts.models import Element, Category

class Command(BaseCommand):
    help = 'Import elements and their categories from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        with open(options['csv_file'], mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                category_name = row['Category'].strip()
                category, created = Category.objects.get_or_create(name=category_name)
                
                Element.objects.create(
                    name=row['Element'].strip(),
                    category=category if category_name else None
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported data from CSV'))
