from rest_framework import generics
from .models import Author, Keyword, ResearchPaper, TG
from .serializers import AuthorSerializer, KeywordSerializer, ResearchPaperSerializer, TGSerializer

class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class KeywordListView(generics.ListCreateAPIView):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer

class KeywordDetailView(generics.RetrieveAPIView):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer

class ResearchPaperListView(generics.ListCreateAPIView):
    queryset = ResearchPaper.objects.all()
    serializer_class = ResearchPaperSerializer

class ResearchPaperDetailView(generics.RetrieveAPIView):
    queryset = ResearchPaper.objects.all()
    serializer_class = ResearchPaperSerializer

class TGListView(generics.ListCreateAPIView):
    queryset = TG.objects.all()
    serializer_class = TGSerializer

class TGDetailView(generics.RetrieveAPIView):
    queryset = TG.objects.all()
    serializer_class = TGSerializer
