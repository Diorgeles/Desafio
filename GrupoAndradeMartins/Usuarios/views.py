# coding: utf-8
'''
Created on 29/03/2017

@author: Diorgeles Dias Lima
'''
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Usuarios.models.usuario import Usuario
from django.contrib.auth.models import User
from Usuarios.models.endereco import Endereco
from rest_framework.authtoken.models import Token
from django.db.models import Q

@api_view(['GET', 'POST'])
def novo_usuario(request):
    '''
    Cria usuário e retorna os dados de acesso a API
    '''    
    dadosUser = []    
    if request.method == 'POST':    
        nome = request.data['name'] 
        # Como preciso criar um username para criar o user django então eu aproveito o nome escrito, deixo todo minusculo e retiro os espaços
        username = request.data['username'] 
        password = request.data['password'] 
        email = request.data['email'] 
        for i in request.data['address']:            
            rua = i['street'] 
            numero = i['number'] 
            cidade = i['city'] 
            estado = i['state'] 
            distrito = i['distric'] 
            pais = i['country']   
        
        # Verificacao de email ja existente
        if len(User.objects.filter(email=email)):
            return Response({'erro':'E-mail já existente'})
        
        # Verificacao de username ja existente
        if User.objects.filter(username=username):            
            return Response({'erro':'Username já existente'})  
        
        elif not len(User.objects.filter(Q(username=username) | Q(email=email))):
            # Verifico se existe endereço igual a este, caso sim, eu aproveito o dado e diminuo a duplicidade do banco
            endereco = Endereco.objects.VerificaIgualdade(rua, numero, distrito, cidade, estado, pais)
            if not endereco: # Não existindo endereço igual, eu crio o endereço com os dados passados
                endereco = Endereco.objects.InsertEndereco(rua, numero, distrito, cidade, estado, pais)               
            
            loginUser = User.objects.create_superuser(username, email, password) if request.data['admin'] == 'True' else User.objects.create_user(username, email, password)
            loginUser.first_name = nome
            loginUser.save()
            
            # Campos extra ao usuario do django 
            Usuario.objects.InsertUsuario(loginUser, endereco) 
            
            # Token do usuário  
            token = Token.objects.create(user=loginUser)
          
            for i in Usuario.objects.filter(usuario=loginUser):                    
                dadosUser.append({'id': i.cod_usuario, 'created':i.usuario.date_joined, 'modified': i.dt_atualiza, 'last_login':i.usuario.last_login, 'token':str(token)})
    return Response(dadosUser)

# Funcao auxiliar que se encarrega de fazer a atualizacao dos dados do usuario
def atualizaDados(usuario, nome, rua, numero, cidade, estado, distrito, pais):
    # Verifico se existe endereço igual a este, caso sim, eu aproveito o dado e diminuo a duplicidade do banco
    endereco = Endereco.objects.VerificaIgualdade(rua, numero, distrito, cidade, estado, pais)
    if not endereco:
        endereco = Endereco.objects.InsertEndereco(rua, numero, distrito, cidade, estado, pais)
    user = User.objects.get(username=usuario)
    user.first_name=nome
    user.save()    
    return True

@api_view(['GET', 'POST'])
def edite_usuario(request):
    '''
        Função extra responsavel pela edição das informações basicas dos usuários
    '''  
    dadosUser = '' 
    if request.method == 'POST':
        dadosUser = {'nome': request.data['name'], "address": [{"street": request.data['street'],
                                                            "number": request.data['number'], "distric": request.data['distric'],
                                                            "city": request.data['city'], "state": request.data['state'],"country": request.data['country']}]}
        if 'email' in request.data:
            erroLogin = {'erro': u'Usuário e/ou senha inválidos'}
            email = request.data['email']
            password = request.data['password']
                        
            if not User.objects.filter(email=email):  # Se email incorreto
                return Response(erroLogin)
            elif not User.objects.get(email=email).check_password(password):  # Se email correto porem senha incorreta
                return Response(erroLogin)
            else:
                user = User.objects.get(email=email)
                if atualizaDados(user.username, request.data['name'], request.data['street'],
                               request.data['number'], request.data['city'], request.data['state'],
                               request.data['distric'], request.data['country']):
                    return Response(dadosUser)
                    
        
        elif 'token' in request.data:
            erroToken = {'erro': u'Não autorizado'}
            token = request.data['token']
            id = request.data['id']
            
            if not Token.objects.filter(key=token):  # Se token nao existe
                return Response(erroToken)
            elif not Usuario.objects.filter(cod_usuario=id):  # Se id nao existe
                return Response(erroToken)
            else:                  
                user = Usuario.objects.get(cod_usuario=id)   
                if not Token.objects.filter(key=token, user=user.usuario):  # Verificacao de Token e Id
                    return Response(erroToken)
                else: 
                    if atualizaDados(user.usuario.username, request.data['name'], request.data['street'], 
                                  request.data['number'], request.data['city'], request.data['state'], 
                                  request.data['distric'], request.data['country']):                        
                        return Response(dadosUser)
                    
    return Response()

@api_view(['GET', 'POST'])
def login(request):
    '''
        Função responsavel pelo login       
    '''
    dadosUser = [] 
    if request.method == 'POST':
        # Login por email e senha 
        if 'email' in request.data:
            erroLogin = {'erro': u'Usuário e/ou senha inválidos'}
            email = request.data['email']
            password = request.data['password']
                        
            if not User.objects.filter(email=email):  # Se email incorreto
                return Response(erroLogin)
            elif not User.objects.get(email=email).check_password(password):  # Se email correto porem senha incorreta
                return Response(erroLogin)
            else:
                user = User.objects.get(email=email)
                token = Token.objects.get(user=user)
                for i in Usuario.objects.filter(usuario=user):                        
                    dadosUser.append({'id': i.cod_usuario, 'created':i.usuario.date_joined, 'modified': i.dt_atualiza, 'last_login':i.usuario.last_login, 'token':str(token)})
                    
        # Login por Id e Token
        elif 'token' in request.data:
            erroToken = {'erro': u'Não autorizado'}
            token = request.data['token']
            id = request.data['id']
            
            if not Token.objects.filter(key=token):  # Se token nao existe
                return Response(erroToken)
            elif not Usuario.objects.filter(cod_usuario=id):  # Se id nao existe
                return Response(erroToken)
            else:                  
                user = Usuario.objects.get(cod_usuario=id)   
                if not Token.objects.filter(key=token, user=user.usuario):  # Verificacao de Token e Id
                    return Response(erroToken)
                else:                    
                    token = Token.objects.get(key=token)
                    for i in Usuario.objects.filter(cod_usuario=id):                        
                        dadosUser.append({'id': i.cod_usuario, 'created':i.usuario.date_joined, 'modified': i.dt_atualiza, 'last_login':i.usuario.last_login, 'token':str(token)})
    return Response(dadosUser)
