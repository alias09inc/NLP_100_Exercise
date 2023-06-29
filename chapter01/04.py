import re

s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can"

s_split = re.split('[. ]', s)
s_split = [a for a in s_split if a != '']

order = [0, 4, 5, 6, 7, 8, 14, 15, 18]

s_ans = {}

for i, word in enumerate(s_split):
    if i in order:
        s_ans[word[:1]] = i+1
    else:
        s_ans[word[:2]] = i+1

print(s_ans)