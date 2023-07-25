from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=250)
    url = models.URLField(max_length=250)
    country = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name

class Keyword(models.Model):
    word = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.word

class ResearchPaper(models.Model):
    tg = models.ForeignKey('TG', on_delete=models.SET_NULL, null=True)
    researchers = models.ManyToManyField(Author)  
    keywords = models.ManyToManyField(Keyword)
    name = models.CharField(max_length=250)
    abstract = models.CharField(max_length=500)
    url = models.URLField(max_length=250)
    country = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name

class TG(models.Model):
    tg = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.tg
