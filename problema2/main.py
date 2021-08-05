#!/usr/bin/env python3


def formatar_nome(nome_completo):
    """
    Formata o `nome_completo` de como 'Sobrenome, Nome'

    :param nome_completo: Nome completo a ser formatado
    :return: Nome formatado
    """
    nome = nome_completo.title()
    nome, sobrenome = nome.split(" ", 1)
    nome = nome.strip()
    sobrenome = sobrenome.strip()
    return "%s, %s" % (sobrenome, nome)


def formatar_telefone(telefone):
    """
    Formata o telefone de acordo com a convenção: +NN (NN) NNNN-NNNN

    :param telefone: Telefone a ser formatado
    :return: Telefone formatado
    """
    telefone = telefone.strip()
    telefone = telefone.replace("(", "")
    telefone = telefone.replace(")", "")
    telefone = telefone.replace("-", "")
    telefone = telefone.replace(" ", "")
    return "+55 (%s) %s-%s" % (telefone[:2], telefone[2:6], telefone[6:])


def formatar_email(email):
    """
    Formata o email de acordo com a convenção: nome@email.com

    :param email: Email a ser formatado
    :return: Email formatado
    """
    email = email.strip()
    email = email.lower()
    email = email.replace("at", "@")
    email = email.replace("dot", ".")
    email = email.replace(" ", "")
    return email


def formatar_campo(campo, valor):
    """
    Formata o valor de acordo com o tipo de campo

    :param campo: Tipo de campo a ser formatado
    :param valor: Valor a ser formatado
    :return: Valor formatado
    """
    if campo == "Nome":
        return formatar_nome(valor)
    if campo == "Telefone":
        return formatar_telefone(valor)
    if campo == "Email":
        return formatar_email(valor)
    return valor


def formatar_agenda(caminho):
    """
    Formata o arquivo de agenda
    :param caminho: Caminho do arquivo a ser formatado
    """
    agenda = open(caminho, "r")
    for linha in agenda.readlines():
        linha = linha.strip()
        if linha:
            campo, valor = linha.split(": ")
            valor = formatar_campo(campo, valor)
            print("{:10} {}".format(campo + ":", valor))
        else:
            print()


if __name__ == "__main__":
    formatar_agenda("problema2/agenda.txt")
