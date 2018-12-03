from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from assurance.forms import FeedbackForm, ProfileForm
from django.db import transaction
from .models import Feedback, Profile
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    # user = request.user
    # feedback = Feedback.objects.filter(username=request.user)
    # profile = Profile.objects.filter(username=request.user)
    # includes = {
    #     "user":user,
    #     "feedback": feedback,
    #     "profile": profile,
    # }
    user = request.user
    return render(request, 'assurance/index.html')

def about(request):
    return render(request, 'assurance/about.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    user = request.user 
    form = ProfileForm()
    feedback = Feedback.objects.filter(username=request.user)
    avatar = Profile.profile_avatar
    includes = {
        "user":user,
        "images": images,
        "profile":profile,
        "avatar": avatar,
        "form": form,
    }
    return render(request, 'assurance/profile.html', includes)

@login_required(login_url='/accounts/login/')
def feedback(request):
    current_user = request.user
    profile = request.user.profile

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.username = current_user
            feedback.profile = profile
            feedback.user_id=request.user.id
            feedback.save()
            return redirect('index')
    else:
        form = FeedbackForm()
    return render(request, 'assurance/feedback.html', {"form":form})

@transaction.atomic
@login_required(login_url ='/accounts/login')
def change_profile(request, user_id):
    profile = request.user.profile 

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save(commit=False)
            profile.save()
        return redirect('profile', user_id)        
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'assurance/edit-profile.html', {"form":form})
