from django.urls import path
from . import views

#app_name = 'homeworks'  # This creates a namespace for your app's URLs

urlpatterns = [
    path('', views.select_test, name='test-list'),
    path('test/<int:pk>/start/', views.start_test, name='test-start'),
    path('test/<int:pk>/submit/', views.submit_test, name='submit-test'),
    path('test-results/<int:pk>/', views.test_results, name='test-results'),
    path('question-details/<pk>', views.question_detail, name = 'question-detail'),
    
]