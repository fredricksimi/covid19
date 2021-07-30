from django import forms
from .models import Comment, DoctorEmails


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'user' ]
        exclude = ('user',)

class DoctorEmailForm(forms.ModelForm):
    class Meta:
        model = DoctorEmails
        fields = ['sender','note']
        exclude = ('sender',) 