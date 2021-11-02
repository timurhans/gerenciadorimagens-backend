from django.urls.conf import path
from .views import MediaDetail, PublicMediaDetail, ViewPublicMedia, ViewMedia


app_name = 'media'

urlpatterns = [
    path('', ViewPublicMedia.as_view(), name='publicmediaview'),
    path('<int:pk>/', PublicMediaDetail.as_view(), name='publicmediadetail'),
    path('admin/', ViewMedia.as_view(), name='mediaview'),
    path('admin/<int:pk>/', MediaDetail.as_view(), name='mediadetail')
]