# coding: utf-8
'''
Created on 29/03/2017

@author: Diorgeles Dias Lima
'''
from django.db import models

class Usuario_manager(models.Manager):
    
    def InsertUsuario(self, usuario, endereco ):  
        return self.create(usuario=usuario, endereco=endereco)
