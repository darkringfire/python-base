inFile = open('input.txt')
wordlist = {}
for line in inFile.readlines():
    for word in line.split():
        if word not in wordlist.keys():
            wordlist[word] = []
        wordlist[word].append(1)
        print(len(wordlist[word]) - 1, end=' ')
inFile.close()
