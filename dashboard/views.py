from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Groups

# Create your views here.

def index(request):
    all_groups = Groups.objects.all()
    context = {
        'all_groups': all_groups,
    }
    return render(request, 'dashboard/index.html', context)
