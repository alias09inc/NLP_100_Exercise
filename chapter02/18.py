import pandas as pd

df = pd.read_table("popular-names.txt", header=None, delimiter="\t")

# print(df)

df = df.sort_values(by=2, ascending=False)
print(df)