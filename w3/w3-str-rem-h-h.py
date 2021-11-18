s = input()
h_pos1 = s.find('h')
h_pos2 = len(s) - s[::-1].find('h')
print(s[:h_pos1], s[h_pos2:], sep='')
