from django import forms

class CommentForm(forms.Form):
    name =  forms.CharField(max_length=30,
    widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Your name'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Write a comment'}))

