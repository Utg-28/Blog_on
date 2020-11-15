from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>hello to site</h1>')

def contact(request):
    return HttpResponse('<h1>welocime to contact page</h1>')