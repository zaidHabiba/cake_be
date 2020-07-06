from rest_framework import serializers
from app.models import Offer, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone']


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['pk', 'image', 'name', 'price']
