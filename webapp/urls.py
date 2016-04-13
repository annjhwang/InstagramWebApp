from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
# , DetailView
from webapp.models import Image as web
import views

urlpatterns = [ 
                url(r'^$', ListView.as_view(
                                    queryset= web.objects.all(),
                                    template_name="webapp/webapp.html")),
                url(r'^(?P<pk>\d+)$', DetailView.as_view(
                                    model = web,
                                    template_name="webapp/image.html")),
                url(r'^search-form/$', views.search_form),
                url(r'^search-form/search/$', views.search)
            ]