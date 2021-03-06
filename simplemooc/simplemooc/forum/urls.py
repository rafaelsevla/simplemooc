from django.conf.urls import url, include
from simplemooc.forum.views import index, thread, reply_correct, reply_incorrect
# from simplemooc.courses.views import home, contact

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^tag/(?P<tag>[\w_-]+)/$', index, name='index_tagged'),
    url(r'^respostas/(?P<pk>\d+)/correta/$', reply_correct, name='reply_correct'),
    url(r'^respostas/(?P<pk>\d+)/incorreta/$', reply_incorrect, name='reply_incorrect'),
    url(r'^topico/(?P<slug>[\w_-]+)/$', thread, name='thread'),
]