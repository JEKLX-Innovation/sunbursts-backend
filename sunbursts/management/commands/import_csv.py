"""
Defines a Django management command for importing elements and their categories from a CSV file.

This module provides the ImportElementsCommand class, which is a management command
for importing data from a CSV file into the Element and Category models.

"""

from django.core.management.base import BaseCommand
import csv
from sunbursts.models import Element, Category

class Command(BaseCommand):
    """
    Management command for importing elements and categories from a CSV file.

    Inherits from Django's BaseCommand.

    Attributes:
        help (str): Description of the command.
    """
    help = 'Import elements and their categories from a CSV file'

    def add_arguments(self, parser):
        """
        Adds command-line arguments to the command.

        Args:
            parser: Argument parser object.
        """
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        """
        Handles the execution of the command.

        Reads data from the specified CSV file and creates Element and Category objects accordingly.

        Args:
            *args: Additional arguments.
            **options: Keyword arguments representing command options.
        """
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