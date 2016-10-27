#!-*encoding:utf-8*-
from django import forms
class diaryform(forms.Form):
    diary_title=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'请键入您的标题' }),max_length=30)
    diary_text=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'请键入您的日记' }),max_length=2000)
    # asdf=forms.Textarea(attrs={'class':'form-control','placeholder':'请键入您的日记' })
