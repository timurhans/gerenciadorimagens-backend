from django.urls.conf import path
from .views import AdminColorDetails, CreateColor, ViewColors


app_name = 'colors'

urlpatterns = [
    path('', ViewColors.as_view(), name='viewcolors'),
    path('create/', CreateColor.as_view(), name='createcolor'),
    path('<int:pk>/', AdminColorDetails.as_view(), name='adminupdatecolor')
]