from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


from django.contrib.auth.mixins import LoginRequiredMixin
class Bird(models.Model):
    title = models.CharField(max_length=200)
    scientific_name = models.CharField(max_length=200)
    conservation_status = models.TextField(max_length=1000, blank=True)
    date = models.DateField(blank=True, null=True)
    image = models.CharField(max_length=500)
    family = models.CharField(max_length = 200, blank=True)
    description = models.TextField(blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'bird_id': self.id})

    class Meta:
        ordering = ['-date']