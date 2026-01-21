from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from viewer.models import Profile


class RegisterProfileForm(UserCreationForm):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)


    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "name", "phone"]
        
    
    def save(self, commit=True):
        user = super().save(commit=commit)
        
        if commit:
            Profile.objects.create(
                user = user,
                name = self.cleaned_data.get("name", ""),
                phone = self.cleaned_data.get("phone", ""),
            )
            
        return user
