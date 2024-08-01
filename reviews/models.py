from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from movies.models import Movie


# Create your models here.
class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name="reviews", on_delete=models.PROTECT)
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, "A avaliação não pode ser inferior a 0 estrelas"),
            MaxValueValidator(5, "A avaliação não pode ser superior a 5 estrelas"),
        ]
    )
    comment = models.TextField(null=True, blank=True)
    # user = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)

    def __str__(self):
        return self.movie
