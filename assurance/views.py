from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'assurance/index.html')

def about(request):
    return render(request, 'assurance/about.html')

def profile(request):

    return render(request, 'assurance/profile.html')

def feedback(request):
    return render(request, 'assurance/feedback.html')
    