from rest_framework import serializers
from . import exceptions, messages
from abc import abstractmethod

class AbstractSerializerValidator(serializers.Serializer):

    
    @abstractmethod
    def is_valid(self, raise_exception):
        if not hasattr(self, 'initial_data'):
            raise exceptions.ApplicationException('missing initial data')

        if not hasattr(self, '_validated_data'):
            self._validated_data = self.run_validation(self.initial_data)

        return True

    def run_validation(self, data):
        value = self.to_internal_value(data)
        
        self.run_validators(value)
        value = self.validate(value)
        return value 
