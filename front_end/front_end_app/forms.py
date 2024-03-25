# front_end_app/forms.py
from django import forms
from .models import UrlData

class YTDownloaderForm(forms.ModelForm):
    class Meta:
        model = UrlData
        fields = ['url']

