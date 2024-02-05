from django.urls import path
from . import views

urlpatterns = [
    # path('register/', views.registration_user_api_view),
    # path('login/', views.login_user_api_view),
    # path('confirm/', views.confirm_user_api_view),
    path('register/', views.UserRegistrationView.as_view()),
    path('login/', views.UserLoginView.as_view()),
    path('confirm/', views.ConfirmUserView.as_view()),
    ]