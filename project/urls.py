from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
	path('', include('blog.urls')),
	path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
]

# Serve media static files in development mode
# https://docs.djangoproject.com/en/2.2/howto/static-files/
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
