# Desafio
Vaga de desenvolvedor
 
# Descrição
API para criação e edição de usuários.
 
# Instruções
 
A API se divide em 3 fases, cadastro do usuário, login do usuário, e de extra, edição básica dos dados do usuário.
 
Escrita em:
  * Python 2.7
  * Django 1.6.5
  * REST framework 3.0.0
  
Observação: Apesar das versões utilizadas neste desafio serem antigas, boa parte do código poderá ser reaproveitado nas versões mais atuais.
 
# 1- Cadastro
 
Segue abaixo o modelo do json que deve ser enviado no momento do cadastro.
 
```json
{
	"admin": "False",
	"name": "seu nome",
	"username": "username",
	"email": "seuemail@email.com",
	"password": "suaSenha",
	"address": [
	  {
		  "street": "rua",
		  "number": "10",
		  "distric": "centro",
		  "city": "cidade",
		  "state": "estado",
		  "country": "país"
	  }
	]
}
```

Usaremos a tabela de usuários que é gerada pelo django, precisaremos passar a key “username” para que o usuário criado esteja devidamente cadastrado na base.

Teremos dois tipos de usuários:
* Usuário admin, que tem acesso ao Admin do django
* Usuário simples, com acesso somente a API


Para criar o usuário admin basta colocar a key “admin” e seu valor True, como mostrado abaixo:

```json
{
	"admin": "True",
	"name": "seu nome",
	"username": "username",
	"email": "seuemail@email.com",
	"password": "suaSenha",
	"address": [
	  {
		  "street": "rua",
		  "number": "10",
		  "distric": "centro",
		  "city": "cidade",
		  "state": "estado",
		  "country": "país"
	  }
	]
}
```

Após cadastrado, a API retornará o TOKEN de acesso junto ao ID do usuário criado, exemplo abaixo:

```json
{
	"token": "000000000000000000000000000", 
	"last_login": "2017-03-31T01:27:46.668Z", 
	"id": "00000000000000000000000000", 
	"modified": "2017-03-31T01:25:30.087Z", 
	"created": "2017-03-31T01:27:46.668Z"
}
```

# 2- Login

O login será por email e senha, exemplo abaixo:

```json
{
	"email": " seuemail@email.com ",
	"password": "suaSenha"
}
```

Para acessar ao perfil de usuário basta passar o ID e o Token, exemplo abaixo:

```json
{
	"token": "00000000000000000000000", 
	"id": "00000000000000000000000000"
}
```

# 3- Editar Usuário
		
Para editar os dados de um usuário será necessário passar o email e senha ou token e ID junto aos dados que deseja alterar, exemplos abaixo:

* Observação: É possível, somente, editar o endereço e o nome do usuário. Ao enviar o json, é necessário enviar o endereço completo, pois no ato da criação do endereço a API se encarrega de verificar se já existe um igual ao informado, caso sim, não será criado um novo. Assim, diminui- se a probabilidade de duplicidade na base de dados. 

```json
{
	"email": " seuemail@email.com ",
	"password": "suaSenha",
        
	"name": "José Soares",
	"street": "rua abc",
	"number": "210",
	"distric": "centro",
	"city": "Belo Horizonte",
	"state": "MG",
	"country": "Brasil"
    }
```

Ou 

```json
{
	"token": "00000000000000000000000", 
	"id": "00000000000000000000000000", 
	
	"name": "José Soares",
	"street": "rua abc",
	"number": "210",
	"distric": "centro",
	"city": "Belo Horizonte",
	"state": "MG",
	"country": "Brasil"
}
```

