# todo  import padrao para abrir o navegador junto do keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# ! options é para quando o selenium abre e fecha sozinho
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico, options=options)



# todo declarar funcoes 
def preencher_formulario(driver):
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

    m2 = input("m2 min:").upper()
    m2 = int(m2)

    
    # driver entrar no site chaves nao mao/ imoveis / brasil
    driver.get("https://www.chavesnamao.com.br/imoveis/brasil/") 
    time.sleep(6)

    # Tentar fechar a barra de consentimento, se ela aparecer
    try:
        consent_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "lgpdBar__button"))
        )
        consent_button.click()
        time.sleep(2)
    except Exception as e:
        print("Barra de consentimento não encontrada ou já fechada")

    # mandar localizacao  /// dessa maneira para poder enviar a informação por completa e apos selecionar a cidade desejada
    campo_localizacao = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "realInput"))
    )
    campo_localizacao.send_keys(localizacao)
    time.sleep(1)
    campo_localizacao.send_keys(Keys.ENTER) 


    #! arvore de condicoes TESTES
    # # bloco 2 ---- Comprar / alugar / imoveis novos
    if alugar_comprar == "ALUGAR":
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="filtros"]/aside/div/div[2]/ul[1]/li[2]'))
        ).click()
        time.sleep(1)
    elif alugar_comprar == "COMPRAR":
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="filtros"]/aside/div/div[2]/ul[1]/li[1]'))
        ).click()
        time.sleep(1)


    # # bloco 3 ---- Apartamento / Casas e sobrados / Casa em condominio / Kitnet studio / Loft / Cobertura ...
    if apt_casa_vilagio == "APARTAMENTO":
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "ti-1"))
        ).click()
        time.sleep(1)


    # quantidade quartos min
    numero_quartos = f"quartos{qnt_quartos_min}"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, numero_quartos))
    ).click()
    time.sleep(1)


    # faixa de preço max
    driver.find_element(By.ID, "maxPrice").send_keys(preco_max)
    time.sleep(1)

    # quantidade banheiro 
    
    # quantidade garagem

    # qunatidade banheiro

    # area util

    return localizacao, alugar_comprar, apt_casa_vilagio, qnt_quartos_min, preco_max, garagem, m2 



# todo Código/ chamar função
localizacao, alugar_comprar, apt_casa_vilagio, qnt_quartos_min, preco_max, garagem, m2 = preencher_formulario(driver)
