from django_filters import rest_framework as filters
from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser

from pereval.filters import UserProfileFilter
from pereval.models import Added
from pereval.serializers import AddedListSerializer


class SubmitDataView(viewsets.ModelViewSet):
    """CRUD for Added model"""
    queryset = Added.objects.all()
    serializer_class = AddedListSerializer
    permission_classes = [permissions.AllowAny]
    parser_classes = (MultiPartParser, FormParser)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = UserProfileFilter
