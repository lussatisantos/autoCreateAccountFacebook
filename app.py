# importacao de bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from design import linha
from time import sleep

#dados pessoais
linha()
nome = str(input('Digite o seu nome:',))
sobreNome = str(input('Digite o seu sobrenome: '))
telefone = int(input('Digite o seu numero de telefone: '))
linha()

# entrar no facebook
for _ in range(5):
    print('.', end='', flush=True)
    sleep(0.5)
print(' Pronto!')

driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')
sleep(10)

# clicar em novo registro
criar = driver.find_element(By.XPATH, "//a[@class='_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy']")
criar.click()
sleep(10)

# preenchimemto automatico
preencher_nome = driver.find_elements(By.XPATH, "//input[@class='inputtext _58mg _5dba _2ph-']")
preencher_nome = preencher_nome[0]
preencher_nome.send_keys(nome)
sleep(10)
# cadastro
# mostrar os dados para login