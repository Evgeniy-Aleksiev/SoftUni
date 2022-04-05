from django.db import models


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH
    )

    image_url = models.URLField(

    )

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    BOOK_TITLE_MAX_LENGTH = 30
    BOOK_TYPE_MAX_LENGTH = 30

    book_title = models.CharField(
        max_length=BOOK_TITLE_MAX_LENGTH
    )

    description = models.TextField(

    )

    image = models.URLField(

    )

    book_type = models.CharField(
        max_length=BOOK_TYPE_MAX_LENGTH
    )