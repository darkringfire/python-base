n = int(input())

prev = n
eq_num = eq_max = 0
while n != 0:
    if n == prev:
        eq_num += 1
        if eq_num > eq_max:
            eq_max = eq_num
    else:
        prev = n
        eq_num = 1
    n = int(input())
print(eq_max)
