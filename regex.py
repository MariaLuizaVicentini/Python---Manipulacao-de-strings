import re 

email1 = "Meu numero é 1234-1234"
email2 = "Fale comigo em 1234-1234 esse é meu telefone"
email3 = "123-1234 é o meu celular"
email4 = "liga liga 99543-1254 alô 9867-1234 alô 9876-1243"

padrao = r"[0-9]{4,5}-*[0-9]{4,4}"

retorno = re.findall(padrao, email4)
if retorno:
    print(retorno)
else:
    print("Nenhum número de telefone encontrado.")



