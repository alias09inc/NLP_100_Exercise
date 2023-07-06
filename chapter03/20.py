import pandas as pd

df = pd.read_json("jawiki-country.json", lines=True)

# print(df)

df2 = df[df['title'] == 'イギリス']

data = df2.iloc[:, 1].values

# print(df2)
print(data)
