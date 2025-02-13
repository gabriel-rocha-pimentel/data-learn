import pandas as pd

tabela = pd.read_csv('../data/estoque_cozinha.csv', delimiter=';')

# O comando set_index é usado para definir uma coluna especifica como index da tabela
# O atributo inplace=True é usado para salvar a alteração na tabela, sem ele a alteração não é aplicada
tabela.set_index('Categoria', inplace=True)

# Como já foi mostrado, pra acesar os dados da tabela, usamos o comando tabela.head()
# print(tabela.head())

# Para acessar uma determinada quantidade de linhas, usamos o comando tabela.head(*numero_de_linhas*)
# print(tabela.head(2))

# Também é possivel dar prioridade para uma coluna especifica, como por exemplo, a coluna 'Quantidade'
# tabela = pd.read_csv('../data/estoque.csv', delimiter=';', index_col=['Quantidade'])
# print(tabela.head())

# Podemos usar o loc para acessar dados de uma linha especifica, usando o comando tabela.loc[*linha*, *coluna*]
# comando_loc = tabela.loc[:, 'Item']
# print(comando_loc)

# Podemos criar uma nova tabela, com os dados de uma coluna especifica, como por exemplo, a coluna 'Categoria'
categoria = ['Grãos', 'Carnes', 'Hortifruti']
info = ['Preço', 'Validade']
# print(tabela.loc[categoria, info])

# Também é possivel estabelecer condições para filtrar os dados, como por exemplo, filtrar os produtos mais baratos
# print(tabela.loc[tabela.Preço <= 4.0, :])

# É possivel escolher filtrar dados de uma coluna especifica também
# print("PRODUTOS MAIS BARATOS")
# print(tabela.loc[tabela.Preço <= 4.0, 'Item'])

# Uma outra forma de filtrar dados é usando as estrutuas condicionais, como por exemplo, filtrar os produtos mais baratos
filtra_graos = tabela.loc[(tabela.Preço <= 4.0) & (tabela.Item == 'Arroz'), :]
print(filtra_graos)

filtra_carnes = tabela.loc[(tabela.Item == 'Arroz') | (tabela.Item == 'Feijão'), :]
print(filtra_carnes)
