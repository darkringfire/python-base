s = input()
h1 = s.find('h')
h2 = s.rfind('h')
if h1 != -1 and h1 != h2:
    print(s[:h1+1], s[h1+1:h2].replace('h', 'H'), s[h2:], sep='')
else:
    print(s)
