from django.db import models
from django.conf import settings
from django.shortcuts import reverse

# Create your models here.

User = settings.AUTH_USER_MODEL

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    slug = models.CharField(max_length=20)
    #image = models.ImageField(upload_to='post_img/', blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.title
    

    def __repr__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'post_id': self.id})
        #return f"/blog/{self.id}"

    '''
    def get_update_url(self):
        return reverse('blog:post_update', kwargs={'post_id': self.id})
        #return f"/blog/{self.id}/update"
        #return f"{self.get_absolute_url}/update"


    def get_delete_url(self):
        return reverse('blog:post_delete', kwargs={'post_id': self.id})
        #return f"/blog/{self.id}/delete"
        #return f"{self.get_absolute_url}/delete"
    '''