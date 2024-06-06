# urls.py
from django.urls import path
from .views import get_csrf_token, LoginView, RegisterUser, LogoutView

urlpatterns = [
    path('get-csrf-token/', get_csrf_token, name='get-csrf-token'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]