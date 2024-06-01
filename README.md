# Automation to search for houses to buy or rent
 
ideia: fazer um for por cador bloco de informaçoes e selecionar por meio de info de pequenas diferenças

30/05
xpath a mao dos itens <li>

qunatidade de quartos tem o id =  "quartos{numquartosmin}" CONSEGUII

amanha resolver o problema dos elemntos clicaveis (botao de cookies entendi ==  class = "body2__Paragraph-xstna9-0") o problema é esse botao mesmo, nao o de notificacao

## contexto gpt:
preciso que o codigo espere ate o elemento da ultima linha de codigo apareça para que ele clique no botao de cookies e assim permita a funcao posterior roda

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# ! options é para quando o selenium abre e fecha sozinho
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico, options=options)
driver.get("https://www.chavesnamao.com.br/imoveis/brasil/") 
time.sleep(6)
driver.find_element(By.CLASS_NAME, "body2__Paragraph-xstna9-0").click()