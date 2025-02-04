# Extrator de Argumentos de URL

Este projeto contém a classe `ExtratorArgumentoUrl`, que tem como objetivo extrair parâmetros de uma URL específica do domínio `bytebank.com`.

## Funcionalidades
- **Validação de URL**: Verifica se a URL fornecida pertence ao domínio esperado.
- **Extração de argumentos**: Identifica e extrai as moedas de origem e destino da conversão.
- **Tratamento de moeda de origem**: Se a moeda de origem for `moedadestino`, ela é substituída por `real`.
- **Extração de valores**: Obtém o valor de conversão presente na URL.
- **Métodos especiais**: Implementação de `__str__`, `__len__` e `__eq__` para facilitar o uso da classe.

## Requisitos
- Python 3.7 ou superior.

## Exemplo de Uso
```python
url = "https://bytebank.com/cambio?moedaorigem=dolar&moedadestino=real&valor=1500"
extrator = ExtratorArgumentoUrl(url)
print(extrator)
```

Saída esperada:
```
Valor: 1500
Moeda Origem: dolar
Moeda Destino: real
```

## Como Contribuir
1. Faça um fork do repositório.
2. Crie uma branch para suas modificações (`git checkout -b minha-modificacao`).
3. Faça suas alterações e commit (`git commit -m "Minha melhoria"`).
4. Envie para o repositório remoto (`git push origin minha-modificacao`).
5. Abra um Pull Request.

## Licença
Este projeto está sob a licença MIT.

