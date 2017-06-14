from django import forms

from .models import StarDetail, Comment
from DjangoUeditor.forms import UEditorField

class StarDetailForm(forms.ModelForm):
    name = forms.CharField(label="name", max_length=200, required=True)
    introduce = UEditorField(label="introduce", max_length=1000, required=True)
    class Meta:
        model = StarDetail
        fields = ['name', 'introduce']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
