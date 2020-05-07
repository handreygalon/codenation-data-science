import pandas as pd
import numpy as np

# ----- DICT ----- #
dados = {'canal_venda' : ['facebook', 'twitter', 'instagram', 'linkedin', 'facebook'],
        'acessos': [100, 200, 300 ,400, 500],
        'site': ['site1', 'site1', 'site2', 'site2', 'site3'],
        'vendas': [1000.52, 1052.34, 2002, 5000, 300 ]}

# Getting the dictionary keys
dados.keys()

# Getting a specific key
dados['site']

# Getting a specific dictionary position
dados['acessos'][2]
dados['canal_venda'][:3]  # output: ['facebook', 'twitter', 'instagram']

# ----- LIST ----- #
lista = [200, 200 , 300 ,800, 900]

# Getting the value from a specific index
lista[1]

# Slice the list
lista[:3]  # output: [200, 200, 300]

# Adding a list to a dict
dados['lista'] = lista

# ----- DATAFRAMES ----- #
# Create a data frame from a dict
dataframe = pd.DataFrame(dados)

# Print the first cases of dataframe
dataframe.head(2)

# Checking the shape of the dataframe
dataframe.shape

# Checking the index of the dataframe
dataframe.index

# Checking the data types of the dataframe
dataframe.dtypes

# Checking the quantity of the columns
dataframe.dtypes.value_counts()

# Checking if there is missing data
dataframe.isna()
dataframe.isna().sum()  # sum the true values (where is missing data)

# Print the column names
dataframe.columns

# Access a specific column
dataframe['canal_venda']

# transform dataframe to a list
list(dataframe['canal_venda'])

# Create a new column
dataframe['nova_coluna'] = [1, 2, 3, 4, 5]

# Delete column
dataframe.drop(columns = 'nova_coluna', inplace = True)  # inplace means that you are really removing a column, otherwise, you just remove the column to visualization
dataframe.drop(columns = ['acessos','site', 'canal_venda'])

# Getting a specific dataframe position
dataframe['canal_venda'][2]

# Getting a slice of a specific column
dataframe['canal_venda'][:2]

# Data split using iloc (line | column)
dataframe.iloc[3:,4:]
dataframe.iloc[:2,2:]

# Data split using loc (index) (line)
dataframe.loc[:3]

# Getting specific columns
dataframe[['canal_venda', 'vendas']]

filter = ['canal_venda', 'vendas']
dataframe[filter]

# General info
dataframe.info()

# Data pivoting (column)
aux = dataframe.pivot(index = 'canal_venda', columns='site', values='acessos')
aux.info()

# Inserting the missing values using fillna
aux= dataframe.pivot(index = 'canal_venda', columns='site', values='acessos').fillna(0)
# Data pivoting (column)
dataframe.pivot(index = 'canal_venda', columns='site', values='acessos').fillna(0)

# Grouping columns
dataframe.melt(id_vars='site', value_vars=['canal_venda'])

# Index reset
print(aux.columns)
aux = dataframe.reset_index()
print(aux.columns)
aux.reset_index()
aux

# Example using melt
aux.melt(id_vars='canal_venda', value_vars=['site1', 'site2', 'site3'])

# Sum the columns of the dataframe
dataframe.sum()

# Sum the rows of the dataframe
dataframe.sum(axis = 1)

# Calc median (mediana) of numeric columns
print('Por linha: ',dataframe.median(axis= 1) )
print('Por coluna: ', dataframe.median())

# Calc average of numeric columns
dataframe.mean()

# Calc standard deviation of numeric columns
dataframe.std()

# Using the describe command that calculates descriptive statistics for numeric columns
dataframe.describe()

# Calc the 'moda'
dataframe.mode()

# Max value per column
dataframe.max()

# Min value per column
dataframe.min()

# Number of unique
dataframe.nunique()

# Counting the unique values of a column
dataframe['canal_venda'].value_counts()

# Unique values from a column
dataframe['canal_venda'].unique()

# groupby command (numeric values)
dataframe.groupby('site')['acessos'].sum()
dataframe.groupby('canal_venda')['acessos'].median()
# groupby (category)
dataframe.groupby('site')['canal_venda'].unique()
dataframe.groupby('site')['canal_venda'].first()

# Aggregation
dataframe.groupby('canal_venda').agg({'site': 'unique',
                                     'acessos': 'sum'})

# Correlations between variables
dataframe.corr(method = 'spearman')

# Creating categorical variables by numeric variable slice
dataframe['categoria_vendas'] = pd.cut(dataframe['vendas'],
                                       bins= (0, 1500, 2000, 8000), 
                                       labels = ('0 a 1500', '1500 a 2000', '2000 a 8000'))

# Creating categorical variable using list compression
dataframe['categoria_acessos'] = ['maior_que_300' if x > 300 else 'menor_que_300' for x in dataframe['acessos']]

# Putting two dataframes together | Creating the dataframe_2
dataframe_2 = pd.DataFrame({'site': ['site1', 'site1', 'site2', 'site2', 'site3'],
               'suporte': ['Carlos', 'Carlos', 'Maria', 'Maria', 'Ezequiel']})

# Merge
dataframe.merge(dataframe_2, on = 'site', how = 'left')

# Save dataframe as csv file
dataframe.to_csv('dataframe.csv', sep = ';', decimal = ',', index = False)

# Reading data from a csv file
dataframe_lido = pd.read_csv('dataframe.csv', sep = ';', decimal = ',')
dataframe_lido.head()
json = pd.read_json('https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/index.json')
json['offers'][99]
json.reset_index(inplace = True)
json['index']