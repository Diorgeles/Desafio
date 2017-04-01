# coding: utf-8
'''
Created on 29/03/2017

@author: Diorgeles Dias Lima
'''
from django.db import models
from django.contrib.auth.models import User
from Usuarios.models.endereco import Endereco
from Usuarios.managers.usuario_manager import Usuario_manager
import uuid
from django.utils.datetime_safe import datetime

SEXO = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
)
class Usuario(models.Model):
    '''
    Modelo de Usuario:
        O mesmo usufrui da classe de usuarios que o django tem, com esta classe teremos varios recursos de controle que tornará 
        a aplicação mais robusta. 
        
        o atributo sn_ativo serve para um controle extra do admin da aplicação caso o mesmo deseja desativar o usuario de forma rapida
        basta setar false no campo. 
    '''
    usuario = models.OneToOneField(User, verbose_name=u'Usuário',null=False, blank=False, unique=True)
    cod_usuario = models.CharField(primary_key=True, max_length=30, default=uuid.uuid4, editable=False)
    dt_atualiza = models.DateTimeField(u'Ultima atualização', default=datetime.now(), null=False, blank=False, unique=False)
    endereco = models.ForeignKey(Endereco, null=False, blank=False, unique=False)

    objects = Usuario_manager()
    class Meta:
        app_label = u'Usuarios'
        verbose_name = u'Usuário'
        verbose_name_plural = u'Usuários'  
        
    def nome(self):
        return self.usuario.get_full_name() 
    
    def cidade(self):
        return self.endereco.cidade
    
    def estado(self):
        return self.endereco.estado