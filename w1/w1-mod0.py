a, b = int(input()), int(input())

f = (a - 1) // b + 1 - a // b
t = (f + 1) % 2

print('YES' * t, 'NO' * f, sep='')
