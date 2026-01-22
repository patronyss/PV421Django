from django.shortcuts import render

# Create your views here.
def index_view(request):
    context = {
        'greetings': 'Ласкаво просимо! Ми раді, що ви тут!',
        'numbers': range(1, 11)
    }

    return render(request, 'main/index.html', context)
