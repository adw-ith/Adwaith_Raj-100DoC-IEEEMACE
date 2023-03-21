array = [1, 2, 3]


def addtoarray(i):
    array.append(i)
    return array


ans = 'y'
while ans == 'y':
    n = int(input('enter Number'))
    addtoarray(n)
    ans = input('Do you want to enter more numbers? y/n').lower()
print(f'update array: {array}')
