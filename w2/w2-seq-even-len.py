n = -1
seq_len = 0
while n != 0:
    n = int(input())
    if n != 0 and n % 2 == 0:
        seq_len += 1
print(seq_len)
