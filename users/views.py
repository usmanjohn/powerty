from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, UserProfileForm, UserProfileUpdateForm
from topics.models import Topic, Answer
from tutorials.models import Tutorial
from homeworks.models import TestAttempt
from practice.models import PracticeAttempt

from django.contrib.auth.models import User
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            authenticated_user = authenticate(request, username=email, password=password)
            if authenticated_user:
                login(request, authenticated_user)
                messages.success(request, f'Account created for {email}!')
                return redirect('home')
            else:
                messages.error(request, 'Authentication failed. Please try logging in.')
        # Remove the else block that adds error messages
    else:
        form = CustomUserCreationForm()
        profile_form = UserProfileForm()

    return render(request, 'users/register.html', {'form': form, 'profile_form': profile_form})
def custom_logout(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('home')  # or any other page you want to redirect to

def view_profile(request, email):
    profile_user = get_object_or_404(User, email=email)
    topics = Topic.objects.filter(topic_author = profile_user)
    tutorials = profile_user.tutoring.all()
    answers = profile_user.answer_auth.all()
    is_own_profile = request.user.is_authenticated and request.user == profile_user
    
    context = {
        'profile_user': profile_user,
        'is_own_profile': is_own_profile,
        'topics':topics,
        'answers':answers,
        'tutorials':tutorials
        }
    return render(request, 'users/profile.html', context)


@login_required
def update_profile(request, email):
    profile_user = get_object_or_404(User, email=email)
    
    # Ensure that only the profile owner can update the profile
    if request.user != profile_user:
        return redirect('profile', email=request.user.email)
    
    if request.method == 'POST':
        p_form = UserProfileUpdateForm(request.POST, request.FILES, instance=profile_user.userprofile)
        
        
        if request.method == 'POST':
            p_form = UserProfileUpdateForm(request.POST, request.FILES, instance=profile_user.userprofile)
            if p_form.is_valid():
                profile = p_form.save(commit=False)
                profile.save()
                # Add this to see if it's uploaded to S3
                print(f"DEBUG: Image uploaded to: {profile.image.url}")
            
            messages.success(request, 'Your profile has been updated.')
            return redirect('profile', email=profile_user.email)
        else:
            print("DEBUG: Form is not valid.")
            print(p_form.errors)  # Print any form errors to terminal for debugging
    
    else:
        p_form = UserProfileUpdateForm(instance=profile_user.userprofile)
    
    context = {
        'p_form': p_form,
        'profile_user': profile_user
    }
    return render(request, 'users/update_profile.html', context)