from django.db import models
from django.urls import reverse


TOPICS = (
    ('world affairs', 'World Affairs'),

)

class Topic(models.Model):
    topic_name: models.CharField(max_length=100)

class Author(models.Model):
    author_name = models.CharField(max_length=100)
    author_bio = models.TextField(blank = True)

    def __str__(self):
        return self.author_name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'author_id': self.id})

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    image = models.CharField(max_length=500)
    descriptor = models.CharField(max_length=20, choices=TOPICS)
    secondary_descriptor = models.CharField(max_length=20, choices=TOPICS, blank=True)
    guts = models.TextField(blank = True)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'article_id': self.id})

    class Meta:
        ordering = ['-date']