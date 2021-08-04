caminho = 'problem1/arquivo.txt'

def converte(tipo, valor):
    if tipo == "string":
        return str(valor)
    if tipo == "int":
        return int(valor)
    if tipo == "float":
        return float(valor)
    if tipo == "boolean":
        return bool(valor)

def separa_linha(linha):
    tipo, dado = linha.split(':')
    nome, valor = dado.split('=')
    tipo = tipo.strip()
    nome = nome.strip()
    valor = valor.strip()

    return tipo, nome, valor

def processa_arquivo(caminho):
    d = {}
    linhas = open(caminho, 'r').readlines()
    for linha in linhas:
        tipo, nome, valor = separa_linha(linha)
        d[nome] = converte(tipo, valor)
    return d

res = processa_arquivo(caminho)
print(res)