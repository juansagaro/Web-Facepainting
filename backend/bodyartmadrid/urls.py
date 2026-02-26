"""
URL configuration for bodyartmadrid project.

- /admin/  → Panel de administración de Django
- /        → Todo lo demás lo gestiona webapp.urls
- /media/  → Archivos subidos (solo en desarrollo con DEBUG=True)
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),
]

# En desarrollo: servir archivos media (imagenes subidas desde el admin)
# En producción esto lo sirve nginx/apache, no Django.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
