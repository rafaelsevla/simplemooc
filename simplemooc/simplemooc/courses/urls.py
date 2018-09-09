from django.conf.urls import url, include
from simplemooc.courses.views import index, details
# from simplemooc.courses.views import home, contact

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^(?P<pk>\d+)/$', details, name='details'),
]