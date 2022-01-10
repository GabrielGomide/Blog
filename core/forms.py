from django import forms

class CreatePost(forms.Form):
    title = forms.CharField(widget=forms.TextInput({'placeholder': 'Title'}), max_length=300)
    content = forms.CharField(widget=forms.Textarea({'placeholder': 'Content'}))
    public = forms.BooleanField(initial=True, required=False)

