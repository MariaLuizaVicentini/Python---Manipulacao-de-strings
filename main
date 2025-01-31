import os # Lida com caminhos e operações do sistema
import nbformat # Manipula os arqvs '.ipynb' para leitura e escrita
from nbconvert import PythonExporter # converte o notebook em um script.py
import importlib # Recarrega automaticamente o módulo importado

def export_notebook_to_py(notebook_name):
    """Exporta um notebook .ipynb para um arquivo .py"""
    # Le o arqv
    with open(f"{notebook_name}.ipynb", 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)
    exporter = PythonExporter()
    # escreve o arqv
    script, _ = exporter.from_notebook_node(notebook)
    with open(f"{notebook_name}.py", 'w', encoding='utf-8') as f:
        f.write(script)

# Nome do notebook que será exportado
notebook_name = "ExtratorArgumentosUrl" 
export_notebook_to_py(notebook_name)

# Importa módulo.py
import ExtratorArgumentosUrl
# Recarrega o módulo
importlib.reload(ExtratorArgumentosUrl) 

# Criando variável para receber a URL
url = "https://bytebank.com?cambio?moedaorigem=real&moedadestino=dolar&valor=700"

# Criando a instância(objeto) da classe "ExtratorArgumentoUrl()"
argumentosUrl = ExtratorArgumentosUrl.ExtratorArgumentoUrl(url)

# Extraindo os argumentos de moedaOrigem e moedaDestino
moedaOrigem, moedaDestino = argumentosUrl.extrairArgumentos()

# Exibindo argumentos: moedaOrigem(real) e moedaDestino(dolar)
print(f'Moeda Origem: {moedaOrigem}\nMoeda Destino: {moedaDestino}')
