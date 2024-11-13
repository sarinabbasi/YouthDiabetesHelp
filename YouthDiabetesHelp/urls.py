from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('home.urls')),

            path('about/', include('about.urls')),
            path('contact/', include('contact.urls')),
            path('article/', include('article.urls')),
            path('donation/', include('donation.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
