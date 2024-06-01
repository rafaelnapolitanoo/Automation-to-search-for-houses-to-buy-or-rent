# Automation to search for houses to buy or rent
 
<<<<<<< HEAD
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
=======
O intuito da aplicação é agilizar minha rotina, estou buscando casas para alugar/comprar em outra cidade porque irei me mudar, mas não tenho tempo o suficiente para encontrar a casa ideal que atenda minhas espectativas 

Então iniciei o projeto criando uma função que recebe os valores desejados (oriundos de inputs) e preenche os campos de formulário com os dados recebidos (formulário dos sites chaves na mão e quinto andar) assim facilita a busca e aplica os filtros desejados de área min, qnt quartos, banheiros, garagens, localização.

Durante a busca utilizei um Xparh que pega os 7 primeiros itens correspondentes aos filtros retornando uma lista com uma pequena descrição e o link dos  anúncios.



The purpose of the application is to streamline my routine. I'm searching for houses to rent/buy in another city because I'm moving, but I don't have enough time to find the ideal house that meets my expectations.

So I started the project by creating a function that receives desired values (from inputs) and fills out form fields with the received data (forms from 'chaves na mão' and 'quinto andar' websites), making the search easier and applying desired filters like minimum area, number of rooms, bathrooms, garages, and location.

During the search, I used an XPath that fetches the first 7 items corresponding to the filters, returning a list with a brief description and the link to the advertisements.
>>>>>>> 16ceda4ff5f19cfba43f155445de15a5eb8d615c
