from django.shortcuts import render
from posts.models import PostModel
# Create your views here.

def home(request):
    data=PostModel.objects.all()
    return render(request, 'home.html', {'data':data})