from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('general.urls')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    
    path('tests/', include('homeworks.urls')),
    path('tutorials/', include('tutorials.urls')),
    path('topics/', include('topics.urls')),
    path('practice/', include('practice.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
