from django.urls import path, include
from workers.views import workers_list_view


urlpatterns = [
    path('all/', workers_list_view, name='workers_list'),
]  # domen/workers/....
