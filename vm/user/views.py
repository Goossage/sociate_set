from django.shortcuts import render

# Create your views here.

def profile(request):
    return render(request, 'user/profile.html')

def login(request):
    pass

def register(request):
    pass