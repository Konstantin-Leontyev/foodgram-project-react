from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Tag
from .serializers import TagSerializer


class TagsViewSet(ReadOnlyModelViewSet):
    """Describes read only tag view set class."""

    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = None
    queryset = Tag.objects.all()
    serializer_class = TagSerializer