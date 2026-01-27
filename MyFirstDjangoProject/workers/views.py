from django.views.generic import ListView

from django.shortcuts import render
from workers.models import Worker

# Create your views here.
class WorkerListView(ListView):
    model = Worker
    template_name = 'workers/all.html'
    context_object_name = 'workers'
