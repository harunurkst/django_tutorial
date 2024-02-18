from django.shortcuts import render
from .models import Question


def home(request):
    questions = Question.objects.all()
    context = {
        'question_list': questions
    }
    return render(request, 'home.html', context)