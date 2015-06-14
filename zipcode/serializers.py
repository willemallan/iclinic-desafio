from django.forms import widgets
from rest_framework import serializers


class ZipCodeSerializer(serializers.Serializer):
    
    zip_code = serializers.CharField(max_length=8)
    address = serializers.CharField(max_length=150)
    neighborhood = serializers.CharField(max_length=150)
    city = serializers.CharField(max_length=150)
    state = serializers.CharField(max_length=2)
    
    def restore_object(self, attrs, instance=None):
        if instance:
            instance.zip_code = attrs.get('zip_code', instance.zip_code)
            instance.address = attrs.get('address', instance.address)
            instance.neighborhood = attrs.get('neighborhood', instance.neighborhood)
            instance.city = attrs.get('city', instance.city)
            instance.state = attrs.get('state', instance.state)
            return instance

        return ZipCode(**attrs)