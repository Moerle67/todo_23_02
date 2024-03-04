from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    liste = Eintrag.objects.filter(done=False)
    user = "Moerli"
    content = {
        'liste': liste,
        'user': user,
    }
    return render(request, "todoapp/todo_list.html", content)
