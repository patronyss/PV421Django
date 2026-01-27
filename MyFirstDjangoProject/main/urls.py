from django.urls import path, include

from main.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index')
]
