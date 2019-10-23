from django.shortcuts import render, get_object_or_404
from projects.models import Project
from django.http import Http404

# Create your views here.


def projects_list(request):
    try:
        projects = Project.objects.all()
        context = {
            'title': 'Projects',
            'projects': projects
        }
    except Project.DoesNotExist:
        raise Http404("This Project does not Exist.")

    return render(request, 'projects/projects_list.html', context)


def project_detail(request, project_id):
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
            'project': project
        }
        
    return render(request, 'projects/project_detail.html', context)