from django.conf.urls import url, include
from simplemooc.forum.views import index, thread
# from simplemooc.courses.views import home, contact

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^tag/(?P<tag>[\w_-]+)/$', index, name='index_tagged'),
    url(r'^topico/(?P<slug>[\w_-]+)/$', thread, name='thread'),
]