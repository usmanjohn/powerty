from django.urls import path, include
from . import views

urlpatterns = [
    
    path('list', views.tutors_list, name = 'tutorial-list'), 
    path('detail/<pk>', views.tutors_detail, name = 'tutorial-detail'),
    path('create', views.tutors_create, name = 'tutorial-create'),
    path('update/<pk>', views.tutor_update, name = 'tutorial-update'),
    path('delete/<pk>', views.tutor_delete, name = 'tutorial-delete'),

    path('<int:pk>/save/', views.save_tutorial, name='save-tutorial'),
    path('saved/tutorials', views.saved_tutorials_list, name='saved-tutorials'),
    path('ckeditor5/image_upload/', views.image_upload, name='ckeditor5_image_upload'),
    
    path('<int:pk>/unsave/', views.unsave_tutorial, name='unsave-tutorial'),
]