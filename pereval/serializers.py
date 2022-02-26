from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer, NestedUpdateMixin

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


class ImageSerializer(WritableNestedModelSerializer):
    """Uploading photo serialization"""

    class Meta:
        model = Image
        fields = '__all__'


class AddedSerializer(WritableNestedModelSerializer):
    """Added model serializer"""
    coords = CoordsSerializer()
    user = UserProfileSerializer()
    images = ImageSerializer()
    level = LevelSerializer()

    class Meta:
        model = Added
        fields = ('id', 'beauty_title', 'title', 'other_titles',
                  'connect', 'add_time', 'user', 'coords',
                  'type', 'level', 'images')
        read_only_fields = ('id', 'type', 'add_time')


class AddedUpdateSerializer(NestedUpdateMixin, serializers.ModelSerializer):
    """PUT method serializer for Added model"""
    coords = CoordsSerializer()
    user = UserProfileSerializer(read_only=True)
    images = ImageSerializer(write_only=True)
    level = LevelSerializer()

    class Meta:
        model = Added
        fields = ('id', 'status', 'beauty_title', 'title', 'other_titles',
                  'connect', 'add_time', 'user', 'coords',
                  'type', 'level', 'images')
        read_only_fields = ('id', 'type', 'add_time', 'status', 'user')











