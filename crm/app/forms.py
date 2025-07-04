from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Record

class SignupForm(UserCreationForm):
    username = forms.CharField(
        label='', 
        widget=forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Full Name' }), 
        max_length=50
    )
    email = forms.EmailField(
        label='', 
        widget=forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Email Address' }), 
        max_length=50
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args: Any, **kwargs: Any):
        super(SignupForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        
        self.fields['username'].help_text = '''
            <span class="form-text text-muted">
               <small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small>
            </span>
        '''
        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        
        self.fields['password1'].help_text = '''
            <ul class="form-text text-muted small"> 
               <li>Your password can\'t be too similar to your other personal information.</li> 
               <li>Your password must contain at least 8 characters.</li> 
               <li>Your password can\'t be a commonly used password.</li> 
               <li>Your password can\'t be entirely numeric.</li>
            </ul>
        '''

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        
        self.fields['password2'].help_text = '''
            <span class="form-text text-muted">
               <small>Enter the same password as before, for verification.</small>
            </span>
        '''
        

class AddRecordForm(forms.ModelForm):
    username    = forms.CharField(max_length=50, required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}), label='')
    email       = forms.EmailField(max_length=50, required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Email Address', 'class': 'form-control'}), label='')
    phone       = forms.CharField(max_length=10, required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Phone No.', 'class': 'form-control'}), label='')
    address     = forms.CharField(max_length=100, required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control'}), label='')
    city        = forms.CharField(max_length=50, required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'City', 'class': 'form-control'}), label='')
    state       = forms.CharField(max_length=50, required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'State', 'class': 'form-control'}), label='')
    zipcode     = forms.CharField(max_length=6, required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Zipcode', 'class': 'form-control'}), label='')

    class Meta:
        model = Record
        exclude = ('user',)
