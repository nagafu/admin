from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import views as auth_views
from .forms import LoginForm


def index(request):
    return render(request, 'index.html')


def index2(request):
    return render(request, 'index2.html')


# def login(request):
#     context = {'template_name': 'login.html', 'authentication_form': LoginForm}
#     return auth_views.login(request, **context)

# 404エラーの作り方
# from django.shortcuts import get_object_or_404, render
# from .models import Question

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})