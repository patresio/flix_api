import csv
import datetime

from django.core.management.base import BaseCommand

from actors.models import Actor


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("file_name", type=str, help="Nome do arquivo com atores")

    def handle(self, *args, **options):
        file_name = options["file_name"]

        with open(file_name, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                name = row["name"]
                birthday = datetime.strftime(row["birthday"], "%Y-%m-%d").date()
                nationality = row["nationality"]

                actor = Actor.objects.create(
                    name=name, birthday=birthday, nationality=nationality
                )
                self.stdout.write(self.style.SUCCESS(f"Actor {actor.name} created"))
