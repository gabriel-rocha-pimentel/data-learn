import pandas as pd

registro_de_voos = pd.read_csv('../data/voos.csv', sep=';')
#print(registro_de_voos.head())

# Nesta aula usaremos o pivot_table para criar uma tabela dinâmica
# com os dados de registro_de_voos, nos vamos criar agrupamentos
# de voos por origem e destino, e vamos calcular a média do tempo
# air_plane_pivot = pd.pivot_table(registro_de_voos, index=['year', 'month'])

# Usando o groupby para agrupar os dados, nos podemos fazer com que os dados
# mostrem dados de origem e destino, e a média do tempo de voo
voos_por_mes = registro_de_voos.groupby('year')
# print(voos_por_mes.describe())
# Agora temos um agrupamento de voos por ano, e podemos ver a média do tempo de voo
print(voos_por_mes['passengers'].mean())
print(voos_por_mes['passengers'].max())