from rest_framework import serializers
from media_file.serializers import BaseMediaSerializer
from restaurant.models.dish import Category, Dish
from .restaurant import RestaurantListSerializer

class DishBannerListSerializer(serializers.Serializer):
    image = BaseMediaSerializer()
    ordinal = serializers.IntegerField()

class DishListSerializer(serializers.Serializer):
    uid = serializers.CharField()
    name = serializers.CharField()
    code = serializers.SlugField()
    serve_count = serializers.IntegerField()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        context = self.context
        if not context.get('include_banners', False):
            return data
        banners = instance.dish_dish_banner.all()
        banners = banners.order_by('ordinal').first()
        banners_data = DishBannerListSerializer(banners).data if banners else []
        data['banners'] = banners_data
        return data

class DishSerializer(DishListSerializer):
    description = serializers.CharField()
    banners = DishBannerListSerializer(many=True, source='dish_dish_banner')
    restaurant = RestaurantListSerializer()

    # def to_representation(self, instance):
    #     return super(serializers.Serializer, self).to_representation(instance)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['id']


