from rest_framework import serializers
from .models import Media
from django.contrib.auth import get_user_model
User = get_user_model()

class BaseMediaSerializer(serializers.ModelSerializer):
    media_url = serializers.ReadOnlyField()
    class Meta:
        model = Media
        fields = [
            'uid',
            'file_name',
            'content_type',
            'media_url',
        ]

