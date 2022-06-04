from django.shortcuts import render

from .forms import EmailForm
from .models import *
# Create your views here.
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView



def index(request):
    ads = Advert.objects.all()
    products = Product.objects.all()
    blogs = Blog.objects.all()[::-1][:3]
    if request.method == 'POST':
        if 'email' in request.POST:
            form = EmailForm(request.POST)
            mail = request.POST['mail']
    context = {
        'ads': ads,
        'products': products,
        'blogs':blogs
    }
    return render(request, 'index.html', context= context)


class Product_list(ListView):
    model = Product
    template_name = 'it_shop.html'
    context_object_name = 'products'


class Product_Detail(DetailView):
    model = Product
    template_name = 'it_shop_detail.html'


def about(request):
    staff = Staff.objects.all()[:4]
    context = {
        'staff': staff
    }
    return render(request, 'it_about.html', context=context)


def blog_list(request):
    blogs = Blog.objects.all()[::-1]#[:3]
    blog_paginator = Paginator(blogs, 3)
    page_num = request.GET.get('page')
    page = blog_paginator.get_page(page_num)
    context = {
        'page': page,
        'count':blog_paginator.count
    }
    return render(request, 'it_blog.html', context=context)

class BlogDetail(DetailView):
    model = Blog
    template_name = 'it_blog_detail.html'
    context_object_name = 'blog'


class SearchResultsView(ListView):
    model = Blog
    template_name = 'search.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Blog.objects.filter(Q(title__icontains=query))

        if list(object_list) == []:
            object_list = 0
        return object_list


def blog_grid(request):
    blogs = Blog.objects.all()
    blog_paginator = Paginator(blogs, 3)
    page_num = request.GET.get('page')
    page = blog_paginator.get_page(page_num)
    context = {
        'page': page,
        'count': blog_paginator.count
    }
    return render(request, 'it_blog_grid.html', context=context)


def service(request):
    services = Service.objects.all()
    staff = Staff.objects.all()[:4]
    context = {
        'services': services,
        'staff': staff
    }
    return render(request, 'it_service.html', context=context)




