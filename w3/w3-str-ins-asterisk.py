s = input()

n = 0
while n < len(s)-1:
    print(s[n], '*', sep='', end='')
    n += 1
print(s[-1])
