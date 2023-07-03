def cipher(string):
    s = ""
    for i in string:
        if ("a" <= i) & (i <= "z"):
            s += chr(219 - ord(i))
        else:
            s += i
    return s

s = input("enter something: ")

print(cipher(s))