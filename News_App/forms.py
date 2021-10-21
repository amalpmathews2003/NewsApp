from django import forms
from django.db.models import fields
from .models import *
class CommentForm(forms.ModelForm):
      #comment=forms.CharField(widget=forms.Textarea)
      class Meta:
            model=Comment
            fields=('comment',)
            labels={'comment':''}
            widgets={
                  'comment':forms.Textarea(attrs={'placeholder':'Write Your Comment','class':'comments-container-textarea'}),
            }