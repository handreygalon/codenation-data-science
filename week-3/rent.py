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

# multivariate exploration
'''
Looking for questions ...

1 - Which city has the most expensive rental average?
2 - How many bathrooms do you have in homes with more expensive rents?
3 - Do the most expensive properties accept animals?
4 - Are the most expensive properties furnished?

... and hypothesis (Based on common sense)

5 - São Paulo is the city with the most expensive rent.
6 - The more bathrooms in a property, the higher the rent.
7 - Property with furniture has the most expensive rent.

We have to convert common sense into statistics
Always think about what data I can have, in addition to what I have in the database
'''

# Definition: high rents are values over R$ 5.000,00
# df.columns
# df.valor_aluguel.describe()

# Question (1)
df.groupby('city')['valor_aluguel'].median().reset_index().sort_values('valor_aluguel', ascending = False)

# Question (2)
df['aluguel_alto'] = ['Alto' if x > 5000 else 'Baixo' for x in df['valor_aluguel']]
df['aluguel_alto'].value_counts()
df.groupby('aluguel_alto')['bathroom'].mean()

