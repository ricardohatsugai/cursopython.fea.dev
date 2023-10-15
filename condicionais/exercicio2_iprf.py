'''Programa de cálculo de imposto de renda'''

'''
Considere as aliquotas e deduções e monte um código para calcular o imposto de renda a depender da renda mensal

Base de cálculo                     alicota     Dedução
Até R$ 1.112,00                     isento      isento
De R$ 2.112,01 até R$ 2.826,65      7,5%        R$ 158,40
De R$ 2.826,66 até R$ 3.751,05      15,0%       R$ 370,40
De R$ 3.751,06 até R$ 4.664,68      22,5%       R$ 651,73
Acima de R$ 4.664,68                27,5%       R$ 884,96
'''

# Solicita a renda mensal do usuário
renda_mensal = float(input(f"Informe sua renda mensal: "))
casas_decimais = int(input(f"Quantas casas decimais de seja o resultado: "))

# Defini faixa de rendas mensais
faixas_de_renda_mensal = [2112.01, 2826.66, 3751.06, 4664,68]
alicotas_mensais = [0.075, 0.15, 0.225, 0.275]
deducao_por_faixa = [158.40, 370.40, 651.73, 884.96]

# Inicializa a variável de imposto de renda
imposto_de_renda_mensal = 0

# Verifica qual faixa de valor de renda mensal que a pessoa se encontra
if (renda_mensal <= faixas_de_renda_mensal[0]):
    imposto_de_renda_mensal = 0
elif(renda_mensal <= faixas_de_renda_mensal[1]):
    imposto_de_renda_mensal = renda_mensal * alicotas_mensais[0] - deducao_por_faixa[0]
elif(renda_mensal <= faixas_de_renda_mensal[2]):
    imposto_de_renda_mensal = renda_mensal * alicotas_mensais[1] - deducao_por_faixa[1]
elif(renda_mensal <= faixas_de_renda_mensal[3]):
    imposto_de_renda_mensal = renda_mensal * alicotas_mensais[2] - deducao_por_faixa[2]
else:
    imposto_de_renda_mensal = renda_mensal * alicotas_mensais[3] - deducao_por_faixa[3]

# Imprime o valor mensal do imposto de renda
print("Seu imposto de renda mensal é R$ {:.4f}" .format(imposto_de_renda_mensal))