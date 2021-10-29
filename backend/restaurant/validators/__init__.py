from rest_framework import serializers

class RestaurantListSerialzier(serializers.Serializer):
    code = serializers.CharField()
    name = serializers.CharField()
    open_at = serializers.CharField()
    close_at = serializers.CharField()

