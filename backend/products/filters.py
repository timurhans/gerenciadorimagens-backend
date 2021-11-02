from .models import Product

def product_filter(query):
    queryset = Product.objects.order_by("-created_at")
    category = query.request.query_params.get('category')
    subcategory = query.request.query_params.get('subcategory')
    collection = query.request.query_params.get('collection')

    color_variations = query.request.query_params.get('colors')

    if category is not None:
        queryset = queryset.filter(category=category)
    if subcategory is not None:
        queryset = queryset.filter(subcategory=subcategory)
    if collection is not None:
        queryset = queryset.filter(collection=collection)
    if color_variations is not None:
        color_variations = [int(tag) for tag in color_variations.split(',')]
        queryset = queryset.filter(color_variations__in=color_variations)

    return queryset

def public_product_filter(query):
    queryset = Product.objects.filter(collection__is_private=False).order_by("-created_at")
    category = query.request.query_params.get('category')
    subcategory = query.request.query_params.get('subcategory')
    collection = query.request.query_params.get('collection')

    color_variations = query.request.query_params.get('colors')

    if category is not None:
        queryset = queryset.filter(category=category)
    if subcategory is not None:
        queryset = queryset.filter(subcategory=subcategory)
    if collection is not None:
        queryset = queryset.filter(collection=collection)
    if color_variations is not None:
        color_variations = [int(tag) for tag in color_variations.split(',')]
        queryset = queryset.filter(color_variations__in=color_variations)

    return queryset