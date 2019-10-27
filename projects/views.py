from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Project
from .forms import ProjectForm

# Create your views here.


def projects_list(request):

    template_name = 'projects/projects_list.html'
    try:
        projects = Project.objects.all()
        context = {
            'title': 'Projects',
            'projects': projects
        }
    except Project.DoesNotExist:
        raise Http404("This Project does not Exist.")
    except ValueError:
        raise Http404("This Project does not Exist.")

    return render(request, template_name, context)


def project_detail(request, project_id):

    template_name = 'projects/project_detail.html'
    project = get_object_or_404(Project, pk=project_id)
    '''
    try:
        project = Project.objects.get(pk=project_id)
        context = {
            'title': f'Project # {project_id}',
            'project': project
        }
    except Project.DoesNotExist:
        raise Http404("This Project does not Exist.")
    '''
    context = {
            'title': f'Project # {project_id}',
            'project': project
        }
        
    return render(request, template_name, context)


def project_create(request):
    
    template_name = 'form.html'
    print(request.POST)
    form = ProjectForm(request.POST, request.FILES or None)
    if form.is_valid():
        print(form.cleaned_data['title'])
        obj = Project.objects.create(**form.cleaned_data)
        form = ProjectForm()
    
    context = {
        'form': form 
    }
    return render(request, template_name, context)



def project_update(request):
    
    template_name = 'form.html'
    form = ProjectForm(request.POST, request.FILES or None)
    if form.is_valid():
        print(form.cleaned_data)
        
        form = ProjectForm()
    
    context = {
        'form': form 
    }
    return render(request, template_name, context)