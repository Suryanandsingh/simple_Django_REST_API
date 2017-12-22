from django.conf.urls import url
from django.contrib import admin
from webs import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^web/$', views.WebApi.as_view()),
    url(r'^web/(?P<pk>[0-9]+)/$', views.WebApiDetails.as_view(), name='details'),
    url(r'^web/login/$', views.Login),
]
urlpatterns = format_suffix_patterns(urlpatterns)
