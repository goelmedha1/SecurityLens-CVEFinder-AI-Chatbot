# Import forms class

from django import forms
from .models import SearchQuery


# class UI_form(forms.Form):
#     search_box = forms.CharField(label='Search CVE', 
#                                  widget=forms.TextInput(attrs={'class': 'search-box'}))  
#     #here length is not required

class UI_form(forms.ModelForm):
    class Meta:
        model = SearchQuery
        fields = ['search_box']
        labels = {'search_box': 'Search CVE'}
        widgets = {'search_box': forms.TextInput(attrs={'class': 'search-box', 'placeholder': 'Ask AI'})}


