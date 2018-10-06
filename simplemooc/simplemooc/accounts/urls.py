from django.conf.urls import url
from django.contrib.auth import views as auth_views

from simplemooc.accounts.views import register

urlpatterns = [
    url(r'^entrar/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^cadastro/$', register, name='register')
]
