from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, my_protected_view

urlpatterns = [
    path('login/', my_protected_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    # other URL patterns
]

