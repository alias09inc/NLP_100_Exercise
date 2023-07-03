import pandas as pd

df = pd.read_table('./popular-names.txt', header=None, delimiter="\t")

num = int(input("How much do you want to split: "))

#切り上げ除算用
step = - (-len(df) // num)

for i in range(num):
    df2 = df.iloc[i*step:(i+1)*step]
    filename = "split" + str(i) + ".txt"
    df2.to_csv(filename, header=False, index=False, sep=" ")

