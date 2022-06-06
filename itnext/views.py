from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import EmailForm, PostCommentForm
from .models import *
# Create your views here.
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.views.generic.edit import FormMixin

class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True


    def get_success_url(self):
        return reverse_lazy('index')

class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)


class Index(LoginRequiredMixin, ListView):
    model = Data
    template_name = 'index.html'
    context_object_name = 'data'
    ads = Advert.objects.all()
    products = Product.objects.all()
    blogs = Blog.objects.filter().order_by('-views')[:3]
    # data = Data.objects.all()
    services = Service.objects.filter().order_by('-orders')[:3]
    service = Service.objects.all()
    extra_context = {
        'ads': ads,
        'products': products,
        'blogs': blogs,
        # 'data': data,
        'services': services,
        'service':service
    }



# def index(request):
#
#     ads = Advert.objects.all()
#     products = Product.objects.all()
#     blogs = Blog.objects.filter().order_by('-views')[:3]
#     data = Data.objects.all()
#     services = Service.objects.filter().order_by('-orders')[:3]
#
#     if request.method == 'POST':
#         if 'email' in request.POST:
#             form = EmailForm(request.POST)
#             mail = request.POST['mail']
#
#     context = {
#         'ads': ads,
#         'products': products,
#         'blogs':blogs,
#         'data': data,
#         'services':services
#     }
#     return render(request, 'index.html', context=context)


class Product_list(LoginRequiredMixin,ListView):
    model = Product
    template_name = 'it_shop.html'
    context_object_name = 'products'


class Product_Detail(LoginRequiredMixin,DetailView):
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

class BlogDetail(LoginRequiredMixin,FormMixin,DetailView):
    model = Blog
    template_name = 'it_blog_detail.html'
    context_object_name = 'blog'
    # def add_comment_to_post(self):
    #     if self.method == 'POST':
    #         form = PostCommentForm(self.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('/')
    form_class = PostCommentForm

    def get_success_url(self):
        return reverse('blog', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(BlogDetail, self).get_context_data(**kwargs)
        context['form'] = PostCommentForm(initial={'post': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(BlogDetail, self).form_valid(form)


class SearchResultsView(LoginRequiredMixin,ListView):
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
    services = Service.objects.filter().order_by('-orders')[:3]
    staff = Staff.objects.all()[:4]
    context = {
        'services': services,
        'staff': staff
    }
    return render(request, 'it_service.html', context=context)

class ServiceList(LoginRequiredMixin,ListView):
    model = Service
    template_name = 'it_service_list.html'
    context_object_name = 'service'

class ServiceDetail(DetailView):
    staff = Staff.objects.all()[:3]
    model = Service
    context_object_name = 'service'
    template_name = 'it_service_detail.html'
    extra_context = {'staff':staff}


def error(request):
    return render(request, 'it_error.html')


def faq(request):
    staff = Staff.objects.all()[:3]
    context = {
        'staff': staff
    }
    return render(request, 'it_faq.html', context=context)


def privacy(request):
    return render(request, 'it_privacy_policy.html')


class BlogView(ListView):
    model = Blog
    template_name = 'blog_by_tag.html'
    context_object_name = 'blogs'


    def get_queryset(self):
        qs = super(BlogView,self).get_queryset()
        # qs.filter(tags__id=int(self.kwargs['tag_id']))
        # return qs
        return qs.filter(tags__id=int(self.kwargs['tag_id']))


class CategoryView(ListView):
    model = Blog
    template_name = 'blog_by_category.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        qs = super(CategoryView, self).get_queryset()
        # qs.filter(tags__id=int(self.kwargs['tag_id']))
        # return qs
        return qs.filter(category__id=int(self.kwargs['category_id']))






