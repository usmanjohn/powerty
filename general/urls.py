from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('search/', views.search_results, name='search_results'),
    path('saved/all', views.saved_all, name='saved-all'),

]