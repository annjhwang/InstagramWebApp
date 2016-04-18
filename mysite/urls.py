
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('personal.url')),
    url(r'^blog/', include('blog.urls')),
    url(r'^webapp/', include('webapp.urls')),
    
]
