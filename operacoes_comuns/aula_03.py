import pandas as pd

# Esta aula tem o objetivo de explicar como funciona a junção de tabelas no python com o pandas
# Primeiro vamos importar o csv, de professores.csv
professores = pd.read_csv('../data/professores.csv', delimiter=';')

# Agora vamos importar o csv de recisão de contrato dos professores
# recisao_contrato = pd.read_csv('../data/recisao_contrato.csv', delimiter=';')
# recisao = recisao_contrato.drop(['Nome'], axis=1)

# print(professores.head(), recisao_contrato.head())

# Agora vamos fazer a junção das duas tabelas, usando o merge do pandas
# Este metodo é muito parecido com o join do SQL, e fuciona da seguinte forma merge(tabela1, tabela2, on='coluna')
# O parametro on é a coluna que será usada para fazer a junção das duas tabelas

# tabela_final = pd.merge(professores, recisao, on='ID')
# print(f"\n{tabela_final.head()}")

# Caso seja necessário fazer a junção de duas tabelas uma abaixo da outra, pode-se usar o metodo concat do pandas
# Este metodo funciona da seguinte forma: pd.concat([tabela1, tabela2])
# O metodo concat aceita mais de duas tabelas, basta colocar as tabelas em uma lista
# Para esse exemplo usaremos os arquivos de estoque da cozinha e do bar
estoque_cozinha = pd.read_csv('../data/estoque_cozinha.csv', delimiter=';', index_col=['Categoria'])
estoque_bar = pd.read_csv('../data/estoque_bar.csv', delimiter=';', index_col=['Categoria'])

estoque_final = pd.concat([estoque_cozinha, estoque_bar])
# print(estoque_final)

# Caso seja necessário fazer a junção de duas tabelas uma ao lado da outra, pode-se usar o metodo join do pandas
# Este metodo funciona da seguinte forma: tabela1.join(tabela2)
professores = pd.read_csv('../data/professores.csv', delimiter=';', index_col=['ID'])
recisao_contrato = pd.read_csv('../data/recisao_contrato.csv', delimiter=';', index_col=['ID'])
recisao_contrato.drop(['Nome'], axis=1, inplace=True)
tabela_final = professores.join(recisao_contrato, on='ID')
print(tabela_final)