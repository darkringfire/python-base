n = -1
seq_sum = 0
seq_len = 0
while n != 0:
    n = int(input())
    if n != 0:
        seq_sum += n
        seq_len += 1
print(seq_sum / seq_len)
