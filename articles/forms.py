from django import forms
from .models import Article, Commnet


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'


class CommentForm(forms.ModelForm):

    class Meta:
        model = Commnet
        exclude = ('article',)
