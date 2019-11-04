from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.http import Http404
from .models import Project
from .forms import ProjectForm, ProjectModelForm

# Create your views here.


def projects_list(request):

    template_name = 'projects/projects_list.html'
    projects = get_list_or_404(Project)
    context = {
            'title': '* Projects *',
            'projects': projects
        }

    '''
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
    '''

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




@staff_member_required
def project_create(request):
    
    template_name = 'form.html'
    print(request.POST)
    if request.method == 'POST':
        form = ProjectModelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            print(form.cleaned_data)
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            messages.success(request, f"New Project Created: {project.title}.")
            return redirect(project)
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
    else:
        context = {
            'title': 'Create A Project',
            'form': form 
        }
    return render(request, template_name, context)



@staff_member_required
def project_update(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    template_name = 'form.html'
    if request.method == 'POST':
        form = ProjectModelForm(request.POST or None, request.FILES or None, instance=project)
        if form.is_valid() and project.user == request.user:
            print(form.cleaned_data)
            project = Project.objects.create(**form.cleaned_data)
            messages.success(request, f"{project.title}: Project Updated.")
            return redirect(project)
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
    else:
        context = {
            'title': f'Update Project {project.title}',
            'form': form 
        }
    return render(request, template_name, context)



@staff_member_required
def project_delete(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    template_name = 'form.html'
    print(request.POST)
    if request.method == 'POST':
        form = ProjectModelForm(request.POST or None, request.FILES or None, instance=project)
        if form.is_valid() and project.user == request.user:
            print(form.cleaned_data)             
            project.delete()
            messages.success(request, f"Project Deleted.")
            return redirect('projects:projects_list')      

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
    else:    
        context = {
            'title': f'Delete Project {project.title}',
            'form': form 
        }
    return render(request, template_name, context)