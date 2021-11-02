from django.urls.conf import path
from .views import  AdminGetColorVariations, AdminProductDetails, AdminViewProducts, ProductDetails, ViewProducts
from .views import CreateColorVariation


app_name = 'products'

urlpatterns = [
    path('', ViewProducts.as_view(), name='viewproducts'),
    path('<int:pk>/', ProductDetails.as_view(), name='productdetails'),
    path('admin/', AdminViewProducts.as_view(), name='adminviewproducts'),
    path('admin/createvariation/', CreateColorVariation.as_view(), name='createcolorvariation'),
    path('admin/<int:pk>/', AdminProductDetails.as_view(), name='adminproductdetails'),
    path('admin/variations/<int:pk>/', AdminGetColorVariations.as_view(), name='getvariations'),
]