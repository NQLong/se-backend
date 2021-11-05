from restaurant.models.restaurant import Restaurant
from utils import exceptions, messages
from utils.validators import AbstractDataValidator



class RestaurantValidator(AbstractDataValidator):
    non_validate_fields = ['restaurant_uid', 'restaurant_code']

    # def validate_restaurant_code(self, value):
    #     try:
    #         Restaurant.get(code=value)
    #     except Exception as exception: pass
    #     else: raise exceptions.ValidationException(messages.RESTAURANT_CODE_EXISTED)

    # def validate_restaurant_code(self,value):
    #     self.set_field('restaurant', Restaurant.get(code=value))

    # def validate_restaurant_uid(self,value):
    #     self.set_field('restaurant', Restaurant.get(uid=value))

    def is_validate_restaurant(self, *args):
        self.set_field(
            'restaurant',
            Restaurant.get(
                uid=self.get_field('restaurant_uid'),
                code=self.get_field('restaurant_code')
                )
        )

    def is_restaurant_exists(self):
        return Restaurant.objects.filter(
            **self.get_restaurant_identifier()
        ).exists()

    def is_valid_for_create(self, user):
        self.is_missing_fields(keys=['name', 'address', 'open_at', 'close_at'])
        self.set_field('creator', user)

        return self.get_data(['name', 'address', 'open_at', 'close_at', 'creator'])

    def is_missing_restaurant_identifier(self):
        identifier = self.get_field('restaurant_code') or self.get_field('restaurant_uid')
        return not identifier

    def get_restaurant_identifier(self):
        return {'code': self.get_field('restaurant_code')} \
            if self.get_field('restaurant_code') \
                else {'uid': self.get_field('restaurant_uid')}

    def is_valid_for_get(self):
        if self.is_missing_restaurant_identifier():
            self.is_missing_fields(['restaurant_identifier']) #use this to raise empty exception
        self.is_validate_restaurant()
        return self.get_restaurant_identifier()


