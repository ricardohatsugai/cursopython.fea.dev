import matplotlib.pyplot as plt

idade = [25, 30, 35, 40, 45, 50]

salario = [50000, 60000, 75000, 80000, 90000, 100000]

plt.scatter(idade, salario)

plt.xlabel('Idade')

plt.ylabel('Salário')

plt.title('Relação entre Idade e Salário')

plt.show()