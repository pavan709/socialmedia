from . import models
from django import forms
from ckeditor.fields import RichTextField


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ('title', 'message', 'group')
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control mb-3'}),
            'title': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
        }
