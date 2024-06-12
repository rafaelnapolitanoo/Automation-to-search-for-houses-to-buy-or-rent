import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def tratar_link(link):
    #?qnt quartos 
    numero_de_quartos = link[62: 71]
    numero_de_quartos = numero_de_quartos.replace("-", "  ")

    #? buscar o trecho entre "sul-" e "/id" // output vai ser bairro m2 e Valor
    posicao_bairro = link.index('sul-') # encontra o indice/onde esta o sul- dentro do link 
    posicao_id = link.index('/id') # acha o inicio do id em indice
    informacoes_link = link[posicao_bairro+4: posicao_id] # pega entre as duas posicoes

    lista_bairro_m2_precoRS = informacoes_link.replace("RS", "R$")
    lista_bairro_m2_preco_final = lista_bairro_m2_precoRS.replace("-", "  ")
    
    texto_do_link = f"{numero_de_quartos}  {lista_bairro_m2_preco_final}"
    return texto_do_link

def executar_script():
    # Obter valores dos campos de entrada
    localizacao = entrada_localizacao.get()
    qnt_quartos_min = int(entrada_quartos.get())
    preco_max = int(entrada_preco.get())
    alugar_comprar = var_tipo.get()
    apt_casa_vilagio = var_tipo_imovel.get()
    garagem = int(entrada_garagem.get())
    m2 = int(entrada_m2.get())
    
    # Verificar se todos os campos foram preenchidos
    if not localizacao or not qnt_quartos_min or not preco_max or not alugar_comprar or not apt_casa_vilagio or not garagem or not m2:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return
    
    # Configurar o Selenium para manter o navegador aberto
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    
    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico, options=options)
    driver.get("https://www.chavesnamao.com.br/imoveis/brasil/")
    time.sleep(3)

    # Mandar localização
    campo_localizacao = driver.find_element(By.CLASS_NAME, "realInput")
    campo_localizacao.send_keys(localizacao)
    time.sleep(1)
    campo_localizacao.send_keys(Keys.ENTER)
    
    # Selecionar alugar ou comprar
    if alugar_comprar == "ALUGAR":
        driver.find_element(By.XPATH, '//*[@id="filtros"]/aside/div/div[2]/ul[1]/li[2]').click()
        time.sleep(1)
    elif alugar_comprar == "COMPRAR":
        driver.find_element(By.XPATH, '//*[@id="filtros"]/aside/div/div[2]/ul[1]/li[1]').click()
        time.sleep(1)

    # Esperar o botão de aceitar cookies aparecer
    while len(driver.find_elements(By.XPATH, '//*[@id="__next"]/div/button')) < 1:
        time.sleep(1)
    
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/button').click()

    # Selecionar tipo de imóvel
    if apt_casa_vilagio == "APARTAMENTO":
        driver.find_element(By.ID, "ti-1").click()
        time.sleep(1)

    # Selecionar quantidade de quartos
    numero_quartos = f"quartos{qnt_quartos_min}"
    driver.find_element(By.ID, numero_quartos).click()    
    time.sleep(1)

    # Definir preço máximo
    campo_preco_max = driver.find_element(By.ID, "maxPrice")
    campo_preco_max.send_keys(preco_max)
    campo_preco_max.send_keys(Keys.ENTER) 
    time.sleep(1)

    # Selecionar quantidade de garagens
    numero_garagens = f"garagem{garagem}"
    driver.find_element(By.ID, numero_garagens).click()    
    time.sleep(1)

    # Selecionar quantidade de banheiros
    numero_banheiros = f"banheiros{qnt_quartos_min}"
    driver.find_element(By.ID, numero_banheiros).click()    
    time.sleep(1)

    # Definir área mínima em m²
    campo_m2 = driver.find_element(By.ID, "areaMin")
    campo_m2.send_keys(m2)
    campo_m2.send_keys(Keys.ENTER) 
    time.sleep(1)

    # Pegar todos os links dos anúncios
    lista_anuncios = driver.find_elements(By.CLASS_NAME, 'containerSlider ')
    lista_links = []
    for anuncio in lista_anuncios:

        # todo pegar o link
        link_anuncio = anuncio.get_attribute('href')
        
        # todo retirar os textos do link
        textos_do_link = tratar_link(link_anuncio)

        #todo add texto e link
        lista_links.append(textos_do_link)
        lista_links.append(link_anuncio)
    
    time.sleep(2)



    # Exibir os links na Listbox
    for item in lista_links:
        lista_resultados.insert(tk.END, item)

    driver.quit





janela = tk.Tk()
janela.title("Formulário de Pesquisa de Imóveis")
fonte = ("Helvetica", 12) # ! alterar depois nao esta plicado ainda
# Configurar cor de fundo da janela
janela.configure(bg="#000000")


# Criar widgets
tk.Label(janela, text="Localização:", bg="#000000", fg="white").grid(row=0, column=0)
entrada_localizacao = tk.Entry(janela, bg="#333333", fg="white")
entrada_localizacao.grid(row=0, column=1)

tk.Label(janela, text="Quantidade de Quartos:", bg="#000000", fg="white").grid(row=1, column=0)
entrada_quartos = tk.Entry(janela, bg="#333333", fg="white")
entrada_quartos.grid(row=1, column=1)

tk.Label(janela, text="Preço Máximo:", bg="#000000", fg="white").grid(row=2, column=0)
entrada_preco = tk.Entry(janela, bg="#333333", fg="white")
entrada_preco.grid(row=2, column=1)

tk.Label(janela, text="Tipo (Alugar/Comprar):", bg="#000000", fg="white").grid(row=3, column=0)
var_tipo = tk.StringVar(value="ALUGAR")
tk.Radiobutton(janela, text="Alugar", variable=var_tipo, value="ALUGAR", bg="#000000", fg="white", selectcolor="#333333").grid(row=3, column=1)
tk.Radiobutton(janela, text="Comprar", variable=var_tipo, value="COMPRAR", bg="#000000", fg="white", selectcolor="#333333").grid(row=3, column=2)

tk.Label(janela, text="Tipo de Imóvel:", bg="#000000", fg="white").grid(row=4, column=0)
var_tipo_imovel = tk.StringVar(value="APARTAMENTO")
tk.Radiobutton(janela, text="Apartamento", variable=var_tipo_imovel, value="APARTAMENTO", bg="#000000", fg="white", selectcolor="#333333").grid(row=4, column=1)
tk.Radiobutton(janela, text="Casa", variable=var_tipo_imovel, value="CASA", bg="#000000", fg="white", selectcolor="#333333").grid(row=4, column=2)

tk.Label(janela, text="Quantidade de Garagens:", bg="#000000", fg="white").grid(row=5, column=0)
entrada_garagem = tk.Entry(janela, bg="#333333", fg="white")
entrada_garagem.grid(row=5, column=1)

tk.Label(janela, text="Área Mínima (m²):", bg="#000000", fg="white").grid(row=6, column=0)
entrada_m2 = tk.Entry(janela, bg="#333333", fg="white")
entrada_m2.grid(row=6, column=1)

tk.Button(janela, text="Buscar Imóveis", command=executar_script, bg="#000000", fg="white").grid(row=7, column=0, columnspan=3)

# Listbox para exibir os resultados
lista_resultados = tk.Listbox(janela, bg="#333333", fg="white", width=200, height=40)
lista_resultados.grid(row=8, column=0, columnspan=4, pady=10)

janela.mainloop()
