'''
Created on 29/03/2017

@author: Diorgeles Dias Lima
'''
from django.conf.urls import url
from . import views

urlpatterns = [url(r'^api/cadastro/user/$', views.novo_usuario),
               url(r'^api/login/$', views.login),
               url(r'^api/edite/user/$', views.edite_usuario)               
              ]
