n = int(input())
s, n = n % 10, n // 10
s = s + n % 10 + n // 10

print(s)
