# Exercícios de Programação 1

## Problema 1: Tipos
Escreva uma função que interprete variáveis declaradas em um arquivo, e retorne um dicionário (dict) com os valores e tipos compatíveis.

_Exemplo:_

Para o arquivo
```
string: nome = Eduardo
int: idade = 30
float: salario = 1000
string: telefone = 5552231273
```

a função deve retornar o dicionário
```python
{
    "nome": "Eduardo",
    "idade": 30,
    "salario": 1000.0,
    "telefone": "5552231273"
}
```

*__Bônus 1__: verificar compatibilidade do valor com o tipo. e.g. um int não pode receber uma letra.*

*__Bônus 2__: Ignorar linhas vazias ou começando com '#'.*

## Problema 2: Manipulação de Strings
Escreva um programa que leia uma agenda de contatos e imprima seus dados formatados.
O arquivo de contendo a agenda pode ser baixado [aqui](https://raw.githubusercontent.com/BrunoCoimbra/prog1/main/problema2/agenda.txt), e o formato:
```
Nome: <NOME>
Telefone: <TELEFONE>
Email: <EMAIL>
```

O programa deve formatar os valores de cada campo, preservando o formato original da agenda.
Os valores de cada campo devem ser formatados de acordo com as regras a seguir:

* Nome
  * Deve ser impresso como "Sobrenome, Nome"
  * Deve conter apenas um espaço em branco entre os nomes
  * Todos os nomes devem começar com letra maiúscula

* Telefone
  * Deve ser impresso no formato "+55 (NN) NNNN-NNNN..."

* Email
  * Deve ser impresso no formato "email@dominio.com"
  * "at" deve ser substituído por "@"
  * "dot" deve ser substituído por "."

* Campos e Valores
  * Os campos devem ter um espaçamento mínimo de 2 espaços dos valores
  * O valores devem estar alinhados na mesma coluna

A saída desejada é a seguinte:
```
Nome:      Nogueira, Alberto
Telefone:  +55 (21) 9555-6984
Email:     alberto@nogueira.com

Nome:      Maia Gomes, Beatriz
Telefone:  +55 (11) 5595-4865
Email:     bmaia@gmail.com

Nome:      Braga De Sá, Carlos
Telefone:  +55 (31) 2257-5987
Email:     cbragasa@hotmail.com

Nome:      Coelho Nobrega, Dante
Telefone:  +55 (11) 5555-5486555
Email:     denobrega@live.com

Nome:      Simão, Eduardo
Telefone:  +55 (21) 5448-6158
Email:     dudusimao@hotmail.com
```
