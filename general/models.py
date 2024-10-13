from django.db import models
from django.contrib.auth.models import User


class Comments(models.Model):
    writer = models.ForeignKey(User, related_name='comment', on_delete=models.CASCADE)
    comment = models.CharField(max_length=400)
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # 1 to 5 stars
    date = models.DateField(auto_now_add=True)

