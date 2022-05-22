from django.shortcuts import render
from space.models import Space

# Create your views here.
def home(request):
    spaces = Space.objects.all()
    print(spaces)
    return render(request, template_name='index.html' , context={"spaces" : spaces})

def spacePage(request, spaceId):
    print(Space.id)
    return render(request, template_name="space/space_page.html")