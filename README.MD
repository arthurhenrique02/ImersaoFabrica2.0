# ImersãoFábrica2.0

## Prontuário

### Descrição

##### Projeto criado em Python/django e django rest para o Projeto Final da Imersão da Fábrica de Software 2023.1 (UNIPE)
##### O projeto busca criar uma simples API que pega dados de um Pacientes, Médicos e Acompanhantes para serem consumidos


### Tecnologias usadas

##### Python
##### Django e Django Rest framework
##### CSS/HTML/JS (com bootstrap)
##### PostgreSQL

### Como Utilizar

####   Primeiro passo: 
* #####      Criar um ambiente virtual. Comando: pyhon -m venv venv
####  Segundo passo:
* #####     Ativar o ambiente virutal. Comandos: (windows) venv\Scripts\activate (linux/mac) source bin/activate
####    Terceiro passo:
* #####      Instalar requirements.txt. Comando: pip install -r .\requirements.txt
####    Quarto passo:
* #####       Rodar o servidor. Comando: python manage.py runserver
* ##### Caso não funcione, criar um banco de dados no PgAdmin 4 (programa para banco de dados) chamado prontuarioDB (ou trocar para um DB de sua escolha)

### Após instalação dos arquivos necessários
#### Para entrar na url raiz do programa ("/") é necessário criar um usuário e senha. Crie-o com o comando python manage.py createsuperuser

### Como acessar a API?
#### As APIs estão nas url: 
* #####  /acompanhantes
* #####  /medicos
* #####  /pacientes

### Sobre a API
#### Nas URLS pode-se fazer o get, post, o put/patch e delete.
#### Para o put/patch, ou delete, ou para selecionar apenas um dado JSON, é necessário apenas o id do dado que deseja fazer a operação (por exemplo: pacientes/1/ (é necessário a / ao final))
#### Para forms, é necessário adicionar o metodo que deseja.
#### Há uma paginação para cada app que retorna apenas 3 dados JSON por pagina, caso queria acessar mais arquivos em uma página, basta adicionar "?limit=(quantidade que deseja)", sem as aspas.
#### A conexão feita com o DB é do próprio django, campos que não relacionados (exceto o paciente_acompanhado, do app acompanhantes) podem ser nulos, inicialmente, dando a entender que quando o Paciente for atendido, a API deve ser atualizada.
#### Arquivos JSON para inserção de novos dados:
* ##### Acompanhantes:
###### { "nome": "", "sobrenome": "", "paciente_acompanhado": null }
* ##### Pacientes:
###### {"nome": "", "sobrenome": "", "idade": null, "sexo": "", "alergias": "", "tipo_sangue": "", "data_hora_entrada": null, "data_hora_saida": null, "medico": null}
* ##### Médicos:
 ###### {"nome": "", "sobrenome": "", "crm": "", "area_atuacao": ""}

### Sobre a home
#### Foi utilizado Boostrap apenas para fazer uma barra de navegação, que, ao clicar no elementos, redireciona para a url correspondente


###### OBS: projetos dos dias anterioes ao final estão na branch develop
