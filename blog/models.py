from django.db import models
from django.conf import settings
from django.shortcuts import reverse

# Create your models here.

User = settings.AUTH_USER_MODEL

class Post(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    text = models.TextField()
    slug = models.CharField(max_length=20)
    #image = models.ImageField(upload_to='post_img/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"{self.title}"
    

    def __repr__(self):
        return f"{self.title}"

    
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