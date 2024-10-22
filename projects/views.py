from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from . import models, forms

# Create your views here.

class ProjectListView(ListView):
    model = models.Project
    template_name = 'project/list.html'


class PrjectCreateView(CreateView):
    model = models.Project
    form_class = forms.ProjectCreateForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('Project_list')
