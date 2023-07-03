import pandas as pd

df = pd.read_table("popular-names.txt", header=None, delimiter="\t")

df = df.iloc[:,0].value_counts()

print(df)