import random

def typoglycemia(s):
    s_lst = s.split()
    new_s = ""
    for i in s_lst:
        print(i)
        if len(i) <= 4:
            new_s += i
        else:
            l = list(range(1,len(i)-1))
            random.shuffle(l)
            print(l)
            tmp = ""
            for j in l:
                tmp += i[j]
            tmp = i[0] + tmp + i[-1]
            new_s += tmp
        new_s += " "
    return new_s

string = input("enter sentence: ")
new_string = typoglycemia(string)
print(new_string)