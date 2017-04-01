# coding: utf-8
'''
Created on 29/03/2017

@author: Diorgeles Dias Lima
'''   
from django.contrib.admin.options import ModelAdmin

class Usuario_admin(ModelAdmin ): 
    list_display = ['cod_usuario','nome','cidade','estado','dt_atualiza']
    ordering = ( 'usuario__first_name',)
    search_fields = [ 'usuario__first_name' ,'endereco__cidade']
    list_per_page = 25

    class Meta:
        app_label = 'Usuarios'
    
    