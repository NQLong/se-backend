from restaurant.models.dish import Dish
from utils import exceptions, messages
from utils.validators import AbstractDataValidator
from .restaurant import RestaurantValidator


class DishValidator(AbstractDataValidator):

    is_missing_restaurant_identifier = RestaurantValidator.is_missing_restaurant_identifier
    is_validate_restaurant = RestaurantValidator.is_validate_restaurant

    def is_valid_for_create(self, user):
        self.set_field('creator', user)
        self.is_missing_restaurant_identifier()
        self.is_validate_restaurant()
        self.is_missing_fields(['name'])

        return self.get_data(['name', 'restaurant', 'creator', 'description', ''])
    
    def is_missing_dish_identifier(self):
        value = self.get_field('dish_code') or self.get_field('dish_uid')
        return not value

    def get_dish_identifier(self):
        return {'code': self.get_field('dish_code')}\
            if self.get_field('dish_code') \
                else {'uid': self.get_field('dish_uid')}

    def is_validate_dish(self):
        self.set_field('dish', Dish.get(**self.get_dish_identifier()))

    def is_valid_for_get(self):
        if self.is_missing_dish_identifier():
            self.is_missing_fields(['dish_identifier'])
        self.is_validate_dish()
        return self.get_dish_identifier()


