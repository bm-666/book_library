from rest_framework import serializers
from structs.Book import BookStruct
from enums.BookStatus import BookStatus

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    author = serializers.CharField()
    genre = serializers.CharField()

class BooksSerializer(serializers.Serializer):
    results = serializers.ListField(child=BookSerializer(), allow_empty=True)


class BookGetSerializer(serializers.Serializer):
    book = serializers.IntegerField()
    status = serializers.ChoiceField(choices=BookStatus)


