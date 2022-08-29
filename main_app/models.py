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
    seen = models.ManyToManyField(User, related_name="seen")
    searching = models.ManyToManyField(User, related_name="searching")

    def number_of_likes(self):
        return self.likes.count()
        
    def __str__(self):
        return self.title

    class Meta:
      verbose_name_plural = "birds"

    def get_absolute_url(self):
        return reverse('main_app:bird', kwargs={'bird_id': self.id})

    class Meta:
        ordering = ['-created_on']


# SOO, we want to do the following in order for a logged in user to be able to add a bird to a "seen", or "want to see" section 

# 1 . create a "seen" section in the model as a many to many field associated with user
# 2. create a url that will associate a user to a bird in this way 
# 3. create a view that executes this
# 4. add a button into html in the appropriate places that allows a user to do this
