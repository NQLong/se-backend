from utils import messages, exceptions

class AbstractDataValidator:
    non_validate_fields = []

    def __init__(self, **kwargs):
        for key,value in kwargs.items():
            label = f'_{key}'
            setattr(self, label, value)


    def is_missing_fields(self, keys):
        error_messages = [
            getattr(messages,f'EMPTY_{key.upper()}') for key in keys if not self.get_field(key)
        ]
        if error_messages:
            raise exceptions.InvalidArgumentException(message=', '.join(error_messages))
    
    def is_validate_field(self, key):
        value = self.get_field(key)
        if value:
            validate_function = self.get_validate_function(key)
            if validate_function:
                validate_function(value)
            else:
                raise exceptions.ApplicationException(f'Missing valdating function on fields {key}')

    def is_validate_fields(self, keys):
        for key in keys:
            self.is_validate_field(key)
            

    def get_validate_function(self, key):
        label = f'validate_{key}'
        return getattr(self, label, None)

    def get_field(self, key):
        label = f'_{key}'
        return getattr(self, label, None)

    def set_field(self, key, value):
        label = f'_{key}'
        return setattr(self, label, value)

    def get_data(self, keys):
        data = dict()
        for key in keys:
            data.update({key:self.get_field(key)})
        return data
