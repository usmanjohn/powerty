from django.forms import ModelForm
from django import forms
from .models import Tutorial, Rating, Review
from django_ckeditor_5.widgets import CKEditor5Widget
class TutorialForm(forms.ModelForm):

      class Meta:
          model = Tutorial
          fields = ['title', 'description',  'category', 'short_description']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review']
        widgets = {
            'review': forms.Textarea(attrs={'rows': 4}),
        }