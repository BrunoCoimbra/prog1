# Exercícios de Programação 1

## Tipos
Escreva uma função que interprete variáveis declaradas em um arquivo, e retorne um dicionário (dict) com os valores e tipos compatíveis.

Exemplo:

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

*__Bonus 1__: verificar compatibilidade do valor com o tipo. e.g. um int não pode receber uma letra.*

*__Bonus 2__: Ignorar linhas vazias ou começando com '#'.*
