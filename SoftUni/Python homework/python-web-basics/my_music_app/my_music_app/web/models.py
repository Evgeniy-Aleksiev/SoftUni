from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from my_music_app.web.validators import validate_letters_numbers_underscore


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 15
    USERNAME_MIN_LENGTH = 2
    MIN_AGE_VALIDATOR = 0

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(USERNAME_MIN_LENGTH),
            validate_letters_numbers_underscore,
        ),
    )

    email = models.EmailField(

    )

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(MIN_AGE_VALIDATOR),
        ),
    )


class Album(models.Model):
    ALBUM_MAX_LENGTH = 30
    ARTIST_MAX_LENGTH = 30
    GENRE_MAX_LENGTH = 30
    MIN_PRICE_VALIDATOR = 0.0

    POP_MUSIC = "Pop Music"
    JAZZ_MUSIC = "Jazz Music"
    RaB_MUSIC = "R&B Music"
    ROCK_MUSIC = "Rock Music"
    COUNTRY_MUSIC = "Country Music"
    DANCE_MUSIC = "Dance Music"
    HIP_HOP_MUSIC = "Hip Hop Music"
    OTHER = "Other"

    TYPES_CONTAINER = (POP_MUSIC, JAZZ_MUSIC,
                       RaB_MUSIC, ROCK_MUSIC,
                       COUNTRY_MUSIC, DANCE_MUSIC,
                       HIP_HOP_MUSIC, OTHER
                       )

    TYPES = [(x, x) for x in TYPES_CONTAINER]

    album_name = models.CharField(
        max_length=ALBUM_MAX_LENGTH,
        unique=True,
    )

    artist = models.CharField(
        max_length=ARTIST_MAX_LENGTH
    )

    genre = models.CharField(
        max_length=GENRE_MAX_LENGTH,
        choices=TYPES,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(

    )

    price = models.FloatField(
        validators=(
            MinValueValidator(MIN_PRICE_VALIDATOR),
        ),
    )