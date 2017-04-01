# coding: utf-8
'''
Created on 29/03/2017

@author: Diorgeles Dias Lima
'''
from django.db import models
from Usuarios.managers.endereco_manager import Endereco_manager

class Endereco(models.Model):
    '''
    Modelo de endereco:
        Nele teremos os detalhes do endereco dos usuários
    '''
    cod_endereco = models.AutoField(primary_key=True)
    rua = models.CharField('rua', max_length=100, null=False, blank=False, unique=False)
    numero = models.CharField(u'número', max_length=20, null=False, blank=False, unique=False)
    distrito = models.CharField('distrito', max_length=100, null=False, blank=False, unique=False)
    cidade = models.CharField('cidade', max_length=20, null=False, blank=False, unique=False)
    estado = models.CharField('estado', max_length=200, null=False, blank=False, unique=False)
    pais = models.CharField(u'país', max_length=50, null=False, blank=False, unique=False)

    objects = Endereco_manager()
    class Meta:
        app_label = u'Usuarios'
        verbose_name = u'Endereço'
        verbose_name_plural = u'Endereços'