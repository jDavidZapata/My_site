from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    goal = models.TextField()
    image = models.FileField(upload_to='img/')

    def __str__(self):
        return f"{self.title} -- Build with {self.technology}"
    
