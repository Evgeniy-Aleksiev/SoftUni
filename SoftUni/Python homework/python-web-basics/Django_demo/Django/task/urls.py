from django.urls import path

from Django.task.views import home

urlpatterns = (
    path('', home),
)