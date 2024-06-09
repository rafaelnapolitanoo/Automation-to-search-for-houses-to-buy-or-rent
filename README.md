# Automation to search for houses to buy or rent
 
<<<<<<< HEAD
ideia: fazer um for por cador bloco de informaçoes e selecionar por meio de info de pequenas diferenças

30/05
xpath a mao dos itens <li>

qunatidade de quartos tem o id =  "quartos{numquartosmin}" CONSEGUII

amanha resolver o problema dos elemntos clicaveis (botao de cookies entendi ==  class = "body2__Paragraph-xstna9-0") o problema é esse botao mesmo, nao o de notificacao

01/06
resolvido o problema de aceitar os cookies, tentei com uma abordagem bruta de time.sleep mas nao fui bem sucedido, criei um loop while para esperar qualquer elemento com a classe aparecer na tela mas o batao nao aparecia
Demorei um pouco pra entender que o batao so aparece depois de duas acoes realizadas na tela, entao coloquei o loop apos o preenchimento da loc e se vai alugar, apos aceitar a confirmação o codigo preenche o restante das informações tranquilamente

=======
O intuito da aplicação é agilizar minha rotina, estou buscando casas para alugar/comprar em outra cidade porque irei me mudar, mas não tenho tempo o suficiente para encontrar a casa ideal que atenda minhas espectativas 

Então iniciei o projeto criando uma função que recebe os valores desejados (oriundos de inputs) e preenche os campos de formulário com os dados recebidos (formulário dos sites chaves na mão e quinto andar) assim facilita a busca e aplica os filtros desejados de área min, qnt quartos, banheiros, garagens, localização.

Durante a busca utilizei um Xparh que pega os 7 primeiros itens correspondentes aos filtros retornando uma lista com uma pequena descrição e o link dos  anúncios.



The purpose of the application is to streamline my routine. I'm searching for houses to rent/buy in another city because I'm moving, but I don't have enough time to find the ideal house that meets my expectations.

So I started the project by creating a function that receives desired values (from inputs) and fills out form fields with the received data (forms from 'chaves na mão' and 'quinto andar' websites), making the search easier and applying desired filters like minimum area, number of rooms, bathrooms, garages, and location.

During the search, I used an XPath that fetches the first 7 items corresponding to the filters, returning a list with a brief description and the link to the advertisements.
>>>>>>> 16ceda4ff5f19cfba43f155445de15a5eb8d615c
