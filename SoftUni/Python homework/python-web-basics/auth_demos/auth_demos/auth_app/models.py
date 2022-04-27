from django.contrib.auth import models as auth_models
from django.db import models

from auth_demos.auth_app.managers import AppUserManager


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    if_staff = models.BooleanField(
        default=False,
    )

    date_join = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'

    objects = AppUserManager()


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 25

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
    )

    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

# UserModel = get_user_model()
#
#
# class UserWithFullNameProxy(UserModel):
#     @property
#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'
#
#
# class Profile(models.Model):
#     # fields
#     # profile_image
#     # date_of_birth
#     # pets
#
#     user = models.OneToOneField(UserModel, on_delete=models.CASCADE)

