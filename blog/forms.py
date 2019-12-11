from django import forms
from .models import Post, Comment, Category

class PostForm(forms.Form):
    
    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea)
    #image = forms.ImageField()


class PostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']

    
    def clean_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get('title')
        qs = Post.objects.filter(title__iexact=title)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("This title already exists.")
        return title



class CategoryForm(forms.Form):
    
    name = forms.CharField(max_length=200)
    summary = forms.CharField(widget=forms.Textarea)



class CategoryModelForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'summary']

    
    def clean_name(self, *args, **kwargs):
        instance = self.instance
        name = self.cleaned_data.get('name')
        qs = Category.objects.filter(name__iexact=name)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("This Category already exists.")
        return name
    



class CommentForm(forms.Form):
    
    content = forms.CharField(widget=forms.Textarea)



class CommentModelForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']