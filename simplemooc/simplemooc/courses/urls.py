from django.conf.urls import url, include
from simplemooc.courses.views import index
# from simplemooc.courses.views import home, contact

urlpatterns = [
    url(r'^$', index, name='index'),
]