import pandas as pd

#Vamos analisar a organização de dados
# e estrutura de um dataframe

ex_dict = {'Nome': ['Aluno1', 'Aluno2', 'Aluno3', 'Aluno4'], 'P1': [1.6, 7.5, 9, 5.5], 'P2': ['-', 6.5, 8, 8]}

print(ex_dict)

#É possível gerar um dataframe a partir de dicionários

#Note o pd de pandas

dataframe = pd.DataFrame.from_dict(ex_dict)
print(dataframe)