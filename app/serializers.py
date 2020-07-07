from rest_framework import serializers
from app.models import Offer, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'email', 'password', 'phone', 'first_name', 'last_name', 'is_superuser']
        extra_kwargs = {
            'pk': {'read_only': True},
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User.objects.create_user(**self.data.serializer.initial_data)
        user.set_password(self.data.serializer.initial_data['password'])
        return user


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['pk', 'image', 'name', 'price']
