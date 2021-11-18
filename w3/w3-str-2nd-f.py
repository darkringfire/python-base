s = input()
pos_f = s.find('f')
if pos_f != -1:
    print(s.find('f', pos_f+1))
else:
    print(-2)
