from django.urls.conf import path
from .views import AdminTagDetails, AdminViewTags, TagDetails, ViewTags


app_name = 'tags'

urlpatterns = [
    path('', ViewTags.as_view(), name='viewtags'),
    path('<int:pk>/', TagDetails.as_view(), name='tagdetails'),
    path('admin/', AdminViewTags.as_view(), name='adminviewtags'),
    path('admin/<int:pk>/', AdminTagDetails.as_view(), name='admintagdetails')
]