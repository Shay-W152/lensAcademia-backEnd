from rest_framework import serializers
from .models import Author, Keyword, ResearchPaper, TG

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'url', 'country', 'research_papers']

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ['id', 'word','research_papers' ]

class ResearchPaperSerializer(serializers.ModelSerializer):
    researchers = AuthorSerializer(many=True, read_only=True)
    tg = serializers.HyperlinkedRelatedField(view_name='tg-detail', read_only=True)
    keywords = KeywordSerializer(many=True)

    class Meta:
        model = ResearchPaper
        fields = ['id', 'tg', 'researchers', 'keywords', 'name', 'abstract', 'url', 'country']

class TGSerializer(serializers.ModelSerializer):
    class Meta:
        model = TG
        fields = ['id', 'tg']
