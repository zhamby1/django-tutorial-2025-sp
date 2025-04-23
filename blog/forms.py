#forms are cool in django..because we used a model we can just grab the things we want from our model to display as text boxes or inputs
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')