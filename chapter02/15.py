import pandas as pd

df = pd.read_table('./popular-names.txt', header=None, delimiter="\t")

print(df.tail(5))