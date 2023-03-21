def squaresum(l):
    sqsum = 0
    for i in l:
        sqsum += (i*i)
    return sqsum


a = eval(input('Enter the numbers to be evaluated(eg:1,2,4,54,23): '))
print(squaresum(a))
