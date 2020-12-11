from django.shortcuts import render
from .models import MiniProjects,Categories,ProjectType

# Create your views here.
def list_projects(request):
    type = request.GET.get('type', 'Artificial Intelligence')
    category = Categories.objects.filter(name=type)
    if type == 'Artificial Intelligence':
        projs = MiniProjects.objects.filter(category__in=category)
    else:
        projs = MiniProjects.objects.all().exclude(category__name='Artificial Intelligence')
    return render(request, 'projects/list_projects.html', {'type':type, 'projs':projs})


def code(request):
    id = request.GET.get('id')
    proj = MiniProjects.objects.get(id=id)
    tools = []
    if proj.tools:
        tools = proj.tools.split('>>?')[1:]
    if proj.description:
        description = proj.description.split('>>?')[1:]
    return render(request, 'projects/code_disp.html', {'proj': proj,'tools':tools,'description':description})