n = int(input())

print(n, 'korov', end='')
if n < 10 or n > 20:
    if n % 10 == 1:
        print('a', end='')
    elif 2 <= n % 10 <= 4:
        print('y', end=' ')
print()
