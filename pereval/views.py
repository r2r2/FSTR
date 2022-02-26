from django_filters import rest_framework as filters
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action
from rest_framework.response import Response

from pereval.filters import UserProfileFilter
from pereval.models import Added
from pereval.serializers import AddedSerializer, AddedUpdateSerializer


class SubmitDataViewSet(viewsets.ModelViewSet):
    """CRUD for Added model"""
    permission_classes = [permissions.AllowAny]
    parser_classes = (MultiPartParser, FormParser)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = UserProfileFilter

    def get_serializer_class(self):
        if self.action == 'update':
            return AddedUpdateSerializer
        else:
            return AddedSerializer

    def get_queryset(self):
        if self.action == 'update':
            queryset = Added.objects.filter(status='new')
            return queryset
        else:
            queryset = Added.objects.all()
            return queryset

    @action(detail=True, url_path='status')
    def get_status(self, request, pk):
        """Return moderation status"""
        check_status = get_object_or_404(Added, pk=pk).status
        return Response(check_status, status=status.HTTP_200_OK)

    def get_parsers(self):
        """Fix to use swagger with nested serializers.
           For nested serializers provided only read-only features
        """
        if getattr(self, 'swagger_fake_view', False):
            return []
        return super().get_parsers()

