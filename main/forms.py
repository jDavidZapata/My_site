from django import forms

class ContactForm(forms.Form):
    sender_name = forms.CharField(label='Your name')
    sender_email = forms.EmailField(label='Your Email')
    subject = forms.CharField(max_length=100)
    message_content = forms.CharField(label='Your Message', widget=forms.Textarea)




   