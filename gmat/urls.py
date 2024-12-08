from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from general.models import TopicAnswerSitemap, TopicSitemap, PracticeQuestionsSitemap, PracticeSitemap, HomeworkQuestionsSitemap, HomeworkSitemap, TutorialSitemap
from django.contrib.sitemaps.views import sitemap
sitemaps = {
    'topics': TopicSitemap,
    'topicanswer': TopicAnswerSitemap,
    'tutorial': TutorialSitemap,
    'practice': PracticeSitemap,
    'practicequestions': PracticeQuestionsSitemap,
    'homeworks': HomeworkSitemap,
    'homeworkquestions': HomeworkQuestionsSitemap
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('general.urls')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    
    path('tests/', include('homeworks.urls')),
    path('tutorials/', include('tutorials.urls')),
    path('topics/', include('topics.urls')),
    path('practice/', include('practice.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
