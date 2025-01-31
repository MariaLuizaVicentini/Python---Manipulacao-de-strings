Extrator de Argumentos de URL

Descrição

Este projeto tem como objetivo extrair os argumentos de uma URL fornecida, identificando as moedas envolvidas em uma transação de câmbio. O projeto é composto por uma classe principal ExtratorArgumentoUrl, que processa a URL, e um script main.py, que executa o fluxo de extração e exibição dos resultados.

Tecnologias Utilizadas

Python 3.x

nbformat (para manipulação de notebooks Jupyter)

nbconvert (para converter notebooks em scripts Python)

importlib (para recarregar módulos dinâmicamente)

Estrutura do Projeto

/
|-- ExtratorArgumentosUrl.py  # Módulo que contém a classe ExtratorArgumentoUrl
|-- main.py                   # Script principal que executa a extração de argumentos
|-- README.md                 # Documentação do projeto

Como Funciona

Módulo: ExtratorArgumentosUrl.py

A classe ExtratorArgumentoUrl possui os seguintes métodos:

__init__(self, url): Inicializa a instância com a URL fornecida, validando-a.

urlEhValida(url): Verifica se a URL fornecida é válida.

encontraIndiceInicial(moedaBuscada): Retorna o índice inicial do valor de uma moeda na URL.

extrairArgumentos(): Extrai os argumentos "moeda de origem" e "moeda de destino" da URL.

Script Principal: main.py

Exporta um notebook Jupyter (.ipynb) para um script Python (.py).

Importa e recarrega dinamicamente o módulo ExtratorArgumentosUrl.

Cria uma instância da classe ExtratorArgumentoUrl, passando uma URL de exemplo.

Extrai e exibe os argumentos de "moeda de origem" e "moeda de destino".

Exemplo de Uso

# Criando a instância da classe
argumentosUrl = ExtratorArgumentosUrl.ExtratorArgumentoUrl("https://bytebank.com?cambio?moedaorigem=real&moedadestino=dolar&valor=700")

# Extraindo os argumentos
moedaOrigem, moedaDestino = argumentosUrl.extrairArgumentos()

# Exibindo os argumentos extraídos
print(f'Moeda Origem: {moedaOrigem}')
print(f'Moeda Destino: {moedaDestino}')

Saída esperada:
