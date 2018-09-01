def timedReading(maxLength, text):

    wordlen = []
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    j = 0
    for i in range(len(text)):
        if text[i] in letters:
            print(i)
            j += 1
        else:
            if j > 0 and j <= maxLength:
                wordlen.append(j)
            j = 0
    if j > 0 and j <= maxLength:
        wordlen.append(j)
    return len(wordlen)
