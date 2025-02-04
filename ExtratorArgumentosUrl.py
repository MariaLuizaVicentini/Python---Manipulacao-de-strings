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

    def __len__(self):
        """Retorna o tamanho da URL"""
        return len(self.url)

    def __str__(self):
        # Extrai os argumentos da URL para formatação da representação textual
        moedaOrigem, moedaDestino = self.extrairArgumentos()
        representacaoString = "\n Valor: {}\n Moeda Origem: {}\n Moeda Destino: {}\n".format(self.extraiValor(), moedaOrigem, moedaDestino)
        return representacaoString

    def __eq__(self, outraIntancia):
        """Compara se duas instâncias da classe possuem a mesma URL."""
        return self.url == outraIntancia.url
        
    @staticmethod
    def urlEhValida(url):
        """Verifica se a URL fornecida é válida."""
        return url and url.startswith("https://bytebank.com")

    def encontraIndiceInicial(self, moedaBuscada):
        """Encontra o índice inicial do valor de uma moeda dentro da URL."""
        return self.url.find(moedaBuscada) + len(moedaBuscada)

    def extrairArgumentos(self):
        """Extrai os argumentos (moeda de origem e destino) da URL."""
        buscaMoedaOrigem = "moedaorigem="
        buscaMoedaDestino = "moedadestino="

        # Encontra a posição da moeda de origem
        indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
        indiceFinalMoedaOrigem = self.url.find("&", indiceInicialMoedaOrigem)
        if indiceFinalMoedaOrigem == -1:
            indiceFinalMoedaOrigem = len(self.url)
        moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]

        # Encontra a posição da moeda de destino
        indiceInicialMoedaDestino = self.encontraIndiceInicial(buscaMoedaDestino)
        indiceFinalMoedaDestino = self.url.find("&", indiceInicialMoedaDestino)
        if indiceFinalMoedaDestino == -1:
            indiceFinalMoedaDestino = len(self.url)
        moedaDestino = self.url[indiceInicialMoedaDestino:indiceFinalMoedaDestino]

        # Caso a moeda de origem seja "moedadestino", troca para "real"
        if moedaOrigem == "moedadestino":
            self.trocaMoedaOrigem()
            moedaOrigem = "real"

        return moedaOrigem, moedaDestino

    def trocaMoedaOrigem(self):
        """Troca 'moedadestino' por 'real' na URL."""
        self.url = self.url.replace("moedadestino", "real", 1)

    def extraiValor(self):
        """Extrai o valor da URL."""
        buscaValor = "valor="
        indiceInicialValor = self.encontraIndiceInicial(buscaValor)
        valor = self.url[indiceInicialValor:]
        return valor
