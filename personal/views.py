from django.shortcuts import render

# Create your views here.


def personal_page(request):

    personal = True
    template_name = 'personal/personal.html'
    context = {
        "title": "Temporary",
        "body": "Body: Temp Page",
        "personal": personal
    }
    return render(request, template_name, context)


def temppage(request):

    personal = True
    template_name = 'personal/temp.html'
    context = {
        "title": "Temporary",
        "body": "Body: Temp Page",
        "personal": personal
    }
    return render(request, template_name, context)
