from django.contrib import admin
from .models import Book, Autor, Zanr

# Register your models here.

admin.site.register(Book)
admin.site.register(Autor)
admin.site.register(Zanr)