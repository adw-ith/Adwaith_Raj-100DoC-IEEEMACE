a = 'abcdefghijklmnopqrstuvwxyz'
b = []
for i in a:
    b.append(i)


def numstring(s):
    p = []
    s = s.replace(' ', '')
    s = s.lower()
    for i in s:
        p.append(i)
    s = ''
    for i in p:
        if i in b:
            s = s + f'{b.index(i)+1} '
    return s


s = input("Enter the String")
print(numstring(s))
