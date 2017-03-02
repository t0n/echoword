from django import forms 


class WordsForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
