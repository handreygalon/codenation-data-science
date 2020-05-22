import pandas as pd


df = pd.read_csv('houses_to_rent_v2.csv')
df.head(5)
df.dtypes
df.dtypes.value_counts()
df.isna().sum()
df.info()

df.rename(columns = {'rent amount (R$)' : 'valor_aluguel'}, inplace = True)

# Single variable exploration
# Just view the data to future analysis 
df.shape[0]  # number of columns
df['valor_aluguel']
df['valor_aluguel'].mean()
df['valor_aluguel'].median()
df['valor_aluguel'].std()
df['valor_aluguel'].describe()

df['valor_aluguel'].plot(kind = 'hist', bins= 100)

# skewness positive skew
df.valor_aluguel.skew()

# kurtose - leptocurtica
df.valor_aluguel.kurtosis()