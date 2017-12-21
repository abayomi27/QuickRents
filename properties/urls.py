from django.urls import path,re_path
from properties import views


urlpatterns = [
    path('', views.homepage, name='apartment_list'),
    re_path('apartment/(?P<pk>\d+)/$', views.apartment_detail, name='apartment_detail'),
]
