from django.shortcuts import render, redirect
from topics.models import Topic, SavedTopic
from homeworks.models import Test, TestAttempt
from tutorials.models import Tutorial, SavedTutorial
from practice.models import Practice, PracticeAttempt
from django.db.models import Count, Q
from django.contrib.auth.decorators import login_required
from users.models import UserProfile
from django.contrib.auth.models import User
from django.db.models import Max
from .forms import CommentForm
from .models import Comments

def about(request):
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.writer = request.user
            comment.save()
            return redirect('about')  # Redirect to prevent double submission
    else:
        form = CommentForm()

    comments = Comments.objects.all()  # Fetch all comments for display
    return render(request, 'general/about.html', {'form': form, 'comments': comments})

def home(request):    
    tests = Test.objects.all()
    tutorials = Tutorial.objects.all()
    practice = Practice.objects.all()
    topics = Topic.objects.all()    
    return render(request, 'general/home.html', {'tests': tests, 'topics': topics, 'practice': practice, 'tutorials': tutorials})

@login_required
def saved_all(request):
    saved_topics = SavedTopic.objects.filter(user=request.user).select_related('topic')
    
    tutorials = SavedTutorial.objects.filter(user=request.user).select_related('tutorial')
    
    # Get unique tests taken by the user, along with their latest attempt
    tests = TestAttempt.objects.filter(user=request.user).values('test').annotate(
        latest_attempt=Max('id')
    ).values_list('latest_attempt', flat=True)
    
    tests = TestAttempt.objects.filter(id__in=tests).select_related('test')
    practice = PracticeAttempt.objects.filter(user=request.user).values('test').annotate(
        latest_attempt=Max('id')
    ).values_list('latest_attempt', flat=True)
     
    practice = PracticeAttempt.objects.filter(id__in=tests).select_related('test')
    context = {
        'saved_topics': saved_topics,
        'saved_tests': tests,
        'saved_practice': practice,
        'saved_tutorials': tutorials
    }
    return render(request, 'general/saved_items.html', context)
def search_results(request):
    query = request.GET.get('q', '')
    if query:
        topic_results = Topic.objects.filter(Q(topic_title__icontains=query) | Q(topic_body__icontains=query)).distinct()
        tutorial_results = Tutorial.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)).distinct()
        test_results = Test.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)| Q(questions__question_text__icontains=query)).distinct()
        practice_results = Practice.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)| Q(practice_questions__question_text__icontains=query)).distinct()
        
    else:
        topic_results  = tutorial_results = test_results = practice_results = []
    
    context = {
        'query': query,
        'topic_results': topic_results,
        
        "practice_results":practice_results,
        "test_results":test_results,
        "tutorial_results":tutorial_results,
    }
    return render(request, 'general/search_results.html', context)