from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
# , DetailView
from webapp.models import Image as web
import views

urlpatterns = [ 
                url(r'^search-form/$', views.search_form),
                url(r'^search-form/search/$', views.search),
                url(r'^search-form/search/entry_index/$', views.entry_index),
            ]

