from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',  include('users.urls', namespace='users')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/media/', include('media.urls', namespace='media')),
    path('api/books/', include('books.urls', namespace='books')),
    path('api/products/', include('products.urls', namespace='products')),
    path('api/tags/', include('tags.urls', namespace='tags')),
    path('api/colors/', include('colors.urls', namespace='colors')),
    path('api/properties/', include('properties.urls', namespace='properties')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)