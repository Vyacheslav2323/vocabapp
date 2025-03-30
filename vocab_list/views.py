from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import TodoItem
from django.contrib.auth.decorators import login_required


def users(request):
  template = loader.get_template('myfirst.html')
  context = {'user': request.user}
  return render(request, 'myfirst.html', context)

