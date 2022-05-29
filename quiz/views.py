from django.shortcuts import render
from quiz.models import Quiz, Question
from quiz.forms import quiz_form, question_form
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from space.models import Space

# Create your views here.
def list_quizes(request, space_id):
    space = Space.objects.get(id = space_id)
    quizes = Quiz.objects.filter(space = space).order_by('published_date')
    context = {"quizes" : quizes , "space" : space}
    return render(request, template_name="quiz/quiz_page.html" , context = context)

def create_quiz(request,space_id):

    return

def quiz_detail(request,space_id,quiz_id):

    return


