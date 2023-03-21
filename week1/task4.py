def sum(l):
    sum = 0
    for i in l:
        sum += i
    return sum


a = eval(input('enter the array for sumation(eg:1,2,4,54,23): '))
print(sum(a))
