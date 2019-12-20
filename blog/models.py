from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.template.defaultfilters import slugify
from PIL import Image


# Create your models here.

User = settings.AUTH_USER_MODEL


class Category(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    slug = models.SlugField(null=False, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "Categories"


    def __str__(self):
        return self.name
    

    def __repr__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        #return reverse('blog:category_detail', kwargs={'cat_id': self.id})
        return reverse('blog:category_detail', kwargs={'slug': self.slug})
            
    def get_delete_url(self):
        #return reverse('blog:category_delete', kwargs={cat_id': self.id})
        return f"{self.get_absolute_url()}delete"



class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(null=False, unique=True)
    image = models.ImageField(upload_to='post_img/', blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    #comment = models.ForeignKey(Comment, verbose_name="Comment", on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title
    

    def __repr__(self):
        return self.title 
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        if self.image:
            img = Image.open(self.image.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)

            
        return super().save(*args, **kwargs)






    def get_absolute_url(self):
        #return reverse('blog:post_detail', kwargs={'post_id': self.id})
        return reverse('blog:post_detail', kwargs={'slug': self.slug})
        #return f"/blog/{self.id}"
   

    def get_update_url(self):
        #return reverse('blog:post_update', kwargs={'post_id': self.id})
        return f"{self.get_absolute_url()}update"


    def get_delete_url(self):
        #return reverse('blog:post_delete', kwargs={'post_id': self.id})
        return f"{self.get_absolute_url()}delete"
   


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    date_commented = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Comments"


    def __str__(self):
        return self.content
    

    def __repr__(self):
        return self.content

    '''
    def get_absolute_url(self):
        return reverse('blog:commet_detail', kwargs={'comment_id': self.id})
        #return reverse('blog:comment_detail', kwargs={'slug': self.slug})
       
   

    def get_update_url(self):
        #return reverse('blog:comment_update', kwargs={'comment_id': self.id})
        return f"{self.get_absolute_url()}update"


    def get_delete_url(self):
        #return reverse('blog:comment_delete', kwargs={'comment_id': self.id})
        return f"{self.get_absolute_url()}delete"
    '''