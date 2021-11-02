from django.urls.conf import path
from .views import AdminBookDetails, AdminViewBooks, ViewBooks, BookDetails


app_name = 'books'

urlpatterns = [
    path('', ViewBooks.as_view(), name='booklist'),
    path('<int:pk>/', BookDetails.as_view(), name='bookdetails'),
    path('admin/', AdminViewBooks.as_view(), name='adminbooklist'),
    path('admin/<int:pk>/', AdminBookDetails.as_view(), name='adminbookdetails')
]