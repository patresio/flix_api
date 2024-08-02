from django.db import models

# Create your models here.

NATIONALITY_CHOICES = (
    ("American", "American"),
    ("Brazilian", "Brazilian"),
    ("British", "British"),
    ("Canadian", "Canadian"),
    ("Mexican", "Mexican"),
    ("Russian", "Russian"),
    ("South African", "South African"),
    ("Turkish", "Turkish"),
    ("Vietnamese", "Vietnamese"),
    ("Filipino", "Filipino"),
    ("Haitian", "Haitian"),
    ("Native American", "Native American"),
    ("Indian", "Indian"),
    ("Asian", "Asian"),
    ("Pacific Islander", "Pacific Islander"),
    ("Other", "Other"),
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100, choices=NATIONALITY_CHOICES, default="American"
    )

    def __str__(self):
        return self.name
