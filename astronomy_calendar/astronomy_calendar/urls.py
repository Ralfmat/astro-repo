from django.contrib import admin
from django.urls import include, path
from .views import hello_world

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world, name='hello_world'),
    path('accounts/', include('user_management.urls')),
]
