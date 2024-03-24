# Resultado - Desáfio CoorLab

Decidi implementar o back-end com Django e o front-end com Vue e Typescript, como segue.

## *Back-end*
Seguindo a terminologia do Django, implementei somente um _app_ para as viagens. Nele, defini os _endpoints_ da API no arquivo **urls.py**:
- **travels/test/** (GET)
    - Para testar a resposta da API.
- **travels/destinations/** (GET)
    - Retorna uma lista de todos os destinos registrados no banco de dados
- **travels/** (GET, POST, UPDATE, DELETE)
    - Endpoint para realizar operações no banco de dados seguindo a arquitetura REST. Somente a função responsável pelo método **GET** foi implementada, uma vez que era a única imprescíndivel para esse desafio. Nela, a *query string* da requisição é processada para obter os filtros de destino e data a serem utilizados para busca no banco de dados.<br>As funções responsáveis pelos métodos **POST**, **UPDATE** e **DELETE** estão definidas e prontas para serem implementadas, de tal forma que o controle do _endpoint_ discerne entre cada operação, porém será retornado um erro na requisição à API utilizando esses métodos.

No arquivo **models.py**, a classe responsável pela representação das viagens no banco de dados está implementada, de acordo com o modelo passado nas instruções do README.md. Os tipos de dados escolhidos para cada atributo foram:
- _name_: Sequência de caracteres de no máximo 100 caracteres.
- _price_confort_: Número de ponto flutuante.
- _price_econ_: Número de ponto flutuante.
- _city_: Sequência de caracteres de no máximo 100 caracteres.
- _duration_: Objeto _timedelta_ que representa uma duração.
- _seat_: Sequência de caracteres de no máximo 3 caracteres.
- _bed_: Sequência de caracteres de no máximo 3 caracteres.

No arquivo **serializers.py**, está implementada somente uma classe responśavel pela formatação dos dados retornados pela API. Especificamente, o atributo _duration_ da _model_ acima é transformado em um valor inteiro de acordo com o valor original contido no arquivo **data.json** disponibilizado.

Por fim, na pasta **/*migrations*** estão contidas as migrações do banco de dados. A primeira é responsável pela criação das tabelas de acordo com os modelos implementados em **models.py**. A segunda migração realiza a inclusão dos dados pré-disponibilizados no banco de dados.

## *Front_end*
Utilizei o Vue3 com a *Compositions* API para implementação da interface do cliente. No script de inicialização do servidor, inclui a instalação do NVM (_Node Version Manager_) para instalar a versão 20 do Node.JS, para evitar quaisquer erros de incompatibilidade de versões ao iniciar o servidor.

Inicialmente, removi algumas configurações iniciais incluídas no inicializador de projetos do Vue. Removi algumas regras de estilo nos arquivos **base.css** e **main.css** em **/public** e deletei os arquivos **.vue**, exceto pelo **App.vue**. Nele, implementei a base da tela inicial, com os seguintes componentes:
- *LeftPanel*: Painel retangular lateral contendo os menus.
- *CalculatorContainer*: *Container* para a calculadora de viagens.

Todos os componentes foram armazenados em **src/components/**. Caso um componente possuísse componentes filhos, o conjunto era armazenado em uma pasta para agrupá-los. Por exemplo, o componente *CalculatorContainer*, que possui subcomponentes, foi armazenado na pasta **src/components/calculator**, com a seguinte estrutura:

```
calculator                      
├── CalculatorContainer.vue     # Componente pai
└── components                  # Componentes filhos
    ├── TravelForm.vue
    ├── TravelResults.vue
    └── TravelResult.vue
```
Com a escalação do projeto, eu seguiria esse mesmo padrão de estrutura de diretórios, sempre agrupando componentes relacionados e subdividindo mais, se necessário. Além disso, outras pastas e arquivos específicos (como _services_) para um conjunto de componentes seriam criados dentro da pasta-raiz do componente.

Cada subcomponente de *CalculatorContainer* compõem um parte do protótipo disponibilizado:
- *TravelForm*
    - Formulário para escolha do destino e data inicial da viagem. A listagem dos destinos é realizada logo após o retorno dos dados do *back-end*, pelo endpoint **travels/destination/**. A escolha da data é restrita para o dia atual ou futuros.
- *TravelResults*
    - Painel para apresentação dos resultados da busca após submissão do formulário, os quais são passados como um atributo ao componente. Possui uma função para filtrar os resultados com base na história de usuário e no cenário. Logo, retorna duas entradas entre os dados da busca: a viagem com assento tipo leito e mais rápida e a viagem com menor preço, considerando as duas opções possíveis de preço para cada viagem. Também há um botão para limpar os resultados, conforme o protótipo.
- *TravelResult*
    - Elemento contendo as informações da viagem a ser apresentada no painel de resultados: empresa, tipo de assento, tempo estimado em horas, data de chegada estimada (com base na duração da viagem) e preço.

A pasta **models/** contém as interfaces utilizadas pelos componentes, para assertividade dos tipos pelo Typescript.

Por último, a pasta **shared/** contém componentes que poderão ser utilizados por qualquer componente do projeto:
- *DefaultButton*
    - Botão padrão com layout de acordo com o protótipo e ação atribuível.
- *LoadingSpinner*
    - Ícone de carregamento com apresentação condicional, por meio de um atributo booleano. Utilizei para indicar ao usuário a realização da busca no banco de dados.
- *WarningModal*
    - Modal com aviso personalizável e de apresentação condicional. Utilizei para avisar ao usuário a existência de campos não-preenchidos no formulário, conforme o protótipo.

A busca dos dados após submissão do formulário é realizada no componente pai *CalculatorContainer*, que, por sua vez, transfere-os para o componente *TravelResults*. A sinalização da submissão do formulário é realizada a partir da emissão de um evento pelo componente *TravelForm* junto a um objeto contendo os dados do formulário. A requisição é realizada somente se o objeto possui tanto o valor de destino quanto de data da viagem, os quais são utilizados para montagem da *query string* do *endpoint* da API. Caso contrário, o modal de aviso é apresentado ao usuário.