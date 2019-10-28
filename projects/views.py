from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Project
from .forms import ProjectForm, ProjectModelForm

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



#@login_required
@staff_member_required
def project_create(request):
    
    template_name = 'form.html'
    print(request.POST)
    form = ProjectModelForm(request.POST, request.FILES or None)
    if form.is_valid():
        print(form.cleaned_data)
        #obj = Project.objects.create(**form.cleaned_data)
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        #form = ProjectForm()
        form = ProjectModelForm()
    
    context = {
        'form': form 
    }
    return render(request, template_name, context)


@login_required(login_url='/login')
def project_update(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    template_name = 'form.html'
    form = ProjectModelForm(request.POST, request.FILES or None, instance=project)
    if form.is_valid():
        print(form.cleaned_data)
        #obj = Project.objects.create(**form.cleaned_data)
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = ProjectModelForm()
    
    context = {
        'title': f'Update Project # {project_id}',
        'form': form 
    }
    return render(request, template_name, context)