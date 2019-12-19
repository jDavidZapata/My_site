from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.utils.decorators import method_decorator
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

    return render(request, template_name, context)


def project_detail(request, project_id):

    template_name = 'projects/project_detail.html'
    project = get_object_or_404(Project, pk=project_id)
   
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
            messages.error(request, "Invalid Create")
    form = ProjectModelForm()
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
            project = form.save(commit=False)
            project.save() 
            messages.success(request, f"{project.title}: Project Updated.")
            return redirect(project)
        else:
            messages.error(request, "Invalid Update")
    
    form = ProjectModelForm(request.POST or None, request.FILES or None, instance=project)
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
            messages.error(request, "Invalid Delete")
    form = ProjectModelForm(request.POST or None, request.FILES or None, instance=project)
    context = {
        'title': f'Delete Project {project.title}',
        'form': form 
    }
    return render(request, template_name, context)






class ProjectListView(ListView):
    
    model = Project
    template_name = 'projects/projects_list.html'
    context_object_name = 'projects'
    #paginate_by = 2
    ordering = ['created_at']

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        context['title'] = '* Projects *'     
        return context

class ProjectDetailView(DetailView):

    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'
    


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'form.html'
    form_class = ProjectModelForm
    #fields = ['title', 'description', 'technology', 'goal', 'image', 'liveProject_url']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@method_decorator(staff_member_required, name='dispatch')
class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'form.html'
    fields = ['title', 'description', 'technology', 'goal', 'image', 'liveProject_url']


@method_decorator(staff_member_required, name='dispatch')
class ProjectDelete(DeleteView):
    model = Project
    template_name = 'projects/project_delete.html'
    success_url = reverse_lazy('projects:projects_list')


