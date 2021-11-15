n = int(input())
nh, nl = n // 100, n % 100

dif = nh - (nl // 10 + nl % 10 * 10)
print(dif + 1)
