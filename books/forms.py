from django import forms
from .models import *

class IssueBookForm(forms.ModelForm):

	class Meta:
		model = BooksIssued
		fields = ('__all__')

class SaveBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('__all__')

