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
    researchers = serializers.PrimaryKeyRelatedField(many=True, queryset=Author.objects.all())
    tg = serializers.HyperlinkedRelatedField(view_name='tg-detail', read_only=True)
    keywords = serializers.PrimaryKeyRelatedField(many=True, queryset=Keyword.objects.all())

    class Meta:
        model = ResearchPaper
        fields = ['id', 'tg', 'researchers', 'keywords', 'name', 'abstract', 'url', 'country']

    def create(self, validated_data):
        researchers_data = validated_data.pop('researchers', [])
        keywords_data = validated_data.pop('keywords', [])
        research_paper = ResearchPaper.objects.create(**validated_data)

        for researcher_data in researchers_data:
            research_paper.researchers.add(researcher_data)

        for keyword_data in keywords_data:
            research_paper.keywords.add(keyword_data)

        return research_paper

class TGSerializer(serializers.ModelSerializer):
    class Meta:
        model = TG
        fields = ['id', 'tg']
