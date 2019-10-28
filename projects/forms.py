from django import forms
from .models import Project

class ProjectForm(forms.Form):

    title = forms.CharField(max_length=100)
    description = forms.CharField()
    technology = forms.CharField(max_length=20)
    goal = forms.CharField()
    liveProject_url = forms.URLField(max_length=200)
    image = forms.ImageField()


class ProjectModelForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['title', 'description', 'technology', 'goal', 'liveProject_url', 'image']

    '''
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        qs = Project.objects.filter(title=title)
        if qs.exists():
            raise forms.ValidationError("This title already exists.")
        return title

    '''