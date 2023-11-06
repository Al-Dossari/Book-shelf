from rest_framework import serializers
from .models import User, Book


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookEditSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['status']


class BookCreateSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['isbn',]


class BookDetailSeralizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
