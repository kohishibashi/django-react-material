from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50, blank=False)
    body = models.CharField(max_length=4000, blank=False)

    def __str__(self):
        return self.title
    
