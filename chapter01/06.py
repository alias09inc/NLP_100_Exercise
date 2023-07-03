def n_gram(n, lst):
    n_gram_list = []
    for i in range(len(lst) - n + 1):
        n_gram_tuple = (lst[i:i+n])
        # print(n_gram_tuple)
        n_gram_list.append(n_gram_tuple)
    return n_gram_list

a = "paraparaparadise"
b = "paragraph"

# print(n_gram(2, a))
x = set(n_gram(2, a))
y = set(n_gram(2, b))
print(x)
print(y)

print(x | y)
print(x & y)
print(x - y)
print("se" in x)
print("se" in y)