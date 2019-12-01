from .models import Comment
from django import forms

# Creating my Comment Forms

class CommentForm(forms.ModelForm):
	
    class Meta:
        model = Comment
        fields = ['name', 'body']