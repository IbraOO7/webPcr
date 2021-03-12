from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Tentang(models.Model):
    text_tentang = RichTextField(blank=True,null=True)
            
class Gallery(models.Model):
    gambar = models.ImageField(null=True, blank=True)
    kataBuka = RichTextField(null=True, blank=True)
    
    def imageGmb(self):
        try:
            url = self.gambar.url
        except:
            url = ''
        return url

class Register(models.Model):
    email = models.EmailField(max_length=300)
    password = models.CharField(max_length=250)
    confirm_password = models.CharField(max_length=250)
    
    def __str__(self):
        self.email

class Pelayanan(models.Model):
    kataBuka = RichTextField(blank=True,null=True)
    judul =  models.CharField(max_length=200)
    judul2 =  models.CharField(max_length=200)
    judul3 =  models.CharField(max_length=200)
    judul4 =  models.CharField(max_length=200)
    isi = RichTextField(blank=True)
    isi2 = RichTextField(blank=True)
    isi3 = RichTextField(blank=True)
    isi4 = RichTextField(blank=True)

class Harga(models.Model):
    pelayanan = models.ForeignKey(Pelayanan, on_delete=models.SET_NULL, blank=True, null=True)
    kataBuka = RichTextField(blank=True, null=True)
    title = models.CharField(max_length=200, blank=True)
    harga = models.CharField(max_length=200,blank=True,null=True)
        
class Kontak(models.Model):
    nomor_wa = models.CharField(max_length=200)
    kataBuka = RichTextField(blank=True, null=True)
    
    def __str__(self):
        self.nomor_wa

class Metode(models.Model):
    kontak = models.ForeignKey(Kontak, on_delete=models.SET_NULL, blank=True, null=True)
    kataBuka = RichTextField(blank=True, null=True)
    gambar = models.ImageField(null=True, blank=True)
    judul = models.CharField(max_length=200)
    isi = RichTextField(null=True, blank=True)
    
    def imageNya(self):
        try:
            url = self.gambar.url
        except:
            url = ''
        return url
    
class FAQ(models.Model):
    kontak = models.ForeignKey(Harga, on_delete=models.SET_NULL, blank=True, null=True)
    kataBuka = RichTextField(blank=True, null=True)
    judul = models.CharField(max_length=200)
    isi = RichTextField(blank=True, null=True)

class Sponsor(models.Model):
    gambar = models.ImageField(null=True, blank=True)
    
    def imageSpons(self):
        try:
            url = self.gambar.url
        except:
            url = ''
        return url

class lamanAtas(models.Model):
    kataUtama = RichTextField(blank=True, null=True)
    brosur = models.ImageField(blank=True, null=True)
