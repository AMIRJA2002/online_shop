from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('product_list/', views.product_list, name='product_list'),
    path('about/', views.about_us, name='about_us'),
    path('contact/', views.contact_us, name='contact_us'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
