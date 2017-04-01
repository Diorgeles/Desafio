# coding: utf-8
 
from django.contrib import admin
 
from models import Endereco, Usuario
from admins import Endereco_admin, Usuario_admin
admin.site.register(Usuario, Usuario_admin)
admin.site.register(Endereco, Endereco_admin)