
# todo  import padrao para abrir o navegador junto do keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# ! options é para quando o selenium abre e fecha sozinho
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico, options=options)



# todo declarar funcoes 
def preencher_formulario():
    '''
    Função vai pagar as principais informações para busca do imovel ideal baseado nos criterios
    #? Return vai  ser uma tupla entao para acessar os valore temos que descompactar

    '''
        
    print(60* '-_-_')
    print("Digite sim, nao, indiferente ou valores")
    
    localizacao = input("Localização(bairro):").upper()
    alugar_comprar = input("Alugar ou Comprar:").upper()
    apt_casa_vilagio = input("Casa apt ou cond fechado:").upper()

    qnt_quartos_min = input("Qnt quarto:").upper()
    qnt_quartos_min = int(qnt_quartos_min)

    preco_max = input("Preço max:").upper()
    preco_max = int(preco_max)

    garagem = input("Quantidade Garagem min:").upper()
    garagem = int(garagem)

    banheiro = input("Quantidade banheiros min:").upper()
    banheiro = int(banheiro)

    m2 = input("m2 min:").upper()
    m2 = int(m2)

    return localizacao, alugar_comprar, apt_casa_vilagio, qnt_quartos, preco_max, garagem, m2 

# localizacao, alugar_comprar, apt_casa_vilagio, qnt_quartos, preco_max, garagem, m2 = preencher_formulario()
# print(apt_casa_vilagio)

# todo Código/ chamar função
localizacao, alugar_comprar, apt_casa_vilagio, qnt_quartos, preco_max, garagem, m2 = preencher_formulario


driver.get("https://www.chavesnamao.com.br/imoveis/brasil/") #driver entrar no site chaves nao mao/ imoveis / brasil

# ! class tipoImovel__Container-sc-5e16gv-0
# localizacao
driver.find_element(By.CLASS_NAME, "realInput").send_keys(localizacao)  # apt / casa sobrado / casa em condominio / kitnet studio / cobertura

# percorrer a lista de Tipo de imovel com um loop for e nisso fazer comparações com base no text de cada elemento e seleciona-lo caso condiza com o deejado
elementos = driver.find_elements(By.CLASS_NAME, "tipoImovel__Container-sc-5e16gv-0")
for item in elementos:
    if "Shopping" in item.text:
        item.click()
        break  

driver.find_element()  # faixa de preço   DE:   Ate:
driver.find_element()  # qnt banheiro
driver.find_element()  # area util   Min:   Max:
