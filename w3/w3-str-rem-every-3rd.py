s = input()

n = 0
while n < len(s):
    s = s.replace(s[:n+1], s[:n], 1)
    n += 2
print(s)
