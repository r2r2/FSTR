from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from pereval.models import Added, Coords, UserProfile, Level, Image


class CoordsSerializer(serializers.ModelSerializer):
    """Coordinates serializer"""

    class Meta:
        model = Coords
        exclude = ('id',)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serialize UserProfile data"""

    class Meta:
        model = UserProfile
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
    """Serialize category of the pass"""

    class Meta:
        model = Level
        exclude = ('id',)


class ImageSerializer(serializers.ModelSerializer):
    """Uploading photo serialization"""

    class Meta:
        model = Image
        fields = '__all__'


class AddedListSerializer(WritableNestedModelSerializer):
    """Added model serializer"""
    coords = CoordsSerializer()
    user = UserProfileSerializer()
    images = ImageSerializer(many=True)
    level = LevelSerializer()

    class Meta:
        model = Added
        fields = ('id', 'beauty_title', 'title', 'other_titles',
                  'connect', 'add_time', 'user', 'coords',
                  'type', 'level', 'images')
        read_only_fields = ('id', 'type', 'add_time')

















