import pandas as pd
import re

df = pd.read_json("jawiki-country.json", lines=True)
# print(df)
df2 = df[df['title'] == 'イギリス']
data = df2.iloc[:, 1].values
# print(data.shape)

ls = data[0].split('\n')
# ls = data.split('\n')
# print(ls)

pattern = "Category"

for line in ls:
    if re.search(pattern, line):
        print(line)