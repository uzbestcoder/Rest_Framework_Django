from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'content', 'author', 'isbn', 'price')

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        # # Kitob sarlavhasi hariflardan iboratligini tekshirish
        # if not title.isalpha():
        #     raise ValidationError(
        #         {
        #             "status": False,
        #             "message": "Kitob sarlavhasi hariflardan iborat bo'lishi kerak."
        #         }
        #     )

        # Kitobni bazada mavjudligini tekshirish
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Siz kiritgan kitob oldin ham kiritilgan"
                }
            )

        return data
