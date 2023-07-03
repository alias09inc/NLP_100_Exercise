import pandas as pd

df =  pd.read_table("popular-names.txt", header=None, delimiter="\t")

kinds = set(df.iloc[:,0])
print(len(kinds))