caminho = 'problem1/arquivo.txt'

def converte(tipo, valor):
    try:
        if tipo == "string":
            return str(valor)
        if tipo == "int":
            return int(valor)
        if tipo == "float":
            return float(valor)
        if tipo == "boolean":
            return bool(valor)
    except ValueError:
        print(f'O valor "{valor}" não é do tipo "{tipo}"')
        return None

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
        if not linha.startswith('#') and not linha.startswith('\n'):
            tipo, nome, valor = separa_linha(linha)
            d[nome] = converte(tipo, valor)
    return d

res = processa_arquivo(caminho)
print(res)