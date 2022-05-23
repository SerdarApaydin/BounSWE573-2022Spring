from django.http import HttpResponse
from django.shortcuts import render
from space.models import LearningMaterialVideos, Space
from space.forms import Video_form

# Create your views here.
def home(request):
    spaces = Space.objects.all()
    print(spaces)
    return render(request, template_name='index.html' , context={"spaces" : spaces})

def spacePage(request, id):
    space = Space.objects.get(id = id)
    learningMaterials = LearningMaterialVideos.objects.filter(space = space)
    context = {
        'space' : space,
        'learningMaterials' : learningMaterials
    }
    return render(request, template_name="space/space_page.html" , context = context)

def uploadContent(request,id):
    if request.method == "POST":
        form = Video_form(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h4>Uploaded succcessfully<h4>")
    else:
        form = Video_form()
    return render(request,'space/upload_file.html',{"form":form})