from datetime import date

from rest_framework import serializers

from library.models import Book, Author


class AutherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'email', 'birth_date']


class BookSerializer(serializers.ModelSerializer):
    author_details = AutherSerializer(source='author' , read_only= True)
    age = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date', 'isbn', 'price' , 'age' , 'author_details']

    def get_age(self, obj):
        return date.today().year - obj.published_date.year

    def validate_isbn(self, value):
        if len(value) not in [10, 13]:
            raise serializers.ValidationError(
                "ISBN must be exactly 10 or 13 characters"
            )
        return value

