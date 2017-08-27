from django import forms
from scotstartup.models import Company, UserProfile
from django.contrib.auth.models import User

class CompanyForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Company name")
    description = forms.CharField(max_length=256, help_text="Description")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Company
        fields = ('name', 'description')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
