from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50, blank=False)
    body = models.CharField(max_length=4000, blank=False)

    def __str__(self):
        return self.title
    
class Account(models.Model):
    name = models.CharField(max_length=255)
    mail = models.EmailField(max_length=255)

    def __str__(self):
        return self.name

class Comment(models.Model):
    body = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.body