from django.conf.urls import url
from django.contrib.auth import views as auth_views

from simplemooc.accounts.views import (register,
                                       dashboard,
                                       edit,
                                       edit_password,
                                       password_reset,
                                       password_reset_confirm)

urlpatterns = [
    url(r'^$', dashboard, name='dashboard'),
    url(r'^entrar/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^sair/$', auth_views.LogoutView.as_view(next_page='core:home'), name='logout'),
    url(r'^cadastre-se/$', register, name='register'),
    url(r'^nova-senha/$', password_reset, name='password_reset'),
    url(r'^confirmar-nova-senha/(?P<key>\w+)/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^editar/$', edit, name='edit'),
    url(r'^editar-senha/$', edit_password, name='edit_password'),
]