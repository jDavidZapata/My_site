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



#@login_required
@staff_member_required
def project_create(request):
    
    template_name = 'form.html'
    print(request.POST)
    form = ProjectModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        print(form.cleaned_data)
        #obj = Project.objects.create(**form.cleaned_data)
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect("/projects")
    
    context = {
        'title': 'Create A Project',
        'form': form 
    }
    return render(request, template_name, context)


#@login_required(login_url='/login')
@staff_member_required
def project_update(request, project_id):
    obj = get_object_or_404(Project, pk=project_id)
    template_name = 'form.html'
    form = ProjectModelForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid() and obj.user == request.user:
        print(form.cleaned_data)
        #form.save()
        #obj = Project.objects.create(**form.cleaned_data)
        form.save() 
        return redirect("/projects")           

    
    context = {
        'title': f'Update Project {obj.title}',
        'form': form 
    }
    return render(request, template_name, context)



@staff_member_required
def project_delete(request, project_id):
    obj = get_object_or_404(Project, pk=project_id)
    template_name = 'form.html'
    print(request.POST)
    form = ProjectModelForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid() and obj.user == request.user:
        print(form.cleaned_data)
             
        obj.delete()
        return redirect("/projects")      
    
    context = {
        'title': f'Delete Project {obj.title}',
        'form': form 
    }
    return render(request, template_name, context)