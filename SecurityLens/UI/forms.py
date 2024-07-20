# Forms
#delete if not required

from django import forms


class UI_form(forms.Form):
    search_box = forms.CharField(label='Search CVE', 
                                 widget=forms.TextInput(attrs={'class': 'search-box'}))  
    #here length is not required



