import pandas as pd 


df = pd.read_csv('train.csv', parse_dates=['transactiondate'])

df['year'] = df['transactiondate'].dt.year
df['month'] = df['transactiondate'].dt.month
df['dayofweek'] = df['transactiondate'].dt.dayofweek

df.to_csv('train.csv', index = False)

