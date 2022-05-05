# projeto01-cadastro-imobiliaria

Esse projeto busca criar um sistema de cadastro para uma imobiliária fictícia. 

# Introdução

Apresentar esse sistema de cadastro é uma forma de exercitar conhecimentos de python, SQL e do paradigma de orientação a objeto que são tão comuns na área de engenharia de dados

# Objetivos

Simular a funcionalidade de cadastro de uma imobiliária fictícia

# Tecnologias e ferramentas
* Python
* SQL
 
# Resolução

1. Criação das classes que serão usadas para cadastro
    > Escolhi usar POO para que pudesse realizar todos os tipos de tratamento dos dados de entrada dentro de uma classe e que enventuais manutenções ficassem isoladas. [Modules](http://www.google.fr/ "Script")

2. Criação das tabelas no MySQL workbench.
    [SQL cript](sql_scripts/create_table.sql "Script")

3. Criação da classe conectora python-MySQL workbench
    [InterageDB](modules/InterageDB.py "Script")

4. Criação da classe Cadastro
    > Onde foi implementado o menu de interação com o usuário. 
        [Cadastro](modules/Cadastro.py "Script")

5. Criação de script para ingestão de dados de fonte CSV.
    > Nessa parte foi necessário fazer tratamento de dados uma vez que foram encontrados duplicados de chaves primárias nos arquivos gerados com o mokcaroo. Para resolver isso funções de tratamento foram criadas 
    * [Pastas CSV](csv_data "Script")     
    * [Popula bancos](popula_bancos.py "Script") 
    * [Functions](functions "Script")
6. Criação de menu

# Conclusão e trabalhos futuros

O programa se mostra funcional e cumpre seu papel como excercício. Ao longo do processo algumas ideias de funcionalidades e expansões surgiram como:

* Fazer tratamento de possíveis erros de digitação do usuário.

* Dockerizar a solução e o banco de dados e subir num cluster de k8s

* Criar uma interface web com streamlit e subir no GCP (cloud RUN, cloud function)

* Implementar funções de busca na base de dados