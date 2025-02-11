# Para importar uma biblioteca ou metodo de algum arquivo que ajude na leitura de dados.
import pandas as pd

# Para acessar um arquivo csv ou com formato adequado, para leitura de dados.
tabela = pd.read_csv('data/alunos.csv', delimiter=';')

# Para acessar dados da tebela como um todo.
tabela.head()

# Para acessar dados de uma coluna especifica
# Por exemplo, coluna 'Nome':
tabela.Nome
tabela['Nome']

# Para criar colunas
aluno_email = ['Nome', 'Email']
print(aluno_email)

tabela[aluno_email]

# Para filtrar dados, usamos o seguinte comando, com o ':' para definir inicio e fim assim como no python.
# O comando: tabela.iloc[*linha*:,*coluna*:]
# A seguinte sintaxe é aceita, o primeiro serve para limitar dados nas linhas e o segundo para limitar os dados na coluna
# Ambos aceitam notação de 0 até o limite de dados inseridos na tabela.
tabela.iloc[:,:]

tabela.iloc[2:,:]

tabela.iloc[:2,1:]

# Caso precise criar uma nova tabela, pode fazer seguindo a sintaxe:
Media = [45.8, 90.9, 20.4, 40.9, 30.5]
print(Media)

# Para adicionar a nova coluna a tabela do CSV
tabela['Media'] = Media
tabela.head()

aluno_notas = ['Nome', 'Curso', 'Media']
tabela[aluno_notas]

# Para eliminar alguma coluna, é usado o seguinte comando
# tabela.drop(['nome_da_coluna', axis='eixo']), o eixo não pode ser 0
# Ao excluir uma tabela é preciso salvar essa informação em algum lugar, como uma variavel
# Se não for necessário ou possivel salvar, pode-se por o parametro inplace=True como em: tabela.drop([], axis=1, inplace=True)
nova_tabela = tabela.drop(['Email'], axis=1)

# Tabela antiga
tabela.head()

# Nova tabela com os dados excluidos
nova_tabela.head()