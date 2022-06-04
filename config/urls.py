from django.contrib import admin
from django.urls import path
from itnext.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('products/', Product_list.as_view(), name='it_shop'),
    path('products/<int:pk>/', Product_Detail.as_view(), name='product'),
    path('about/', about, name='about'),
    path('blogs/',blog_list, name='blog_list'),
    path('blogs/<int:pk>/',BlogDetail.as_view(),name='blog'),
    path('search/',SearchResultsView.as_view(),name = 'search'),
    path('blog_grid/', blog_grid, name ='blog_grid'),
    path('service/', service, name = 'service'),
    path('service/<int:pk>/', ServiceDetail.as_view(),name='service_detail'),
    path('service_list/',ServiceList.as_view(),name='service_list')
    # path('service_list/', )
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

