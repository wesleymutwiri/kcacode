from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'assurance/index.html')

def about(request):
    return render(request, 'assurance/about.html')

def profile(request):

    return render(request, 'assurance/profile.html')

def feedback(request):
    return render(request, 'assurance/feedback.html')
    