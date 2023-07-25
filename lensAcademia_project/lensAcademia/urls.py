from django.urls import path
from .views import AuthorListView, AuthorDetailView, KeywordListView, KeywordDetailView, ResearchPaperListView, ResearchPaperDetailView, TGListView, TGDetailView

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('keywords/', KeywordListView.as_view(), name='keyword-list'),
    path('keywords/<int:pk>/', KeywordDetailView.as_view(), name='keyword-detail'),
    path('researchpapers/', ResearchPaperListView.as_view(), name='researchpaper-list'),
    path('researchpapers/<int:pk>/', ResearchPaperDetailView.as_view(), name='researchpaper-detail'),
    path('tgs/', TGListView.as_view(), name='tg-list'),
    path('tgs/<int:pk>/', TGDetailView.as_view(), name='tg-detail'),
]
