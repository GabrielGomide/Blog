from django import forms

class CreateAccount(forms.Form):
    username = forms.CharField(widget=forms.TextInput({'placeholder': 'Username'}), max_length=50, label='')
    password = forms.CharField(widget=forms.PasswordInput({'placeholder': 'Password'}), max_length=50, label='')

