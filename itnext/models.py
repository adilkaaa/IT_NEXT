from django.db import models


# Create your models here.


class Blog(models.Model):
    TOPICS = (('Marketting', 'Marketting'), ('Economics', 'Economics'))
    # TAGS = ()
    image = models.ImageField(upload_to='image/blogs/', blank=True)
    title = models.CharField(max_length=100, blank=True)
    topic = models.CharField(max_length=100, choices=TOPICS, blank=True)
    # comments = models.ForeignKey()
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True)

    # tags = models.CharField(max_length=100, choices=TAGS)

    def __str__(self):
        return self.title


class Product(models.Model):
    image = models.ImageField(upload_to='products/', blank=True)
    name = models.CharField(max_length=50, blank=True)
    price = models.IntegerField(blank=True)
    description = models.TextField(blank=True)

    # review = models.ManyToOneRel()

    def __str__(self):
        return self.name


class Service(models.Model):
    image = models.ImageField(upload_to='image/services/')
    name = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)

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


class Category(models.Model):
    pass


# class Comment(models.Model):
#     name = models.CharField(max_length=100, blank=True)
#     date = models.DateTimeField(auto_now_add=True)
#     comment = models.TextField(blank=True)

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

