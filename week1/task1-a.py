'''Using ASCII'''


def numstring(s):
    s = s.lower()
    num_str = ''
    for i in s:
        if i > 'a' and i < 'z':
            num_str += f'{ord(i)-96} '
        else:
            continue
    return num_str


string = input("Enter the required string")
print(f'The new string is: {numstring(string)}')
