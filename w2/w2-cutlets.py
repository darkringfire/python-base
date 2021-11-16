k, m, n = int(input()), int(input()), int(input())

s0 = n
t = s0 // k
s0 = s0 % k
s1 = k * t
if s0 > 0:
    t += 1
    if s1 > 0:
        s2 = k - s0
        s1 += s0 - s2
    else:
        s1 += s0
t += (s1 + k - 1) // k

print(t * m)
