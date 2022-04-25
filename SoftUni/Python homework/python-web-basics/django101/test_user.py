from django.contrib.auth import get_user_model
from django.db import  models


UserModel = get_user_model()
UserModel.objects.create_user(
    username='aleksiev',
    password='12345qwe',
)