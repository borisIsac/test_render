from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.conf import settings


# Create your views here.
def index(request):

    print('------',settings.TEMPLATES)
    context = {
        "title": "Главная страница",
        'user1': "Boris Isac",
        'user2': "Oxana Bruieva",
    }
    return HttpResponse(f"{context['user1']}-{context['user2']}")
    #return render(request, "templates\index\index.html", context=context)
