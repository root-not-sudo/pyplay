def timedReading(maxLength, text):

    wordlen = []
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    j = 0
    for i in text:
        if i in letters:
            j += 1
        else:
            if j > 0 and j <= maxLength:
                wordlen.append(j)
            j = 0
    return len(wordlen)
