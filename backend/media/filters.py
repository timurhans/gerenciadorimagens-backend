from .models import Media

def media_filter(query):
    queryset = Media.objects.order_by("-created_at")
    style = query.request.query_params.get('style')
    media_type = query.request.query_params.get('type')
    tags = query.request.query_params.get('tags')
    if style is not None:
        queryset = queryset.filter(style=style)
    if media_type is not None:
        queryset = queryset.filter(media_type=media_type)
    if tags is not None:
        tags = [int(tag) for tag in tags.split(',')]
        queryset = queryset.filter(tags__in=tags)

    return queryset