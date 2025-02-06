import pandas as pd

tabela_alunos = pd.read_csv('../data/alunos.csv', delimiter=';', encoding='utf-8')
print(tabela_alunos)

Media = [45.8, 90.9, 20.4, 40.9, 30.5]
tabela_alunos['Media'] = Media

nova_tabela = tabela_alunos[['Nome', 'Curso', 'Media']]
print(nova_tabela)