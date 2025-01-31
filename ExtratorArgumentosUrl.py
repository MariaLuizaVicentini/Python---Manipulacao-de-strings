class ExtratorArgumentoUrl:  # Definição da classe responsável por extrair argumentos de uma URL
    
    def __init__(self, url): 
        """Método construtor que inicializa a instância(atributos) da classe com a URL fornecida"""
        # Verifica se a URL fornecida é válida, ou seja, se ela não esta vazia:
        if self.urlEhValida(url):
            self.url = url  # self acessa o atributo 'url' e defini que ele recebe o argumento que equivale a URL
        # Se não, se ela estiver vazia:
        else:
            # Lança um erro "Erro de pesquisa" caso a URL seja inválida
            # 'raise' é uma palavra chave que significa "levantar" ela é utilizada para forçar uma exeção e interromper o fluxo do programa. 
            raise LookupError("Erro de pesquisa: Url inválida!!!") 

    @staticmethod
    def urlEhValida(url):
        """Método estático que verifica se a URL fornecida é válida"""
        if url:  # Se a URL não for uma string vazia
            return True  # Retorna True, indicando que é válida
        else:
            return False  # Retorna False, indicando que é inválida

    def encontraIndiceInicial(self, moedaBuscada):
        """Método auxiliar que encontra o índice inicial do valor de uma moeda dentro da URL"""
        # Retorna o índice inicial do valor da moeda (após a chave de busca)
        return self.url.find(moedaBuscada) + len(moedaBuscada)


    def extrairArgumentos(self):
        """Método que extrai os argumentos (substrings que representam os valores das moedas) da URL"""
        
        # Define as palavras-chave que identificam as moedas na URL
        buscaMoedaOrigem = "moedaorigem="
        buscaMoedaDestino = "moedadestino="

        # Encontra a posição INICIAL do valor correspondente da substring 'real' na URL
        indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
        # Encontra o índice final do valor da moeda de origem, que é o próximo '&'
        indiceFinalMoedaOrigem = self.url.find("&", indiceInicialMoedaOrigem)
        
        # Separa a substring correspondente à moeda de origem
        moedaOrigem = self.url[indiceInicialMoedaOrigem : indiceFinalMoedaOrigem]  # Exemplo: 'real'
        
        # Encontra o índice inicial do valor correspondente à moeda de destino na URL
        indiceInicialMoedaDestino = self.encontraIndiceInicial(buscaMoedaDestino)
        # Encontra o índice final do valor da moeda de destino (próximo '&' ou final da string)
        indiceFinalMoedaDestino = self.url.find("&", indiceInicialMoedaDestino)
        
        # Se não houver '&' após a moeda de destino, significa que ela está no final da string
        if indiceFinalMoedaDestino == -1:
            indiceFinalMoedaDestino = len(self.url)  # Define o final da string como limite

        # Separa a substring correspondente à moeda de origem
        moedaOrigem = self.url[indiceInicialMoedaOrigem : indiceFinalMoedaOrigem]  # Exemplo: 'real'
    
        # Separa a substring correspondente à moeda de destino
        moedaDestino = self.url[indiceInicialMoedaDestino: indiceFinalMoedaDestino]
        
        # Retorna as moedas de origem e destino extraídas da URL
        return moedaOrigem, moedaDestino

    def encontraIndiceInicial(self, moedaBuscada):
        """Método auxiliar que encontra o índice inicial do valor de uma moeda dentro da URL"""
        # Retorna o índice inicial do valor da moeda (após a chave de busca)
        return self.url.find(moedaBuscada) + len(moedaBuscada)

