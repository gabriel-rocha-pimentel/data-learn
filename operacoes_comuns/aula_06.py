import seaborn as sns
import pandas as pd

titanic = pd.read_csv('../data/titanic.csv', sep=';', decimal=',')
#titanic.head()

survivers = titanic.survived.value_counts()
#print(survivers)

embark_people = titanic.embarked.value_counts()
#print(embark_people)

titanic_info = titanic.info()
#print(titanic_info)

no_value = titanic.isnull()
#print(no_value)

list_no_value = titanic.isnull().any()
#print(list_no_value)

seaborn_heatmap = sns.heatmap(titanic.isnull())
#print(seaborn_heatmap)

#print(titanic.columns)
numeric_cols = ['pclass', 'age', 'fare', 'survived']

result = titanic[numeric_cols].corr()
print(result)