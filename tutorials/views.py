from django.shortcuts import render, redirect, get_object_or_404
from .models import Tutorial, SavedTutorial, Review
from .forms import TutorialForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.conf import settings
import os

@csrf_exempt  # Use with caution. Ensure proper security measures are in place.
def image_upload(request):
    if request.method == 'POST' and request.FILES.get('upload'):
        upload = request.FILES['upload']
        # Optionally, add validation for the file type and size here
        file_name = default_storage.save(os.path.join('uploads/', upload.name), upload)
        file_url = default_storage.url(file_name)
        
        # CKEditor5 expects a specific JSON response
        return JsonResponse({
            'url': file_url
        })
    return JsonResponse({'error': 'Invalid request'}, status=400)
def tutors_list(request):
    query = request.GET.get('q', '')  # Get the search query from GET request
    tutoring = Tutorial.objects.filter(status='posted').order_by('-date', 'title')
    if query:  # If a query is present, filter by the search term in the title
        tutoring = tutoring.filter(Q(title__icontains=query) | Q(description__icontains=query)).distinct()
    context = {'tutoring': tutoring, 'query': query}
    return render(request, 'tutorials/tutorial_list.html', context)



def tutors_detail(request, pk):
    tutorial = get_object_or_404(Tutorial, id=pk)
    user_reviews = Review.objects.filter(tutorial=tutorial).order_by('-date')
    is_saved = False
    if request.user.is_authenticated:
        is_saved = SavedTutorial.objects.filter(user=request.user, tutorial=tutorial).exists()
    if request.method == 'POST' and request.user.is_authenticated:
        user_review = user_reviews.filter(reviewer=request.user).first()

        form = ReviewForm(request.POST, instance=user_review)
        if form.is_valid():
            review = form.save(commit=False)
            review.tutorial = tutorial
            review.reviewer = request.user
            review.save()
            messages.success(request, 'Your review has been submitted.')
            return redirect('tutorial-detail', pk=pk)
    else:
        form = ReviewForm()
    context = {
        'tutor': tutorial,
        'form': form,
        'user_review': user_reviews,
        'is_saved':is_saved
    }
    return render(request, 'tutorials/tutorial_detail.html', context)



@login_required
def tutors_create(request):
    print("Method:", request.method)  # Check the method
    if request.method == 'POST':
        forms = TutorialForm(request.POST)
        print("Form received:", forms.is_bound)  # Check if form is bound
        if forms.is_valid():
            print("Form is valid")
            form = forms.save(commit=False)
            form.author = request.user  # Manually assign the author
            form.save()
            forms.save_m2m()
            messages.success(request, 'Tutorial created successfully and in Review')
            return redirect('tutorial-list')
        else:
            forms = TutorialForm() 
            messages.error(request, 'Some of the fields are not filled correctly')

            print("Form errors:", forms.errors)  # Log form errors
    else:
        forms = TutorialForm()
    
    context = {'forms': forms}
    return render(request, 'tutorials/tutorial_create.html', context)


@login_required
def tutor_update(request, pk):
    tutor = get_object_or_404(Tutorial, id = pk)
    if request.user == tutor.author and request.method == 'POST':

        form = TutorialForm(request.POST, instance=tutor)
        if form.is_valid():
            form = form.save(commit = False)
            form.status = 'submitted'
            form.save()
            messages.success(request, 'Tutorial updated successfully and in Review')
            return redirect('tutorial-detail', pk = tutor.pk)
    else:
        form = TutorialForm(instance=tutor)
    context = {'form':form}
    return render(request, 'tutorials/tutorial_update.html',context)


def tutor_delete(request, pk):
    tutor = get_object_or_404(Tutorial, id = pk)
    if request.user == tutor.author and request.method == 'POST':
        tutor.delete()
        messages.success(request, 'Tutorial deleted')
        return redirect('tutorial-list')
    context = {'tutor':tutor}
    return render(request, 'tutorials/tutorial_delete.html', context)



@login_required
def save_tutorial(request, pk):
    tutorial = get_object_or_404(Tutorial, id=pk)
    SavedTutorial.objects.get_or_create(user=request.user, tutorial=tutorial)
    return redirect('tutorial-detail', pk=pk)

@login_required
def saved_tutorials_list(request):
    saved_tutorials = SavedTutorial.objects.filter(user=request.user).select_related('tutorial')    
    context = {'saved_tutorials': saved_tutorials}
    return render(request, 'tutorials/saved_tutorial.html', context)

@login_required
def unsave_tutorial(request, pk):
    tutorial = get_object_or_404(Tutorial, id=pk)
    saved_tutorial = SavedTutorial.objects.filter(user=request.user, tutorial=tutorial)
    if saved_tutorial.exists():
        saved_tutorial.delete()
    return redirect('tutorial-detail', pk=pk)