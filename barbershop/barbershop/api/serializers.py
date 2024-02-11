from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Serveces, Orders


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serveces
        fields = ['id', 'title']


class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Orders
        fields = ['id', 'date_of_order', 'services', 'description', 'owner']


class UserSerializer(serializers.ModelSerializer):
    orders = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'orders']
