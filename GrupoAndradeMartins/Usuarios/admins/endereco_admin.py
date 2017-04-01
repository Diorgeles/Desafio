# coding: utf-8
'''
Created on 29/03/2017

@author: Diorgeles Dias Lima
''' 
from django.contrib.admin.options import ModelAdmin

class Endereco_admin(ModelAdmin): 
    list_display = ['rua', 'numero', 'distrito', 'cidade', 'estado', 'pais']    
    ordering = ('cidade',)
    search_fields = [ 'rua' , 'cidade', 'estado']
    list_per_page = 25

    class Meta:
        app_label = 'Usuarios'
    
    
