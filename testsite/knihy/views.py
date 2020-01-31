from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import DetailView
from .models import Book, Zanr, Autor
from .forms import BookForm, GenreForm, AuthorForm
# Create your views here.



def index(request):
    template_name = "knihy/index.html"
    all_books = Book.objects.all()
    number_books = Book.objects.count()
    response = HttpResponse()
    #response.write("<h1>Knihy</h1>")
    response.write(template_name)
    return response

class index2(generic.DetailView):
    template_name = "knihy/index.html"


class BookIndex(generic.ListView):
    template_name = "knihy/index.html" # cesta k templatu ze složky templates (je možné sdílet mezi aplikacemi)
    context_object_name = "books" # pod tímto jménem budeme volat list objektů v templatu
    # tato funkce nám získává list knizek od největšího id (9,8,7...)
    def get_queryset(self):
        return Book.objects.all()[:]
        #return Book.objects.all().order_by("-id")


class CurrentBookView(generic.DetailView):
    model = Book
    template_name = "knihy/book_detail.html"

"""def CurrentAuthorView(request):
    template_name = "knihy/author_detail.html"
    autors = Autor.objects.all()
    context = { 'autors' : autors}
    return render(request, self.template_name, self.context)
"""

#class CurrentAuthorView(DetailView):
class CurrentAuthorView(generic.edit.CreateView):
    context_object_name = 'autor'
    all_autors = Autor.objects.all()
    all_books = Book.objects.all()
    queryset =  {"autor": all_autors, "all_books": all_books}
    #queryset = { 'all_autors': all_autors, 'all_books': all_books}
    template_name = "knihy/author_detail.html"

    # Metoda pro GET request, zobrazí pouze formulář
    def get(self, request, pk):
        #form = self.form_class(None)
        self.queryset["pk"] = pk
        actual_autor = Autor.objects.get(pk=pk)
        this_autor_books = Book.objects.filter(autor=pk)
        queryset2 = {"autor": actual_autor, "books": this_autor_books, "pk": pk }
        return render(request, self.template_name, queryset2)
    #def get_queryset(self):
            #return Book.objects.filter(autor=self.autor)


class AddBook(generic.edit.CreateView):
    form_class = BookForm
    template_name = "knihy/create_book.html"
# Metoda pro GET request, zobrazí pouze formulář
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {"form":form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=True)
        #return render(request, self.template_name, {"form":form})
        response = HttpResponse()
        response.write("<h1>Kniha přidána</h1>")
        response.write("<a href=\"/add_book/\">Přidat další<br> </a>")
        response.write("<a href=\"/home/\">Zpět<br> </a>")
        return response


class AddGenre(generic.edit.CreateView):
    form_class = GenreForm
    template_name = "knihy/add_genre.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {"form":form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save(commit=True)
            #return render(request, self.template_name, {"form":form})
        response = HttpResponse()
        response.write("<h1>Žánr přidán</h1>")
        response.write("<a href=\"/home/\">Zpět<br> </a>")
        return response

class AddAuthor(generic.edit.CreateView):
    form_class = AuthorForm
    template_name = "knihy/add_author.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {"form":form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=True)
        response = HttpResponse()
        response.write("<h1>Autor přidán</h1>")
        response.write("<a href=\"/home/\">Zpět<br> </a>")
        return response
####