from django.shortcuts import render
from workers.models import Worker

# Create your views here.
def workers_list_view(request):
    all_workers = Worker.objects.all()

    context = {
        'workers': all_workers
    }

    return render(request, 'workers/all.html', context)
