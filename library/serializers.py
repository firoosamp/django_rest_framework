from datetime import date

from rest_framework import serializers

from library.models import Book


class BookSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date', 'isbn', 'price' , 'age']

    def get_age(self, obj):
        return date.today().year - obj.published_date.year

    def validate_isbn(self, value):
        if len(value) not in [10, 13]:
            raise serializers.ValidationError(
                "ISBN must be exactly 10 or 13 characters"
            )
        return value
