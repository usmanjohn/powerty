from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field
from storages.backends.s3boto3 import S3Boto3Storage
from django.utils.html import strip_tags

class S3Storage(S3Boto3Storage):
    location = 'media'
class Test(models.Model):
    Type = (('math','Math'),
    ('geometry', 'geometry'),
    ('mixed','Mixed'),
    ('other','Other'),
    )

    Category_CHOICES = (
    ('quant','Quant'),
    ('verbal', 'Verbal'),
    ('insight','Insight'),
    ('all','All')
    )
    Easy_level = (
        ('easy','Easy'),
        ('Medium', 'Medium'),
        ('hard','Hard'),
        ('mixed','Mixed'),
        ('real', 'Real')
    )
    
    
    category = models.CharField(choices=Category_CHOICES, default='quant', max_length=20)
    level = models.CharField(choices=Easy_level, default='real', max_length=20)
    type = models.CharField(choices=Type, default='math', max_length=20)
    order = models.IntegerField(default=1)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField( auto_now_add = True)
    is_free = models.BooleanField(default = False)
    link = models.URLField(blank=True, null=True, default="youtube.com/channel/UCv2shQIaFCsfUL29YL9uxIQ")
    def __str__(self):
        return self.title

class MultipleChoiceQuestion(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    question_text = CKEditor5Field('Question', config_name='extends')
    image = models.ImageField(storage=S3Boto3Storage(),upload_to='question_images/', null=True, blank=True)
    choice1 = CKEditor5Field('Choice 1', config_name='extends')
    choice2 = CKEditor5Field('Choice 2', config_name='extends')
    choice3 = CKEditor5Field('Choice 3', config_name='extends')
    choice4 = CKEditor5Field('Choice 4', config_name='extends')
    choice5 = CKEditor5Field('Choice 5', config_name='extends')
    
    correct_answer = models.IntegerField(choices=[(1, 'Choice 1'), (2, 'Choice 2'), (3, 'Choice 3'), (4, 'Choice 4'), (5, 'Choice 5')])
    explanation = CKEditor5Field('Explanation', config_name='extends', null=True, blank=True)
    made_by = models.ForeignKey(User, related_name='questions', on_delete=models.CASCADE)
    date_made = models.DateTimeField(auto_now_add=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {strip_tags(self.question_text)[:50]}"

class TestAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, null= True, blank= True)
    timestamp = models.DateTimeField(auto_now_add=True)
    score = models.FloatField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.test.title} ({self.timestamp.strftime('%Y-%m-%d %H:%M')})"

    class Meta:
        ordering = ['-timestamp']

class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(MultipleChoiceQuestion, on_delete=models.CASCADE)
    selected_choice = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    test_instance = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='user_answers', blank=True, null=True)
    test_attempt = models.ForeignKey(TestAttempt, on_delete=models.CASCADE, blank = True, null = True, related_name='user_answers')

    def is_correct(self):
        return self.selected_choice == self.question.correct_answer

    def __str__(self):
        return f"{self.user.username} - Q{self.question.id} - {'Correct' if self.is_correct() else 'Incorrect'}"