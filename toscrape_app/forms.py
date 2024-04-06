from django import forms
from .models import Quote, Author

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = '__all__'
        
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'