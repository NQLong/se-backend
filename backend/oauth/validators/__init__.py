from utils import exceptions, messages
from user_account.models.user import User
from utils.validators import AbstractDataValidator

class UserValidator(AbstractDataValidator):

    def get_identifier(self):
        data = self.get_data(['username','email'])
        return {key:value for key, value in data.items() if value}

    def is_user_exist(self):
        identifier = self.get_identifier()
        return User.is_exist(**identifier)

    def is_valid_for_log_in(self):
        self.is_missing_fields(['username', 'password'])
        self.is_validate_fields(['username', 'password'])

        if not self.is_user_exist():
            raise exceptions.NotFoundException(messages.USER_NOT_FOUND)

        return self.get_identifier()

    def validate_username(self, value):
        ...

    def validate_password(self, value):
        ...
