# Pré-Processamento dos Dados
import pandas as pd
import seaborn as sns

def imprimir(texto):
    print(f"{texto}\n")

# Carregando o dataset
titanic = pd.read_csv('../data/titanic.csv', sep=';')
imprimir(titanic.head())
imprimir(titanic.info())

#imprimir(sns.heatmap(titanic.isnull()))
#imprimir(sns.heatmap(titanic.isna()))
imprimir(titanic.alive.isna().value_counts())
imprimir(titanic.age.isna().value_counts())
imprimir(titanic.embarked.isna().value_counts())

# titanic.dropna(subset=['embarked', 'embark_town'], inplace=True)

#imprimir(titanic.isna())

imprimir(titanic.deck.value_counts())
imprimir(titanic.deck.fillna('C'))

#titanic.drop(['age'], axis=1, inplace=True)
#imprimir(titanic.info())

imprimir(titanic.survived.mean())