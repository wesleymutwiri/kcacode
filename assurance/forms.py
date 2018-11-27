from .models import Feedback, Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = ['user', 'date', 'report']
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['date', 'firstname', 'lastname', 'email', 'username']        

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True,)
    last_name = forms.CharField(max_length=30, required=True, )
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address')

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name', 'email','password1','password2',)
        