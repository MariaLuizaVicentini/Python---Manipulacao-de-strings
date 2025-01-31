class ExtratorArgumentoUrl:
    """Classe responsável por extrair argumentos de uma URL."""

    def __init__(self, url):
        """Inicializa a instância com a URL fornecida, verificando sua validade."""
        # Verifica se a URL fornecida é válida usando o método urlEhValida()
        if self.urlEhValida(url):
            # Armazena a URL em letras minúsculas para padronização
            self.url = url.lower()
        else:
            # Se a URL for inválida, lança uma exceção do tipo LookupError
            raise LookupError("Erro de pesquisa: URL inválida!")

    @staticmethod
    def urlEhValida(url):
        """Verifica se a URL fornecida é válida."""
        # Retorna True se a URL não for vazia (string não vazia é avaliada como True)
        return bool(url)

    def encontraIndiceInicial(self, moedaBuscada):
        """Encontra o índice inicial do valor de uma moeda dentro da URL."""
        # Retorna a posição onde a moeda foi encontrada na URL somada ao seu tamanho,
        # para obter a posição do valor correspondente
        return self.url.find(moedaBuscada) + len(moedaBuscada)

    def extrairArgumentos(self):
        """Extrai os argumentos (moeda de origem e destino) da URL."""

        # Define as chaves de busca para identificar os argumentos na URL
        buscaMoedaOrigem = "moedaorigem="
        buscaMoedaDestino = "moedadestino="

        # Encontra a posição inicial e final da moeda de origem na URL
        indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
        indiceFinalMoedaOrigem = self.url.find("&", indiceInicialMoedaOrigem)
        # Se não encontrar o caractere '&', significa que está no final da URL
        if indiceFinalMoedaOrigem == -1:
            indiceFinalMoedaOrigem = len(self.url)

        # Extrai a moeda de origem da URL
        moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]

        # Encontra a posição inicial e final da moeda de destino na URL
        indiceInicialMoedaDestino = self.encontraIndiceInicial(buscaMoedaDestino)
        indiceFinalMoedaDestino = self.url.find("&", indiceInicialMoedaDestino)
        # Se não encontrar o caractere '&', significa que está no final da URL
        if indiceFinalMoedaDestino == -1:
            indiceFinalMoedaDestino = len(self.url)

        # Extrai a moeda de destino da URL
        moedaDestino = self.url[indiceInicialMoedaDestino:indiceFinalMoedaDestino]

        # Caso a moeda de origem seja "moedadestino", troca para "real"
        if moedaOrigem == "moedadestino":
            self.trocaMoedaOrigem()
            moedaOrigem = "real"

        # Retorna as moedas extraídas
        return moedaOrigem, moedaDestino

    def trocaMoedaOrigem(self):
        """Troca 'moedadestino' por 'real' na URL."""
        # Substitui a primeira ocorrência de "moedadestino" por "real" na URL
        self.url = self.url.replace("moedadestino", "real", 1)

    def extraiValor(self):
        """Extrai o valor da URL."""
        buscaValor = "valor="
        # Encontra o índice inicial onde o valor numérico começa
        indiceInicialValor = self.encontraIndiceInicial(buscaValor)
        # Captura o valor correspondente na URL a partir do índice encontrado
        valor = self.url[indiceInicialValor:]
        return valor
