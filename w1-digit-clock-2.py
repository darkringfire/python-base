s = int(input())

m, s = s // 60, s % 60
h, m = m // 60 % 24, m % 60

print(h, end=':')
print(m // 10, m % 10, sep='', end=':')
print(s // 10, s % 10, sep='')
