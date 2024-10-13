from django.urls import path, include
from . import views
from .views import TopicListView

from django.views.generic import RedirectView





urlpatterns = [
        
    path('', TopicListView.as_view(), name = 'topics-list'), 
    path('detail/<int:pk>/', views.topic_detail, name='topic-detail'),
    path('topics/create', views.createTopic, name = 'topic-create'),
    path('topics/update/<pk>/', views.updateTopic, name = 'topic-update'),
    path('answer/update/<pk>/', views.updateAnswer, name = 'answer-update'),
    path('topics/delete/<pk>/', views.deleteTopic, name = 'topic-delete'),
    path('answer/delete/<pk>/', views.deleteAnswer, name = 'answer-delete'),
    path('topic/<int:topic_id>/save/', views.save_topic, name='save-topic'),
    path('saved/topics', views.saved_topics_list, name='saved-topics'),
    path('topic/<int:topic_id>/unsave/', views.unsave_topic, name='unsave-topic'),
    path('topic/<int:topic_id>/upvote/', views.upvote_topic, name='upvote-topic'),
    path('answer/<int:answer_id>/upvote/', views.upvote_answer, name='upvote-answer'),
    path('unauthorized-vote/', views.unauthorized_vote, name='unauthorized-vote'),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')),

    
    
    
    # Add other URLs as needed


]