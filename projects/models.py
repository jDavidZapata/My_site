from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.template.defaultfilters import slugify


# Create your models here.

User = settings.AUTH_USER_MODEL

class Project(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    goal = models.TextField()
    image = models.ImageField(upload_to='project_img/', blank=True, null=True)
    liveProject_url =  models.URLField(max_length=200)
    slug = models.SlugField(null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            
        return super().save(*args, **kwargs)

    
    def __str__(self):
        return f"{self.title} -- Build with {self.technology}"
    

    def __repr__(self):
        return f"{self.title} -- Build with {self.technology}"

    
    def get_absolute_url(self):
        #return reverse('projects:project_detail', kwargs={'project_id': self.id})
        #return reverse('projects:project_detail', kwargs={'pk': self.id})
        return reverse('projects:project_detail', kwargs={'slug': self.slug})
        #return f"/projects/{self.id}"

    
    def get_update_url(self):
        #return reverse('projects:project_update', kwargs={'project_id': self.id})
        #return f"/projects/{self.id}/update"
        return f"{self.get_absolute_url()}update"


    def get_delete_url(self):
        #return reverse('projects:project_delete', kwargs={'project_id': self.id})
        #return f"/projects/{self.id}/delete"
        return f"{self.get_absolute_url()}delete"
