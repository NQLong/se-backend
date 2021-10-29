from rest_framework import serializers
from media_file.serializers import BaseMediaSerializer

class RestaurantBannerListSerialier(serializers.Serializer):
    ordinal = serializers.IntegerField()
    image = BaseMediaSerializer()

class RestaurantListSerializer(serializers.Serializer):
    name = serializers.CharField()
    code = serializers.CharField()
    address = serializers.CharField()
    open_at = serializers.DateTimeField()
    close_at = serializers.DateTimeField()

class RestaurantBannerSerializer(RestaurantBannerListSerialier):
    restaurant = RestaurantListSerializer()

class RestaurantSerializer(RestaurantListSerializer):
    banners = RestaurantBannerListSerialier(many=True, source='restaurant_restaurant_banner')

    def to_representation(self, instance):
        return super().to_representation(instance)

