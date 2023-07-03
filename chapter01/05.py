string =  "I am an NLPer"

def n_gram(n, lst):
    n_gram_list = []
    for i in range(len(lst) - n + 1):
        n_gram_tuple = (lst[i:i+n])
        print(n_gram_tuple)
        n_gram_list.append(n_gram_tuple)
    return n_gram_list

print(n_gram(2, string))
print(n_gram(2, string.split()))