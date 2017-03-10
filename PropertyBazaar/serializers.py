from rest_framework import serializers
from PropertyBazaar.models import Property
from django.contrib.auth.models import User


class PropertySerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Property
        fields = ('id', 'title', 'created', 'description', 'propertytype', 'address', 'city',
                  'owner', 'bathrooms', 'bedrooms',
                  'garages', 'rooms', 'area', 'price', 'image')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    properties = serializers.HyperlinkedRelatedField(many=True, view_name='property-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'properties')
        extra_kwargs = {'password': {'write_only': True}, }

    def create(self, validated_data):
        user = User()
        user.set_password(validated_data['password'])
        validated_data['password'] = user.password
        return super(UserSerializer, self).create(validated_data)
