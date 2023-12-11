import pandas as pd

listao = [['Aluno1', 1.6,'-'], ['Aluno2', 7.5, 6.5], ['Aluno3', 9, 8], ['Aluno4', 5.5, 8]]

dataframe = pd.DataFrame(listao, columns=['Nome', 'P1', 'P2'])
print(dataframe)