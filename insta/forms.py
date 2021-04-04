from django import forms 
from .models import post, comment

class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'share with friends'
        })
    )

    class Meta:
        model = post
        fields = ['body']

class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'share with friends'
        })
    )

    class Meta:
        model = comment
        fields = ['comment']
