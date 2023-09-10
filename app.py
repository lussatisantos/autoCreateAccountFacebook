# importacao de bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

#dados pessoais
nome = str(input('Digite o seu nome: '))
sobreNome = str(input('Digite o seu sobrenome: '))
telefone = int(input('Digite o seu numero de telefone: '))

# entrar no facebook
print ('Iniciando...')
# clicar em novo registro
# dados manuais via script
# preenchimemto automatico
# cadastro
# mostrar os dados para login