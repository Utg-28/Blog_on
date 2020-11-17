from django.shortcuts import render
from django.http import HttpResponse
from blogs.models  import Post
# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'blogs/index.html', context)

def contact(request):
    return HttpResponse('<h1>welocome to contact page</h1>')