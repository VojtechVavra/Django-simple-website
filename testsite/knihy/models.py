from django.db import models

class Zanr(models.Model):
    nazev_zanru = models.CharField(max_length=80, verbose_name="Žánr")
    def __str__(self):
        return self.nazev_zanru
        #return "Nazev zanru: {0}".format(self.nazev_zanru)

    class Meta:
        verbose_name="Žánr"
        verbose_name_plural="Žánry"


class Autor(models.Model):
    cele_jmeno = models.CharField(max_length=100)
    info_text = models.CharField(max_length=600, null=True)
    #books = None

    def __str__(self):
        return self.cele_jmeno
        #return "Autor: {0}".format(self.cele_jmeno)


class Book(models.Model):
    nazev = models.CharField(max_length=200, verbose_name="Název Knihy")
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
    zanr = models.ForeignKey(Zanr, on_delete=models.SET_NULL, null=True, verbose_name="Žánr")

    def __str__(self):
        return "Nazev: {0} | Autor: {1} | Zanr: {2}".format(self.nazev, self.autor.cele_jmeno, self.zanr.nazev_zanru)

    """ class Meta:
        verbose_name="Kniha"
        verbose_name_plural="Knihy" """
