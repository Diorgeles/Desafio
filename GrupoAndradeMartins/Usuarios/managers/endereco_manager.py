# coding: utf-8
'''
Created on 29/03/2017

@author: Diorgeles Dias Lima
'''
from django.db import models

class Endereco_manager(models.Manager):
    
    def InsertEndereco(self, rua, numero, distrito, cidade, estado, pais):
        return self.create(rua=rua, numero=numero, distrito=distrito, cidade=cidade, estado=estado, pais=pais)
    
    def VerificaIgualdade(self, rua, numero, distrito, cidade, estado, pais):
        if self.get_query_set().filter(rua__iexact=rua, numero=numero, distrito__iexact=distrito, cidade__iexact=cidade, estado__iexact=estado, pais__iexact=pais).count() > 0:
            return self.get_query_set().get(rua=rua, numero=numero, distrito=distrito, cidade=cidade, estado=estado, pais=pais)    