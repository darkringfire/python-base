n = int(input())

prev = n
mono_len, mono_len_max, prev_dif = 0, 0, 0
while n != 0:
    dif = n - prev
    if prev_dif * dif <= 0:
        mono_len = 1
    if dif != 0:
        mono_len += 1

    prev_dif = dif
    prev = n

    if mono_len > mono_len_max:
        mono_len_max = mono_len

    n = int(input())
print(mono_len_max)
