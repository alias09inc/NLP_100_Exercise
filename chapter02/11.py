import pandas as pd

df = pd.read_table('./popular-names.txt', header=None, delimiter="\t")
df.to_csv('spact.txt', sep=" ", header=False, index=False)