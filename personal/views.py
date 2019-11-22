from django.shortcuts import render

# Create your views here.


def temppage(request):

    personal = True
    template_name = 'personal/temp.html'
    context = {
        "title": "Temporary",
        "body": "Body: Temp Page",
        "personal0": "True"
    }
    return render(request, template_name, context)
