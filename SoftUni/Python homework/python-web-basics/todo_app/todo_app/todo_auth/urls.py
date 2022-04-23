from django.urls import path

from todo_app.todo_auth import views

urlpatterns = (
    path('register/', views.RegisterView.as_view(), name='register view'),
    path('login/', views.LoginView.as_view(), name='login view'),
    # path('logout/', views.LogoutView.as_view(), name='logout view'),
)