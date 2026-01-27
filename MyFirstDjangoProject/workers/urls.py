from django.urls import path, include
from workers.views import WorkerListView


urlpatterns = [
    path('all/', WorkerListView.as_view(), name='workers_list'),
]  # domen/workers/....
