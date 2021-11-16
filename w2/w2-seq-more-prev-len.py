n = int(input())
prev = n
seq_len = 0
while n != 0:
    n = int(input())
    if n != 0 and n > prev:
        seq_len += 1
    prev = n
print(seq_len)
