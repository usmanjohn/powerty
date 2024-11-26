from django.urls import path
from . import views
urlpatterns = [
    path('', views.select_practice, name='practice-list'),
    path('practice/<int:pk>/start/', views.start_practice, name='practice-start'),
    path('practice/<int:pk>/submit/', views.submit_practice, name='submit-practice'),
    path('practice-results/<int:pk>/', views.practice_results, name='practice-results'),
    path('pr-question-details/<int:pk>/', views.pr_question_detail, name = 'pr-question-detail'),
    
]