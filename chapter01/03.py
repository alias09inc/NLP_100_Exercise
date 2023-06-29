import re

string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics"

split_str = re.split("[, ]", string)

print(split_str)
split_str2 = [a for a in split_str if a != '']

print(split_str2)
str_len = []
for i in split_str2:
    str_len.append(len(i))

print(str_len)