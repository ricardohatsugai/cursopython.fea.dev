def soma_argumentos(*args):
    sum = 0
    for arg in args:
        sum += arg
        print(f"A soma dos números inseridos é {sum}")

soma_argumentos(99, 10, 20, 80, 90, 15)
