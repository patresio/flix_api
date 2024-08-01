# Generated by Django 5.0.7 on 2024-08-01 17:37

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'A avaliação não pode ser inferior a 0 estrelas'), django.core.validators.MaxValueValidator(5, 'A avaliação não pode ser superior a 5 estrelas')])),
                ('comment', models.TextField(blank=True, null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reviews', to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
