import pandas as pd


df = pd.read_csv('train.csv')

aux = pd.DataFrame({'colunas': df.columns,
                    'tipos': df.dtypes,
                    'percentual_faltante': df.isna().sum() / df.shape[0]})

# Filling in missing data:

# Numerical data
df['Age'] = df['Age'].fillna(df['Age'].mode())

# Categorical data
df['Cabin'] = df['Cabin'].fillna('Unknown')
df['Cabin'].value_counts()

df.shape[0]