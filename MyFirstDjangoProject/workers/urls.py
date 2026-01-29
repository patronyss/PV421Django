from django.urls import path, include
from workers.views import WorkerListView, WorkerDetailView, WorkerCreateView, WorkerDeleteView, ResumeCreateView


urlpatterns = [
    path('all/', WorkerListView.as_view(), name='workers_list'),
    path('<int:pk>/', WorkerDetailView.as_view(), name='worker_detail'),
    path('<int:pk>/delete/', WorkerDeleteView.as_view(), name='worker_delete'),
    path('create/', WorkerCreateView.as_view(), name='worker_create'),

    path('<int:worker_id>/resume/create', ResumeCreateView.as_view(), name='resume_create'),
]  # domen/workers/
