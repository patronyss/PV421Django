from django.urls import reverse_lazy, reverse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.shortcuts import get_object_or_404, redirect

from django.shortcuts import render
from workers.models import Worker, Resume

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


class ResumeCreateView(CreateView):
    model = Resume
    fields = ['description']
    template_name = 'workers/resume-create.html'

    def form_valid(self, form):
        form.instance.worker = self.worker
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('worker_detail', kwargs={'pk': self.worker.id})

    def dispatch(self, request, *args, **kwargs):
        self.worker = get_object_or_404(Worker, pk=kwargs['worker_id'])

        if Resume.objects.filter(worker=self.worker).exists():
            return redirect('worker_detail', pk=self.worker.id)

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['worker'] = self.worker
        return context
