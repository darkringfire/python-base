n = int(input())
m = 0
m_l = 1
while n != 0:
    if n == m:
        m_l += 1
    elif n > m:
        m, m_l = n, 1
    n = int(input())
print(m_l)
