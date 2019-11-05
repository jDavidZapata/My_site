from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']



class UpdateProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image',]


class NewUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user