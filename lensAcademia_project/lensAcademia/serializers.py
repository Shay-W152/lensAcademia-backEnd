from rest_framework import serializers
from .models import Author, Keyword, ResearchPaper, TG

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'url', 'country',]

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ['id', 'word']

class ResearchPaperSerializer(serializers.ModelSerializer):
    researchers = AuthorSerializer(many=True, read_only=True)  # Use the AuthorSerializer

    class Meta:
        model = ResearchPaper
        fields = ['id', 'tg', 'researchers', 'name', 'abstract', 'url', 'country', ]

class TGSerializer(serializers.ModelSerializer):
    class Meta:
        model = TG
        fields = ['id', 'tg']
