from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("hello")
    return render(request, 'monsters/home.html')

def about(request):
    return render(request, 'monsters/about.html')