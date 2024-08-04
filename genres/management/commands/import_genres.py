import csv

from django.core.management.base import BaseCommand

from genres.models import Genre


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("file_name", type=str, help="Nome do arquivo com generos")

    def handle(self, *args, **options):
        file_name = options["file_name"]

        with open(file_name, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                name = row["name"]

                genre = Genre.objects.create(name=name)
                self.stdout.write(self.style.SUCCESS(f"Genre {genre.name} created"))
