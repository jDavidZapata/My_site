from django import forms

class ContactForm(forms.Form):
    sender_name = forms.CharField()
    sender_email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message_content = forms.CharField(widget=forms.Textarea)




   