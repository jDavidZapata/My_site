from django.db import models
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

class Project(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    goal = models.TextField()
    image = models.ImageField(upload_to='img/')
    liveProject_url =  models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.title} -- Build with {self.technology}"
    

    def __repr__(self):
        return f"{self.title} -- Build with {self.technology}"