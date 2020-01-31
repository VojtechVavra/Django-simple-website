from django import forms
from .models import Book, Zanr, Autor

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields=["nazev", "autor", "zanr"]

class GenreForm(forms.ModelForm):
    class Meta:
        model = Zanr
        fields=["nazev_zanru"]

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields=["cele_jmeno", "info_text"]