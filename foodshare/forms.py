from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import FoodPost, Interest

class RegisterForm(UserCreationForm):
    """User registration form"""
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class FoodPostForm(forms.ModelForm):
    """Form for creating and editing food posts"""
    class Meta:
        model = FoodPost
        fields = ['food_type', 'quantity', 'donor_name', 'location', 'description', 'price', 'is_available']
        widgets = {
            'food_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Pasta, Bread, Vegetables'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 5 kg, 10 servings'}),
            'donor_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name or organization'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pickup location'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Additional details (optional)'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00', 'step': '0.01'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class InterestForm(forms.ModelForm):
    """Form for expressing interest in a food post"""
    class Meta:
        model = Interest
        fields = ['contact_info', 'message']
        widgets = {
            'contact_info': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your phone number or email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Message to the donor (optional)'}),
        }
