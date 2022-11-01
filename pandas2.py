import pandas as pd

df = pd.read_csv('Datapandas.csv')
print(df)

print(df.memory_usage())
print(df.ndim)
print(df.tail(2))
print(df.head(2))
print(df.at[3,'State'])
print(df.dtypes)
print(df.memory_usage())
print(df.sort_index(ascending=True))
print(df.sort_values('Age',ascending=True))
print(df.select_dtypes(exclude=object))
print(df.info())
print(df.nunique())