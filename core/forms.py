from django import forms

class CreatePost(forms.Form):
    title = forms.CharField(widget=forms.TextInput({'placeholder': 'Title'}), max_length=300, label='')
    content = forms.CharField(widget=forms.Textarea({'placeholder': 'Content'}), label='')
    public = forms.BooleanField(initial=True, required=False)

