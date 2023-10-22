nomes = ["Alice", "Bob", "Charlie"]
idades = [25, 30, 35]
pessoas = dict(zip(nomes, idades))

for chave in pessoas:
    print(chave, pessoas[chave])