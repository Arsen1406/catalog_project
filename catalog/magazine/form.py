from django import forms


class ArticleForm(forms.Form):
    article = forms.CharField()