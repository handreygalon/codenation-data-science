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