from django.db import models
from django.contrib.auth.models import User

import datetime
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field 
from django.urls import reverse


class Tutorial(models.Model):
    status_choice = (('submitted', 'submitted'), ('in_review', 'in_review'), ('posted', 'posted'))
    category_choice = (('insight', 'Data Insights'), ('quant', 'Quant'), ('verbal', 'Verbal'), ('other', 'other'))
    title = models.CharField(max_length=60)
    description=CKEditor5Field('Description', config_name='extends')
    short_description = models.CharField('Describe shortly what it is about',max_length=200, default='No short describtion provided, you can read full description')
    author = models.ForeignKey(User, related_name = 'tutoring', on_delete=models.SET_NULL, null=True)
    status = models.CharField(choices=status_choice, default='submitted', max_length=20)
    category = models.CharField(choices= category_choice, default='topik', max_length=20)
    date = models.DateField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self) -> str:
        return self.title
    def get_absolute_url(self):
        return reverse('tutorial-detail', kwargs={'pk': self.pk})

class SavedTutorial(models.Model): 
    user = models.ForeignKey(User, related_name='saved_tutorials', on_delete=models.CASCADE)
    tutorial = models.ForeignKey(Tutorial, related_name='saved', on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'tutorial')

    def __str__(self) -> str:
        return self.tutorial.title  # Assuming 'title' is a field in the Topic model 


    


Rating = (
    (1, '★☆☆☆☆'),
    (2, '★★☆☆☆'),
    (3, '★★★☆☆'),
    (4, '★★★★☆'),
    (5, '★★★★★')
)
class Review(models.Model):
    reviewer = models.ForeignKey(User, related_name='tutor_review', on_delete= models.CASCADE)
    tutorial = models.ForeignKey(Tutorial, related_name = 'reviews', on_delete=models.CASCADE)
    review = models.TextField(blank = True, null=True)
    rating = models.IntegerField(choices=Rating, default=None)
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.tutorial.title
    def get_rating(self):
        return self.rating

    

    

    
    
    