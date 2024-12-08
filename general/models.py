from django.db import models
from django.contrib.auth.models import User
from practice.models import PracitceQuestions, Practice
from homeworks.models import Test, MultipleChoiceQuestion
from django.contrib.sitemaps import Sitemap

from tutorials.models import Tutorial
from topics.models import Topic, Answer

class TopicSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Topic.objects.all().order_by('id') 

    def lastmod(self, obj):
        return obj.updated_at
    
class TutorialSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Tutorial.objects.all().order_by('id') 

    def lastmod(self, obj):
        return obj.updated_at

    
class TopicAnswerSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Answer.objects.all().order_by('id') 

    def lastmod(self, obj):
        return obj.updated_at


    
class PracticeSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Practice.objects.all().order_by('id') 

    def lastmod(self, obj):
        return obj.updated_at

class PracticeQuestionsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return PracitceQuestions.objects.all().order_by('id') 

    def lastmod(self, obj):
        return obj.updated_at

class HomeworkQuestionsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return MultipleChoiceQuestion.objects.all().order_by('id') 

    def lastmod(self, obj):
        return obj.updated_at

class HomeworkSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Test.objects.all().order_by('id') 

    def lastmod(self, obj):
        return obj.updated_at



class Comments(models.Model):
    writer = models.ForeignKey(User, related_name='comment', on_delete=models.CASCADE)
    comment = models.CharField(max_length=400)
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # 1 to 5 stars
    date = models.DateField(auto_now_add=True)

