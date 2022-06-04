from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})



class Tag(models.Model):
    tag = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={"slug": self.slug})


class Blog(models.Model):
    TOPICS = (('Marketting', 'Marketting'), ('Economics', 'Economics'))
    # author = models.ForeignKey(User, on_delete= models.CASCADE)
    image = models.ImageField(upload_to='image/blogs/', blank=True)
    title = models.CharField(max_length=100, blank=True)
    topic = models.CharField(max_length=100, choices=TOPICS, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True)
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    tags = models.ManyToManyField(Tag,blank=True ,related_name='blogs')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='blogs')


    def __str__(self):
        return self.title


class Product(models.Model):
    image = models.ImageField(upload_to='products/', blank=True)
    name = models.CharField(max_length=50, blank=True)
    price = models.IntegerField(blank=True)
    description = models.TextField(blank=True)

    # review = models.ManyToOneRel()
    def get_absolute_url(self):
        return self.pk#"", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Service(models.Model):
    image = models.ImageField(upload_to='image/services/')
    name = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    orders = models.IntegerField(default=0,verbose_name='order')

    def __str__(self):
        return self.name


class Staff(models.Model):
    image = models.ImageField(upload_to='image/staff/', blank=True)
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    url = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    number = models.CharField(max_length=10, blank=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name





class Advert(models.Model):
    image = models.ImageField(upload_to='ads/')
    title = models.CharField(max_length=40)





# forms
class PostComment(models.Model):
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=10, blank=True)
    password = models.CharField(max_length=30, blank=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.email


class Email(models.Model):
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.email


class Data(models.Model):
    CHOICES = [('Happy Customers','Happy Customers'),('Repaired Laptops','Repaired Laptops'),('Repaired Computers','Repaired Computers'),('OS INSTALLED','OS INSTALLED')]
    name = models.CharField(blank=True, max_length=100, choices=CHOICES)
    quantity = models.IntegerField(blank=True)
    logo = models.FileField(upload_to='logo/')
    def __str__(self):
        return self.name

