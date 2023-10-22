'''Exemplo:
O usuário vai digitar 3 números a, b, c. Precisamos imprimir os números em ordem decrescente. Como escrever o código?(lembrar do uso do float(input())

1°: escreva o código usando apenas 1 operador de comparação por condição estabelecida    
2°: escreva o código livremente

(dica: há 6 situações possíveis.)'''

a = float(input(f"Digite um número: "))
b = float(input(f'Digite outro número: '))
c = float(input(f'Digite outro número: '))

if a > b:
    if b >= c:
        print(f"{a} >= {b} >= {c}")
    elif a >= c:
        print(f"{a} >= {c} >= {b}")
    else:
        print(f"{c} >= {a} >= {b}")
else:
    if a >= c:
        print(f"{b} >= {a} >= {c}")
    elif b >= c:
        print(f"{b} >= {c} >= {a}")
    else:
        print(f"{c} >= {b} >= {a}")

