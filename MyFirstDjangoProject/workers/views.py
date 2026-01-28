from django.urls import reverse_lazy, reverse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.shortcuts import render
from workers.models import Worker

# Create your views here.
class WorkerListView(ListView):
    model = Worker
    template_name = 'workers/workers-all.html'
    context_object_name = 'workers'


class WorkerDetailView(DetailView):
    model = Worker
    template_name = 'workers/worker-detail.html'
    context_object_name = 'worker'


class WorkerCreateView(CreateView):
    model = Worker
    fields = ['name', 'salary', 'note']
    template_name = 'workers/worker-create.html'

    def get_success_url(self):
        return reverse('worker_detail', kwargs={'pk': self.object.id})


class WorkerDeleteView(DeleteView):
    model = Worker
    template_name = 'workers/worker-delete.html'
    context_object_name = 'worker'
    success_url = reverse_lazy('workers_list')
