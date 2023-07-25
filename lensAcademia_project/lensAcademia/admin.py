from django.contrib import admin
from .models import Author, Keyword, ResearchPaper, TG

admin.site.register(Author)
admin.site.register(Keyword)
admin.site.register(ResearchPaper)
admin.site.register(TG)
