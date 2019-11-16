from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {'test' : 'HELLO THIS IS A TEST'}
    return render(request, 'fitboi_photo/index.html', context)