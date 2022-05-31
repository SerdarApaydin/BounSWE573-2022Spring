from django.http import HttpResponse
from django.shortcuts import render
from space.models import LearningMaterials, Space
from space.forms import Material_form, Space_form
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    spaces = Space.objects.all()
    print(spaces)
    return render(request, template_name='index.html' , context={"spaces" : spaces})

def spacePage(request, space_id):
    space = Space.objects.get(id = space_id)
    learningMaterials = LearningMaterials.objects.filter(space = space)
    context = {
        'space' : space,
        'learningMaterials' : learningMaterials
    }
    return render(request, template_name="space/space_page.html" , context = context)

def uploadContent(request,space_id):
    space = Space.objects.get(id = space_id)
    if request.method == "POST":
        form = Material_form(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h4>Uploaded succcessfully<h4>")
    else:
        form = Material_form()
    return render(request,'space/upload_file.html',{"form":form , "space":space})

@login_required
def create_space(request):
    if request.method == "POST":
        form = Space_form(data=request.POST, files=request.FILES)
        if form.is_valid():
            space = form.save(commit=False)
            space.author = request.user
            space.save()
            learningMaterials = ()
            return render(request, "space/space_page.html", {"space" : space , "learningMaterials" : learningMaterials})
    else:
        form = Space_form()
    return render(request,'space/create_space.html',{"form":form})

@login_required
def material_detail(request, space_id, material_id):
    space = Space.objects.get(id = space_id)
    learningMaterial = LearningMaterials.objects.get(id = material_id)
    context = {
        'space' : space,
        'learningMaterial' : learningMaterial
    }
    return render(request, template_name="space/content_detail.html" , context = context)