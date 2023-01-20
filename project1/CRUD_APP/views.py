from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Course
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import CourseForm

@method_decorator(login_required,name='dispatch')
class Create_View(CreateView):
    model = Course
    form_class = CourseForm
    success_url = '/v1/lv/'

@method_decorator(login_required,name='dispatch')
class List_View(ListView):
    model = Course

class Update_View(UpdateView):
    model= Course
    fields ='__all__'
    success_url = '/v1/lv/'

class Delete_View(DeleteView):
    model = Course
    success_url = '/v1/lv/'

class Detail_View(DetailView):
    model = Course
