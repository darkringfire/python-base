s = input()

pos1 = s.find('f')
if pos1 != -1:
    print(pos1, end='')
    pos2 = len(s) - s[::-1].find('f') - 1
    if pos2 != pos1:
        print(' ', pos2, sep='', end='')
print()
