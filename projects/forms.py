from django import forms
from .models import Project

class ProjectForm(forms.Form):

    title = forms.CharField(max_length=100)
    description = forms.CharField()
    technology = forms.CharField(max_length=20)
    goal = forms.CharField()
    image = forms.ImageField()


class ProjectModelForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['title', 'description', 'technology', 'goal', 'image']
