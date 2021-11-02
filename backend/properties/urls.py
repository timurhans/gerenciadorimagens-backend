from django.urls.conf import path
from .views import ViewMediaStyle, ViewMediaStyles, ViewMediaType, ViewMediaTypes
from .views import ViewProductCollection, ViewProductCollections
from .views import ViewProductCategory ,ViewProductCategories
from .views import ViewProductSubCategory, ViewProductSubCategories
from .views import CreateMediaType, CreateMediaStyle
from .views import CreateProductCategory, CreateProductCollection, CreateProductSubCategory

app_name = 'properties'

urlpatterns = [
    path('media/type/', ViewMediaTypes.as_view(), name='mediatypes'),
    path('media/type/<int:pk>/', ViewMediaType.as_view(), name='mediatype'),
    path('media/type/create/', CreateMediaType.as_view(), name='createtype'),

    path('media/style/', ViewMediaStyles.as_view(), name='mediastyles'),
    path('media/style/<int:pk>/', ViewMediaStyle.as_view(), name='mediastyle'),
    path('media/style/create/', CreateMediaStyle.as_view(), name='createstyle'),

    path('product/collection/', ViewProductCollections.as_view(), name='productcollections'),
    path('product/collection/<int:pk>/', ViewProductCollection.as_view(), name='productcolection'),
    path('product/collection/create/', CreateProductCollection.as_view(), name='createcollection'),

    path('product/categories/', ViewProductCategories.as_view(), name='productcategories'),
    path('product/categories/<int:pk>/', ViewProductCategory.as_view(), name='productcategory'),
    path('product/categories/create/', CreateProductCategory.as_view(), name='createcategory'),

    path('product/subcategories/', ViewProductSubCategories.as_view(), name='productsubcategories'),
    path('product/subcategories/<int:pk>/', ViewProductSubCategory.as_view(), name='productsubcategory'),
    path('product/subcategories/create/', CreateProductSubCategory.as_view(), name='createsubcategory'),
]

