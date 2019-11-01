from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):
    sender_name = forms.CharField(label='Your name')
    sender_email = forms.EmailField(label='Your Email')
    subject = forms.CharField(max_length=100)
    message_content = forms.CharField(label='Your Message', widget=forms.Textarea)


class CreateUserForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields #+ ('custom_field',)