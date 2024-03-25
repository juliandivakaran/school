import pandas as pd
from django.core.management.base import BaseCommand
from calc.models import Student

class Command(BaseCommand):
    help = 'Import students from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        df = pd.read_csv(csv_file_path)
        for index, row in df.iterrows():
            student_id, school_name = row['student_id'], row['school_name']
            Student.objects.create(student_id=student_id, school_name=school_name)
