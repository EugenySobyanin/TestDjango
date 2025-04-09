from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


User = get_user_model()


class Film(models.Model):
    title = models.CharField('Название', max_length=255)
    rating_kp = models.SmallIntegerField(
        'Оценка кинопоиска',
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    release_year = models.IntegerField(
        'Год выпуска',
        validators=[MinValueValidator(1985)])
