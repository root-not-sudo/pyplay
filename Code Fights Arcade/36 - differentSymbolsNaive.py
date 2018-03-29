def differentSymbolsNaive(s):

    count = 0
    letters = []
    for i in range(0, 26):
        letters.append(chr(ord('a') + i))
    for i in s:
        if i in letters:
            count += 1
            letters.remove(i)
    return count
