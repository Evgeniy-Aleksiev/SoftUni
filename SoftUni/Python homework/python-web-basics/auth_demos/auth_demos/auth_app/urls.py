from django.urls import path

from auth_demos.auth_app.views import UserRegistrationView, UserLoginView, UserLogoutView, RestrictedView

urlpatterns = (
    path('register/', UserRegistrationView.as_view(), name='register user'),
    path('login/', UserLoginView.as_view(), name='login view'),
    path('logout/', UserLogoutView.as_view(), name='logout view'),
    path('restricted/', RestrictedView.as_view(), name='restricted'),
)