# lab2/forms.py

from django import forms

class SentimentForm(forms.Form):
    text = forms.CharField(label="Nhập văn bản", widget=forms.Textarea(attrs={"rows": 5, "cols": 50}))
