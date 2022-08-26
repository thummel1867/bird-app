from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Bird(models.Model):
    title = models.CharField(max_length=200)
    scientific_name = models.CharField(max_length=200)
    conservation_status = models.TextField(max_length=1000, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image = models.CharField(max_length=2000, blank=True)
    family = models.CharField(max_length = 200, blank=True)
    description = models.TextField(blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blogpost_like')

    def number_of_likes(self):
        return self.likes.count()
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main_app:bird', kwargs={'bird_id': self.id})

    class Meta:
        ordering = ['-created_on']