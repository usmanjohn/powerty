from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import UserProfile
User = get_user_model()
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username','image', 'bio','telegram_username']
        labels = {
            'telegram_username': 'Not required:Telegram Username (without @)',
        }
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("email", "password1", "password2")
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email address is already in use.")
        return email
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["email"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image', 'bio','telegram_username']
        labels = {
            'telegram_username': 'Not required: Telegram Username (without @)',
        }