from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('api-auth/', include('rest_framework.urls')),  # Para la autenticación de DRF
    path('authentication/', include('authentication.urls')),  # Incluye las rutas de autenticación
]